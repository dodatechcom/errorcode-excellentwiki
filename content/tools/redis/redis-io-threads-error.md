---
title: "[Solution] Redis IO Threads Configuration Error"
description: "How to fix Redis io-threads configuration errors for multi-threaded I/O"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- io-threads set higher than CPU cores
- io-threads-do-reads not enabled
- System not supporting multi-threaded I/O

## Fix

Check CPU cores:

```bash
nproc
```

Set io-threads:

```bash
redis-cli CONFIG SET io-threads 4
redis-cli CONFIG SET io-threads-do-reads yes
```

Check if multi-threading is active:

```bash
redis-cli INFO server | grep io_threads
```

## Examples

```bash
# Check CPU cores
nproc

# Set io-threads
redis-cli CONFIG SET io-threads 4

# Verify settings
redis-cli CONFIG GET io-threads
redis-cli CONFIG GET io-threads-do-reads
```
