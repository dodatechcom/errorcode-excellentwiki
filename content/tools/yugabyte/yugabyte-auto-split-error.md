---
title: "[Solution] YugabyteDB Auto Split Error — How to Fix"
description: "Fix YugabyteDB auto split errors by tuning split thresholds, resolving excessive tablet creation, and fixing split configuration issues"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Auto Split Error

YugabyteDB auto split errors occur when automatic tablet splitting creates too many tablets, too few tablets, or fails during the split process.

## Why It Happens

- Auto-split threshold is too low causing excessive splitting
- Split produces tablets below minimum size
- Too many tablets degrade performance
- Split is not triggered when needed
- Concurrent writes prevent clean split
- Tablet count exceeds recommended limit

## Common Error Messages

```
WARNING: auto-split creating excessive tablets
```

```
ERROR: tablet below minimum size after split
```

```
WARNING: tablet count exceeds recommended limit
```

```
ERROR: auto-split unable to split tablet
```

## How to Fix It

### 1. Tune Auto-Split Thresholds

```bash
# In tserver.gflags:
--enable_tablet_split_of_hot_data=true
--auto_split_num_tablets_shards_per_tserver=10

-- Increase size thresholds to reduce splitting:
--tablet_split_low_phase_size_threshold_bytes=2147483648   # 2GB
--tablet_split_high_phase_size_threshold_bytes=42949672960  # 40GB
```

### 2. Control Tablet Count Per Table

```sql
-- Set specific tablet count for table
CREATE TABLE events (
  id UUID NOT NULL,
  data JSONB,
  PRIMARY KEY (id)
) SPLIT INTO 8 TABLETS;

-- Or use hash sharding
CREATE TABLE users (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name TEXT
) SPLIT INTO 4 TABLETS;
```

### 3. Monitor Tablet Creation

```bash
# Check tablet count per table
/home/yugabyte/tserver/bin/yb-admin list_tables

# Monitor auto-split events
grep "auto_split\|split_tablet" /home/yugabyte/yugabyte-data/master/logs/yb-master.INFO | tail -20

# Check tablet sizes
curl http://yb-tserver-1:9000/metrics | grep tablet_size
```

### 4. Fix Excessive Tablets

```bash
# Disable auto-split temporarily
# In tserver.gflags:
--enable_tablet_split_of_hot_data=false

# Wait for tablet count to stabilize
# Then re-enable with higher thresholds
```

## Common Scenarios

- **Tablet count explodes**: Increase split thresholds or disable auto-split.
- **Split not triggering**: Decrease size threshold for faster splitting.
- **Too many small tablets**: Merge tables or reduce initial tablet count.

## Prevent It

- Set appropriate split thresholds for your workload
- Monitor tablet count and size regularly
- Pre-split tables with known large data volumes

## Related Pages

- [YugabyteDB Split Error](/tools/yugabyte/yugabyte-split-error)
- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
- [YugabyteDB Config Error](/tools/yugabyte/yugabyte-gflag-error)
