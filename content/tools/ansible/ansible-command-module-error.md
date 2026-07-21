---
title: "[Solution] Ansible Command Module Error"
description: "Fix Ansible command module errors when shell commands fail to execute on remote hosts."
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

# Ansible Command Module Error

The Ansible `command` module fails to execute a shell command on the remote host.

```
FAILED! => {"changed": false, "msg": "AnsibleError: An error occurred"}
```

## Common Causes

- Command does not exist on the target host
- Insufficient permissions to run the command
- Pipe characters not supported in the command module
- Command has shell-specific syntax
- Environment variables not set

## How to Fix

### Use the Shell Module for Shell Syntax

```yaml
- name: Run command with pipes
  ansible.builtin.shell: cat /etc/passwd | grep deploy
  register: result

- name: Show output
  ansible.builtin.debug:
    var: result.stdout_lines
```

### Use Creates Parameter

```yaml
- name: Compile from source
  ansible.builtin.command: ./configure --prefix=/usr/local
  args:
    chdir: /tmp/app-1.0
    creates: /usr/local/bin/app
```

### Handle Missing Commands

```yaml
- name: Check if command exists
  ansible.builtin.command: which docker
  register: docker_check
  ignore_errors: true

- name: Install Docker if missing
  ansible.builtin.apt:
    name: docker.io
    state: present
  when: docker_check.rc != 0
```

## Examples

```yaml
- name: Various command module usage
  ansible.builtin.command: "{{ item }}"
  loop:
    - nginx -t
    - systemctl daemon-reload
    - journalctl --vacuum-time=7d
  register: cmd_results
  failed_when: false
```
