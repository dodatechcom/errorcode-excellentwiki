---
title: "[Solution] CouchDB Replication Inconsistent Error — How to Fix"
description: "Fix CouchDB replication inconsistent errors by resolving data inconsistencies during replication, fixing inconsistent state issues, and handling replication data integrity problems"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Inconsistent Error

CouchDB replication inconsistent errors occur when source and target databases become inconsistent due to failed or partial replication.

## Why It Happens

- Replication failed midway through
- Documents were modified during replication
- Network interruption caused partial replication
- Replication filter skipped documents
- Checkpoint saved before all documents replicated
- Conflicting revisions not resolved

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "Source and target inconsistent" }
```

```
{ "error": "internal_server_error", "reason": "Replication incomplete" }
```

```
{ "error": "internal_server_error", "reason": "Document count mismatch" }
```

```
WARNING: Replication consistency check failed
```

## How to Fix It

### 1. Check Consistency

```bash
# Compare document counts
curl http://localhost:5984/source_db | jq '.doc_count'
curl http://localhost:5984/target_db | jq '.doc_count'

# Compare document revisions
curl "http://localhost:5984/source_db/_all_docs?limit=10" | jq '.rows[].rev'
curl "http://localhost:5984/target_db/_all_docs?limit=10" | jq '.rows[].rev'
```

### 2. Fix Inconsistency

```bash
# Reset replication from beginning
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "since": "0"
  }'

# Use changes feed to sync specific documents
curl "http://localhost:5984/source_db/_changes?since=0&include_docs=true" | \
  jq -c '.rows[] | {doc: .doc}' | \
  while read -r line; do
    curl -X PUT "http://localhost:5984/target_db/$(echo $line | jq -r '.doc._id')" \
      -H "Content-Type: application/json" \
      -d "$(echo $line | jq '.doc')"
  done
```

### 3. Verify Replication

```bash
# Check replication status
curl http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication")'

# Check for differences
curl "http://localhost:5984/source_db/_all_docs" | jq '.total_rows' > source_count.txt
curl "http://localhost:5984/target_db/_all_docs" | jq '.total_rows' > target_count.txt
diff source_count.txt target_count.txt
```

### 4. Monitor Going Forward

```bash
# Set up replication monitoring
while true; do
  source=$(curl -s http://localhost:5984/source_db | jq '.doc_count')
  target=$(curl -s http://localhost:5984/target_db | jq '.doc_count')
  echo "$(date): source=$source target=$target"
  sleep 60
done
```

## Common Scenarios

- **Document count mismatch**: Run full replication from beginning.
- **Partial replication**: Use changes feed to sync missing documents.
- **Replication failed midway**: Check and fix root cause, then restart.

## Prevent It

- Monitor replication consistency regularly
- Use continuous replication for real-time sync
- Verify replication after network outages

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
- [CouchDB Data Integrity Error](/tools/couchdb/couchdb-data-integrity-error)
