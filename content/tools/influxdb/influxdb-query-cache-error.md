---
title: "InfluxDB Query Cache Error"
description: "Query cache invalidation or overflow"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
The query cache is returning stale data or has overflowed.

## Common Causes
- Cache size exceeded
- Stale cache entries
- Memory pressure

## How to Fix
```bash
# Check cache statistics
curl -s http://localhost:8086/debug/vars | python -m json.tool | grep cache

# Flush cache
curl -X POST http://localhost:8086/debug/flush
```

## Examples
```yaml
# influxdb.conf cache settings
[query]
  cache-max-memory-size = 1073741824
  cache-snapshot-memory-size = 26214400
```

