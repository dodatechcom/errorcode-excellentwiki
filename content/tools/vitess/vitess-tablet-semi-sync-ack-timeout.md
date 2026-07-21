---
title: "[Solution] Vitess Tablet Semi-Sync ACK Timeout"
description: "Fix Vitess semi-synchronous replication ACK timeout when replicas fail to acknowledge writes"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Semi-Sync ACK Timeout

Semi-sync ACK timeout errors occur when the primary tablet does not receive replica acknowledgment within the configured timeout.

## Common Causes

- Replica tablet lagging behind primary
- Network latency between primary and replicas
- Semi-sync timeout configured too low
- Replica IO thread stopped or sql thread behind

## How to Fix

Check replication status:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "SHOW REPLICA STATUS\G"
```

Increase semi-sync timeout:

```sql
SET GLOBAL rpl_semi_sync_master_timeout = 5000;
```

Restart replication on lagging replica:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-101 "START REPLICA"
```

## Examples

```sql
SHOW STATUS LIKE 'Rpl_semi_sync_master_yes_tx';
```
