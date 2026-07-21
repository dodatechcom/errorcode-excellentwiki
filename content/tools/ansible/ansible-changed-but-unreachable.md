---
title: "[Solution] Ansible Changed But Unreachable Host"
description: "Fix Ansible unreachable host errors after a task reports changed status during playbook execution."
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

# Ansible Changed But Unreachable Host

Ansible reports a task as changed but then marks the host as unreachable.

```
fatal: [webserver1]: FAILED! => {"changed": true, "msg": "unreachable"}
```

## Common Causes

- SSH connection dropped after task execution
- Host rebooted during task
- Network timeout between control node and managed host
- Firewall rule changed blocking SSH
- Host went into standby mode

## How to Fix

### Add Connection Keepalive

```yaml
- name: Configure webserver
  hosts: webservers
  vars:
    ansible_ssh_args: "-o ServerAliveInterval=60 -o ServerAliveCountMax=3"
  tasks:
    - name: Deploy application
      ansible.builtin.copy:
        src: app.conf
        dest: /etc/app.conf
```

### Increase SSH Timeout

```ini
# ansible.cfg
[ssh_connection]
pipelining = True
ssh_args = -o ServerAliveInterval=60 -o ServerAliveCountMax=3 -o ControlMaster=auto
```

### Add Rescue Block

```yaml
- name: Deploy with recovery
  block:
    - name: Run deployment
      ansible.builtin.command: /opt/deploy.sh
      register: deploy_result
  rescue:
    - name: Check host status
      ansible.builtin.ping:
    - name: Restart SSH if needed
      ansible.builtin.service:
        name: sshd
        state: restarted
```

## Examples

```yaml
- name: Tasks with connection recovery
  hosts: all
  serial: 1
  max_fail_percentage: 0
  tasks:
    - name: Update packages
      ansible.builtin.apt:
        upgrade: dist
        update_cache: true

    - name: Reboot if required
      ansible.builtin.reboot:
        reboot_timeout: 300
```
