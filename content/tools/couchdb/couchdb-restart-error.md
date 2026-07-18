---
title: "[Solution] CouchDB Restart Error — How to Fix"
description: "Fix CouchDB restart errors by resolving service startup failures, fixing configuration syntax, and recovering from crash loops"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Restart Error

CouchDB restart errors occur when the service fails to start after a restart, configuration change, or crash. Common causes include config syntax errors, port conflicts, and permission issues.

## Why It Happens

- Configuration file contains syntax errors
- Port 5984 is already in use by another process
- Data directory permissions are incorrect
- Erlang VM fails to start due to resource limits
- Log directory is not writable
- CouchDB crashes immediately after starting

## Common Error Messages

```
{ "error": "eaddrinuse", "reason": "Address already in use - bind(2) for 0.0.0.0:5984" }
```

```
{ "error": "eacces", "reason": "Permission denied - open(2) for /opt/couchdb/data" }
```

```
{ "error": "enomem", "reason": "not enough memory" }
```

```
Error: process already_running
```

## How to Fix It

### 1. Check Configuration Syntax

```bash
# Validate local.ini syntax
cat /opt/couchdb/etc/local.ini

# Check for common issues:
# - Missing section headers [section]
# - Incorrect key-value format
# - Unclosed quotes or brackets
# - Invalid Erlang terms in daemons section
```

```ini
; Correct format example
[chttpd]
bind_address = 0.0.0.0
port = 5984

[httpd]
bind_address = 0.0.0.0
port = 5984
```

### 2. Fix Port Conflict

```bash
# Check what's using port 5984
sudo lsof -i :5984
sudo ss -tlnp | grep 5984

# Kill conflicting process
sudo fuser -k 5984/tcp

# Or change CouchDB port
# In local.ini:
# [chttpd]
# port = 5985
```

### 3. Fix Permission Issues

```bash
# Check CouchDB user
id couchdb

# Fix data directory permissions
sudo chown -R couchdb:couchdb /opt/couchdb/data/
sudo chmod -R 755 /opt/couchdb/data/

# Fix log directory
sudo chown -R couchdb:couchdb /opt/couchdb/log/
sudo chmod -R 755 /opt/couchdb/log/

# Fix config directory
sudo chown -R couchdb:couchdb /opt/couchdb/etc/
```

### 4. Start CouchDB and Debug

```bash
# Start with verbose output
sudo systemctl start couchdb
sudo systemctl status couchdb

# Check logs for startup errors
sudo journalctl -u couchdb -n 100 --no-pager
tail -100 /opt/couchdb/log/couch.log

# Run CouchDB directly for debugging
sudo -u couchdb /opt/couchdb/bin/couchdb -c /opt/couchdb/etc/local.ini

# Check erlang distribution
curl http://localhost:5984/
curl http://localhost:5984/_up
```

## Common Scenarios

- **Config change breaks startup**: Revert to the last known good configuration.
- **OOM kill on restart**: Increase system memory or reduce CouchDB memory limits.
- **Crash loop after data corruption**: Start with a clean data directory and restore from backup.

## Prevent It

- Always validate configuration before restarting
- Use `systemctl status couchdb` to check status before proceeding
- Keep backup copies of working configuration files

## Related Pages

- [CouchDB Node Error](/tools/couchdb/couchdb-node-error)
- [CouchDB Disk Error](/tools/couchdb/couchdb-disk-error)
- [CouchDB Connection Error](/tools/couchdb/couchdb-connection-error)
