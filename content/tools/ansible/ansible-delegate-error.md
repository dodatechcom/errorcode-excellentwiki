---
title: "[Solution] Ansible Delegate To Host Unreachable Error Fix"
description: "Fix Ansible delegate_to host unreachable errors. Resolve delegation connectivity issues and target host problems."
tools: ["ansible"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Ansible Delegate To Host Unreachable Error Fix

The `delegate_to host unreachable` error occurs when Ansible cannot connect to the delegated host specified in a task, or when the delegation target is not accessible.

## What This Error Means

The `delegate_to` directive runs a task on a different host than the current play target. When the delegated host is unreachable, has wrong credentials, or network issues prevent connection, the task fails.

A typical error:

```
web1 | FAILED! => {"msg": "Failed to connect to the host via ssh: Connection refused"}
```

## Why It Happens

Common causes include:

- **Delegated host unreachable** — Target machine is down or firewalled.
- **Wrong SSH credentials** — Delegation target uses different authentication.
- **Network connectivity issue** — Control node cannot reach delegation target.
- **DNS resolution failure** — Hostname does not resolve.
- **Host not in inventory** — Delegation target not defined.
- **SSH port mismatch** — Delegated host uses non-standard SSH port.

## How to Fix It

### Fix 1: Verify delegation target connectivity

```bash
# RIGHT: Test connection first
ssh user@delegated-host echo "connected"
ping delegated-host
nmap -p 22 delegated-host
```

### Fix 2: Configure proper connection parameters

```yaml
# RIGHT: Set connection vars for delegated host
- name: Backup database
  ansible.builtin.command: mysqldump --all-databases
  delegate_to: db-backup-server
  vars:
    ansible_host: 192.168.1.50
    ansible_user: backup
    ansible_port: 22
```

### Fix 3: Use delegate_to with run_once

```yaml
# RIGHT: Run on delegation target once
- name: Update load balancer
  ansible.builtin.uri:
    url: "http://lb/api/update"
    method: POST
  delegate_to: localhost
  run_once: true
```

### Fix 4: Handle delegation failures

```yaml
# RIGHT: Ignore delegation errors
- name: Notify monitoring
  ansible.builtin.uri:
    url: "http://monitor/api/alert"
  delegate_to: monitor-server
  ignore_errors: yes
  failed_when: false
```

### Fix 5: Use add_host for dynamic delegation

```yaml
# RIGHT: Add host dynamically
- name: Add temporary host
  ansible.builtin.add_host:
    name: temp-server
    ansible_host: 10.0.0.50
    ansible_user: admin

- name: Run on temp server
  ansible.builtin.command: /opt/run-task.sh
  delegate_to: temp-server
```

## Common Mistakes

- **Assuming delegation uses same credentials as main host** — May need different vars.
- **Not checking firewall rules on delegation target** — SSH must be allowed.
- **Forgetting that delegate_to bypasses serial** — Delegated tasks run immediately.

## Related Pages

- [Ansible Connection Refused](ansible-connection-refused) — SSH connection issues
- [Ansible Host Key Error](ansible-host-key-error) — SSH host key issues
- [Ansible Async Error](ansible-async-error) — Async task timeout
