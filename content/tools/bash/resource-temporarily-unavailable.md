---
title: "[Solution] Resource Temporarily Unavailable"
description: "Fix 'resource temporarily unavailable' (EAGAIN) in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Resource Temporarily Unavailable

A system resource is temporarily exhausted and the operation would block.

### Common Causes
- Too many open file descriptors.
- Process table full.
- Memory pressure causing OOM conditions.

### How to Fix
```bash
# Check open file descriptors
ls /proc/$$/fd | wc -l

# Increase file descriptor limit
ulimit -n 65536

# Check system-wide limits
cat /proc/sys/fs/file-nr

# Monitor memory
free -h
vmstat 1 5
```

### Example
```bash
# Broken: opens too many files
for f in /tmp/*.log; do
    exec 3< "$f"
done

# Fixed: close file descriptors
for f in /tmp/*.log; do
    exec 3< "$f"
    # process file...
    exec 3<&-
done
```
