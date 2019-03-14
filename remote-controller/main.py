#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import click

from remote_controller.command_handler import CommandHandler

dir = os.path.dirname(__file__)
api_path = os.path.join(dir, 'api.py')


@click.command()
@click.argument('mode')
@click.argument('device')
@click.option('--review_mode', '-r', is_flag=True, help='Don\'t execute lirc commands.')
def main(mode, device, review_mode):
    print('----- AVS Remote Controller -----')
    print('Copyright (C) 2019 Sebastián Pérez, Cesar Torres and Erick Durán.')
    if mode == 'cli':
        command_handler = CommandHandler(device, review_mode)
        command_handler.load()
        while True:
            command = input('Please enter a command: ')

            if command == 'exit':
                break
            else:
                response = command_handler.send(command)
                print('{}: {}'.format(response[0], response[1]))

    elif mode == 'api':
        os.system('python3 {}'.format(api_path))


if __name__ == '__main__':
    main()
