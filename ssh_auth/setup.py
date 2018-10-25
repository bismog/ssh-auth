from setuptools import setup
from setuptools.command.install import install
from shutil import copyfile
import subprocess

class myinstall(install):
    """ My Installation scripts"""
    def run(self):
        install.run(self)
        # print self.install_lib
        # print "Hello, this is my installation script"
        # Copy ssh-auth.service to system service path
        src = ''.join((self.install_lib, 'ssh_auth/system.d/ssh-auth.service'))
        dst = '/etc/systemd/system/ssh-auth.service'
        copyfile(src, dst)

        # run daemon-reload
        cmd = 'systemctl daemon-reload'
        p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        o,e = p.communicate()

setup(name='ssh_auth',
    version='0.1',
    description='Setup SSH mutual authorization with etcd key-value',
    url='https://github.com/bismog/ssh-auth',
    author='bismog',
    author_email='bismogg@gmail.com',
    license='MIT',
    packages=['ssh_auth'],
    package_data={
        'ssh_auth':['playbook.d/*', 'system.d/ssh-auth.service', '*.yaml'],
    },
    scripts=['ssh_auth/bin/ssh-auth'],
    cmdclass={
        'install': myinstall,
    },
    zip_safe=False)
