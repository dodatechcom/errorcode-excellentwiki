---
title: "[Solution] Neo4j Store Files Corrupted Error"
description: "How to fix Neo4j store file corruption errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Unclean shutdown
- Disk failure
- Power loss during write

## How to Fix

Run consistency check:

```bash
neo4j-admin database consistency mydb --check-graph --verbose
```

## Examples

```bash
neo4j-admin database consistency mydb
```
