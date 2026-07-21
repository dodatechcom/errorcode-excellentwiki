---
title: "YugabyteDB CDC Error"
description: "Change Data Capture error"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Change Data Capture (CDC) is failing.

## Common Causes
- CDC stream expired
- CDC consumer too slow
- Log retention exceeded

## How to Fix
```bash
# Check CDC streams
yb-admin list_cdc_streams

# Create new stream
yb-admin create_change_data_stream
```

## Examples
```bash
# List CDC streams
yb-admin list_cdc_streams
# Delete old stream
yb-admin delete_cdc_stream <stream-id>
```

