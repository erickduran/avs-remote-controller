import yaml

from .command_validator import CommandValidator
from .ir_sender import IRSender
from .errors import FileNotLoadedError


class IRController:
    def __init__(self, device, review_mode):
        self.__device = device
        self.__review_mode = review_mode
        self.__raw_commands_path = './resources/commands/raw-commands.yml'
        self.__commands_path = './resources/commands/commands.yml'
        self.__actions_path = './resources/commands/commands-actions.yml'
        self.__command_validator = None
        self.__ir_sender = None

    def load_config(self):
        with open(self.__raw_commands_path, 'r') as stream:
            try:
                raw_commands = yaml.load(stream)
            except yaml.YAMLError as exception:
                raw_commands = None
                print(exception)

        with open(self.__commands_path, 'r') as stream:
            try:
                commands = yaml.load(stream)
            except yaml.YAMLError as exception:
                commands = None
                print(exception)

        with open(self.__actions_path, 'r') as stream:
            try:
                actions = yaml.load(stream)
            except yaml.YAMLError as exception:
                actions = None
                print(exception)

        if commands is not None and raw_commands is not None:
            self.__command_validator = CommandValidator(self.__device, commands, raw_commands)
        else:
            raise FileNotLoadedError('Commands file not loaded correctly.')

        if actions is not None:
            self.__ir_sender = IRSender(self.__device, actions, self.__review_mode)
        else:
            raise FileNotLoadedError('Actions file not loaded correctly.')

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
        return self.__command_validator.exists(command)[2]
