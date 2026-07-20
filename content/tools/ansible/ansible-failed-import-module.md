---
title: "[Solution] Ansible Failed to Import Module Library"
description: "Fix Ansible Python module import failures on managed nodes"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot import a required Python module on the remote host.

```
FAILED! => "Failed to import the required Python library (paramiko)"
```

## Common Causes

- Missing Python library on remote host
- Wrong Python interpreter selected
- pip not installed
- Virtual environment issues

## How to Fix

```bash
sudo apt-get install python3-pip python3-paramiko
```

```yaml
[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

```yaml
- name: Install missing libraries
  ansible.builtin.pip:
    name:
      - paramiko
      - pyyaml
    executable: pip3
```
