---
title: "LXD Cluster Operation Error"
description: "LXD cluster operations fail between nodes"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# LXD Cluster Operation Error

LXD cluster operations fail between nodes

## Common Causes

- Cluster member unreachable or offline
- Database replication failure between members
- Certificate mismatch between cluster nodes
- Network partition between cluster members

## How to Fix

1. Check cluster status: `lxc cluster list`
2. Verify member health: `lxc cluster show <member>`
3. Check certificates: `lxc cluster certificate show`
4. Review logs: `journalctl -u snap.lxd.daemon`

## Examples

```bash
# Check cluster status
lxc cluster list

# Show cluster member details
lxc cluster show node1

# Check cluster certificates
lxc cluster certificate show
```
