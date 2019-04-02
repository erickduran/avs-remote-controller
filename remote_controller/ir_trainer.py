import os


class IRTrainer:

    @staticmethod
    def run(device):
        print('Please stop the lirc service by running:')
        print('sudo service lircd stop')

        command = 'irrecord -d /dev/lirc0'
        os.system(command)

        copy_command = 'sudo cp {}.lircd.conf /etc/lirc/lircd.conf.d/{}.lircd.conf'.format(device, device)
        print('Please copy your lirc configuration file by running:')
        print(copy_command)
