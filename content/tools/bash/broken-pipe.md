---
title: "[Solution] Broken Pipe Error (SIGPIPE)"
description: "Fix broken pipe and SIGPIPE errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Broken Pipe Error (SIGPIPE)

A process in a pipe closed its input before the upstream process finished writing.

### Common Causes
- `head` or `grep` closing pipe early.
- Network pipe disconnection.
- Large data piped to a fast consumer.

### How to Fix
```bash
# Broken pipe is usually harmless
# but causes SIGPIPE in the writing process

# Suppress SIGPIPE
trap '' PIPE
command | head -1

# Use process substitution to avoid pipe
head -1 < <(command)

# Check pipe status
set -o pipefail    # propagate pipeline errors
command | head -1
echo ${PIPESTATUS[@]}    # all pipeline exit codes
```

### Example
```bash
# Broken (writes SIGPIPE)
yes | head -1000000    # yes gets SIGPIPE

# Fixed (normal behavior)
set -o pipefail
yes | head -5
```
