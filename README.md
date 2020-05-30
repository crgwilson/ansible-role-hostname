# Ansible role: Hostname

![Molecule Test](https://github.com/crgwilson/ansible-role-hostname/workflows/Molecule%20Test/badge.svg)

Configure the hostname of a linux host

* Set the hostname via `hostnamectl`
* Update the hosts file with the new hostname

## Variables

| Name | Default | Description |
| ---- | ------- | ----------- |
| `hostname_fqdn` | `localhost.localdomain` | The FQDN to set as the hostname |
| `hostname_refresh_facts` | `true` | Gather facts again after changing the hostname? |

## Testing

Testing for this project is setup using [Molecule](https://molecule.readthedocs.io/en/stable/) & [Vagrant](https://www.vagrantup.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```
