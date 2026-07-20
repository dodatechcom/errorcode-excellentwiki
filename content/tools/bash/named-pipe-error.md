---
title: "[Solution] Named Pipe (FIFO) Error"
description: "Fix named pipe (FIFO) creation and usage errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Named Pipe (FIFO) Error

Named pipes (FIFOs) failed to create or communicate properly.

### Common Causes
- FIFO already exists at the path.
- Permission denied on the FIFO path.
- Deadlock when both ends block on open.

### How to Fix
```bash
# Create a named pipe
mkfifo /tmp/mypipe

# Remove existing FIFO before creating
rm -f /tmp/mypipe
mkfifo /tmp/mypipe

# Non-blocking read/write to avoid deadlock
exec 3<>/tmp/mypipe    # open for both read and write
echo "data" >&3
read -r line <&3
exec 3>&-

# Clean up
rm -f /tmp/mypipe
```

### Example
```bash
# Broken (FIFO exists)
mkfifo /tmp/mypipe    # error: File exists

# Fixed
rm -f /tmp/mypipe
mkfifo /tmp/mypipe
```
