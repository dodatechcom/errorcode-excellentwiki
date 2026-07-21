---
title: "[Solution] ScyllaDB Hinted Handoff Overflow Error — How to Fix"
description: "Fix ScyllaDB hinted handoff overflow errors when the hint queue fills up and starts dropping hints"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Hinted Handoff Overflow Error

Hinted handoff overflow errors occur when the hint queue for a target node exceeds its maximum capacity, causing ScyllaDB to drop hints and potentially lose data.

## Why It Happens

- Target node has been down for an extended period
- Too many concurrent writes to down nodes
- Hint storage disk is full
- Hint window has expired
- Network partition prevents hint delivery

## Common Error Messages

```
HintedHandoff: dropping hints for node3, queue is full
```

```
WARN: exceeded maximum hinted handoff queue for node 10.0.0.3
```

```
error: hint handoff disk full, cannot store new hints
```

## How to Fix It

### 1. Check Hint Queue Status

```bash
nodetool tpstats | grep -i hint
nodetool hintssubmitrate
```

### 2. Increase Hint Queue Size

```yaml
# In scylla.yaml
max_hint_window_in_ms: 10800000
hinted_handoff_throttle_in_kb: 1024
max_hints_per_node_per_sec: 10
```

### 3. Free Hint Storage Disk Space

```bash
df -h /var/lib/scylla/hints
du -sh /var/lib/scylla/hints/*
```

### 4. Run Full Repair After Node Recovery

```bash
# After the down node recovers
nodetool repair mykeyspace
```

## Examples

```
$ nodetool tpstats | grep -i hint
  HintedHandoff     | pending=5000 | completed=25000 | dropped=2500
```

## Prevent It

- Monitor hinted handoff queue metrics
- Ensure target nodes are healthy
- Run repair after extended outages

## Related Pages

- [ScyllaDB Hinted Handoff Error](/tools/scylladb/scylladb-hinted-handoff-error)
- [ScyllaDB Hints Not Enabled](/tools/scylladb/scylladb-hints-not-enabled)
- [ScyllaDB Node Down](/tools/scylladb/scylladb-node-down)
