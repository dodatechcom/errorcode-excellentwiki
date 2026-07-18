---
title: "[Solution] Bash Source File Not Found Error Fix"
description: "Fix 'source: file not found' in Bash. Resolve missing scripts and incorrect paths when sourcing external files."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Source File Not Found Error Fix

The `source: file not found` error occurs when the `source` (or `.`) command cannot locate the file you are trying to include in your shell script.

## What This Error Means

The `source` command reads and executes commands from a file in the current shell context. If the file path is wrong, the file does not exist, or there is a typo in the filename, Bash reports this error.

A typical error:

```
bash: source: /path/to/config.sh: No such file or directory
```

## Why It Happens

Common causes include:

- **Wrong file path** — Typo or incorrect relative/absolute path.
- **File does not exist** — The file was deleted or never created.
- **Permission denied** — File exists but is not readable.
- **Using relative path from wrong directory** — `source script.sh` fails when run from a different directory.
- **Missing file extension** — Filenames must match exactly.

## How to Fix It

### Fix 1: Verify file exists before sourcing

```bash
# RIGHT: Check file exists first
CONFIG_FILE="/path/to/config.sh"
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
else
    echo "Warning: Config file not found at $CONFIG_FILE"
fi
```

### Fix 2: Use absolute paths

```bash
# WRONG: Relative path may fail
source ../config/settings.sh

# RIGHT: Use absolute path
source /opt/myapp/config/settings.sh

# RIGHT: Or compute absolute path from script location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/config/settings.sh"
```

### Fix 3: Set correct permissions

```bash
# Check permissions
ls -la /path/to/config.sh

# Make readable
chmod +r /path/to/config.sh

# Make executable (optional, source does not require +x)
chmod +x /path/to/config.sh
```

### Fix 4: Use BASH_SOURCE for reliable paths

```bash
#!/bin/bash
# Get directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Source relative to script location
source "$SCRIPT_DIR/lib/utils.sh"
source "$SCRIPT_DIR/lib/config.sh"
```

### Fix 5: Handle missing files gracefully

```bash
# RIGHT: Source with fallback
load_library() {
    local lib="$1"
    local paths=(
        "./lib/$lib.sh"
        "/opt/shared/lib/$lib.sh"
        "$HOME/.config/lib/$lib.sh"
    )
    
    for path in "${paths[@]}"; do
        if [ -f "$path" ]; then
            source "$path"
            return 0
        fi
    done
    
    echo "Library not found: $lib"
    return 1
}

load_library "utils"
```

## Common Mistakes

- **Using `source` from a different directory** — The working directory affects relative paths.
- **Forgetting that sourced scripts share the caller's scope** — Variables leak into the caller.
- **Not using quotes around variable paths** — `source $file` fails if path has spaces.

## Related Pages

- [Bash Exec Error](bash-exec-error) — Command execution issues
- [Bash Builtin Error](bash-builtin-error) — Shell builtin errors
- [Bash Read Error](bash-read-error) — File reading issues
