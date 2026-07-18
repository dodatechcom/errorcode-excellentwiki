---
title: "[Solution] CouchDB Changes Feed Error — How to Fix"
description: "Fix CouchDB changes feed errors by resolving long-poll timeouts, correcting since parameter usage, and fixing feed corruption issues"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Changes Feed Error

CouchDB changes feed errors occur when streaming or polling the `/_changes` endpoint fails. The changes feed is critical for real-time applications and replication.

## Why It Happens

- Long-poll connection times out before receiving changes
- `since` parameter references a sequence that has been compacted away
- Filter function throws an error
- Database is closed or does not exist
- Changes feed buffer is too large for the response
- Continuous feed connection is dropped by reverse proxy

## Common Error Messages

```
{ "error": "bad_request", "reason": "bad_since_param" }
```

```
{ "error": "not_found", "reason": "missing" }
```

```
{ "error": "internal_server_error", "reason": "Changes feed error" }
```

```
{ "error": "bad_request", "reason": "invalid_feed_type" }
```

## How to Fix It

### 1. Use Valid Since Parameter

```bash
# Get current sequence number
curl http://localhost:5984/mydb/_changes?limit=1 | jq '.last_seq'

# Use valid since parameter
curl 'http://localhost:5984/mydb/_changes?since=0&limit=100'

# Use now to skip all existing changes
curl 'http://localhost:5984/mydb/_changes?since=now'

# Use longpoll for efficient change detection
curl 'http://localhost:5984/mydb/_changes?feed=longpoll&since=100&timeout=30000'
```

### 2. Configure Changes Feed for Production

```bash
# Continuous feed with heartbeat
curl 'http://localhost:5984/mydb/_changes?feed=continuous&heartbeat=10000&since=0'

# With filter for specific document types
curl 'http://localhost:5984/mydb/_changes?filter=app/design&since=100'

# With include_docs for full document data
curl 'http://localhost:5984/mydb/_changes?include_docs=true&since=100&limit=50'
```

### 3. Fix Changes Feed Timeout

```ini
; In local.ini - increase timeout for long-running feeds
[chttpd]
; Increase timeout for changes feed
; request_timeout = 60000

; Increase max HTTP connections
; max_connections = 2048
```

```bash
# Set up reverse proxy with long timeout
# In nginx:
# proxy_read_timeout 3600s;
# proxy_send_timeout 3600s;
```

### 4. Implement Change Processing with Checkpoints

```javascript
// Save and restore sequence for reliable processing
async function processChanges(db, lastSeq) {
  const response = await db.changes({
    since: lastSeq || 0,
    include_docs: true,
    live: true,
    returnDocs: false
  });

  response.on('change', async (change) => {
    await processDocument(change.doc);
    // Save checkpoint
    await saveSequence(change.seq);
  });

  response.on('error', (err) => {
    console.error('Changes feed error:', err);
    // Restart from last saved sequence
    setTimeout(() => processChanges(db, getSavedSequence()), 5000);
  });
}
```

## Common Scenarios

- **Changes feed drops connection**: Use `heartbeat` parameter and configure reverse proxy timeouts.
- **Since value too old after compaction**: Use `since=now` or the current `last_seq`.
- **Real-time app misses changes**: Implement checkpoints and restart from last processed sequence.

## Prevent It

- Always save processing checkpoints for long-running change listeners
- Use `heartbeat` to detect dead connections early
- Set up monitoring for changes feed lag

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Filter Error](/tools/couchdb/couchdb-filter-error)
- [CouchDB Stale Error](/tools/couchdb/couchdb-stale-error)
