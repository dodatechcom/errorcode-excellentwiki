---
title: "[Solution] CouchDB Replication Attachment Error — How to Fix"
description: "Fix CouchDB replication attachment errors by resolving attachment replication failures, fixing attachment transfer issues, and handling attachment sync problems"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Attachment Error

CouchDB replication attachment errors occur when attachments fail to replicate between source and target databases.

## Why It Happens

- Attachment is too large to transfer
- Attachment MIME type is invalid
- Attachment data is corrupted
- Target database has attachment size limits
- Network timeout during attachment transfer
- Attachment encoding is incorrect

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "Attachment replication failed" }
```

```
{ "error": "bad_request", "reason": "Invalid attachment data" }
```

```
{ "error": "timeout", "reason": "Attachment transfer timeout" }
```

```
{ "error": "internal_server_error", "reason": "Attachment too large" }
```

## How to Fix It

### 1. Check Attachments

```bash
# List document attachments
curl http://localhost:5984/mydb/doc123 | jq '._attachments'

# Get attachment metadata
curl -I http://localhost:5984/mydb/doc123/photo.jpg
```

### 2. Fix Large Attachments

```bash
# Check attachment size
curl http://localhost:5984/mydb/doc123 | jq '._attachments | to_entries[] | {key: .key, length: .value.length}'

# Use chunked upload for large files
curl -X PUT http://localhost:5984/mydb/doc123/large_file.pdf \
  -H "Content-Type: application/pdf" \
  --data-binary @large_file.pdf
```

### 3. Fix Attachment Replication

```bash
# Create replication with attachment support
curl -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "my_rep",
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "create_target": true,
    "attachments": true
  }'
```

### 4. Monitor Attachment Replication

```bash
# Check attachment replication progress
curl http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {docs_written, doc_write_failures}'

# Check attachment sizes
curl "http://localhost:5984/mydb/_all_docs?include_docs=true" | jq '.rows[] | {id: .id, attachments: (._attachments // {} | keys)}'
```

## Common Scenarios

- **Attachment too large**: Split into smaller chunks or use external storage.
- **Transfer timeout**: Increase timeout or use faster network.
- **Attachment corrupted**: Re-upload attachment on source.

## Prevent It

- Use appropriate attachment size limits
- Monitor attachment transfer performance
- Verify attachments after replication

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Attachment Error](/tools/couchdb/couchdb-attachment-error)
- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
