---
title: "[Solution] Process Substitution Not Available in POSIX"
description: "Fix process substitution errors when using POSIX sh."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Process Substitution Not Available in POSIX

Process substitution `<()` and `>()` are Bash-specific, not POSIX compliant.

### Common Causes
- Using `#!/bin/sh` which may be `dash` or `ash`.
- Script needs to be portable to other shells.

### How to Fix
```bash
# Use bash shebang
#!/bin/bash

# Or use temp files for POSIX portability
tmpfile=$(mktemp)
command1 > "$tmpfile"
command2 < "$tmpfile"
rm -f "$tmpfile"

# Use named pipes (FIFO)
mkfifo /tmp/mypipe
command1 > /tmp/mypipe &
command2 < /tmp/mypipe
rm -f /tmp/mypipe

# Use eval + here-string for simple cases
eval 'command2 <<< "$(command1)"'
```

### Example
```bash
# Broken (POSIX sh)
#!/bin/sh
diff <(ls dir1) <(ls dir2)

# Fixed
#!/bin/bash
diff <(ls dir1) <(ls dir2)
```
