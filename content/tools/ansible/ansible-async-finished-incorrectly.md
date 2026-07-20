---
title: "[Solution] Ansible Async Task Finished Incorrectly"
description: "Fix Ansible async task completion status errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible async task finished but not as expected.

```
ERROR! Async task failed with unexpected status
```

## Common Causes

- Task returned error code
- Task was killed by system
- Task timed out silently
- Output not captured correctly

## How to Fix

```yaml
- name: Start task
  ansible.builtin.command: /opt/scripts/task.sh
  async: 3600
  poll: 0
  register: async_result

- name: Wait and check
  ansible.builtin.async_status:
    jid: "{{ async_result.ansible_job_id }}"
  register: status
  until: status.finished
  retries: 60
  delay: 60

- name: Handle failure
  ansible.builtin.debug:
    msg: "Task failed: {{ status.msg | default('unknown error') }}"
  when: status.failed
```
