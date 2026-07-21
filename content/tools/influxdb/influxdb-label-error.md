---
title: "InfluxDB Label Error"
description: "Label assignment or query failure"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Cannot create, update, or query labels in InfluxDB.

## Common Causes
- Label name conflict
- Too many labels on resource
- Permission denied

## How to Fix
```flux
// List labels
label.get(resource: {buckets: ["mydb"]})

// Delete conflicting label
label.delete(resource: {buckets: ["mydb"]}, label: "old-label")
```

## Examples
```flux
// Add label
label.add(resource: {buckets: ["mydb"]}, key: "env", value: "prod")
```

