class IRController:
    def __init__(self):
        pass

    def send_command(self, command):
        print('Sending {} command...'.format(command))

    def power_on(self):
        print('Powering on...')

    def power_off(self):
        print('Powering off...')
