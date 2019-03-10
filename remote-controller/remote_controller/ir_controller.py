import yaml

from .command_validator import CommandValidator
from .ir_sender import IRSender
from .errors import InvalidCommandError


class IRController:
    def __init__(self, device):
        self.__device = device
        self.__raw_commands_path = './resources/commands/raw-commands.yml'
        self.__commands_path = './resources/commands/commands.yml'
        self.__actions_path = './resources/commands/commands-actions.yml'
        self.__raw_commands = None
        self.__commands = None
        self.__actions = None
        self.__command_validator = None
        self.__ir_sender = None

    def load_config(self):
        with open(self.__raw_commands_path, 'r') as stream:
            try:
                self.__raw_commands = yaml.load(stream)
            except yaml.YAMLError as exception:
                print(exception)

        with open(self.__commands_path, 'r') as stream:
            try:
                self.__commands = yaml.load(stream)
            except yaml.YAMLError as exception:
                print(exception)

        with open(self.__actions_path, 'r') as stream:
            try:
                self.__actions = yaml.load(stream)
            except yaml.YAMLError as exception:
                print(exception)

        self.__command_validator = CommandValidator(self.__device, self.__commands, self.__raw_commands)
        self.__ir_sender = IRSender(self.__device, self.__actions)

    def send_raw_command(self, command):
        print('Attempting {} command...'.format(command))
        self.__command_validator.validate_raw(command)
        self.__ir_sender.send_raw(command)

    def send_command(self, command, value=None):
        if value:
            print('Attempting {} command with value of {}...'.format(command, value))
        else:
            print('Attempting {} command...'.format(command))
        self.__command_validator.validate(command, value)
        self.__ir_sender.send(command, value)

    def help(self, command):
        if command in self.__raw_commands['commands'].keys():
            return self.__raw_commands['commands'][command]['description']
        elif command in self.__commands['commands'].keys():
            return self.__commands['commands'][command]['description']
        else:
            raise InvalidCommandError('Command doesn\'t exist')
