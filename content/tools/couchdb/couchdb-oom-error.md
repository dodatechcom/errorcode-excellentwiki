---
title: "[Solution] CouchDB OOM Error — How to Fix"
description: "Fix CouchDB OOM errors by resolving out-of-memory crashes, fixing memory-intensive operations, and handling Erlang VM memory limits"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB OOM Error

CouchDB OOM errors occur when the CouchDB process is killed by the OS due to excessive memory consumption during queries, compaction, or attachment processing.

## Why It Happens

- Large result sets are loaded entirely into memory
- View compaction requires more memory than available
- Attachment processing consumes too much memory
- Too many concurrent requests exhaust memory
- JavaScript functions use excessive memory
- Erlang VM heap grows without bound

## Common Error Messages

```
FATAL: out of memory (OOM Killed)
```

```
ERROR: Erlang VM memory allocation failed
```

```
{ "error": "internal_server_error", "reason": "Memory exhausted" }
```

```
WARNING: Memory usage exceeds 90%
```

## How to Fix It

### 1. Check Memory Usage

```bash
# Check Erlang VM memory
curl http://localhost:5984/_node/_local | jq '.memory'

# Check system memory
free -h

# Check CouchDB process memory
ps aux | grep couchdb | awk '{print $6/1024 " MB"}'
```

### 2. Limit Query Results

```bash
# Add limit to queries
curl "http://localhost:5984/mydb/_all_docs?limit=100"

# Use pagination
curl "http://localhost:5984/mydb/_all_docs?limit=50&skip=50"

# Limit view results
curl "http://localhost:5984/mydb/_design/stats/_view/by_device?limit=100"
```

### 3. Configure Memory Limits

```ini
; In local.ini
[couchdb]
; Maximum memory in MB
max_memory = 2048

[query_server]
; Reduce JavaScript memory
reduce_limit = true
```

### 4. Fix Compaction Memory

```bash
# Compact during low-traffic periods
curl -X POST http://localhost:5984/mydb/_compact

# Check compaction status
curl http://localhost:5984/_active_tasks | jq '.[] | select(.type == "compaction")'
```

## Common Scenarios

- **OOM during view query**: Add limit and reduce result set size.
- **OOM during compaction**: Run compaction during low-traffic periods.
- **OOM with large attachments**: Process attachments in smaller batches.

## Prevent It

- Set appropriate memory limits for CouchDB
- Use pagination for all queries
- Monitor memory usage during peak hours

## Related Pages

- [CouchDB Memory Error](/tools/couchdb/couchdb-memory-error)
- [CouchDB Query Error](/tools/couchdb/couchdb-view-error)
- [CouchDB Node Error](/tools/couchdb/couchdb-node-error)
