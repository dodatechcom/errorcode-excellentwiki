---
title: "InfluxDB Integer Overflow"
description: "Integer field value overflow"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Writing integer values that exceed the 64-bit signed integer range.

## Common Causes
- Large counter values
- Incorrect data type in write payload
- Counter reset causing negative values

## How to Fix
```javascript
// Use proper integer bounds
// Max: 9223372036854775807
// Min: -9223372036854775808

// Convert to float if needed
data.fields.value = parseFloat(data.fields.value)
```

## Examples
```bash
# Write with bounds check
curl -X POST 'http://localhost:8086/api/v2/write?org=myorg&bucket=mydb' \
  -H 'Authorization: Token mytoken' \
  -H 'Content-Type: text/plain' \
  -d 'cpu value=1234567890i'
```

