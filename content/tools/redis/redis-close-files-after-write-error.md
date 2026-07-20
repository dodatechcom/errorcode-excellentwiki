---
title: "[Solution] Redis Close Files After Write Error"
description: "How to fix Redis close-files-after configuration issues"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- File descriptors not being closed after writes
- File descriptor leak
- Too many open files

## Fix

Check open files:

```bash
ls /proc/$(pidof redis-server)/fd | wc -l
```

Set close-files-after-write:

```bash
redis-cli CONFIG SET close-files-after-write yes
```

Check file descriptor limits:

```bash
cat /proc/$(pidof redis-server)/limits | grep "open files"
```

Increase FD limit:

```bash
ulimit -n 65535
```

## Examples

```bash
# Check open FDs
ls /proc/$(pidof redis-server)/fd | wc -l

# Check FD limit
ulimit -n

# Monitor file descriptors
watch -n 5 'ls /proc/$(pidof redis-server)/fd | wc -l'
```
