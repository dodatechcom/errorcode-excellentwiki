---
title: "[Solution] Ansible Block Rescue Always Error Handling Fix"
description: "Fix Ansible block/rescue/always error handling errors. Configure proper try/catch patterns in Ansible playbooks."
tools: ["ansible"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Ansible Block Rescue Always Error Handling Fix

The `block/rescue/always error handling` error occurs when Ansible block structures are misconfigured, rescue tasks fail, or always blocks have issues with task execution order.

## What This Error Means

Ansible uses `block/rescue/always` for error handling (similar to try/catch/finally). When the block structure is invalid, rescue tasks fail, or always tasks have dependencies, the playbook errors.

A typical error:

```
ERROR! 'block' is not a valid attribute for a Task
```

Or rescue tasks fail silently causing unexpected behavior.

## Why It Happens

Common causes include:

- **Wrong indentation** — Block tasks not properly nested.
- **Missing block keyword** — Tasks not wrapped in block.
- **Rescue tasks failing** — Error handler itself has errors.
- **Always tasks on wrong hosts** — Always block runs on wrong target.
- **register in block** — Variable scope issues.
- **When condition in block** — Conditions not evaluated correctly.

## How to Fix It

### Fix 1: Use correct block syntax

```yaml
# RIGHT: Proper block structure
- name: Deploy with error handling
  block:
    - name: Deploy application
      ansible.builtin.copy:
        src: app.tar.gz
        dest: /opt/app/
    
    - name: Restart service
      ansible.builtin.service:
        name: myapp
        state: restarted
  
  rescue:
    - name: Rollback deployment
      ansible.builtin.copy:
        src: backup.tar.gz
        dest: /opt/app/
    
    - name: Restart old version
      ansible.builtin.service:
        name: myapp
        state: restarted
  
  always:
    - name: Send notification
      ansible.builtin.uri:
        url: "http://slack/api/notify"
        method: POST
```

### Fix 2: Use when condition with block

```yaml
# RIGHT: Conditional block
- name: Production deployment
  block:
    - name: Run database migration
      ansible.builtin.command: migrate.sh
  when: environment == "production"
  rescue:
    - name: Log failure
      ansible.builtin.debug:
        msg: "Migration failed in production"
```

### Fix 3: Register block results

```yaml
# RIGHT: Capture block result
- name: Try operation
  block:
    - name: Attempt task
      ansible.builtin.command: risky-operation
      register: block_result
  
  rescue:
    - name: Handle failure
      ansible.builtin.debug:
        msg: "Operation failed: {{ block_result.msg }}"
```

### Fix 4: Use always for cleanup

```yaml
# RIGHT: Cleanup in always block
- name: Process files
  block:
    - name: Create temp files
      ansible.builtin.file:
        path: "/tmp/work-{{ ansible_date_time.epoch }}"
        state: directory
  
  always:
    - name: Cleanup temp files
      ansible.builtin.file:
        path: "/tmp/work-*"
        state: absent
```

## Common Mistakes

- **Indentation errors** — Tasks under block must be indented properly.
- **Rescue tasks have their own errors** — Always test rescue tasks independently.
- **Forgetting always runs even on success** — Use for guaranteed cleanup.

## Related Pages

- [Ansible Async Error](ansible-async-error) — Async task timeout
- [Ansible Serial Error](ansible-serial-error) — Serial execution issues
- [Ansible Filter Error](ansible-filter-error) — Jinja2 filter issues
