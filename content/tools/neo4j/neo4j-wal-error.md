---
title: "[Solution] Neo4j WAL Error — How to Fix"
description: "Fix Neo4j Write-Ahead Log (WAL) errors including WAL file issues, log rotation problems, and WAL configuration errors"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j WAL Error

Write-Ahead Log (WAL) errors in Neo4j occur when the transaction log files are corrupted, full, or misconfigured. WAL is critical for data durability and recovery.

## Why It Happens

- The WAL directory is full and cannot write new transactions
- The WAL files are corrupted due to a crash during write
- The WAL rotation settings are too aggressive or too conservative
- The WAL file size exceeds the configured maximum
- The transaction log is not properly flushed to disk

## Common Error Messages

```
ERROR: Failed to write to transaction log: No space left on device
```

```
ERROR: Transaction log corruption detected
```

```
WARNING: WAL file size exceeds maximum configured size
```

```
Neo4j failed to start: Could not open transaction log
```

## How to Fix It

### 1. Fix WAL Disk Space

```bash
# Check WAL directory space
df -h /var/lib/neo4j/data/transactions/

# Find large WAL files
ls -lhS /var/lib/neo4j/data/transactions/neo4j/

# Clean up old WAL files (only if Neo4j is stopped)
sudo systemctl stop neo4j
rm /var/lib/neo4j/data/transactions/neo4j/neostore.*.db
sudo systemctl start neo4j
```

### 2. Fix WAL Rotation Settings

```bash
# In neo4j.conf
dbms.tx_log.rotation.size=100M
dbms.tx_log.rotation.retention_policy=7 days
```

### 3. Fix Corrupted WAL

```bash
# Stop Neo4j
sudo systemctl stop neo4j

# Check and repair the database
neo4j-admin database recover /var/lib/neo4j/data/databases/neo4j

# If repair fails, restore from backup
neo4j-admin database load neo4j --from-path=/backup

sudo systemctl start neo4j
```

### 4. Monitor WAL Health

```bash
# Check WAL file count and size
ls -la /var/lib/neo4j/data/transactions/neo4j/

# Monitor WAL rotation in logs
grep -i "wal\|transaction log" /var/log/neo4j/neo4j.log
```

## Common Scenarios

- **WAL directory fills up**: Free disk space and clean old WAL files.
- **WAL corruption after crash**: Use `neo4j-admin database recover` to repair.
- **WAL rotation not working**: Adjust `dbms.tx_log.rotation.size` and retention policy.

## Prevent It

- Monitor WAL disk usage and set alerts at 70% capacity
- Configure appropriate WAL rotation settings for your workload
- Ensure proper shutdown of Neo4j to avoid WAL corruption

## Related Pages

- [Neo4j Kernel Error](/tools/neo4j/neo4j-kernel-error)
- [Neo4j Transaction Error](/tools/neo4j/neo4j-transaction-error)
- [Neo4j Backup Error](/tools/neo4j/neo4j-backup-error)
