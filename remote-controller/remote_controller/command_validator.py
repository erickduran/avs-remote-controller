from .errors import InvalidCommandError, InvalidArgumentError


class CommandValidator:
    def __init__(self, device, commands, raw_commands):
        self.__device = device
        self.__commands = commands
        self.__raw_commands = raw_commands

    def validate_raw(self, command):
        if command not in self.__raw_commands['commands'].keys():
            raise InvalidCommandError('Command doesn\'t exist')

    def validate(self, command, value):
        if command not in self.__commands['commands'].keys():
            raise InvalidCommandError('Command doesn\'t exist')

        if self.__commands['commands'][command]['args']:
            if self.__commands['commands'][command]['args']['OPTIONAL'] is False and value is None:
                raise InvalidArgumentError('Command\'s argument is required')

            if value is not None:
                try:
                    int(value)
                except ValueError:
                    raise InvalidArgumentError('Command\'s argument must be interger')
