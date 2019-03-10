from flask import Flask, jsonify, request

from remote_controller.command_handler import CommandHandler

app = Flask(__name__)
command_handler = CommandHandler('lg')
command_handler.load()


@app.route('/', methods=['POST'])
def index():
    response = dict()
    if 'raw-command' not in request.json:
        response['status'] = 'ERROR'
        response['message'] = 'Please specify the raw-command param.'
        return jsonify(response), 400

    if 'command' not in request.json:
        response['status'] = 'ERROR'
        response['message'] = 'Please specify the command name param.'
        return jsonify(response), 400

    if request.json['raw-command'] is True:
        answer = command_handler.send('raw {}'.format(request.json['command']))
        response['status'] = answer[0]
        response['message'] = answer[1]
        return jsonify(response), 200

    elif request.json['raw-command'] is False:
        if 'value' in request.json:
            print('{} {}'.format(request.json['command'], str(request.json['value'])))
            answer = command_handler.send('{} {}'.format(request.json['command'], str(request.json['value'])))
        else:
            answer = command_handler.send(request.json['command'])
        response['status'] = answer[0]
        response['message'] = answer[1]
        return jsonify(response), 200

    else:
        response['status'] = 'ERROR'
        response['message'] = 'The raw-command param must be boolean.'
        return jsonify(response), 400


if __name__ == '__main__':
    app.run()

