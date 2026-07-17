---
title: "[Solution] Bash No Such File or Directory Error"
description: "Fix 'No such file or directory' in Bash when a file, command, or path doesn't exist."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Bash No Such File or Directory Error Fix

This error occurs when Bash tries to access a file, directory, or executable that doesn't exist at the specified path.

## Description

Bash resolves every path reference — whether for executing a command, sourcing a file, or reading input. If the path is wrong, the file was moved, or the name is misspelled, this error is raised.

## Common Causes

- **Misspelled filename or path** — a typo in the file or directory name.
- **File was deleted or moved** — referencing a path that no longer exists.
- **Relative path used incorrectly** — the working directory isn't what you expect.
- **Missing shebang target** — script has `#!/usr/bin/env notreal` with no such interpreter.

## How to Fix

### Fix 1: Verify the path exists

```bash
ls -la /path/to/file
# Or check before using
if [[ -f "$FILE" ]]; then
    source "$FILE"
else
    echo "File not found: $FILE"
fi
```

### Fix 2: Use absolute paths for reliability

```bash
# Instead of
source config.sh

# Use
source /home/user/project/config.sh
```

### Fix 3: Check for typos and whitespace

```bash
# Trailing whitespace causes invisible errors
file="config.sh "  # Note the trailing space
ls "$file"         # No such file or directory
```

### Fix 4: Use `which` or `command -v` to locate executables

```bash
which mycommand || echo "Command not found"
command -v mycommand || echo "Command not found"
```

## Examples

```bash
$ source missing-file.sh
bash: missing-file.sh: No such file or directory

$ ./deploy.sh
bash: ./deploy.sh: No such file or directory

$ ls /tmp/data
ls: cannot access '/tmp/data': No such file or directory
```

## Related Errors

- [Is a Directory](is-a-directory) — trying to use a directory where a file is expected.
- [Not a Directory](not-a-directory) — trying to use a file where a directory is expected.
- [Command Not Found](command-not-found) — command doesn't exist in PATH.
