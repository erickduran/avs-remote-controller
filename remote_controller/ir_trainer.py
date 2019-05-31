# ir_trainer.py
"""This is the definition of the IRTrainer class. This class is a static class that simply executes
the necessary lircd commands to perform the training.
"""
import os


class IRTrainer:

    @staticmethod
    def run(device):
        print('Please stop the lirc service by running:')
        print('sudo service lircd stop')

        # Bash command to execute
        command = 'irrecord -d /dev/lirc0'
        os.system(command)

        # Help to perform the copy command (not executed because it needs sudo)
        copy_command = 'sudo cp {}.lircd.conf /etc/lirc/lircd.conf.d/{}.lircd.conf'.format(device, device)
        print('Please copy your lirc configuration file by running:')
        print(copy_command)
