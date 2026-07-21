---
title: "InfluxDB Measurement Name Length"
description: "Measurement name exceeds maximum length"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Measurement name exceeds the 256 character maximum.

## Common Causes
- Auto-generated measurement names too long
- Incorrect naming convention
- Concatenated tags in measurement name

## How to Fix
```javascript
// Truncate measurement name
const measurement = originalName.substring(0, 255)
```

## Examples
```bash
# Valid measurement name (under 256 chars)
curl -X POST 'http://localhost:8086/api/v2/write?org=myorg&bucket=mydb' \
  -d 'cpu value=0.5'
# Invalid: measurement name > 256 chars
```

