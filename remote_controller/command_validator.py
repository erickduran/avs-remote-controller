# command_validator.py
"""This is the definition of the CommandValidator class. This class validates if the command exists
and if the value is valid. This validation is necessary to avoid code injection.
"""
from remote_controller.errors import InvalidCommandError, InvalidArgumentError


class CommandValidator:
    def __init__(self, device, commands, raw_commands):
        self.__device = device
        self.__commands = commands
        self.__raw_commands = raw_commands

    # Validation of raw commands
    def validate_raw(self, command):
        if command not in self.__raw_commands['commands'].keys():
            raise InvalidCommandError('Command doesn\'t exist')
        return True

    # Validation of composite commands commands
    def validate(self, command, value):
        if command not in self.__commands['commands'].keys():
            raise InvalidCommandError('Command doesn\'t exist')

        # Validation of composite commands args
        if self.__commands['commands'][command]['args']:
            if self.__commands['commands'][command]['args']['OPTIONAL'] is False and value is None:
                raise InvalidArgumentError('Command\'s argument is required')

            # Currently, all values should be integers. Validating this
            if value is not None:
                try:
                    int(value)
                except ValueError:
                    raise InvalidArgumentError('Command\'s argument must be integer')
        return True

    # Check if a desired command exists
    def exists(self, command):
        if command in self.__raw_commands['commands'].keys():
            return 'raw_command', command, self.__raw_commands['commands'][command]['description']
        elif command in self.__commands['commands'].keys():
            return 'command', command, self.__commands['commands'][command]['description']
        else:
            raise InvalidCommandError('Command doesn\'t exist')
