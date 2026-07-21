---
title: "[Solution] Vitess Tablet Alias Error"
description: "Fix Vitess tablet alias mismatch errors when tablet references become invalid"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Alias Error

Tablet alias errors occur when a tablet operation references an alias that does not match any registered tablet in the topology.

## Common Causes

- Tablet was recreated with a new alias after hostname change
- Topo entry deleted but vtctl still referencing old alias
- Cell name changed in tablet alias after infrastructure migration
- Stale alias in routing rules or shard configuration

## How to Fix

List current tablets:

```bash
vtctlclient ListAllTablets cell1
```

Remove stale topo entries:

```bash
vtctlclient DeleteTablet cell1-tablet-100
```

Re-register tablet with correct alias:

```bash
vttablet -tablet-path cell1-tablet-100 -init_keyspace keyspace1 -init_shard 0 -tablet_type replica
```

## Examples

```bash
vtctlclient GetTablet cell1-tablet-100
```
