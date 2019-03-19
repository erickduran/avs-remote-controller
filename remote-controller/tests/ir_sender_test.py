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

    # Commands & Raw commands
    # Power
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

    # Ok
    def test_send_raw_ok_command(self):
        command = 'KEY_OK'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_ok_command(self):
        command = 'OK'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'OK')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # List
    def test_send_raw_list_command(self):
        command = 'KEY_LIST'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_list_command(self):
        command = 'LIST'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'LIST')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Undo
    def test_send_raw_undo_command(self):
        command = 'KEY_UNDO'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_undo_command(self):
        command = 'UNDO'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'UNDO')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Back
    def test_send_raw_back_command(self):
        command = 'KEY_BACK'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_back_command(self):
        command = 'BACK'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'BACK')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Info
    def test_send_raw_info_command(self):
        command = 'KEY_INFO'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_info_command(self):
        command = 'INFO'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'INFO')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Exit
    def test_send_raw_exit_command(self):
        command = 'KEY_EXIT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_exit_command(self):
        command = 'EXIT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'EXIT')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Menu
    def test_send_raw_menu_command(self):
        command = 'KEY_MENU'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_menu_command(self):
        command = 'MENU'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'MENU')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Mute
    def test_send_raw_mute_command(self):
        command = 'KEY_MUTE'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_mute_command(self):
        command = 'MUTE'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'MUTE')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Config
    def test_send_raw_config_command(self):
        command = 'KEY_CONFIG'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_config_command(self):
        command = 'SETTINGS'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'SETTINGS')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Video
    def test_send_raw_video_command(self):
        command = 'KEY_VIDEO'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_config_command(self):
        command = 'INPUT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'INPUT')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Screen
    def test_send_raw_screen_command(self):
        command = 'KEY_SCREEN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_screen_command(self):
        command = 'SCREEN_RATIO'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'SCREEN_RATIO')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Volume
    # Up
    def test_send_raw_volumeup_command(self):
        command = 'KEY_VOLUMEUP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_volumeup_command(self):
        command = 'VOLUME_UP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'VOLUME_UP')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Down
    def test_send_raw_volumedown_command(self):
        command = 'KEY_VOLUMEDOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_volumedown_command(self):
        command = 'VOLUME_DOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'VOLUME_DOWN')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Channel
    # Up
    def test_send_raw_channelup_command(self):
        command = 'KEY_CHANNELUP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_channelup_command(self):
        command = 'CHANNEL_UP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'CHANNEL_UP')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)
    # Down
    def test_send_raw_channeldown_command(self):
        command = 'KEY_CHANNELDOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_channeldown_command(self):
        command = 'CHANNEL_DOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'CHANNEL_DOWN')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Directions
    # Up
    def test_send_raw_keyup_command(self):
        command = 'KEY_UP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_keyup_command(self):
        command = 'MOVE_UP'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'MOVE_UP')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Down
    def test_send_raw_keydown_command(self):
        command = 'KEY_DOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_keydown_command(self):
        command = 'MOVE_DOWN'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'MOVE_DOWN')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Right
    def test_send_raw_keyright_command(self):
        command = 'KEY_RIGHT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_keyright_command(self):
        command = 'MOVE_RIGHT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'MOVE_RIGHT')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Left
    def test_send_raw_keyleft_command(self):
        command = 'KEY_LEFT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, command)]
        result = self.__ir_sender.send_raw(command)
        self.assertTrue(expected, result)

    def test_send_keyleft_command(self):
        command = 'MOVE_LEFT'
        expected = ['irsend SEND_ONCE {} {}'.format(self.__device, 'MOVE_LEFT')]
        result = self.__ir_sender.send(command, None)
        self.assertTrue(expected, result)

    # Repetition commands
    # Channel
    def test_composite_channelup_command(self):
        # command = 'CHANNEL_UP'

    def test_composite_channeldown_command(self):
        # command = 'CHANNEL_DOWN'

    # Volume
    def test_composite_volumeup_command(self):
        # command = 'VOLUME_UP'

    def test_composite_volumedown_command(self):
        # command = 'VOLUME_DOWN'

    # Move
    def test_composite_moveup_command(self):
        # command = 'MOVE_UP'

    def test_composite_movedown_command(self):
        # command = 'MOVE_DOWN'

    def test_composite_moveleft_command(self):
        # command = 'MOVE_LEFT'

    def test_composite_moveright_command(self):
        # command = 'MOVE_RIGHT'


    # Composite number commands
    def test_number_channels_command(self):
        # commands = 'KEY 0 to 1? '

    # test more commands and raw commands                               Done
    # test composite repetition commands (volume up, volume down, etc.) ToDo
    # test composite number commands (channel)                          ToDo