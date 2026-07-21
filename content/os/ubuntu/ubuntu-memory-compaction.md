---
title: "Ubuntu Memory Compaction Error"
description: "Memory compaction fails causing allocation stalls and performance issues"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Memory Compaction Error

Memory compaction fails causing allocation stalls and performance issues

## Common Causes

- Memory fragmentation preventing large contiguous allocations
- Compaction daemon not running
- Zone reclaim mode too aggressive
- Transparent hugepage compaction failing

## How to Fix

1. Check compaction: `cat /proc/vmstat | grep compact`
2. Trigger manual compaction: `echo 1 > /proc/sys/vm/compact_memory`
3. Check fragmentation: `cat /proc/buddyinfo`
4. Tune watermark: `sysctl vm.watermark_boost_factor=0`

## Examples

```bash
# Check memory compaction stats
grep -i compact /proc/vmstat

# Trigger manual compaction
echo 1 | sudo tee /proc/sys/vm/compact_memory

# Check buddyinfo for fragmentation
cat /proc/buddyinfo | head -5
```
