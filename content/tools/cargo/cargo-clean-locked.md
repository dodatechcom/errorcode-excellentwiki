---
title: "[Solution] Cargo Clean Locked -- Fix Locked Cache Cleanup"
description: "Fix cargo clean locked errors when cargo cannot clean because files are locked by another process. Find and stop the locking process."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means cargo cannot remove build artifacts because another cargo process has a lock on them.

## Common Causes

- Another cargo build is running
- A cargo watch process is active
- The process crashed without releasing the lock
- Build directory permissions are wrong

## How to Fix

### 1. Find the Locking Process

```bash
fuser target/
lsof +D target/
```

### 2. Kill Stale Processes

```bash
pkill -f "cargo build"
```

### 3. Remove Target Directory

```bash
rm -rf target/
```

### 4. Clean Without Lock Check

```bash
cargo clean --target-dir /tmp/cargo-clean-target
```

## Examples

```bash
$ cargo clean
error: could not remove build directory: target/

$ fuser target/
cargo    12345  # PID holding the lock

$ kill 12345
$ cargo clean
```
