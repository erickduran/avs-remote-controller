import yaml

from .command_validator import CommandValidator
from .ir_sender import IRSender


class IRController:
    def __init__(self, device):
        self.__device = device
        self.__command_validator = CommandValidator(device)
        self.__ir_sender = IRSender(device)
        self.__raw_commands_path = './resources/commands/raw-commands.yml'
        self.__commands_path = './resources/commands/commands.yml'
        self.__actions_path = './resources/commands/commands.yml'
        self.__raw_commands = None
        self.__commands = None
        self.__actions = None

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

    def send_raw_command(self, command):
        print('Sending {} command...'.format(command))
        self.__command_validator.validate_raw(command)
        self.__ir_sender.send_raw(command)

    def send_command(self, command, value=None):
        print('Sending {} command...'.format(command))
        self.__command_validator.validate(command, value)
        self.__ir_sender.send(command, value)

    def help(self, command):
        if command in self.__raw_commands['commands'].keys():
            print(self.__raw_commands['commands'][command]['description'])
        elif command in self.__commands['commands'].keys():
            print(self.__commands['commands'][command]['description'])
        else:
            print('Command not found.')
