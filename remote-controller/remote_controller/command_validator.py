class CommandValidator:
    def __init__(self, device, commands, raw_commands):
        self.__device = device
        self.__commands = commands
        self.__raw_commands = raw_commands

    def validate_raw(self, command):
        # just check if command exists in raw-commands.yml
        pass

    def validate(self, command, value):
        # check if command exists in commands.yml
        # check if args are required
        # check if value is an int when applies
        pass
