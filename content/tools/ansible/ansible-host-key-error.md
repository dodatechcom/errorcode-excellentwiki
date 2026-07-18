---
title: "[Solution] Ansible Host Key Verification Failed Error Fix"
description: "Fix Ansible host key verification failed errors. Resolve SSH host key mismatches and known_hosts issues in Ansible."
tools: ["ansible"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Ansible Host Key Verification Failed Error Fix

The `host key verification failed` error occurs when the SSH host key of a managed node does not match what is stored in the known_hosts file, or has never been seen before.

## What This Error Means

SSH verifies host identity using public keys stored in `~/.ssh/known_hosts`. When a host key changes (reinstalled OS, IP reuse) or is unknown, SSH rejects the connection for security.

A typical error:

```
Failed to connect to the host via ssh: @ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
```

## Why It Happens

Common causes include:

- **Host key changed** — Server was reinstalled or reprovisioned.
- **IP address reused** — Different server now has the same IP.
- **Known_hosts entry stale** — Old key no longer matches.
- **StrictHostKeyChecking enabled** — Default SSH behavior rejects unknown keys.
- **Multiple users** — Different user known_hosts files.

## How to Fix It

### Fix 1: Remove old host key

```bash
# RIGHT: Remove specific host
ssh-keygen -R 192.168.1.10

# Remove by hostname
ssh-keygen -R webserver.example.com
```

### Fix 2: Disable strict host key checking in ansible.cfg

```ini
# ansible.cfg
[defaults]
host_key_checking = False

# Or per inventory
[ssh_connection]
ssh_args = -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no
```

### Fix 3: Use ssh-keyscan to add host key

```bash
# RIGHT: Add host key before connecting
ssh-keyscan -H 192.168.1.10 >> ~/.ssh/known_hosts

# Add multiple hosts
ssh-keyscan web1 web2 web3 >> ~/.ssh/known_hosts
```

### Fix 4: Use known_hosts module in playbook

```yaml
# RIGHT: Manage known_hosts from Ansible
- name: Add host key
  ansible.builtin.known_hosts:
    name: 192.168.1.10
    key: "{{ lookup('pipe', 'ssh-keyscan 192.168.1.10') }}"
    state: present
```

### Fix 5: Use different known_hosts file

```yaml
# RIGHT: Custom known_hosts file
- name: Run playbook
  hosts: all
  vars:
    ansible_ssh_extra_args: "-o UserKnownHostsFile=/ansible/known_hosts"
```

## Common Mistakes

- **Disabling host key checking in production** — Only use in development.
- **Not updating known_hosts after OS reinstall** — Always clear stale keys.
- **Forgetting that known_hosts is per-user** — Different users have different files.

## Related Pages

- [Ansible Connection Refused](ansible-connection-refused) — SSH connection issues
- [Ansible Permission Denied](ansible-permission-denied-become) — Privilege escalation errors
- [Kubectl Connection Refused](/tools/kubectl/kubectl-connection-refused/) — API server issues
