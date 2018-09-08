import etcd


class Data(object):

    def __init__(self):
        pass

    def put(self, data, key='default_key'):
        client = etcd.Client(host='localhost', port=2379)
        # client.delete(key)
        client.write(key, data)

    def get(self, key='default_key'):
        client = etcd.Client(host='localhost', port=2379)
        o = client.get(key).value
        return o

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
