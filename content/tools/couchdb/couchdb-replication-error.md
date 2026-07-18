---
title: "[Solution] CouchDB Replication Error — How to Fix"
description: "Fix CouchDB replication errors by correcting filter functions, resolving document conflicts, and tuning replication batch settings"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Error

CouchDB replication errors occur when continuous or one-shot replication between databases fails. These errors can interrupt data synchronization between nodes, data centers, or devices.

## Why It Happens

- Source or target database does not exist or is unreachable
- Authentication credentials are invalid or expired
- Document conflicts prevent consistent replication
- Filter functions contain errors or reference missing design documents
- Replication timeout due to large documents or network issues
- Insufficient disk space on source or target node

## Common Error Messages

```
{ "error": "db_not_found", "reason": "could not open http://localhost:5984/target_db" }
```

```
{ "error": "unauthorized", "reason": "Name or password is incorrect." }
```

```
{ "error": "conflict", "reason": "Document update conflict." }
```

```
{ "error": "missing", "reason": "missing" }
```

## How to Fix It

### 1. Verify Source and Target Databases

```bash
# Check source database exists
curl http://admin:password@localhost:5984/source_db

# Check target database exists
curl http://admin:password@localhost:5984/target_db

# Create target if missing
curl -X PUT http://admin:password@localhost:5984/target_db
```

### 2. Configure Replication with Credentials

```json
{
  "source": "http://admin:password@localhost:5984/source_db",
  "target": "http://admin:password@localhost:5984/target_db",
  "continuous": true,
  "create_target": true,
  "batch_size": 500
}
```

```bash
# Start replication via API
curl -X POST http://admin:password@localhost:5984/_replicator \
  -H "Content-Type: application/json" \
  -d @replication_doc.json
```

### 3. Fix Document Conflicts

```bash
# List conflicting revisions
curl 'http://admin:password@localhost:5984/db_name/doc_id?conflicts=true'

# Resolve by keeping winning revision or merging
curl -X PUT http://admin:password@localhost:5984/db_name/doc_id \
  -H "Content-Type: application/json" \
  -d '{"_rev": "2-xxx", "field": "merged_value"}'
```

### 4. Tune Replication Performance

```json
{
  "source": "http://localhost:5984/source_db",
  "target": "http://localhost:5984/target_db",
  "continuous": true,
  "batch_size": 1000,
  "http_connections": 20,
  "checkpoint_interval": 10000,
  "worker_processes": 4
}
```

## Common Scenarios

- **Master-master replication loops**: Use `selector` filters or `_replication_id` to avoid infinite loops.
- **Replication stalls on large databases**: Increase `batch_size` and `http_connections` for better throughput.
- **Credentials rotate and replication breaks**: Use session cookies or API tokens with long-lived expiry.

## Prevent It

- Monitor `_active_tasks` for replication status and errors
- Set up alerts on `_scheduler/docs` for failed replication jobs
- Use `_replicator` database for persistent replication configuration

## Related Pages

- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
- [CouchDB Conflict Error](/tools/couchdb/couchdb-conflict-error)
- [CouchDB Filter Error](/tools/couchdb/couchdb-filter-error)
