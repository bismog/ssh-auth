#!/usr/bin/env python

import os
import json
# from deploy import Compose
# from play import Playbook
from run_etcd_cmd import Deploy
from set_auth_cmd import Auth
from data import Data

PATH = os.path.dirname(os.path.abspath(__file__))


class SSHAuth(object):
    def __init__(self):
        pass

    def watch(self, host, port, key):
        d = Data(host=host, port=port)
        d.watch(key=key)
        data = json.loads(d.get(key=key))
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
    while True:
        ssh_auth.watch('localhost', 2379, 'nodes')
        ssh_auth.callback()

if __name__ == "__main__":
    main()
