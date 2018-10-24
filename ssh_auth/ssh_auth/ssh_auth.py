#!/usr/bin/env python

import os
import json
# from deploy import Compose
# from play import Playbook
# from run_etcd_cmd import Deploy
from set_auth_cmd import Auth
from data import Data
from utils import logging

PATH = os.path.dirname(os.path.abspath(__file__))

logger = logging.getLogger('ssh_auth')

class SSHAuth(object):
    def __init__(self):
        self.server = 'localhost'
        self.port = 12379
        self.key = 'nodes'
        self.former = set()

    def watch(self, inst):
        inst.watch(key=self.key)
        cur_nodes = set(inst.get(key=self.key).value.split(','))
        logger.debug(cur_nodes)
        diff = cur_nodes.difference(self.former)
        self.former = self.former.union(cur_nodes)
        logger.debug('diff is {}'.format(diff))
        return diff

    def gen_hosts(self, nodes):
        fd = open('./playbook/hosts', 'w+')
        fd.write('[cluster]\n')
        for node in nodes:
            host_line = '{} ansible_ssh_user=bismog ansible_ssh_pass=***'.format(node)
            fd.write(host_line)
        fd.close()

    def callback(self, diff):
        # Update 'hosts' file with diff
        logger.debug('Update hosts file')

        a = Auth()
        a.run()

def main():
    logger.info('Program running...')
    s = SSHAuth()
    d = Data(host=s.server, port=s.port)
    s.nodes = d.get(key=s.key).value
    logger.debug(s.nodes)
    while True:
        diff = s.watch(d)
        if not diff:
            logger.info('No valid change occurred')
            continue
        s.callback(diff)

if __name__ == "__main__":
    main()
