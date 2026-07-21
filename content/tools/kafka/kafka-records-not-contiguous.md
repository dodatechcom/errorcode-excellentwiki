---
title: "[Solution] Kafka Records Not Contiguous Error"
description: "Fix Kafka records not contiguous errors. Resolve gaps in offset sequences within log segments."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Records Not Contiguous Error

Kafka records not contiguous errors occur when the broker detects gaps in the offset sequence within a log segment, indicating data corruption or incomplete writes.

## Common Causes

- Unclean broker shutdown during a write operation
- Disk I/O error causing partial segment writes
- Log segment file corruption from storage failure
- Compaction merging error in compacted topics

## How to Fix

1. Check for disk errors on the broker:

```bash
dmesg | grep -i "error\|fail\|sector"
smartctl -a /dev/sda
```

2. Use the kafka-dump-log tool to inspect the segment:

```bash
kafka-run-class.sh kafka.tools.DumpLogSegments \
  --files /data/kafka-logs/my-topic-0/00000000000000000000.log
```

3. Delete the corrupted log segment (data loss):

```bash
# Stop the broker, then remove the corrupted segment
rm /data/kafka-logs/my-topic-0/00000000000000000005.log
```

4. Use the kafka-repair tool if available:

```bash
kafka-dirs.sh recover --cluster-metadata-directory \
  /data/kafka-logs/__cluster_metadata-0
```

## Examples

```bash
# Dump log segment contents
kafka-run-class.sh kafka.tools.DumpLogSegments \
  --files /data/kafka-logs/my-topic-0/00000000000000000000.log \
  --print-decoded-headers
```
