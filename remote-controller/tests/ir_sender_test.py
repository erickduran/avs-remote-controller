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

    def test_send_raw_command(self):
        command = 'KEY_VOLUMEDOWN'
        expected = ['irsend SEND_ONCE{} {}'.format(self.__device, '')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_volumedown_command(self):
        command = 'VOLUME_DOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'VOLUME_DOWN')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_raw_volumeup_command(self):
        command = 'VOLUME_UP'
        expected = ['irsend SEND_ONCE{} {}'.format(self.__device, 'VOLUME_UP')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_volumeup_command(self):
        command = 'KEY_VOLUMEUP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_VOLUMEUP')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_raw_channeldown_command(self):
        command = 'KEY_CHANNELDOWN'
        expected = ['irsend SEND_ONCE{} {}'.format(self.__device, 'KEY_CHANNELDOWN')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_channeldown_command(self):
        command = 'CHANNEL_DOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'CHANNEL_DOWN')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_raw_channelup_command(self):
        command = 'KEY_CHANNELUP'
        expected = ['irsend SEND_ONCE{} {}'.format(self.__device, 'KEY_CHANNELUP')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_channelup_command(self):
        command = 'CHANNEL_UP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, '')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_raw_up_command(self):
        command = 'KEY_UP'
        expected = ['irsend SEND_ONCE{} {}'.format(self.__device, 'KEY_UP')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_up_command(self):
        command = 'MOVE_UP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'MOVE_UP')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_raw_down_command(self):
        command = 'KEY_DOWN'
        expected = ['irsend SEND_ONCE{} {}'.format(self.__device, 'KEY_DOWN')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_down_command(self):
        command = 'MOVE_DOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'MOVE_DOWN')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_raw_right_command(self):
        command = 'KEY_RIGHT'
        expected = ['irsend SEND_ONCE{} {}'.format(self.__device, 'KEY_RIGHT')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_right_command(self):
        command = 'MOVE_RIGHT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'MOVE_RIGHT')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_raw_left_command(self):
        command = 'RAW_LEFT'
        expected = ['irsend SEND_ONCE{} {}'.format(self.__device, 'RAW_LEFT')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_left_command(self):
        command = 'MOVE_LEFT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'MOVE_LEFT')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_raw_ok_command(self):
        command = 'KEY_OK'
        expected = ['irsend SEND_ONCE{} {}'.format(self.__device, 'KEY_OK')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_ok_command(self):
        command = 'OK'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'OK')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)



    def test_send_raw_key0_command(self):
        command = 'KEY_0'
        expected = ['irsend SEND_ONCE{} {}'.format(self.__device, 'KEY_0')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_raw_key1_command(self):
        command = 'KEY_1'
        expected = ['irsend SEND_ONCE{} {}'.format(self.__device, 'KEY_1')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # TODO
    # test more commands and raw commands
    # test composite repetition commands (volume up, volume down, etc.)
    # test composite number commands (channel)