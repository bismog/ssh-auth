#!/usr/bin/env python

import os
import json
# from deploy import Compose
# from play import Playbook
# from run_etcd_cmd import Deploy
from set_auth_cmd import Auth
from data import Data

PATH = os.path.dirname(os.path.abspath(__file__))


class SSHAuth(object):
    def __init__(self):
        self.server = 'localhost'
        self.port = 2379
        self.key = 'nodes'
        self.d = Data(host=self.server, port=self.port)
        self.nodes = self.d.get(key=self.key)
        print json.loads(self.nodes)

    def watch(self, host, port):
        self.d.watch(key=self.key)
        cur_nodes = self.d.get(key=self.key)
        data = json.loads(cur_nodes)
        print data
        return data

    def gen_hosts(self, nodes):
        fd = open('./playbook/hosts', 'w+')
        fd.write('[cluster]\n')
        for node in nodes:
            host_line = '{} ansible_ssh_user=bismog ansible_ssh_pass=***'.format(node)
            fd.write(host_line)
        fd.close()

    def callback(self, data):
        a = Auth()
        a.run()

def main():
    ssh_auth = SSHAuth()
    # while True:
    #     ssh_auth.watch('localhost', 2379)
    #     ssh_auth.callback()

if __name__ == "__main__":
    main()
