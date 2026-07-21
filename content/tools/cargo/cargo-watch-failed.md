---
title: "[Solution] Cargo Watch Failed -- Fix File Watch Error"
description: "Fix cargo watch failed errors when cargo-watch fails to monitor file changes. Check file system events and configuration."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `cargo watch` encountered an error while monitoring file changes.

## Common Causes

- Too many files to watch (inotify limit)
- File system does not support inotify
- Network filesystem (NFS) cannot be watched
- cargo-watch is not installed

## How to Fix

### 1. Install cargo-watch

```bash
cargo install cargo-watch
```

### 2. Increase Inotify Limit

```bash
echo 65536 | sudo tee /proc/sys/fs/inotify/max_user_watches
```

### 3. Ignore Target Directory

```bash
cargo watch -i target/ -x run
```

### 4. Use Polling Instead

```bash
CARGO_WATCH_USE_POLLING=true cargo watch -x run
```

## Examples

```bash
$ cargo watch -x run
error: system limit for number of file watchers reached

$ echo 65536 | sudo tee /proc/sys/fs/inotify/max_user_watches
$ cargo watch -x run
Watching...
```
