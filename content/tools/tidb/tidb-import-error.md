---
title: "[Solution] TiDB Import Error — How to Fix"
description: "Fix TiDB import errors by resolving Lightning import failures, fixing CSV/SQL loading issues, and handling bulk data import problems"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Import Error

TiDB import errors occur when using TiDB Lightning, LOAD DATA, or other bulk import tools to load data into TiDB.

## Why It Happens

- TiDB Lightning cannot connect to TiKV
- Import file format is incorrect
- CSV data has parsing errors
- Import exceeds memory limits
- Target table already has data
- Import is interrupted by network issues

## Common Error Messages

```
ERROR: TiDB Lightning import failed
```

```
ERROR: CSV parsing failed
```

```
ERROR: target table already has data
```

```
ERROR: import timeout
```

## How to Fix It

### 1. Use TiDB Lightning

```bash
# Configure TiDB Lightning
cat > lightning.toml << 'EOF'
[lightning]
tidb-host = "tidb1"
tidb-port = 4000
pd-urls = "pd1:2379,pd2:2379,pd3:2379"

[mydumper]
data-source-dir = "/data/dump"

[tikv-importer]
backend = "local"
EOF

# Run TiDB Lightning
tidb-lightning -config lightning.toml
```

### 2. Fix CSV Import

```sql
-- Load CSV data
LOAD DATA LOCAL INFILE '/data/users.csv'
INTO TABLE users
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(name, email, created_at);
```

### 3. Fix Lightning Import

```bash
# Check Lightning logs
tail -50 /var/log/tidb-lightning/lightning.log

# Fix common issues:
# 1. Increase memory: --tidb-lightning-tidb-mem-quota=10737418240
# 2. Use local backend for speed
# 3. Ensure TiKV is healthy before import
```

### 4. Monitor Import Progress

```bash
# Check Lightning progress
curl http://tidb1:10080/status | jq '.lightning'

# Monitor TiKV during import
curl http://tikv1:20180/metrics | grep import
```

## Common Scenarios

- **Lightning import is slow**: Use local backend instead of tidb backend.
- **CSV parsing fails**: Check file format and encoding.
- **Import fails mid-way**: Restart Lightning with checkpoint enabled.

## Prevent It

- Validate data files before import
- Test Lightning on staging first
- Monitor import progress and TiKV health

## Related Pages

- [TiDB DML Error](/tools/tidb/tidb-dml-error)
- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)
- [TiDB DDL Error](/tools/tidb/tidb-ddl-error)
