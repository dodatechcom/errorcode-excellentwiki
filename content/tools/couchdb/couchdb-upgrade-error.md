---
title: "[Solution] CouchDB Upgrade Error — How to Fix"
description: "Fix CouchDB upgrade errors by migrating configuration files, resolving version compatibility issues, and handling data directory changes"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Upgrade Error

CouchDB upgrade errors occur when upgrading between major versions (e.g., 2.x to 3.x) due to configuration changes, data format incompatibilities, or missing migration steps.

## Why It Happens

- Configuration file format changed between versions
- Data directory structure is incompatible
- Erlang version requirement is not met
- Design documents use deprecated APIs
- Cluster configuration needs manual migration
- npm/node dependencies are missing for Fauxton

## Common Error Messages

```
{ "error": "bad_config", "reason": "invalid configuration" }
```

```
{ "error": "internal_server_error", "reason": "data directory incompatible" }
```

```
{ "error": "not_found", "reason": "missing" }
```

```
Error: Erlang/OTP version mismatch
```

## How to Fix It

### 1. Backup Before Upgrade

```bash
# Stop CouchDB
sudo systemctl stop couchdb

# Backup configuration
cp -r /opt/couchdb/etc /backup/couchdb-etc-backup

# Backup data
cp -r /opt/couchdb/data /backup/couchdb-data-backup

# Backup _replicator state
curl http://localhost:5984/_replicator/_all_docs?include_docs=true > /backup/replicator.json

# Create full backup
tar -czf /backup/couchdb-full-backup-$(date +%Y%m%d).tar.gz \
  /opt/couchdb/etc /opt/couchdb/data
```

### 2. Migrate Configuration

```bash
# CouchDB 3.x uses different config structure
# Key changes from 2.x to 3.x:

# 1. [couch_httpd] renamed to [chttpd]
# 2. bind_address default changed
# 3. Authentication is enabled by default (no more "admin party")
# 4. Default port changed for clusters

# Generate new default config
/opt/couchdb/etc/local.ini.default

# Merge old settings into new config
vimdiff /opt/couchdb/etc/local.ini.default /opt/couchdb/etc/local.ini
```

### 3. Run Data Migration

```bash
# CouchDB 3.x requires specific data directory format
# Check current data format
ls -la /opt/couchdb/data/

# For clustered setup, ensure proper shard naming
ls /opt/couchdb/data/shards/

# If upgrading from 1.x to 3.x:
# 1. First upgrade to 2.x
# 2. Run _replicate to migrate data
# 3. Then upgrade to 3.x
```

### 4. Verify Upgrade Success

```bash
# Start CouchDB
sudo systemctl start couchdb

# Check version
curl http://localhost:5984/ | jq '.version'

# Check membership
curl http://localhost:5984/_membership

# Verify all databases are accessible
curl http://localhost:5984/_all_dbs

# Check replicator state
curl http://localhost:5984/_replicator/_changes?limit=5

# Test a document operation
curl -X PUT http://localhost:5984/testdb/_design/test \
  -H "Content-Type: application/json" \
  -d '{"_id": "_design/test", "views": {"all": {"map": "function(doc) { emit(doc._id, null); }"}}}'
```

## Common Scenarios

- **Config syntax error after upgrade**: Merge old config with new default config format.
- **Authentication required**: Create admin user immediately after upgrade.
- **Design documents broken**: Update view functions to use compatible JavaScript.

## Prevent It

- Always read the release notes before upgrading
- Test upgrades on a staging environment first
- Keep backups of configuration and data directories

## Related Pages

- [CouchDB Config Error](/tools/couchdb/couchdb-config-error)
- [CouchDB Restart Error](/tools/couchdb/couchdb-restart-error)
- [CouchDB Node Error](/tools/couchdb/couchdb-node-error)
