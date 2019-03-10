#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import os
import sys

from remote_controller.ir_controller import IRController

@click.command()
@click.argument('mode')
@click.argument('device')
def main(mode, device):
    if mode == 'cli':
        print('----- AVS Remote Controller -----')
        print('Copyright (C) 2019 Sebastián Pérez, Cesar Torres and Erick Durán.')

        ir = IRController(device)
        while True:
            command = input('Please enter a command: ')

            if command == 'exit':
                break
            elif command.startswith('help'):
                command = command.split(' ')[1]
                ir.help(command)
            elif command.startswith('raw'):
                command = command.split(' ')[1]
                ir.send_raw_command(command)
            else:
                command = command.split(' ')
                if len(command) > 1:
                    ir.send_command(command[0], command[1])
                else:
                    ir.send_command(command[0])


if __name__ == '__main__':
    main()
