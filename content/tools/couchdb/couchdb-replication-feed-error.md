---
title: "[Solution] CouchDB Replication Feed Error — How to Fix"
description: "Fix CouchDB replication feed errors by resolving replication feed failures, fixing continuous feed issues, and handling replication stream problems"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Feed Error

CouchDB replication feed errors occur when the replicator fails to read or process the changes feed from the source database during replication.

## Why It Happens

- Changes feed connection is lost
- Feed timeout is too short
- Feed is too large to process at once
- Source database is overloaded
- Network interruption during feed read
- Heartbeat not received from feed

## Common Error Messages

```
{ "error": "timeout", "reason": "Replication feed timeout" }
```

```
{ "error": "internal_server_error", "reason": "Feed connection lost" }
```

```
{ "error": "internal_server_error", "reason": "Feed processing error" }
```

```
{ "error": "internal_server_error", "reason": "Changes feed interrupted" }
```

## How to Fix It

### 1. Check Replication Feed

```bash
# Test changes feed
curl "http://localhost:5984/mydb/_changes?limit=10"

# Check feed status
curl http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication")'

# Monitor feed progress
curl "http://localhost:5984/mydb/_changes?feed=continuous&heartbeat=10000"
```

### 2. Fix Feed Timeout

```bash
# Create replication with longer timeout
curl -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "my_rep",
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "heartbeat": 60000,
    "connection_timeout": 120000
  }'
```

### 3. Fix Feed Connection

```bash
# Check network connectivity
ping source-host
telnet source-host 5984

# Restart replication
curl -X DELETE http://localhost:5984/_replicator/my_rep?rev=1-abc

curl -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "my_rep",
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "continuous": true
  }'
```

### 4. Monitor Feed Health

```bash
# Watch feed progress
while true; do
  curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {docs_written, doc_write_failures}'
  sleep 10
done

# Check feed logs
tail -f /opt/couchdb/log/couch.log | grep -i "feed\|changes"
```

## Common Scenarios

- **Feed timeout**: Increase heartbeat and connection_timeout.
- **Feed connection lost**: Check network and restart replication.
- **Feed too large**: Reduce batch size and increase workers.

## Prevent It

- Monitor replication feed health
- Set appropriate heartbeat values
- Use reliable network connections

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Changes Feed Error](/tools/couchdb/couchdb-changes-feed-error)
- [CouchDB Connection Error](/tools/couchdb/couchdb-connection-error)
