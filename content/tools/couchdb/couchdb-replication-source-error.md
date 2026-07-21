---
title: "[Solution] CouchDB Replication Source Error — How to Fix"
description: "Fix CouchDB replication source errors by resolving source database connection issues, fixing source authentication problems, and handling source database unavailability"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Source Error

CouchDB replication source errors occur when the replicator cannot connect to or read from the source database during replication.

## Why It Happens

- Source database is unreachable
- Source credentials are invalid
- Source database does not exist
- Source database has permission restrictions
- Network timeout during replication
- Source database is overloaded

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "Source database unreachable" }
```

```
{ "error": "unauthorized", "reason": "Source authentication failed" }
```

```
{ "error": "not_found", "reason": "Source database not found" }
```

```
{ "error": "timeout", "reason": "Source connection timeout" }
```

## How to Fix It

### 1. Check Source Connectivity

```bash
# Test source connection
curl -u user:pass http://source-host:5984/mydb

# Check source database exists
curl -u user:pass http://source-host:5984/ | jq '.couchdb'

# Check source replication info
curl -u user:pass http://source-host:5984/mydb
```

### 2. Fix Source Authentication

```bash
# Test authentication
curl -u user:pass http://source-host:5984/_session

# Create replication with correct credentials
curl -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "my_rep",
    "source": {
      "url": "http://source-host:5984/db",
      "headers": {
        "Authorization": "Basic dXNlcjpwYXNz"
      }
    },
    "target": "http://localhost:5984/db"
  }'
```

### 3. Fix Source Database Issues

```bash
# Verify source database
curl -u user:pass http://source-host:5984/mydb | jq '.db_name, .doc_count'

# Check source disk space
ssh source-host "df -h /opt/couchdb/data"

# Check source logs
ssh source-host "tail -50 /opt/couchdb/log/couch.log"
```

### 4. Increase Timeouts

```bash
# Create replication with longer timeouts
curl -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "my_rep",
    "source": "http://source:5984/db",
    "target": "http://localhost:5984/db",
    "connection_timeout": 30000,
    "retries_per_request": 10,
    "worker_processes": 2
  }'
```

## Common Scenarios

- **Source unreachable**: Check network connectivity and firewall rules.
- **Authentication failed**: Verify credentials and user permissions.
- **Source database not found**: Verify database name and existence on source.

## Prevent It

- Verify source connectivity before starting replication
- Store credentials securely using CouchDB secrets
- Monitor replication for connection issues

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Connection Error](/tools/couchdb/couchdb-connection-error)
- [CouchDB Replication Target Error](/tools/couchdb/couchdb-replication-target-error)
