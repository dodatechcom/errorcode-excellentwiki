---
title: "[Solution] Bash Process Substitution Error"
description: "Fix Bash process substitution errors when <() or >() syntax fails or produces unexpected results."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# Bash Process Substitution Error

Bash process substitution `<()` or `>()` fails to create the expected file descriptor.

```
bash: /dev/fd/63: No such file or directory
```

## Common Causes

- Shell does not support process substitution
- /dev/fd not mounted or not available
- Process terminates before file descriptor is read
- Too many open file descriptors
- Trying to use in POSIX sh mode

## How to Fix

### Ensure Bash Is Used

```bash
#!/bin/bash
# Process substitution requires bash, not sh

# Compare files
diff <(sort file1.txt) <(sort file2.txt)

# Feed command output to while loop
while IFS= read -r line; do
    echo "$line"
done < <(find /var/log -name "*.log")
```

### Handle Missing /dev/fd

```bash
# Check if process substitution is available
if echo test > >(cat) 2>/dev/null; then
    echo "Process substitution available"
else
    echo "Not available, using temp files"
fi
```

### Use Named Pipes as Fallback

```bash
FIFO=$(mktemp -u)
mkfifo "$FIFO"

sort big_file.txt > "$FIFO" &
diff other_file.txt "$FIFO"

rm "$FIFO"
```

### Limit Open File Descriptors

```bash
# Close unused descriptors
exec 3>&- 4>&- 5>&-

# Use process substitution sparingly
while IFS= read -r line; do
    process "$line"
done < <(generate_data)
```

## Examples

```bash
#!/bin/bash
# Process substitution patterns

# Merge sorted streams
sort <(head -n 1000 file1.txt) <(head -n 1000 file2.txt)

# Parallel processing
while IFS= read -r line; do
    echo "Processing: $line"
done < <(command1 | command2 | command3)

# Compare command outputs
diff <(ssh server1 "cat /etc/config") <(ssh server2 "cat /etc/config")
```
