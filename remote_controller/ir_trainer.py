import os


class IRTrainer:

    @staticmethod
    def run():
        print('Please stop the lirc service by running:')
        print('sudo service lircd stop')

        name = input('Name of the new device: ')
        name = name.lower()

        command = 'irrecord -d /dev/lirc0'
        os.system(command)

        copy_command = 'sudo cp {}.lircd.conf /etc/lirc/lircd.conf.d/{}.lircd.conf'.format(name, name)
        print('Please copy your lirc configuration file by running:')
        print(copy_command)
