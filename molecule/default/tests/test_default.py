import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_default_hostname(host):
    o = host.check_output('hostname -f')
    assert o == 'molecule.testdomain'


def test_default_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.contains('127.0.0.1 localhost')
