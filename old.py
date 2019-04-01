import json
from pprint import pprint

from waitress import serve
from flask import Flask
from flask_ask import Ask, statement, question, session

from remote_controller.command_handler import CommandHandler

app = Flask(__name__)
ask = Ask(app, '/')
command_handler = CommandHandler('lg', False)
command_handler.load()

@ask.launch
def start_skill():
    welcome_message = '¿Qué le digo a la tele?'
    return question(welcome_message)


@ask.intent('PowerIntent')
def power_intent():
    command_handler.send('POWER')
    return statement('Listo')


@ask.intent('OKIntent')
def ok_intent():
    answer = command_handler.send('OK')
    return statement('Listo')


@ask.intent('ChannelIntent')
def channel_intent(channel):
    command_handler.send('CHANNEL {}'.format(channel))
    return statement('Listo')


@ask.intent('VolumeUpIntent')
def volume_up_intent(value):
    command_handler.send('VOLUME_UP {}'.format(value))
    return statement('Listo')


@ask.intent('VolumeDownIntent')
def volume_down_intent(value):
    if value is not None:
        command_handler.send('VOLUME_DOWN {}'.format(value))
    else:
        command_handler.send('VOLUME_DOWN')
    return statement('Listo')

if __name__ == '__main__':
    serve(app, host='localhost', port=5000)
