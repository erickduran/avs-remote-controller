#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# cli.py
"""This is the definition of the main CLI class."""

import os

import click

from remote_controller.command_handler import CommandHandler
from remote_controller.ir_trainer import IRTrainer

FILE_PATH = os.path.dirname(__file__)
API_PATH = os.path.join(FILE_PATH, 'api.py')
ALEXA_PATH = os.path.join(FILE_PATH, 'alexa.py')


@click.command()
@click.argument('mode')
@click.option('--device', '-d', help='Specify the destination device.')
@click.option('--review_mode', '-r', is_flag=True, help='Don\'t execute lirc commands.')
def main(mode, device, review_mode):
    # The main CLI screen
    print('----- AVS Remote Controller -----')
    print('Copyright (C) 2019 Sebastián Pérez, Cesar Torres and Erick Durán.')

    # CLI mode for keyboard interaction
    if mode == 'cli':
        if device:
            command_handler = CommandHandler(device, review_mode)
            command_handler.load()
            while True:
                command = input('Please enter a command: ')

                if command == 'exit':
                    break
                else:
                    response = command_handler.send(command)
                    print('{}: {}'.format(response[0], response[1]))
        else:
            print('Please specify a device for CLI mode.')

    # API mode for wireless interaction
    elif mode == 'api':
        if device:
            os.system('python3 {} {}'.format(API_PATH, device))
        else:
            print('Please specify a device for API mode.')

    # Training mode to add new devices
    elif mode == 'training':
        if device:
            IRTrainer.run(device)
        else:
            print('Please specify a device for training mode.')

    # API mode for Alexa Voice Service interaction
    elif mode == 'alexa':
        if device:
            os.system('python3 {} {}'.format(API_PATH, device))
        else:
            print('Please specify a device for Alexa mode.')


if __name__ == '__main__':
    main()
