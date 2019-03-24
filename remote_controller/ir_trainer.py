import os


class IRTrainer:

    def __init__(self, review_mode):
        self.__review_mode = review_mode

    def train(self):
        bash_command = 'irrecord -d /dev/lirc0'
        pass
