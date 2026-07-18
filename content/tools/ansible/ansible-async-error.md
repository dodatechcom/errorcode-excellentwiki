---
title: "[Solution] Ansible Async Task Timed Out Error Fix"
description: "Fix Ansible async task timed out errors. Configure async polling, timeouts, and fire-and-forget task execution properly."
tools: ["ansible"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Ansible Async Task Timed Out Error Fix

The `async task timed out` error occurs when an Ansible task running asynchronously does not complete within the specified `async` timeout, or the poll interval is too short.

## What This Error Means

Ansible's `async` directive allows tasks to run in the background. The `async` value sets the maximum runtime, and `poll` sets how often to check status. When the task exceeds the timeout or polling fails, the task is marked as failed.

A typical error:

```
FAILED - TASK: [deploy app] Timed out
```

## Why It Happens

Common causes include:

- **async timeout too short** — Task needs more time than specified.
- **poll value too low** — Checking status before task completes.
- **Task hangs** — Process deadlocked or waiting indefinitely.
- **Connection lost** — SSH connection dropped during async task.
- **Fork limit** — Too many async tasks running simultaneously.

## How to Fix It

### Fix 1: Increase async timeout

```yaml
# RIGHT: Set adequate timeout
- name: Deploy application
  ansible.builtin.command: /opt/deploy.sh
  async: 600    # Wait up to 10 minutes
  poll: 15      # Check every 15 seconds
```

### Fix 2: Use fire-and-forget pattern

```yaml
# RIGHT: Start and forget (poll: 0)
- name: Start background job
  ansible.builtin.command: /opt/long-job.sh
  async: 3600   # Run for up to 1 hour
  poll: 0       # Don't wait

- name: Do other work
  ansible.builtin.command: /opt/other-task.sh

- name: Check job status later
  ansible.builtin.async_status:
    jid: "{{ job_result.ansible_job_id }}"
  register: job_result
  until: job_result.finished
  retries: 30
  delay: 10
```

### Fix 3: Handle async failures gracefully

```yaml
# RIGHT: Check async result
- name: Long running task
  ansible.builtin.command: /opt/task.sh
  async: 300
  poll: 30
  register: async_result
  ignore_errors: yes

- name: Handle failure
  ansible.builtin.debug:
    msg: "Task failed: {{ async_result.msg }}"
  when: async_result is failed
```

### Fix 4: Use async_status module

```yaml
# RIGHT: Poll for completion
- name: Start job
  ansible.builtin.command: /opt/job.sh
  async: 600
  poll: 0
  register: job

- name: Wait for job
  ansible.builtin.async_status:
    jid: "{{ job.ansible_job_id }}"
  register: job_result
  until: job_result.finished
  retries: 60
  delay: 10
```

## Common Mistakes

- **Setting poll to 0 without follow-up** — Task runs but you never check result.
- **Not using register with async** — Need job ID to check status later.
- **Async with serial** — Async tasks bypass serial batching.

## Related Pages

- [Ansible Connection Refused](ansible-connection-refused) — Connection issues
- [Ansible Serial Error](ansible-serial-error) — Serial execution issues
- [Ansible Delegate Error](ansible-delegate-error) — Delegation issues
