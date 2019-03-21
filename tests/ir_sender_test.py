import os

import unittest
import yaml

from remote_controller.ir_sender import IRSender

FILE_PATH = os.path.dirname(__file__)

ACTIONS_PATH = '../resources/commands/commands-actions.yml'


class IRSenderTest(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(FILE_PATH, ACTIONS_PATH), 'r') as stream:
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
        self.assertEqual(expected, result)

    def test_send_power_command(self):
        command = 'POWER'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_POWER')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_ok_command(self):
        command = 'KEY_OK'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_ok_command(self):
        command = 'OK'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_OK')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_list_command(self):
        command = 'KEY_LIST'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_list_command(self):
        command = 'LIST'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_LIST')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_undo_command(self):
        command = 'KEY_UNDO'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_undo_command(self):
        command = 'UNDO'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_UNDO')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_back_command(self):
        command = 'KEY_BACK'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_back_command(self):
        command = 'BACK'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_BACK')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_info_command(self):
        command = 'KEY_INFO'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_info_command(self):
        command = 'INFO'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_INFO')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_exit_command(self):
        command = 'KEY_EXIT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_exit_command(self):
        command = 'EXIT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_EXIT')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_menu_command(self):
        command = 'KEY_MENU'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_menu_command(self):
        command = 'MENU'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_MENU')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_raw_mute_command(self):
        command = 'KEY_MUTE'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_mute_command(self):
        command = 'MUTE'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_MUTE')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_raw_config_command(self):
        command = 'KEY_CONFIG'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_config_command(self):
        command = 'SETTINGS'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_CONFIG')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_video_command(self):
        command = 'KEY_VIDEO'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_input_command(self):
        command = 'INPUT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_VIDEO')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_screen_command(self):
        command = 'KEY_SCREEN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_screen_command(self):
        command = 'SCREEN_RATIO'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_SCREEN')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_volume_up_command(self):
        command = 'KEY_VOLUMEUP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_volume_up_command(self):
        command = 'VOLUME_UP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_VOLUMEUP')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_volume_down_command(self):
        command = 'KEY_VOLUMEDOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_volume_down_command(self):
        command = 'VOLUME_DOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_VOLUMEDOWN')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_channel_up_command(self):
        command = 'KEY_CHANNELUP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_channel_up_command(self):
        command = 'CHANNEL_UP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_CHANNELUP')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_channel_down_command(self):
        command = 'KEY_CHANNELDOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_channel_down_command(self):
        command = 'CHANNEL_DOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_CHANNELDOWN')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_key_up_command(self):
        command = 'KEY_UP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_key_up_command(self):
        command = 'MOVE_UP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_UP')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    def test_send_raw_key_down_command(self):
        command = 'KEY_DOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_key_down_command(self):
        command = 'MOVE_DOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_DOWN')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_key_right_command(self):
        command = 'KEY_RIGHT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_key_right_command(self):
        command = 'MOVE_RIGHT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_RIGHT')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_send_raw_key_left_command(self):
        command = 'KEY_LEFT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertEqual(expected, result)

    def test_send_key_left_command(self):
        command = 'MOVE_LEFT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_LEFT')]
        result = self.__ir_sender.send(command, None)
        self.assertEqual(expected, result)

    def test_composite_channel_up_command(self):
        command = 'CHANNEL_UP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_CHANNELUP'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_CHANNELUP'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_CHANNELUP')]
        result = self.__ir_sender.send(command, 3)
        self.assertEqual(expected, result)

    def test_composite_channel_down_command(self):
        command = 'CHANNEL_DOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_CHANNELDOWN'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_CHANNELDOWN'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_CHANNELDOWN')]
        result = self.__ir_sender.send(command, 3)
        self.assertEqual(expected, result)

    def test_composite_volume_up_command(self):
        command = 'VOLUME_UP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_VOLUMEUP'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_VOLUMEUP')]
        result = self.__ir_sender.send(command, 2)
        self.assertEqual(expected, result)

    def test_composite_volume_down_command(self):
        command = 'VOLUME_DOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_VOLUMEDOWN'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_VOLUMEDOWN'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_VOLUMEDOWN')]
        result = self.__ir_sender.send(command, 3)
        self.assertEqual(expected, result)

    # Move
    def test_composite_move_up_command(self):
        command = 'MOVE_UP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_UP')]
        result = self.__ir_sender.send(command, 1)
        self.assertEqual(expected, result)

    def test_composite_move_down_command(self):
        command = 'MOVE_DOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_DOWN'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_DOWN'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_DOWN')]
        result = self.__ir_sender.send(command, 3)
        self.assertEqual(expected, result)

    def test_composite_move_left_command(self):
        command = 'MOVE_LEFT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_LEFT'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_LEFT'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_LEFT')]
        result = self.__ir_sender.send(command, 3)
        self.assertEqual(expected, result)

    def test_composite_move_right_command(self):
        command = 'MOVE_RIGHT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_RIGHT'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_RIGHT'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_RIGHT')]
        result = self.__ir_sender.send(command, 3)
        self.assertEqual(expected, result)

    def test_number_channel_345_command(self):
        command = 'CHANNEL'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_3'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_4'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_5')]
        result = self.__ir_sender.send(command, '345')
        self.assertEqual(expected, result)

    def test_number_channel_123_command(self):
        command = 'CHANNEL'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_1'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_2'),
                    'irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_3')]
        result = self.__ir_sender.send(command, '123')
        self.assertEqual(expected, result)

    def test_number_channel_8_command(self):
        command = 'CHANNEL'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'KEY_8')]
        result = self.__ir_sender.send(command, '8')
        self.assertEqual(expected, result)