---
title: "[Solution] Ansible Module Execution Timeout"
description: "Fix Ansible module timeout errors during long-running operations"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible module exceeds the configured timeout during execution.

```
ERROR! Timeout waiting for module result
```

## Common Causes

- Task taking longer than expected
- Default timeout too short
- Resource contention on remote host
- Network issues causing slow responses

## How to Fix

```yaml
- name: Long-running task
  ansible.builtin.command: /opt/scripts/heavy_computation.sh
  async: 3600
  poll: 0
  register: job_result

- name: Wait for completion
  ansible.builtin.async_status:
    jid: "{{ job_result.ansible_job_id }}"
  register: job_status
  until: job_status.finished
  retries: 60
  delay: 60
```
