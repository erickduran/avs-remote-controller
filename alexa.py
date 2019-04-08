import sys

import requests
from waitress import serve
from flask import Flask
from flask_ask import Ask, statement, question

from remote_controller.command_handler import CommandHandler


app = Flask(__name__)
ask = Ask(app, '/')
hostname = 'http://10.0.0.10:55555'


@ask.launch
def start_skill():
    welcome_message = '¿Qué le digo a la tele?'
    return question(welcome_message)


@ask.intent('AMAZON.HelpIntent')
def help_intent():
    return statement('Puedes enviar comandos como: encender, canal 10, sube el volumen, etcétera.')


@ask.intent('PowerIntent')
def power_intent():
    request = {'raw-command': False, 'command': 'POWER'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('OKIntent')
def ok_intent():
    request = {'raw-command': False, 'command': 'OK'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('UndoIntent')
def undo_intent():
    request = {'raw-command': False, 'command': 'UNDO'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('ListIntent')
def list_intent():
    request = {'raw-command': False, 'command': 'LIST'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('BackIntent')
def back_intent():
    request = {'raw-command': False, 'command': 'BACK'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('InfoIntent')
def info_intent():
    request = {'raw-command': False, 'command': 'INFO'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('ExitIntent')
def exit_intent():
    request = {'raw-command': False, 'command': 'EXIT'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('MenuIntent')
def menu_intent():
    request = {'raw-command': False, 'command': 'MENU'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('MuteIntent')
def mute_intent():
    request = {'raw-command': False, 'command': 'MUTE'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('SettingsIntent')
def settings_intent():
    request = {'raw-command': False, 'command': 'SETTINGS'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('InputIntent')
def input_intent(value):
    if value is not None:
        request = {'raw-command': False, 'command': 'INPUT {}'.format(value)}
    else:
        request = {'raw-command': False, 'command': 'INPUT'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('ScreenRatioIntent')
def screen_ratio_intent():
    request = {'raw-command': False, 'command': 'SCREEN_RATIO'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('MoveUpIntent')
def move_up_intent():
    request = {'raw-command': False, 'command': 'MOVE_UP'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('MoveDownIntent')
def move_down_intent():
    request = {'raw-command': False, 'command': 'MOVE_DOWN'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('MoveLeftIntent')
def move_left_intent():
    request = {'raw-command': False, 'command': 'MOVE_LEFT'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('MoveRightIntent')
def move_right_intent():
    request = {'raw-command': False, 'command': 'MOVE_RIGHT'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('ChannelIntent')
def channel_intent(channel):
    request = {'raw-command': False, 'command': 'CHANNEL {}'.format(channel)}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('VolumeUpIntent')
def volume_up_intent(value):
    if value is not None:
        request = {'raw-command': False, 'command': 'VOLUME_UP {}'.format(value)}
    else:
        request = {'raw-command': False, 'command': 'VOLUME_UP'}
    requests.post(hostname, json=request)
    return statement('Listo')


@ask.intent('VolumeDownIntent')
def volume_down_intent(value):
    if value is not None:
        request = {'raw-command': False, 'command': 'VOLUME_DOWN {}'.format(value)}
    else:
        request = {'raw-command': False, 'command': 'VOLUME_DOWN'}
    requests.post(hostname, json=request)
    return statement('Listo')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a device name, aborting...')
    else:
        command_handler = CommandHandler(sys.argv[1], False)
        command_handler.load()
        print('Starting on device: {}'.format(sys.argv[1]))
        serve(app, host='localhost', port=33333)


