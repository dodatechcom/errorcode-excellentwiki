---
title: "[Solution] Bash Not a Directory Error"
description: "Fix 'Not a directory' in Bash when a file path is used where a directory is expected."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["not-a-directory", "directory-error", "path-error"]
weight: 5
---

# Bash Not a Directory Error Fix

This error occurs when you try to `cd` into or reference a file path as if it were a directory.

## Description

When a command expects a directory — such as `cd`, `ls -R`, or path concatenation — but encounters a regular file instead, the system returns "Not a directory." This usually means a path component was misidentified.

## Common Causes

- **`cd` into a file** — accidentally typing `cd /etc/hostname` instead of `cd /etc`.
- **Path concatenation assumes a directory** — `$dir/file` where `$dir` is actually a file.
- **Symlink points to a file** — a symlink expected to be a directory actually points to a file.
- **Deleted directory replaced by a file** — a directory was removed and a file created at the same name.

## How to Fix

### Fix 1: Check if the path is a directory before using it

```bash
if [[ -d "$TARGET" ]]; then
    cd "$TARGET"
else
    echo "Error: $TARGET is not a directory"
fi
```

### Fix 2: Verify the parent path before file operations

```bash
TARGET="/path/to/location"

if [[ -d "$TARGET" ]]; then
    echo "$TARGET is a directory"
elif [[ -f "$TARGET" ]]; then
    echo "$TARGET is a file"
fi
```

### Fix 3: Use `dirname` to extract the directory component

```bash
FULLPATH="/etc/hostname"
DIR=$(dirname "$FULLPATH")
cd "$DIR"  # /etc — works correctly
```

### Fix 4: Check symlinks

```bash
ls -la /path/to/link
# Verify what the symlink actually points to
readlink -f /path/to/link
```

## Examples

```bash
$ cd /etc/hostname
bash: cd: /etc/hostname: Not a directory

$ ls /etc/hostname/
ls: cannot access '/etc/hostname/': Not a directory

$ source /etc/hosts/config
bash: source: /etc/hosts: Not a directory
```

## Related Errors

- [Is a Directory](is-a-directory) — opposite error, directory used where file expected.
- [No Such File or Directory](no-such-file) — path doesn't exist at all.
