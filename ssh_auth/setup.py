from setuptools import setup
from setuptools.command.install import install

class myinstall(install):
    """ My Installation scripts"""
    def run(self):
        print "Hello, this is my installation script"
        install.run(self)

setup(name='ssh_auth',
    version='0.1',
    description='Setup SSH mutual authorization with etcd key-value',
    url='https://github.com/bismog/ssh-auth',
    author='bismog',
    author_email='bismogg@gmail.com',
    license='MIT',
    packages=['ssh_auth'],
    package_data={
        'ssh_auth':['playbook.d/*',],
    },
    scripts=['ssh_auth/etc/systemd/system/multi-user.target.wants/ssh_auth.service'],
    cmdclass={
        'install': myinstall,
    },
    zip_safe=False)
