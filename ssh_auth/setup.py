from setuptools import setup
setup(name='ssh-auth',
    version='0.1',
    descrition='Setup SSH mutual authorization with etcd key-value',
    url='https://github.com/bismog/ssh-auth',
    author='bismog',
    author_email='bismogg@gmail.com',
    license='MIT',
    packages=['ssh-auth', 'python-etcd'],
    zip_safe=False)
