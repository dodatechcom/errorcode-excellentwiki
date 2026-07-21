---
title: "InfluxDB Secret Store Error"
description: "Secret store access or decryption failure"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
InfluxDB cannot access or decrypt stored secrets.

## Common Causes
- Secret store key rotated
- Encryption key mismatch
- Backend secret store unreachable

## How to Fix
```bash
# List secrets
influx secret list

# Update secret
influx secret update --id <id> --secret-value <new-value>
```

## Examples
```bash
# Store new secret
influx secret --org-id myorg put my-secret --secret-value s3cretKey
# Verify
influx secret list
```

