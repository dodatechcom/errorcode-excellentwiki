---
title: "[Solution] Ansible Async Task Timeout"
description: "Fix Ansible async task timeout and polling errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible async task times out or fails to complete within the specified timeout.

```
ERROR! Async task timed out after 3600 seconds
```

## Common Causes

- Async timeout too short
- Task takes longer than expected
- Polling interval too infrequent

## How to Fix

```yaml
- name: Long task with extended timeout
  ansible.builtin.command: /opt/scripts/heavy_computation.sh
  async: 14400
  poll: 0
  register: job

- name: Wait for job
  ansible.builtin.async_status:
    jid: "{{ job.ansible_job_id }}"
  register: job_result
  until: job_result.finished
  retries: 100
  delay: 60
```
