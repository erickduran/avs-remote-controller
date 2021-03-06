# ir_controller.py
"""This is the definition of the IRController class. This class delegates the commands to the IRSender
after the necessary validations are passed. It also loads the necessary configuration files.
"""
import os

import yaml

from remote_controller.command_validator import CommandValidator
from remote_controller.ir_sender import IRSender
from remote_controller.errors import FileNotLoadedError, InvalidCommandError

FILE_PATH = os.path.dirname(__file__)

RAW_COMMANDS_PATH = '../resources/commands/raw-commands.yml'
COMMANDS_PATH = '../resources/commands/commands.yml'
ACTIONS_PATH = '../resources/commands/commands-actions.yml'


class IRController:
    def __init__(self, device, review_mode):
        self.__device = device
        self.__review_mode = review_mode
        self.__command_validator = None
        self.__ir_sender = None

    # Load all the necessary configuration YAML files
    def load_config(self):
        with open(os.path.join(FILE_PATH, RAW_COMMANDS_PATH), 'r') as stream:
            try:
                raw_commands = yaml.load(stream)
            except yaml.YAMLError as exception:
                raw_commands = None
                print(exception)

        with open(os.path.join(FILE_PATH, COMMANDS_PATH), 'r') as stream:
            try:
                commands = yaml.load(stream)
            except yaml.YAMLError as exception:
                commands = None
                print(exception)

        with open(os.path.join(FILE_PATH, ACTIONS_PATH), 'r') as stream:
            try:
                actions = yaml.load(stream)
            except yaml.YAMLError as exception:
                actions = None
                print(exception)

        # Errors for bad files
        if commands is not None and raw_commands is not None:
            self.__command_validator = CommandValidator(self.__device, commands, raw_commands)
        else:
            raise FileNotLoadedError('Commands files not loaded correctly.')

        if actions is not None:
            self.__ir_sender = IRSender(self.__device, actions, self.__review_mode)
        else:
            raise FileNotLoadedError('Actions file not loaded correctly.')

    # Validate, inform and send a raw command
    def send_raw_command(self, command):
        print('Attempting {} command...'.format(command))
        try:
            self.__command_validator.validate_raw(command)
        except InvalidCommandError:
            print('Command isn\'t registered, but attempting as raw...')
        self.__ir_sender.send_raw(command)

    # Validate, inform and send a composite command
    def send_command(self, command, value=None):
        if value:
            print('Attempting {} command with value of {}...'.format(command, value))
        else:
            print('Attempting {} command...'.format(command))
        self.__command_validator.validate(command, value)
        self.__ir_sender.send(command, value)

    # Inform of a help message for a command
    def help(self, command):
        return self.__command_validator.exists(command)[2]
