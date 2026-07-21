---
title: "InfluxDB Bucket Error Code"
description: "Bucket operation error code"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Bucket operations returning specific error codes.

## Common Causes
- Bucket name conflict
- Retention period too short
- Quota exceeded

## How to Fix
```bash
# List buckets
influx bucket list

# Delete conflicting bucket
influx bucket delete --id <bucket-id>
```

## Examples
```bash
# Create bucket with proper settings
influx bucket create --name mydb --org myorg --retention 30d
```

