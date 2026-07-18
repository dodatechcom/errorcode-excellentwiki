---
title: "[Solution] Ansible Check Mode Failed Not Supported Error Fix"
description: "Fix Ansible check mode errors when playbooks are not compatible with dry-run. Enable check mode support in tasks and roles."
tools: ["ansible"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Ansible Check Mode Failed Not Supported Error Fix

The `check mode failed` or `not supported` error occurs when running Ansible in dry-run mode (`--check`) and a task or module does not support check mode.

## What This Error Means

Ansible check mode simulates changes without applying them. When a module lacks check mode support, or a task is explicitly marked as check mode incompatible, the playbook fails.

A typical error:

```
fatal: [web1]: FAILED! => {"msg": "check mode is not supported for this task"}
```

## Why It Happens

Common causes include:

- **Module does not support check mode** — Some modules cannot simulate changes.
- **Task explicitly disabled check mode** — Using `check_mode: no` or `check_mode: false`.
- **Custom modules without check support** — Third-party modules missing check logic.
- **Shell/command modules** — These always execute even in check mode unless configured.
- **Missing `changed_when`** — Tasks cannot determine if they would change anything.

## How to Fix It

### Fix 1: Skip tasks that do not support check mode

```yaml
# RIGHT: Skip task in check mode
- name: Run database migration
  command: /opt/app/migrate.sh
  check_mode: no
  tags: always
```

### Fix 2: Use changed_when for command tasks

```yaml
# RIGHT: Define when task reports changes
- name: Check disk space
  command: df -h
  register: disk_check
  changed_when: false
  check_mode: yes
```

### Fix 3: Handle check mode in roles

```yaml
# RIGHT: Conditional tasks based on check mode
- name: Deploy application
  ansible.builtin.copy:
    src: app.tar.gz
    dest: /opt/app/
  when: not ansible_check_mode

- name: Verify deployment
  ansible.builtin.stat:
    path: /opt/app/app.tar.gz
  register: app_stat
```

### Fix 4: Use diff mode with check

```bash
# RIGHT: Show what would change
ansible-playbook playbook.yml --check --diff
```

### Fix 5: Allow check mode failures gracefully

```yaml
# RIGHT: Ignore check mode errors
- name: Unreliable task
  command: /opt/app/setup.sh
  check_mode: no
  ignore_errors: yes
  failed_when: false
```

## Common Mistakes

- **Assuming all modules support check mode** — Verify module documentation.
- **Not testing playbooks with --check** — Always test with check mode first.
- **Forgetting `check_mode: no` for critical tasks** — Mark irreversible tasks appropriately.

## Related Pages

- [Ansible Host Key Error](ansible-host-key-error) — SSH host key issues
- [Ansible Connection Refused](ansible-connection-refused) — Connection problems
- [Ansible Permission Denied](ansible-permission-denied-become) — Privilege escalation errors
