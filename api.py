# api.py
"""This is the definition of the API class for wireless interaction."""

import sys
import logging

from waitress import serve
from paste.translogger import TransLogger
from flask import Flask, jsonify, request, redirect

from remote_controller.command_handler import CommandHandler


app = Flask(__name__)


# Redirect GET requests, just for fun
@app.route('/', methods=['GET'])
def home():
    return redirect("https://www.erickduran.com", code=302)


# Handle POST requests to root
@app.route('/', methods=['POST'])
def index():
    response = dict()
    # Handle help commands, responding a description
    if 'help' in request.json:
        answer = command_handler.send('help {}'.format(request.json['help']))
        response['status'] = answer[0]
        response['message'] = answer[1]
        return jsonify(response), 200

    # Must specify if command is raw, returns error if not in dictionary
    if 'raw-command' not in request.json:
        response['status'] = 'ERROR'
        response['message'] = 'Please specify the raw-command param.'
        return jsonify(response), 400

    # Must specify the command to execute, returns error if not in dictionary
    if 'command' not in request.json:
        response['status'] = 'ERROR'
        response['message'] = 'Please specify the command name param.'
        return jsonify(response), 400

    # Handle raw commands (as created by lircd)
    if request.json['raw-command'] is True:
        answer = command_handler.send('raw {}'.format(request.json['command']))
        response['status'] = answer[0]
        response['message'] = answer[1]
        return jsonify(response), 200

    # Handle composite commands (as defined in resources)
    elif request.json['raw-command'] is False:
        # Commands that receive a value
        if 'value' in request.json:
            answer = command_handler.send('{} {}'.format(request.json['command'], str(request.json['value'])))
        else:
            answer = command_handler.send(request.json['command'])
        response['status'] = answer[0]
        response['message'] = answer[1]
        return jsonify(response), 200

    # Handle non-boolean param
    else:
        response['status'] = 'ERROR'
        response['message'] = 'The raw-command param must be boolean.'
        return jsonify(response), 400


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a device name, aborting...')
    else:
        command_handler = CommandHandler(sys.argv[1], False)
        command_handler.load()

        # Logging interactions with the API
        app = TransLogger(app, logger_name='api_logger')

        logger = logging.getLogger('api_logger')
        logger.setLevel(logging.DEBUG)

        # Logging to file
        file_handler = logging.FileHandler('api.log')
        file_handler.setLevel(logging.DEBUG)

        logger.addHandler(file_handler)

        # Setting server port and opening to the internet
        # This will be trasferred to HTTPS by the proxy
        serve(app, host='0.0.0.0', port=55555)
