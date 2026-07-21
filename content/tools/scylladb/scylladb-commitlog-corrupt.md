---
title: "[Solution] ScyllaDB Commit Log Corruption Error"
description: "How to fix ScyllaDB commit log corruption errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Power failure during commit log write
- Disk failure
- Full disk during commit

## How to Fix

Recover from corruption:

```bash
sudo systemctl stop scylla-server
rm /var/lib/scylla/commitlog/*
sudo systemctl start scylla-server
```

## Examples

```bash
ls -la /var/lib/scylla/commitlog/
sudo systemctl restart scylla-server
```
