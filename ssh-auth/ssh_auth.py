
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

    def gen_hosts(self, data):
        pass

    def callback(self, data):
        a = Auth()
        a.run()

def main():
    # Deploy Etcd cluster
    # c = Compose()
    # compose_temp = '{}/docker-compose.d/docker-compose.etcd1.yml.template'.format(PATH)
    # print(compose_temp)
    # c.gen_compose_file(compose_temp)
    # # compose_file = '{}docker-compose.d/docker-compose.etcd1.yml'.format(PATH)
    # compose_file = '{}/docker-compose.d/docker-compose.single-node.yml'.format(PATH)
    # c.run(compose_file)
    # print('run Etcd ok')
    d = Deploy()
    d.run()

    # # Append nodes
    # d = Data()
    # nodes = ["192.168.3.45"]
    # snodes = json.dumps(nodes)
    # d.put(snodes, key='nodes')
    # # print(d.get(key='nodes'))
    # print('Update data ok')
    # data = json.loads(d.get(key='nodes'))
    # # print(type(data))

    # # Setup mutual authorization
    # # pb = Playbook(data, playbooks=['./playbook/auth.yml'])
    # # print(pb.inventory)
    # # # hack for verbosity
    # # from ansible.utils.display import Display
    # # display = Display(verbosity=7)
    # # import __main__ as main
    # # setattr(main, "display", display)

    # # # import pdb;pdb.set_trace()
    # # pb.run()
    # # print('Auth ok')

    # a = Auth()
    # a.run()

    # 
    ssh_auth = SSHAuth()
    ssh_auth.watch('192.168.3.45', 2379, 'nodes')

if __name__ == "__main__":
    main()
