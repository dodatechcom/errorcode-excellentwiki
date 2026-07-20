---
title: "[Solution] Ansible Async Job ID Not Found"
description: "Fix Ansible async_status errors when job ID cannot be found"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible async_status cannot find the specified job ID.

```
ERROR! Could not find job ID '12345678901234'
```

## Common Causes

- Job ID expired
- Job ID incorrect
- Async control files cleaned up
- PID file removed

## How to Fix

```yaml
- name: Start async task
  ansible.builtin.command: /opt/scripts/task.sh
  async: 3600
  poll: 0
  register: async_task

- name: Wait for task
  ansible.builtin.async_status:
    jid: "{{ async_task.ansible_job_id }}"
  register: task_status
  until: task_status.finished
  retries: 60
  delay: 60
```
