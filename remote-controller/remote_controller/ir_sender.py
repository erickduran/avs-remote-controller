import os


class IRSender:
    def __init__(self, device, actions):
        self.__device = device
        self.__actions = actions

    def send_raw(self, command):
        os.system('irsend SEND_ONCE {} {}'.format(self.__device, command))

    def send(self, command, value):
        # if not composite, just send parsed command
        # if composite, use repetition or number logic to send command, apply waiting
        pass

    def __parse(self, command):
        # get according raw command from commands-actions.yml
        pass
