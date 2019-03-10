class CommandValidator:
    def __init__(self, device, commands, raw_commands):
        self.__device = device
        self.__commands = commands
        self.__raw_commands = raw_commands

    def validate_raw(self, command):
        # just check if command exists in raw-commands.yml
        if command in self.__raw_commands['commands'].keys():
            print(command + " is a raw_command")
        else:
            pass

    def validate(self, command, value):
        # check if command exists in commands.yml
        # check if args are required
        # check if value is an int when applies

        if command in self.__commands['commands'].keys():
            print(command + " is a command")
        try:
            if(str.isdecimal(value) == False):
                print("Given argument is not decimal")
            if  self.__commands['commands'][command]['args']['OPTIONAL'] == False:
                print("Command requiere argument")
            else:
                print("Command with optional arguments")

        except:
            print("Command without optional arguments")