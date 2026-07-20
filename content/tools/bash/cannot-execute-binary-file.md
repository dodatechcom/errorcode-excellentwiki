---
title: "[Solution] Cannot Execute Binary File"
description: "Fix 'cannot execute binary file' error in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Cannot Execute Binary File

The file is not a valid executable for the current architecture or is not a script.

### Common Causes
- Trying to run a binary compiled for a different architecture (e.g., ARM on x86).
- File lacks execute permission.
- Script has wrong or missing shebang.

### How to Fix
```bash
# Check file type
file ./mybinary

# Check architecture
uname -m
file ./mybinary | grep -o 'ELF.*'

# Fix shebang
#!/bin/bash    # for scripts
#!/usr/bin/env bash  # portable

# Check for wrong line endings
file -i script.sh
dos2unix script.sh
```

### Example
```bash
# Broken
./myapp  # compiled for ARM, running on x86

# Fixed: recompile for correct architecture
gcc -o myapp myapp.c  # on the correct machine
```
