import os
import time

from .errors import InvalidCompositeCommandError


class IRSender:
    def __init__(self, device, actions):
        self.__device = device
        self.__actions = actions

    def send_raw(self, command):
        os.system('irsend SEND_ONCE {} {}'.format(self.__device, command))

    def send(self, command, value):
        parsed = self.__parse(command)
        if parsed[1] is None:
            self.send_raw(parsed[0])
        else:
            if parsed[1] == 'number':
                for char in value:
                    command = 'KEY_{}'.format(char)
                    self.send_raw(command)
                    time.sleep(1)
            elif parsed[1] == 'repetition':
                if value is not None:
                    for i in range(0, int(value)):
                        self.send_raw(parsed[0])
                        time.sleep(1)
                else:
                    self.send_raw(parsed[0])
            else:
                raise InvalidCompositeCommandError('Composite command configuration not understood')

    def __parse(self, command):
        raw = self.__actions['commands'][command]['raw-command']
        if 'composite' in self.__actions['commands'][command].keys():
            return raw, self.__actions['commands'][command]['composite']
        else:
            return raw, None
