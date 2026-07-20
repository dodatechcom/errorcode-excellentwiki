---
title: "[Solution] Redis OOM Score Adjust Configuration Error"
description: "How to fix Redis oom-score-adj configuration for Linux OOM killer behavior"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- oom-score-adj set too low causing Redis to be killed first
- oom-score-adj value out of range (-1000 to 1000)
- OOM killer targeting Redis in memory pressure

## Fix

Check oom-score-adj:

```bash
redis-cli CONFIG GET oom-score-adj
```

Set lower oom-score-adj (less likely to be killed):

```bash
redis-cli CONFIG SET oom-score-adj -500
```

Check Redis OOM score:

```bash
cat /proc/$(pidof redis-server)/oom_score
```

## Examples

```bash
# Check OOM score
cat /proc/$(pidof redis-server)/oom_score

# Set oom-score-adj
redis-cli CONFIG SET oom-score-adj -500

# Check OOM adj
cat /proc/$(pidof redis-server)/oom_score_adj
```
