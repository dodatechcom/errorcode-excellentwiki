---
title: "[Solution] Prometheus TSDB Block Corruption Error"
description: "How to fix Prometheus TSDB block corruption errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Disk I/O error during block write
- Power failure during compaction
- Filesystem corruption
- Insufficient disk space

## How to Fix

Check block integrity:

```bash
promtool tsdb analyze prometheus-data/
```

Identify and remove corrupted blocks:

```bash
sudo systemctl stop prometheus

# List blocks
ls -la prometheus-data/chunks_head/

# Remove corrupted block directories
rm -rf prometheus-data/chunks_head/<corrupted-block-id>

sudo systemctl start prometheus
```

Verify disk health:

```bash
sudo smartctl -a /dev/sda
```

## Examples

```bash
# Analyze TSDB
promtool tsdb analyze prometheus-data/

# Check block sizes
du -sh prometheus-data/chunks_head/*/

# Monitor compaction
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_compactions_total'
```
