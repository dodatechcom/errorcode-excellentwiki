---
title: "[Solution] Process Substitution Error"
description: "Fix process substitution <() >() errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Process Substitution Error

Process substitution `<()` or `>()` failed or is not supported.

### Common Causes
- Using process substitution in `sh` instead of `bash`.
- `/dev/fd` not available on the system.
- Too many open file descriptors.

### How to Fix
```bash
# Ensure bash shebang
#!/bin/bash

# Check /dev/fd availability
ls /dev/fd

# Use process substitution for diff
diff <(sort file1) <(sort file2)

# Fallback: use temp files
sort file1 > /tmp/sorted1
sort file2 > /tmp/sorted2
diff /tmp/sorted1 /tmp/sorted2
```

### Example
```bash
# Broken (in sh)
diff <(ls) <(ls -a)    # sh doesn't support <()

# Fixed
#!/bin/bash
diff <(ls) <(ls -a)
```
