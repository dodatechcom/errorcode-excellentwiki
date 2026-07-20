---
title: "[Solution] Ansible Async Task Not Supported"
description: "Fix Ansible async execution errors for unsupported task types"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot run the specified task asynchronously.

```
ERROR! Async is not supported for this task type
```

## Common Causes

- Module does not support async mode
- Local connection with async
- Module requires synchronous execution

## How to Fix

```yaml
# Modules that support async: command, shell, script, raw, expect
# Modules that DON'T: copy, template, file, service, systemd

- name: Long-running task
  ansible.builtin.command: /opt/scripts/compute.sh
  async: 3600
  poll: 0
  register: async_result

# Alternative for non-async tasks
- name: Wait for completion
  ansible.builtin.wait_for:
    path: /tmp/long_task.pid
    state: absent
    timeout: 3600
```
