---
title: "[Solution] Ansible Connection Timeout"
description: "Diagnose and fix Ansible SSH connection timeout errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible connection timeout occurs when the controller cannot establish a connection to the managed host within the configured time limit.

```
UNREACHABLE! => {"changed": false, "msg": "Failed to connect to the host via ssh: Connection timed out"}
```

## Common Causes

- Host is down or not reachable on the network
- Firewall blocking SSH port (default 22)
- Incorrect host IP address or DNS name
- SSH service not running on remote host
- Network latency too high

## How to Fix

```yaml
# In inventory
[all]
webserver ansible_host=192.168.1.100 ansible_timeout=30

# In ansible.cfg
[defaults]
timeout = 30

# In playbook
- hosts: all
  gather_facts: false
  vars:
    ansible_timeout: 60
  tasks:
    - name: Ping test
      ansible.builtin.ping:
```
