#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import os

from remote_controller.ir_controller import IRController

dir = os.path.dirname(__file__)


@click.command()
@click.argument('mode')
def main(mode):
    if mode == 'cli':
        print('----- AVS Remote Controller -----')
        print('Copyright (C) 2019 Sebastián Pérez, Cesar Torres and Erick Durán.')

        ir = IRController()
        while True:
            command = input('Please enter a command: ')

            if command == 'exit':
                break
            else:
                ir.send_command(command)


if __name__ == '__main__':
    main()
