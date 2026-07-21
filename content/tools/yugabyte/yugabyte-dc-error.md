---
title: "[Solution] YugabyteDB Data Center Error"
description: "How to fix YugabyteDB data center configuration errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- DC not in placement policy
- Network between DCs blocked
- DC replication factor wrong

## How to Fix

```bash
yb-admin modify_placement_info mydb placement_info=cloud1.dc1.rack1:1
```

## Examples

```bash
yb-admin get_placement_info mydb
```
