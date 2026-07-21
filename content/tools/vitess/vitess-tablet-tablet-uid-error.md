---
title: "[Solution] Vitess Tablet UID Error"
description: "Fix Vitess tablet UID conflicts when two tablets share the same UID"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet UID Error

Tablet UID errors occur when two tablets register with the same UID, causing topology conflicts.

## Common Causes

- Tablet UID not unique within the cell
- Tablet restarted without cleaning up old topo entry
- UID assigned manually and collided with auto-generated UID
- Container orchestration reusing UIDs across restarts

## How to Fix

List all tablets with UIDs:

```bash
vtctlclient ListAllTablets cell1 | awk '{print $1, $5}'
```

Delete conflicting tablet entry:

```bash
vtctlclient DeleteTablet -allow_remove_master cell1-tablet-100
```

Re-register with unique UID:

```bash
vttablet -tablet_uid 200 -init_keyspace keyspace1 -init_shard 0 -tablet_type replica
```

## Examples

```bash
vtctlclient ListAllTablets cell1
```
