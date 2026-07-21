---
title: "PostgreSQL Shared Memory Allocation Error"
description: "PostgreSQL cannot allocate required shared memory on startup"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PostgreSQL Shared Memory Allocation Error

PostgreSQL cannot allocate required shared memory on startup

## Common Causes

- shared_buffers set higher than available RAM
- kernel.shmmax too low for PostgreSQL allocation
- System V IPC limits exceeded
- Another PostgreSQL instance already using shared memory

## How to Fix

1. Check shared_buffers: `SHOW shared_buffers;`
2. Set kernel limits: `sysctl -w kernel.shmmax=1073741824`
3. Check IPC: `ipcs -m`
4. Reduce shared_buffers to fit within RAM limits

## Examples

```bash
# Check current shared memory settings
sysctl kernel.shmmax
sysctl kernel.shmall

# Set shared memory for PostgreSQL
sudo sysctl -w kernel.shmmax=2147483648
sudo sysctl -w kernel.shmall=524288

# Make persistent
echo 'kernel.shmmax=2147483648' | sudo tee -a /etc/sysctl.conf
```
