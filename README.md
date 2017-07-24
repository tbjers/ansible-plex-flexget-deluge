# Ansible Playbook for Plex/Flexget/Deluge system

Installs Plex Media Server, Flexget and Deluge for a fully automated media center.

## Requirements

If running against a Fedora 26 server, make sure that your local Ansible is at least 2.3.

```sh
$ pip install ansible -U
``` 

## Setup

```sh
$ ANSIBLE_NOCOWS=1 python setup.py <user>@<hostname>
```
