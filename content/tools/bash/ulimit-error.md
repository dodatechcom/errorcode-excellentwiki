---
title: "[Solution] Ulimit Command Error"
description: "Fix ulimit resource limit errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Ulimit Command Error

The `ulimit` command failed to set or query resource limits.

### Common Causes
- Trying to set limit higher than allowed maximum.
- Insufficient privileges (non-root).
- Using soft limit higher than hard limit.

### How to Fix
```bash
# Query current limits
ulimit -a

# Check specific limits
ulimit -n    # open files
ulimit -u    # max user processes

# Set limits (within allowed range)
ulimit -n 4096    # increase open files

# Check hard limit (maximum allowed)
ulimit -Hn

# Set in /etc/security/limits.conf (permanent)
# <domain> <type> <item> <value>
# * soft nofile 65536
# * hard nofile 65536
```

### Example
```bash
# Broken
ulimit -n 1000000    # may exceed hard limit

# Fixed
ulimit -Hn           # check hard limit first
ulimit -n 4096       # set within allowed range
```
