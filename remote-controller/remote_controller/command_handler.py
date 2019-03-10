from .ir_controller import IRController
from .errors import Error


class CommandHandler:
    def __init__(self, device):
        self.__ir = IRController(device)

    def load(self):
        self.__ir.load_config()

    def send(self, command):
        if command.startswith('help'):
            command = command.split(' ')[1]
            try:
                return 'SUCCESS', self.__ir.help(command)
            except Error as error:
                return 'ERROR', str(error)

        elif command.startswith('raw'):
            command = command.split(' ')[1]
            try:
                self.__ir.send_raw_command(command)
                return 'SUCCESS', 'Command sent'
            except Error as error:
                return 'ERROR', str(error)

        else:
            command = command.split(' ')
            try:
                if len(command) > 1:
                    self.__ir.send_command(command[0], value=command[1])
                else:
                    self.__ir.send_command(command[0])
                return 'SUCCESS', 'Command sent'
            except Error as error:
                return 'ERROR', str(error)
