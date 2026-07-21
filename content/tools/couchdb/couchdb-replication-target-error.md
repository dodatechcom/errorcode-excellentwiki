---
title: "[Solution] CouchDB Replication Target Error — How to Fix"
description: "Fix CouchDB replication target errors by resolving target database connection issues, fixing target write permission problems, and handling target database unavailability"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Target Error

CouchDB replication target errors occur when the replicator cannot connect to or write to the target database during replication.

## Why It Happens

- Target database is unreachable
- Target credentials are invalid
- Target database is read-only
- Target database disk is full
- Target database does not exist and create_target is false
- Target database conflicts prevent writes

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "Target database unreachable" }
```

```
{ "error": "unauthorized", "reason": "Target authentication failed" }
```

```
{ "error": "forbidden", "reason": "Target database is read-only" }
```

```
{ "error": "internal_server_error", "reason": "Target disk full" }
```

## How to Fix It

### 1. Check Target Connectivity

```bash
# Test target connection
curl -u user:pass http://target-host:5984/mydb

# Check target database
curl -u user:pass http://target-host:5984/mydb | jq '.db_name'

# Check target disk space
ssh target-host "df -h /opt/couchdb/data"
```

### 2. Fix Target Permissions

```bash
# Check target user permissions
curl -u user:pass http://target-host:5984/_session | jq '.userCtx'

# Grant write permissions to target user
curl -X PUT http://target-host:5984/_users/org.couchdb.user:replicator \
  -H "Content-Type: application/json" \
  -d '{"name": "replicator", "password": "secret", "roles": [], "type": "user"}'

# Grant database admin
curl -X PUT http://target-host:5984/_node/_local/_security \
  -H "Content-Type: application/json" \
  -d '{"admins": {"names": ["replicator"], "roles": []}, "readers": {"names": [], "roles": []}}'
```

### 3. Fix Target Database Issues

```bash
# Create target database
curl -X PUT http://target-host:5984/mydb

# Enable create_target in replication
curl -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "my_rep",
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "create_target": true
  }'

# Free disk space on target
ssh target-host "rm -f /opt/couchdb/data/shards/*/.compact*"
```

### 4. Handle Target Conflicts

```bash
# Check for conflicts on target
curl -u user:pass "http://target-host:5984/mydb/doc123?conflicts=true"

# Resolve conflicts on target
curl -u user:pass -X DELETE "http://target-host:5984/mydb/doc123?rev=2-abc"
```

## Common Scenarios

- **Target unreachable**: Check network connectivity and firewall rules.
- **Target disk full**: Free space on target or add more storage.
- **Target read-only**: Check and update user permissions.

## Prevent It

- Verify target connectivity and permissions before replication
- Monitor target disk space
- Use create_target option for new databases

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Connection Error](/tools/couchdb/couchdb-connection-error)
- [CouchDB Replication Source Error](/tools/couchdb/couchdb-replication-source-error)
