---
title: "[Solution] Bash No Matches Found (Glob Error)"
description: "Fix 'bash: no matches found' when glob patterns don't match any files. Handle empty globs and nullglob settings."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["glob", "no-matches", "wildcard", "pattern-matching"]
weight: 5
---

# Bash No Matches Found (Glob Error) Fix

The `no matches found` error occurs when a glob pattern (wildcard) doesn't match any files or directories, and `failglob` is enabled (default in some configurations).

## What This Error Means

When you use `*.txt` but no `.txt` files exist, Bash can either expand to the literal string `*.txt` or report an error. The `failglob` shell option controls this behavior.

## Common Causes

- Wildcard pattern doesn't match any files
- Working directory is wrong
- Files have hidden extensions (e.g., `.txt.` on Windows)
- Case sensitivity mismatch (file.txt vs File.TXT)

## How to Fix

### 1. Enable nullglob for safe empty globs

```bash
shopt -s nullglob
files=(*.txt)
# If no matches, files is empty array instead of error
shopt -u nullglob
```

### 2. Check working directory

```bash
# Verify where you are
pwd
ls *.txt  # Check what exists

# Use full path if needed
ls /path/to/dir/*.txt
```

### 3. Use ls to test pattern first

```bash
# Test the pattern
ls *.txt 2>/dev/null && echo "Files found" || echo "No files"
```

### 4. Handle empty globs in scripts

```bash
#!/bin/bash
for f in *.log; do
    [ -e "$f" ] || continue  # Skip if glob didn't match
    echo "Processing: $f"
done
```

## Related Errors

- [Glob Expand](glob-expand) — glob expansion behavior
- [No Such File](no-such-file) — file not found errors
