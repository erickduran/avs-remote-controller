import os


class IRTrainer:
    @staticmethod
    def ir_trainer():
        bash_kill_command = 'sudo service lircd stop'
        print('killing lircd service: ')
        print(bash_kill_command)
        os.system(bash_kill_command)
        name = input('Name of the new device: (name will be converted to lowercase)')
        name = name.lower()
        bash_train_command = 'irrecord -d /dev/lirc0'
        os.system(bash_train_command)
        bash_copy_command = 'sudo cp {}.lircd.conf /etc/lirc/lircd.conf.d/{}.lircd.conf'.format(name, name)
        os.system(bash_copy_command)
