---
title: "YugabyteDB Compaction Error Code"
description: "Compaction error with specific code"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Compaction returning specific error code.

## Common Causes
- Compaction backlog
- Disk space insufficient
- Compaction thread stuck

## How to Fix
```bash
# Check compaction
curl http://localhost:9000/metrics | grep compaction

# Monitor RocksDB
curl http://localhost:9000/metrics | grep rocksdb
```

## Examples
```bash
# Check compaction pending
curl http://localhost:9000/metrics | grep compaction_pending
# Monitor L0 files
curl http://localhost:9000/metrics | grep l0_files
```

