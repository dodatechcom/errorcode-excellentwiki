---
title: "[Solution] CouchDB Replication Heartbeat Error — How to Fix"
description: "Fix CouchDB replication heartbeat errors by resolving heartbeat timeout issues, fixing heartbeat configuration problems, and handling heartbeat detection failures"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["warning"]
weight: 5
comments: true
---

# CouchDB Replication Heartbeat Error

CouchDB replication heartbeat errors occur when the replicator fails to receive heartbeats from source or target, causing false disconnection detection.

## Why It Happens

- Heartbeat interval is too short
- Network latency exceeds heartbeat timeout
- Source or target is overloaded
- Heartbeat packets are lost
- Heartbeat configuration is incorrect
- Slow network causes heartbeat delays

## Common Error Messages

```
{ "error": "timeout", "reason": "Heartbeat timeout" }
```

```
{ "error": "internal_server_error", "reason": "No heartbeat received" }
```

```
{ "error": "timeout", "reason": "Replication heartbeat failed" }
```

```
WARNING: Heartbeat not received from source
```

## How to Fix It

### 1. Check Heartbeat Settings

```bash
# Check replication document
curl http://localhost:5984/_replicator/my_rep | jq '.heartbeat'

# Check active tasks
curl http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {pid, status}'
```

### 2. Increase Heartbeat Interval

```bash
# Create replication with longer heartbeat
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

### 3. Fix Network Issues

```bash
# Test network latency
ping source-host
ping target-host

# Check for packet loss
ping -c 100 source-host | tail -3

# Check network stats
netstat -s | grep -i "retransmit\|timeout"
```

### 4. Monitor Heartbeat

```bash
# Watch replication status
while true; do
  curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {pid, status, docs_written}'
  sleep 30
done

# Check CouchDB logs for heartbeat
tail -f /opt/couchdb/log/couch.log | grep -i heartbeat
```

## Common Scenarios

- **Heartbeat timeout**: Increase heartbeat interval.
- **False disconnection**: Check network latency and increase timeout.
- **Heartbeat not received**: Check source/target health.

## Prevent It

- Configure appropriate heartbeat values
- Monitor network latency
- Use reliable network connections

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Replication Timeout Error](/tools/couchdb/couchdb-replication-timeout-error)
- [CouchDB Network Error](/tools/couchdb/couchdb-network-error)
