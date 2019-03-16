import os

import unittest
import yaml

from remote_controller.ir_sender import IRSender

dir = os.path.dirname(__file__)

ACTIONS_PATH = '../resources/commands/commands-actions.yml'


class IRSenderTest(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(dir, ACTIONS_PATH), 'r') as stream:
            try:
                actions = yaml.load(stream)
            except yaml.YAMLError as exception:
                actions = None
                print(exception)

        self.__device = 'lg'
        self.__ir_sender = IRSender(self.__device, actions, True)

    def test_send_raw_power_command(self):
        command = 'KEY_POWER'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_power_command(self):
        command = 'POWER'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_POWER')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # TODO
    # test more commands and raw commands
    # test composite repetition commands (volume up, volume down, etc.)
    # test composite number commands (channel)
