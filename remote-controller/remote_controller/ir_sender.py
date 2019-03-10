import os


class IRSender:
    def __init__(self, device):
        self.__device = device

    def send_raw(self, command):
        os.system('irsend SEND_ONCE {} {}'.format(self.__device, command))

    def send(self, command, value):
        pass

    def __parse(self, command):
        pass
