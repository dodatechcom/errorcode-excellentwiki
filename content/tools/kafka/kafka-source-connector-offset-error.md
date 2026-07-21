---
title: "[Solution] Kafka Source Connector Offset Error"
description: "Fix Kafka source connector offset errors. Resolve offset commit failures in Kafka Connect source tasks."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Source Connector Offset Error

Kafka source connector offset errors occur when a source connector task fails to commit offsets, causing duplicate records or offset inconsistency in the internal offset topic.

## Common Causes

- offset.storage.topic does not exist or is not writable
- Connector task restart before offset was committed
- offset.flush.interval.ms set too high causing data gaps
- Internal __consumer_offsets topic corruption

## How to Fix

1. Check the offset storage topic:

```bash
kafka-topics.sh --describe --bootstrap-server localhost:9092 \
  --topic connect-offsets
```

2. Adjust offset flush settings:

```json
{
  "offset.flush.interval.ms": "10000",
  "offset.flush.timeout.ms": "5000"
}
```

3. Verify the connector task status:

```bash
curl -X GET "localhost:8083/connectors/my-source/status" | python3 -m json.tool
```

4. If offset topic is corrupted, reset the connector:

```bash
# Delete the connector and recreate
curl -X DELETE "localhost:8083/connectors/my-source"
curl -X POST "localhost:8083/connectors" \
  -H "Content-Type: application/json" \
  -d @source-config.json
```

## Examples

```bash
# Monitor offset commits
watch -n 5 "curl -s localhost:8083/connectors/my-source/status | \
  python3 -c 'import sys,json; d=json.load(sys.stdin); \
  [print(f\"Task {t[\"id\"]}: {t[\"state\"]}\") for t in d[\"tasks\"]]'"
```
