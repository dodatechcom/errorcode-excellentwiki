---
title: "[Solution] Redis Active Defrag Configuration Error"
description: "How to fix Redis active defragmentation configuration errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- activedefrag enabled without sufficient CPU
- Active defrag thresholds not set properly
- Memory fragmentation ratio incorrect

## Fix

Check defrag settings:

```bash
redis-cli CONFIG GET activedefrag
redis-cli CONFIG GET active-defrag-enabled
```

Configure defrag thresholds:

```bash
redis-cli CONFIG SET active-defrag-threshold-lower 10
redis-cli CONFIG SET active-defrag-threshold-upper 100
redis-cli CONFIG SET active-defrag-cycle-min 1
redis-cli CONFIG SET active-defrag-cycle-max 25
```

Enable active defrag:

```bash
redis-cli CONFIG SET activedefrag yes
```

## Examples

```bash
# Check fragmentation
redis-cli INFO memory | grep mem_fragmentation_ratio

# Check defrag status
redis-cli INFO stats | grep active_defrag

# Configure defrag
redis-cli CONFIG SET activedefrag yes
```
