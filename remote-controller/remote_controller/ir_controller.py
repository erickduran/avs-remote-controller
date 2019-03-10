from .command_validator import CommandValidator
from .ir_sender import IRSender

class IRController:
    def __init__(self, device):
        self.__device = device
        self.__command_validator = CommandValidator(device)
        self.__ir_sender = IRSender(device)

    def send_raw_command(self, command):
        print('Sending {} command...'.format(command))
        self.__command_validator.validate_raw(command)
        self.__ir_sender.send_raw(command)

    def send_command(self, command, value=None):
        print('Sending {} command...'.format(command))
        self.__command_validator.validate(command, value)
        self.__ir_sender.send(command, value)

    def help(self, command):
        pass

