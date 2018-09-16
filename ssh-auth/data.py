# import etcd
from etcd import Client


class Data(Client):

    def __init__(self, host=None, port=None):
        host = 'localhost' if host==None else host
        port = 2379 if port==None else port
        super(Data, self).__init__(host=host, port=port)

    def put(self, data, key='default_key'):
        # client = etcd.Client(host='localhost', port=2379)
        # # client.delete(key)
        # client.write(key, data)
        self.write(key, data)

    def get(self, key='default_key'):
        # client = etcd.Client(host='localhost', port=2379)
        # o = client.get(key).value
        o = self.get(key).value
        return o

    @staticmethod
    def dump(self, nodes, file='/tmp/nodes.txt'):
        with open(file, 'w+') as f:
            f.writelines(['%s\n' % item for item in nodes])

def main():
    d = Data()
    # d.put('hello bismog')
    # print(d.get().value)
    d.put('{"aa": 1, "bb": 2}')
    print(d.get())


if __name__ == "__main__":
    main()
