import os

import unittest
import yaml

from remote_controller.errors import InvalidCommandError, InvalidArgumentError
from remote_controller.command_validator import CommandValidator

FILE_PATH = os.path.dirname(__file__)

RAW_COMMANDS_PATH = '../resources/commands/raw-commands.yml'
COMMANDS_PATH = '../resources/commands/commands.yml'


class IRSenderTest(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(FILE_PATH, RAW_COMMANDS_PATH), 'r') as stream:
            try:
                raw_commands = yaml.load(stream)
            except yaml.YAMLError as exception:
                raw_commands = None
                print(exception)

        with open(os.path.join(FILE_PATH, COMMANDS_PATH), 'r') as stream:
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

    def test_validate_valid_channel_down_command(self):
        command = 'CHANNEL_DOWN'
        result = self.__command_validator.validate(command, None)
        self.assertTrue(result)

    def test_validate_raw_valid_channel_down_command(self):
        command = 'KEY_CHANNELDOWN'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_exists_for_existing_raw_channel_down_command(self):
        command = 'KEY_CHANNELDOWN'
        result = self.__command_validator.exists(command)
        description = 'This command turns the channel down by a value of 1.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_validate_valid_volume_up_command(self):
        command = 'VOLUME_UP'
        result = self.__command_validator.validate(command, None)
        self.assertTrue(result)

    def test_validate_raw_valid_volume_up_command(self):
        command = 'KEY_VOLUMEUP'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_exists_for_existing_raw_volume_up_command(self):
        command = 'KEY_VOLUMEUP'
        result = self.__command_validator.exists(command)
        description = 'This command turns the volume up by a value of 1.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_validate_valid_volume_down_command(self):
        command = 'VOLUME_DOWN'
        result = self.__command_validator.validate(command, None)
        self.assertTrue(result)

    def test_validate_raw_valid_volume_down_command(self):
        command = 'KEY_VOLUMEDOWN'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_exists_for_existing_raw_volume_down_command(self):
        command = 'KEY_VOLUMEDOWN'
        result = self.__command_validator.exists(command)
        description = 'This command turns the volume down by a value of 1.'
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

    def test_validate_valid_left_command(self):
        command = 'MOVE_LEFT'
        result = self.__command_validator.validate(command, None)
        self.assertTrue(result)

    def test_validate_raw_valid_left_command(self):
        command = 'KEY_LEFT'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_exists_for_existing_raw_left_command(self):
        command = 'KEY_LEFT'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the LEFT selection arrow.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_validate_valid_right_command(self):
        command = 'MOVE_RIGHT'
        result = self.__command_validator.validate(command, None)
        self.assertTrue(result)

    def test_validate_raw_valid_right_command(self):
        command = 'KEY_RIGHT'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_exists_for_existing_raw_right_command(self):
        command = 'KEY_RIGHT'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the RIGHT selection arrow.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_validate_valid_up_command(self):
        command = 'MOVE_LEFT'
        result = self.__command_validator.validate(command, None)
        self.assertTrue(result)

    def test_validate_raw_valid_up_command(self):
        command = 'KEY_UP'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_exists_for_existing_raw_up_command(self):
        command = 'KEY_UP'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the UP selection arrow.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

    def test_validate_valid_down_command(self):
        command = 'MOVE_DOWN'
        result = self.__command_validator.validate(command, None)
        self.assertTrue(result)

    def test_validate_raw_valid_down_command(self):
        command = 'KEY_DOWN'
        result = self.__command_validator.validate_raw(command)
        self.assertTrue(result)

    def test_exists_for_existing_raw_down_command(self):
        command = 'KEY_DOWN'
        result = self.__command_validator.exists(command)
        description = 'This command invokes the DOWN selection arrow.'
        expected = ('raw_command', command, description)
        self.assertEqual(result, expected)

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

    def test_exists_for_not_existing_pawer_command(self):
        command = 'PAWER'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.exists(command)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_exists_for_not_existing_ko_command(self):
        command = 'KO'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.exists(command)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_exists_for_not_existing_minu_command(self):
        command = 'MINU'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.exists(command)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_exists_for_not_existing_raw_10_command(self):
        command = 'KEY_10'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.exists(command)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_exists_for_not_existing_raw_20_command(self):
        command = 'KEY_20'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.exists(command)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_exists_for_not_existing_raw_2o_command(self):
        command = 'KEY_2o'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.exists(command)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_exists_for_not_existing_raw_ko_command(self):
        command = 'KEY_KO'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.exists(command)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_exists_for_not_existing_raw_minu_command(self):
        command = 'KEY_MINU'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.exists(command)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_exists_for_not_existing_raw_pawer_command(self):
        command = 'KEY_PAWER'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.exists(command)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_validate_invalid_pawer_command(self):
        command = 'PAWER'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.validate(command, None)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_validate_raw_invalid_pawer_command(self):
        command = 'KEY_PAWER'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.validate_raw(command)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_validate_invalid_ko_command(self):
        command = 'KO'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.validate(command, None)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_validate_raw_invalid_ko_command(self):
        command = 'KEY_KO'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.validate_raw(command)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_validate_invalid_mut_command(self):
        command = 'MUT'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.validate(command, None)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_validate_raw_invalid_mut_command(self):
        command = 'KEY_MUT'
        with self.assertRaises(InvalidCommandError) as error:
            self.__command_validator.validate_raw(command)
        self.assertTrue('Command doesn\'t exist' in str(error.exception))

    def test_validate_valid_volume_up_10_command(self):
        command = 'VOLUME_UP'
        result = self.__command_validator.validate(command, 10)
        self.assertTrue(result)

    def test_validate_invalid_volume_up_1o_command(self):
        command = 'VOLUME_UP'
        with self.assertRaises(InvalidArgumentError) as error:
            self.__command_validator.validate(command, '1o')
        self.assertTrue('Command\'s argument must be integer' in str(error.exception))

    def test_validate_valid_channel_up_10_command(self):
        command = 'CHANNEL_UP'
        result = self.__command_validator.validate(command, 10)
        self.assertTrue(result)

    def test_validate_invalid_move_up_1o_command(self):
        command = 'MOVE_UP'
        with self.assertRaises(InvalidArgumentError) as error:
            self.__command_validator.validate(command, '1o')
        self.assertTrue('Command\'s argument must be integer' in str(error.exception))

    def test_validate_invalid_channel_command(self):
        command = 'CHANNEL'
        with self.assertRaises(InvalidArgumentError) as error:
            self.__command_validator.validate(command, None)
        self.assertTrue('Command\'s argument is required' in str(error.exception))
