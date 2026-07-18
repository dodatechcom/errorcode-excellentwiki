---
title: "[Solution] Ansible SSH Timeout Error — Fix SSH Connection Timed Out"
description: "Fix Ansible SSH timeout errors when connections to managed hosts fail. Increase timeout values, optimize SSH settings, and resolve network latency issues."
---

## What This Error Means

Ansible SSH timeout errors occur when the SSH connection to a managed host does not complete within the configured timeout period. The connection attempt is aborted and the host is marked as unreachable.

A typical error:

```
host1 | UNREACHABLE! => {
    "changed": false,
    "msg": "Failed to connect to the host via ssh: ssh: connect to host 192.168.1.10 port 22: Connection timed out",
    "unreachable": true
}
```

## Why It Happens

SSH timeout errors happen when:

- **Firewall blocks port 22**: Security groups, iptables, or cloud firewalls drop SSH traffic.
- **Network latency exceeds timeout**: High latency connections need longer timeout values.
- **Host is overloaded**: The SSH daemon cannot accept new connections under heavy load.
- **DNS resolution is slow**: Ansible resolves hostnames on every connection attempt.
- **ControlMaster socket issues**: Stale multiplexing sockets slow down or break connections.
- **SSH key exchange timeout**: Slow key exchange on encrypted connections.

## How to Fix It

**Step 1: Test SSH manually**

```bash
ssh -vvv -o ConnectTimeout=10 user@hostname
```

**Step 2: Increase SSH timeout in ansible.cfg**

```ini
[defaults]
timeout = 60

[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s -o ConnectTimeout=30
```

**Step 3: Use pipelining to reduce SSH overhead**

```ini
[ssh_connection]
pipelining = True
```

**Step 4: Disable SSH key verification**

```ini
[ssh_connection]
host_key_checking = False
```

**Step 5: Increase timeout for specific hosts**

```yaml
- name: My playbook
  hosts: all
  vars:
    ansible_ssh_timeout: 30
  tasks:
    - ping:
```

**Step 6: Use ssh_args for faster connections**

```ini
[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=180s -o ConnectTimeout=60 -o ServerAliveInterval=15
```

## Common Mistakes

- **Not testing SSH manually before debugging Ansible**: Always test `ssh` first to isolate the issue.
- **Setting timeout too low for cloud instances**: Cloud hosts can take 30+ seconds to accept connections.
- **Using passwords instead of SSH keys**: Key-based auth is faster and more reliable.
- **Not enabling pipelining**: Pipelining significantly reduces SSH round trips.

## Related Pages

- [Ansible Unreachable Host](/tools/ansible/ansible-unreachable-host/) -- Host unreachable
- [Ansible Connection Refused](/tools/ansible/ansible-connection-refused/) -- Port refused
- [Ansible Permission Denied](/tools/ansible/ansible-permission-denied/) -- Authentication failures
