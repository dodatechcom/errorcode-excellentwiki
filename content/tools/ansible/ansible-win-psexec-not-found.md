---
title: "[Solution] Ansible win_psexec Not Found"
description: "Fix Ansible win_psexec module errors when managing remote Windows processes"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible win_psexec module is not available or not working.

```
ERROR! The 'ansible.windows.win_psexec' module is not available
```

## Common Causes

- ansible.windows collection not installed
- PSExec not available on target
- Module name incorrect

## How to Fix

```bash
ansible-galaxy collection install ansible.windows
```

```yaml
- name: Run command via PSExec
  ansible.windows.win_psexec:
    command: whoami
    host: 10.0.0.50
    username: administrator
    password: "{{ vault_win_password }}"
    interactive: true
```

```yaml
# Full example
- name: Execute remote command
  ansible.windows.win_psexec:
    command: "cmd.exe /c echo hello > C:\\temp\\output.txt"
    host: "{{ target_host }}"
    username: "{{ win_user }}"
    password: "{{ win_password }}"
    executable: C:\\Windows\\System32\\psexec.exe
    elevated: true
```
