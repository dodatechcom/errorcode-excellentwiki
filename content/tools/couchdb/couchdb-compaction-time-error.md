---
title: "[Solution] CouchDB Compaction Time Error — How to Fix"
description: "Fix CouchDB compaction time errors by resolving slow compaction issues, fixing compaction scheduling problems, and handling long-running compaction tasks"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["warning"]
weight: 5
comments: true
---

# CouchDB Compaction Time Error

CouchDB compaction time errors occur when compaction tasks take too long to complete, impacting performance or failing due to timeouts.

## Why It Happens

- Database is very large
- Disk I/O is slow
- Compaction is running during peak hours
- Too many compaction tasks running simultaneously
- Memory is insufficient for compaction
- Concurrent writes slow down compaction

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "Compaction timeout" }
```

```
{ "error": "internal_server_error", "reason": "Compaction too slow" }
```

```
{ "error": "timeout", "reason": "Compaction exceeded time limit" }
```

```
WARNING: Compaction is running for extended period
```

## How to Fix It

### 1. Check Compaction Status

```bash
# Check active tasks
curl http://localhost:5984/_active_tasks | jq '.[] | select(.type == "compaction")'

# Check database size
curl http://localhost:5984/mydb | jq '.data_size, .disk_size'

# Check disk I/O
iostat -x 1 5
```

### 2. Schedule Compaction

```bash
# Schedule compaction during off-peak hours
echo "0 2 * * * curl -X POST http://localhost:5984/mydb/_compact" | crontab -

# Run compaction manually during maintenance
curl -X POST http://localhost:5984/mydb/_compact
```

### 3. Optimize Compaction

```bash
# Increase compaction throughput
curl -X PUT http://localhost:5984/_node/_local/_config/compaction/db_fragmentation_proportion \
  -H "Content-Type: text/plain" \
  -d '"0.25"'

# Reduce fragmentation threshold
curl -X PUT http://localhost:5984/_node/_local/_config/compaction/view_fragmentation_proportion \
  -H "Content-Type: text/plain" \
  -d '"0.25"'
```

### 4. Monitor Compaction Progress

```bash
# Watch compaction progress
while true; do
  curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "compaction") | {database, progress}'
  sleep 10
done
```

## Common Scenarios

- **Compaction too slow**: Increase resources or reduce database size.
- **Compaction during peak hours**: Schedule compaction during off-peak times.
- **Compaction timeout**: Increase timeout settings or optimize compaction.

## Prevent It

- Schedule regular compaction
- Monitor database size growth
- Use faster storage for CouchDB data

## Related Pages

- [CouchDB Compaction Error](/tools/couchdb/couchdb-compaction-error)
- [CouchDB Performance Error](/tools/couchdb/couchdb-performance-error)
- [CouchDB Disk Error](/tools/couchdb/couchdb-disk-error)
