---
title: "[Solution] Neo4j Backup Error — How to Fix"
description: "Fix Neo4j backup errors including backup tool failures, dump issues, and restore problems with Neo4j database backups"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Backup Error

Backup errors in Neo4j occur when using `neo4j-admin database dump`, `neo4j-admin database backup`, or online backup tools. These include file access issues, lock conflicts, and version compatibility problems.

## Why It Happens

- The backup destination does not have enough disk space
- Another backup is running and the database is locked
- The backup tool version does not match the Neo4j version
- The database is in use and cannot be dumped cleanly
- The backup file is corrupted or incomplete
- The online backup agent is not configured

## Common Error Messages

```
Error: Backup failed: Unable to acquire lock on database 'neo4j'
```

```
Error: Unable to create backup: disk space insufficient
```

```
Error: Backup file is not a valid Neo4j backup
```

```
Error: Cannot backup: database is not idle
```

## How to Fix It

### 1. Use neo4j-admin Database Dump

```bash
# Stop Neo4j first for consistent dump
sudo systemctl stop neo4j

# Dump a specific database
neo4j-admin database dump neo4j --to-path=/backup/neo4j.dump

# Dump all databases
neo4j-admin database dump --to-path=/backup/all-databases.dump

# Start Neo4j
sudo systemctl start neo4j
```

### 2. Use Online Backup with neo4j-admin

```bash
# Online backup (requires Enterprise)
neo4j-admin database backup --from=localhost:6362 --to-path=/backup/neo4j-backup

# Backup with incremental support
neo4j-admin database backup --from=localhost:6362   --to-path=/backup/neo4j-backup   --name=neo4j
```

### 3. Fix Backup Lock Issues

```bash
# Check if another backup is running
ps aux | grep neo4j-admin

# Kill stale backup process
kill <pid>

# Retry backup
neo4j-admin database dump neo4j --to-path=/backup/neo4j.dump
```

### 4. Restore from Backup

```bash
# Stop Neo4j
sudo systemctl stop neo4j

# Copy backup to data directory
cp /backup/neo4j.dump /var/lib/neo4j/data/databases/neo4j.dump

# Restore
neo4j-admin database load neo4j --from-path=/backup --database=neo4j

# Start Neo4j
sudo systemctl start neo4j
```

## Common Scenarios

- **Backup fails with disk space error**: Free up space or use a different backup destination.
- **Online backup is slow**: Increase backup transfer rate or use compression.
- **Restore fails with version mismatch**: Use the same neo4j-admin version as the running Neo4j instance.

## Prevent It

- Schedule regular backups with cron and monitor for failures
- Test backup restoration on a staging server
- Keep backups in a different location from the data directory

## Related Pages

- [Neo4j Import Error](/tools/neo4j/neo4j-import-error)
- [Neo4j Transaction Error](/tools/neo4j/neo4j-transaction-error)
- [Neo4j Memory Error](/tools/neo4j/neo4j-memory-error)
