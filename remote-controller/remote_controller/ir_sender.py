import os
import time

from .errors import InvalidCompositeCommandError


class IRSender:
    def __init__(self, device, actions, review_mode):
        self.__device = device
        self.__actions = actions
        self.__review_mode = review_mode

    def send_raw(self, command):
        bash_command = 'irsend SEND_ONCE {} {}'.format(self.__device, command)
        if not self.__review_mode:
            os.system(bash_command)
        return [bash_command]

    def send(self, command, value):
        bash_commands = []
        parsed = self.__parse(command)
        if parsed[1] is None:
            return self.send_raw(parsed[0])
        else:
            if parsed[1] == 'number':
                for char in value:
                    command = 'KEY_{}'.format(char)
                    bash_commands += self.send_raw(command)
                    time.sleep(1)
            elif parsed[1] == 'repetition':
                if value is not None:
                    for i in range(0, int(value)):
                        bash_commands += self.send_raw(parsed[0])
                        time.sleep(1)
                else:
                    return self.send_raw(parsed[0])
            else:
                raise InvalidCompositeCommandError('Composite command configuration not understood')
            return bash_commands

    def __parse(self, command):
        raw = self.__actions['commands'][command]['raw-command']
        if 'composite' in self.__actions['commands'][command].keys():
            return raw, self.__actions['commands'][command]['composite']
        else:
            return raw, None
