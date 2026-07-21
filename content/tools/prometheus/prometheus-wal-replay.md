---
title: "[Solution] Prometheus WAL Replay Error"
description: "How to fix errors during Prometheus WAL replay on startup"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- WAL segments corrupted or incomplete
- Version mismatch between WAL writer and reader
- Insufficient disk space for WAL replay
- Memory limit exceeded during replay

## How to Fix

Check WAL replay status:

```bash
journalctl -u prometheus | grep -i "replay"
```

If replay fails, truncate WAL:

```bash
sudo systemctl stop prometheus

# Move corrupted WAL
mv prometheus-data/wal prometheus-data/wal.corrupted

# Start fresh
sudo systemctl start prometheus
```

Increase memory for large WAL:

```bash
prometheus --storage.tsdb.wal-compression --storage.tsdb.retention.time=30d
```

## Examples

```bash
# Monitor WAL replay progress
journalctl -u prometheus -f | grep replay

# Check WAL segment count
ls prometheus-data/wal/ | wc -l

# Check disk space before restart
df -h prometheus-data/
```
