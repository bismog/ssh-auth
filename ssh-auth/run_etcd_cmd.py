#!/usr/bin/env python
# from ansible.playbook import Playbook
# pb = Playbook(playbook='/tmp/ls.yml')
# pb.run()


# run ansible-playbook via subprocess.check_output 
# Later I wish I'll update the calling to python API

import os
import subprocess

PATH = os.path.dirname(os.path.abspath(__file__))
ANSIBLE_CONFIG_PATH=PATH+'/playbook'


class Deploy(object):

    def __init__(self):
        pass

    def run(self, play='playbook/etcd.yml', log='/tmp/ansible.log'):
        cmd = 'ansible-playbook {}/{}'.format(PATH, play)
        # subprocess.check_output(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        with open(log, 'w+') as f:
            os.putenv('ANSIBLE_CONFIG', ANSIBLE_CONFIG_PATH)
            p = subprocess.Popen(cmd.split(), stdout=f, stderr=f)
            # p.communicate()
            # o,e = p.communicate()
            # print o
            # print e

def main():
    d = Deploy()
    d.run()

if __name__ == "__main__":
    main()
