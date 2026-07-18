---
title: "[Solution] Ansible Facts Error — Fix Failed to Gather Facts"
description: "Fix Ansible facts gathering errors when setup module cannot collect host information. Resolve connection issues, fact caching, and timeout problems."
---

## What This Error Means

Ansible facts errors occur when the setup module fails to gather system information from a managed host. Facts gathering is the first step in most playbook runs and failures here prevent all subsequent tasks.

A typical error:

```
host1 | FAILED! => {
    "ansible_facts": {},
    "changed": false,
    "msg": "Failed to prefetch facts for host1"
}
```

Or:

```
fatal: [host1]: FAILED! => {
    "msg": "The task includes an option with an undefined variable."
}
```

## Why It Happens

Facts gathering failures happen when:

- **Connection issue**: The host is unreachable or SSH is not responding.
- **Python not installed**: The remote host lacks Python (required for Ansible modules).
- **Missing platform module**: The remote host has an incomplete Python installation.
- **Fact caching corruption**: The fact cache file is corrupted or stale.
- **Gathering timeout**: The setup module takes longer than the configured timeout.
- **SELinux blocking**: SELinux policies prevent reading system files during fact collection.
- **Insufficient permissions**: The remote user cannot read system information files.

## How to Fix It

**Step 1: Disable fact gathering for troubleshooting**

```yaml
- hosts: all
  gather_facts: false
  tasks:
    - ping:
```

**Step 2: Check Python on the remote host**

```bash
ansible host1 -m raw -a "python3 --version"
ansible host1 -m raw -a "python --version"
```

**Step 3: Increase fact gathering timeout**

```ini
# ansible.cfg
[defaults]
gathering_timeout = 30
```

**Step 4: Clear cached facts**

```bash
rm -rf ~/.ansible/facts_cache/
```

**Step 5: Use a minimal fact subset**

```yaml
- hosts: all
  gather_facts: true
  gather_subset:
    - minimal
    - network
```

**Step 6: Set minimum Python version on remote**

```ini
[defaults]
ansible_python_interpreter = /usr/bin/python3
```

## Common Mistakes

- **Assuming Python is installed on all target hosts**: Always verify or use `raw` module for bootstrapping.
- **Using stale fact caches**: Clear the fact cache after host configuration changes.
- **Setting gather_facts to no permanently**: Facts are needed for most meaningful playbooks.
- **Not specifying the Python interpreter for mixed-OS environments**: Windows and Linux need different settings.

## Related Pages

- [Ansible Unreachable Host](/tools/ansible/ansible-unreachable-host/) -- Host connectivity
- [Ansible SSH Timeout](/tools/ansible/ansible-ssh-timeout/) -- SSH issues
- [Ansible Undefined Variable](/tools/ansible/ansible-undefined-variable/) -- Variable not found
