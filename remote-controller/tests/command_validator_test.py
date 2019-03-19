import os

import unittest
import yaml

from remote_controller.command_validator import CommandValidator

dir = os.path.dirname(__file__)

RAW_COMMANDS_PATH = '../resources/commands/raw-commands.yml'
COMMANDS_PATH = '../resources/commands/commands.yml'


class IRSenderTest(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(dir, RAW_COMMANDS_PATH), 'r') as stream:
            try:
                raw_commands = yaml.load(stream)
            except yaml.YAMLError as exception:
                raw_commands = None
                print(exception)

        with open(os.path.join(dir, COMMANDS_PATH), 'r') as stream:
            try:
                commands = yaml.load(stream)
            except yaml.YAMLError as exception:
                commands = None
                print(exception)

        self.__device = 'lg'
        self.__command_validator = CommandValidator(self.__device, commands, raw_commands)

    def test_validate_valid_power_command(self):
        command = 'POWER'
        result = self.__command_validator.validate(command, None)
        self.assertTrue(result)

    def test_validate_raw_valid_power_command(self):
        command = 'KEY_POWER'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_exists_for_existing_raw_power_command(self):
        command = 'KEY_POWER'
        result = self.__command_validator.exists(command)
        description = 'This command powers on/off the TV.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_validate_valid_ok_command(self):
        command = 'OK'
        result = self.__command_validator.validate(command, None)
        self.assertTrue(result)

    def test_validate_raw_valid_ok_command(self):
        command = 'KEY_OK'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_exists_for_existing_raw_ok_command(self):
        command = 'KEY_OK'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the OK key.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_validate_valid_channel_up_command(self):
        command = 'CHANNEL_UP'
        result = self.__command_validator.validate(command, None)
        self.assertTrue(result)

    def test_validate_raw_valid_channel_up_command(self):
        command = 'KEY_CHANNELUP'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_exists_for_existing_raw_channel_up_command(self):
        command = 'KEY_CHANNELUP'
        result = self.__command_validator.exists(command)
        description = 'This command turns the channel up by a value of 1.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    # Test for number keys

    def test_validate_raw_valid_0_command(self):
        command = 'KEY_0'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_validate_raw_valid_1_command(self):
        command = 'KEY_1'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_validate_raw_valid_3_command(self):
        command = 'KEY_3'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_validate_raw_valid_4_command(self):
        command = 'KEY_4'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_validate_raw_valid_5_command(self):
        command = 'KEY_5'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_validate_raw_valid_6_command(self):
        command = 'KEY_6'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_validate_raw_valid_7_command(self):
        command = 'KEY_7'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_validate_raw_valid_8_command(self):
        command = 'KEY_8'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_validate_raw_valid_9_command(self):
        command = 'KEY_9'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    # Test for exists number keys

    def test_exists_for_existing_raw_0_command(self):
        command = 'KEY_0'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the 0 number key.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_exists_for_existing_raw_1_command(self):
        command = 'KEY_1'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the 1 number key.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_exists_for_existing_raw_2_command(self):
        command = 'KEY_2'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the 2 number key.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_exists_for_existing_raw_3_command(self):
        command = 'KEY_3'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the 3 number key.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_exists_for_existing_raw_4_command(self):
        command = 'KEY_4'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the 4 number key.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_exists_for_existing_raw_5_command(self):
        command = 'KEY_4'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the 4 number key.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_exists_for_existing_raw_6_command(self):
        command = 'KEY_6'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the 6 number key.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_exists_for_existing_raw_7_command(self):
        command = 'KEY_7'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the 7 number key.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_exists_for_existing_raw_8_command(self):
        command = 'KEY_8'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the 8 number key.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_exists_for_existing_raw_9_command(self):
        command = 'KEY_9'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the 9 number key.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    # TODO
    # test more commands and raw commands
    # test not existing commands and raw commands with validate and validate_raw
    # test commands with arguments
    # test commands with arguments fail because of no arguments
    # test commands with arguments sending invalid argument (string instead of int)
    # test mode existing commands and raw commands
    # test not existing commands and raw commands with exists
