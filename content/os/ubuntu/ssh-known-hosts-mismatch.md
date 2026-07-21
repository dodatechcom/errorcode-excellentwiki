---
title: "SSH Known Hosts Key Mismatch"
description: "Remote host key does not match known_hosts entry indicating possible MITM"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# SSH Known Hosts Key Mismatch

Remote host key does not match known_hosts entry indicating possible MITM

## Common Causes

- Server reinstalled or OS changed generating new host key
- IP address reassigned to different server
- Actual man-in-the-middle attack
- Known_hosts file corrupted or edited incorrectly

## How to Fix

1. Verify server identity through separate channel
2. Remove old entry: `ssh-keygen -R <hostname>`
3. If legitimate change, accept new key
4. Check if key fingerprints match: `ssh-keygen -lf /etc/ssh/ssh_host_rsa_key.pub`

## Examples

```bash
# Remove old known_hosts entry
ssh-keygen -R server.example.com

# Connect and verify new key fingerprint
ssh user@server.example.com
```
