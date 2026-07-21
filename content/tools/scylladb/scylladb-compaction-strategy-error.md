---
title: "ScyllaDB Compaction Strategy Error"
description: "Compaction strategy misconfiguration"
tools:
  - scylladb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Compaction strategy is misconfigured or failing.

## Common Causes
- Strategy not suitable for workload
- Compaction backlog
- Insufficient disk space

## How to Fix
```cql
-- Check compaction strategy
DESCRIBE TABLE mytable;

-- Change compaction strategy
ALTER TABLE mytable WITH compaction = {'class': 'LeveledCompactionStrategy'};
```

## Examples
```cql
-- Check compaction status
nodetool compactionstats
-- Monitor compaction
curl http://localhost:10000/metrics | grep compaction
```

