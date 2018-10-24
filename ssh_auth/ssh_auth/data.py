# import etcd
from etcd import Client
from utils import logging

logger = logging.getLogger('data')


class Data(Client):

    def __init__(self, host=None, port=None):
        logger.debug('Initiate Data')
        self._host = host or 'localhost'
        self._port = port or 2379
        super(Data, self).__init__(host=self._host, port=self._port)

    # def write_key(self, data, key='default_key'):
    #     self.write(key, data)

    # def read_key(self, key='default_key'):
    #     o = self.get(key).value
    #     return o

    @staticmethod
    def dump(self, nodes, file='/tmp/nodes.txt'):
        with open(file, 'w+') as f:
            f.writelines(['%s\n' % item for item in nodes])

def main():
    d = Data()
    d.write('{"aa": 1, "bb": 2}')
    logger.info(d.get())


if __name__ == "__main__":
    main()
