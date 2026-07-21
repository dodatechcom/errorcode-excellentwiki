---
title: "TiDB Region Error Code"
description: "Region error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Region operation returning specific error code.

## Common Causes
- Region not found
- Region peer unavailable
- Epoch mismatch

## How to Fix
```bash
# Check region info
tiup pd-ctl region <region-id>

# Check region peers
tiup pd-ctl region peer <region-id>
```

## Examples
```bash
# Check region distribution
tiup pd-ctl region --limit 10
# Fix region peer
tiup pd-ctl operator add remove-peer <region-id> <store-id>
```

