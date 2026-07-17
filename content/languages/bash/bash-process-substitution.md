---
title: "[Solution] Bash Process Substitution Failed"
description: "Fix 'cannot use process substitution' when Bash fails with <() or >() syntax. Resolve /dev/fd and named pipe issues."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["process-substitution", "dev-fd", "named-pipe", "compare"]
weight: 5
---

# Bash Process Substitution Failed Fix

Process substitution errors occur when Bash cannot create a process substitution using `<()` (read from process) or `>()` (write to process).

## What This Error Means

Process substitution creates a temporary named pipe or `/dev/fd` entry that represents the stdout/stdin of a subprocess. Errors occur when `/dev/fd` is unavailable or the shell doesn't support the feature.

## Common Causes

- Using `sh` instead of `bash` (sh doesn't support process substitution)
- `/dev/fd` not available on the system
- Named pipe creation failing due to permissions
- Too many open file descriptors

## How to Fix

### 1. Use bash shebang

```bash
#!/bin/bash  # NOT #!/bin/sh
diff <(sort file1) <(sort file2)
```

### 2. Check /dev/fd availability

```bash
# Verify /dev/fd exists
ls -la /dev/fd/

# If missing, mount it (Linux):
sudo mount -t devtmpfs devtmpfs /dev
```

### 3. Use temporary files as alternative

```bash
# Instead of process substitution:
sort file1 > /tmp/sorted1
sort file2 > /tmp/sorted2
diff /tmp/sorted1 /tmp/sorted2
rm /tmp/sorted1 /tmp/sorted2
```

### 4. Use named pipes manually

```bash
mkfifo /tmp/pipe1
sort file1 > /tmp/pipe1 &
diff /tmp/pipe1 file2
rm /tmp/pipe1
```

## Related Errors

- [Pipe Error](bash-pipe-error) — pipeline failures
- [Here Document](bash-here-document) — heredoc syntax issues
