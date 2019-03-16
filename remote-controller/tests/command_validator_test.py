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

    # TODO
    # test more commands and raw commands
    # test not existing commands and raw commands with validate and validate_raw
    # test commands with arguments
    # test commands with arguments fail because of no arguments
    # test commands with arguments sending invalid argument (string instead of int)
    # test mode existing commands and raw commands
    # test not existing commands and raw commands with exists


