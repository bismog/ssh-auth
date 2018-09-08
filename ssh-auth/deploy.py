

import os
from jinja2 import Environment, FileSystemLoader
import subprocess

PATH = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(os.path.join(PATH, 'templates')))


class Compose(object):

    def __init__(self):
        pass

    def get_compose_data(self, context, template):
        p,f = os.path.split(template)
        env = Environment(loader=FileSystemLoader(p))
        compose_data = env.get_template(f)
        return compose_data.render(context)
    
    
    def gen_compose_file(self, compose_temp='docker-compose.yml.template'):
        args = {
           'etcd1': '172.19.1.10',
           'etcd2': '172.19.1.11',
           'etcd3': '172.19.1.12'
        }
        data = self.get_compose_data(args, compose_temp)
        compose_file,_ = os.path.splitext(compose_temp)
        with open(compose_file, 'w') as f:
            f.write(data)

    def run(self, compose_file):
        cmd = "docker-compose -f {} up -d".format(compose_file)
        subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT)


def main():
    c = Compose()
    # c.gen_compose_file('./docker-compose.d/docker-compose.etcd1.yml.template')
    # c.gen_compose_file('./docker-compose.d/docker-compose.etcd2.yml.template')
    # c.gen_compose_file('./docker-compose.d/docker-compose.etcd3.yml.template')
    # c.run('./docker-compose.d/docker-compose.etcd1.yml')
    c.run(PATH+'/docker-compose.d/docker-compose.single-node.yml')

if __name__ == "__main__":
    main()
