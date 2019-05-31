# ir_sender.py
"""This is the definition of the IRSender class. This class creates the necessary additional
processes to execute the commands. This class implements the use of the lircd library.
"""
import os
import time
import threading

from remote_controller.errors import InvalidCompositeCommandError


class IRSender:
    def __init__(self, device, actions, review_mode):
        self.__device = device
        self.__actions = actions
        self.__review_mode = review_mode

    # Generates the bash command
    def send_raw(self, command):
        bash_command = 'irsend SEND_ONCE {} {}'.format(self.__device, command)
        # If not in review mode, create the thread and execute the OS command
        if not self.__review_mode:
            thread = threading.Thread(target=os.system, args=[bash_command])
            thread.daemon = True
            thread.start()
        return [bash_command]

    # Generates the necessary bash commands
    def send(self, command, value):
        bash_commands = []
        parsed = self.__parse(command)
        # Commands that are just aliases
        if parsed[1] is None:
            return self.send_raw(parsed[0])
        else:
            # Commands that use digits
            if parsed[1] == 'number':
                # Executes the next command every half second
                for char in value:
                    command = 'KEY_{}'.format(char)
                    bash_commands += self.send_raw(command)
                    time.sleep(0.5)
            # Commands that use repetition
            elif parsed[1] == 'repetition':
                if value is not None:
                    # Repeats the command every half second
                    for i in range(0, int(value)):
                        bash_commands += self.send_raw(parsed[0])
                        time.sleep(0.5)
                else:
                    return self.send_raw(parsed[0])
            # Error for bad input
            else:
                raise InvalidCompositeCommandError('Composite command configuration not understood')
            return bash_commands

    # Translates a composite command to a raw command
    def __parse(self, command):
        raw = self.__actions['commands'][command]['raw-command']
        if 'composite' in self.__actions['commands'][command].keys():
            return raw, self.__actions['commands'][command]['composite']
        else:
            return raw, None
