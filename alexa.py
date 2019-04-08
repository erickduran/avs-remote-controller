import sys

import requests
from waitress import serve
from flask import Flask
from flask_ask import Ask, statement, question

from remote_controller.command_handler import CommandHandler


app = Flask(__name__)
ask = Ask(app, '/')
hostname = '10.0.0.10:33333'



@ask.launch
def start_skill():
    welcome_message = '¿Qué le digo a la tele?'
    return question(welcome_message)


@ask.intent('AMAZON.HelpIntent')
def power_intent():
    return statement('Puedes enviar comandos como: encender, canal 10, sube el volumen, etcétera.')


@ask.intent('PowerIntent')
def power_intent():
    request = {'raw-command': False, 'command': 'POWER'}
    response = requests.post(hostname, json=request)
    # command_handler.send('POWER')
    return statement('Listo')


@ask.intent('OKIntent')
def ok_intent():
    answer = command_handler.send('OK')
    return statement('Listo')


@ask.intent('UndoIntent')
def ok_intent():
    answer = command_handler.send('UNDO')
    return statement('Listo')


@ask.intent('ListIntent')
def ok_intent():
    answer = command_handler.send('LIST')
    return statement('Listo')


@ask.intent('BackIntent')
def ok_intent():
    answer = command_handler.send('BACK')
    return statement('Listo')


@ask.intent('InfoIntent')
def ok_intent():
    answer = command_handler.send('INFO')
    return statement('Listo')


@ask.intent('ExitIntent')
def ok_intent():
    answer = command_handler.send('EXIT')
    return statement('Listo')


@ask.intent('MenuIntent')
def ok_intent():
    answer = command_handler.send('MENU')
    return statement('Listo')


@ask.intent('MuteIntent')
def ok_intent():
    answer = command_handler.send('MUTE')
    return statement('Listo')


@ask.intent('SettingsIntent')
def ok_intent():
    answer = command_handler.send('SETTINGS')
    return statement('Listo')


@ask.intent('InputIntent')
def ok_intent():
    answer = command_handler.send('INPUT')
    return statement('Listo')


@ask.intent('ScreenRatioIntent')
def ok_intent():
    answer = command_handler.send('SCREEN_RATIO')
    return statement('Listo')


@ask.intent('MoveUpIntent')
def ok_intent():
    answer = command_handler.send('MOVE_UP')
    return statement('Listo')


@ask.intent('MoveDownIntent')
def ok_intent():
    answer = command_handler.send('MOVE_DOWN')
    return statement('Listo')


@ask.intent('MoveLeftIntent')
def ok_intent():
    answer = command_handler.send('MOVE_LEFT')
    return statement('Listo')


@ask.intent('MoveRightIntent')
def ok_intent():
    answer = command_handler.send('MOVE_RIGHT')
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
    if len(sys.argv) < 2:
        print('Please enter a device name, aborting...')
    else:
        command_handler = CommandHandler(sys.argv[1], False)
        command_handler.load()
        print('Starting on device: {}'.format(sys.argv[1]))
        serve(app, host='localhost', port=33333)


