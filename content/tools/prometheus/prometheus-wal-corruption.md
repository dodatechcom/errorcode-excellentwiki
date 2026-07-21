---
title: "[Solution] Prometheus WAL Corruption Error"
description: "How to fix Prometheus Write-Ahead Log (WAL) corruption errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Power failure or unclean shutdown during writes
- Disk I/O error during WAL write
- Filesystem corruption
- Disk full during WAL operation

## How to Fix

Check WAL integrity:

```bash
promtool tsdb check-tombstones prometheus-data/
```

If WAL is corrupted, truncate and rebuild:

```bash
# Stop Prometheus
sudo systemctl stop prometheus

# Back up WAL directory
mv prometheus-data/wal prometheus-data/wal.bak

# Start Prometheus (will recreate WAL)
sudo systemctl start prometheus
```

Check disk health:

```bash
sudo smartctl -a /dev/sda
dmesg | grep -i error
```

Prevent future corruption with WAL config:

```yaml
storage:
  tsdb:
    wal_compression: true
```

## Examples

```bash
# Check WAL directory
ls -la prometheus-data/wal/

# Monitor WAL size
du -sh prometheus-data/wal/

# Check for corruption in logs
journalctl -u prometheus | grep -i "corrupt"
```
