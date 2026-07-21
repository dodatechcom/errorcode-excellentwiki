---
title: "[Solution] ScyllaDB Node Down Error"
description: "How to fix ScyllaDB node down errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Node process crashed
- Hardware failure
- Disk full or I/O error
- OOM killed by kernel

## How to Fix

Check node logs:

```bash
journalctl -u scylla-server --since '10 minutes ago'
```

Start the node:

```bash
sudo systemctl start scylla-server
```

## Examples

```bash
nodetool status
journalctl -u scylla-server -f
dmesg | grep -i oom
```
