---
title: "[Solution] Ansible SSH Protocol Error"
description: "Resolve SSH protocol version mismatch errors in Ansible connections"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible encounters an SSH protocol error during connection negotiation.

```
UNREACHABLE! => {"msg": "ssh_dispatch_runssh: SSH protocol error"}
```

## Common Causes

- Remote host SSH daemon using incompatible protocol version
- SSH client and server algorithm mismatch
- Corrupted SSH session
- Network middlebox interference

## How to Fix

```ini
# ansible.cfg
[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no
pipelining = True
```
