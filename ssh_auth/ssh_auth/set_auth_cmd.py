#!/usr/bin/env python
# from ansible.playbook import Playbook
# pb = Playbook(playbook='/tmp/ls.yml')
# pb.run()


# run ansible-playbook via subprocess.check_output 
# Later I wish I'll update the calling to python API

import os
import subprocess
from utils import logging

logger = logging.getLogger(__name__)

PATH = os.path.dirname(os.path.abspath(__file__))
ANSIBLE_CONFIG_PATH=PATH+'/playbook'


class Auth(object):

    def __init__(self, inventory=None, playbook=None, log='/tmp/ansible.log'):
        self.inventory = inventory or '{}/{}'.format(PATH, 'playbook/hosts')
        self.playbook = playbook or '{}/{}'.format(PATH, 'playbook/auth.yml')
        self.ansible_log = log

    def run(self):
        cmd = 'ansible-playbook -i {} {}'.format(self.inventory, self.playbook)
        # subprocess.check_output(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info('Run ansible playbook')
        with open(self.ansible_log, 'a') as f:
            os.putenv('ANSIBLE_CONFIG', ANSIBLE_CONFIG_PATH)
            p = subprocess.Popen(cmd.split(), stdout=f, stderr=f)
            # p.communicate()
            # o,e = p.communicate()

def main():
    a = Auth()
    a.run()

if __name__ == "__main__":
    main()
