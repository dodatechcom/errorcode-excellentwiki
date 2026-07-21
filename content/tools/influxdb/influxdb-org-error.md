---
title: "InfluxDB Organization Error"
description: "Organization management failure"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Cannot create, modify, or delete organizations.

## Common Causes
- Organization name already exists
- Last organization cannot be deleted
- Insufficient permissions

## How to Fix
```bash
# List organizations
influx org list

# Create new org
influx org create --name neworg
```

## Examples
```bash
# Delete org (must not have buckets)
influx org delete --id <org-id>
# Rename org
influx org update --id <org-id> --name new-name
```

