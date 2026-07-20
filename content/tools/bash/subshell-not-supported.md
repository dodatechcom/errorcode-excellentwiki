---
title: "[Solution] Subshell Not Supported Error"
description: "Fix subshell ( ) not supported errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Subshell Not Supported Error

The subshell syntax `( )` is not supported or behaving unexpectedly.

### Common Causes
- Using `sh` instead of `bash` for advanced subshell features.
- Process substitution vs subshell confusion.
- Nested subshell depth issues.

### How to Fix
```bash
# Ensure bash is being used
#!/bin/bash

# Subshell syntax
( command1; command2 )
echo $?    # exit code of last command in subshell

# Variables set in subshell don't affect parent
(x=1; echo "inside: $x")    # inside: 1
echo "outside: $x"          # outside: (empty)

# Use for isolation
( cd /tmp && ls )
echo "$PWD"    # unchanged
```

### Example
```bash
# Broken (in sh)
#!/bin/sh
(command; exit 1)

# Fixed
#!/bin/bash
(command; exit 1)
```
