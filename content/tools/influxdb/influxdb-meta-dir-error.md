---
title: "InfluxDB Meta Directory Error"
description: "Meta directory permission or access issue"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
InfluxDB cannot access or write to the meta directory.

## Common Causes
- Incorrect file permissions
- Directory does not exist
- Disk full

## How to Fix
```bash
# Fix permissions
chown -R influxdb:influxdb /var/lib/influxdb/meta
chmod 755 /var/lib/influxdb/meta

# Recreate directory
mkdir -p /var/lib/influxdb/meta
```

## Examples
```bash
# Verify permissions
ls -la /var/lib/influxdb/
# Expected output shows influxdb ownership
```

