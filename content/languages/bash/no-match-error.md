---
title: "[Solution] Bash No Match Found Error"
description: "Fix 'bash: no match found' when glob patterns don't match any files."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "command", "glob", "pattern", "wildcard", "nomatch"]
severity: "error"
---

# No Match

## Error Message

```
bash: no match found
```

## Common Causes

- A glob pattern (wildcard) doesn't match any files in the current directory
- The `failglob` option is enabled and the pattern has no matches
- Typo in the glob pattern or wrong directory
- Hidden files (starting with `.`) are not matched by default globs

## Solutions

### Solution 1: Verify the Glob Pattern and Directory

Make sure you're in the correct directory and the pattern matches the actual filenames. Use `ls` to see available files.

```bash
# Check what files exist
ls -la *.txt

# Wrong — no .txt files in current directory
for f in *.txt; do
    echo "$f"
done

# Right — check first
shopt -s nullglob  # Don't iterate if no matches
for f in *.txt; do
    echo "$f"
done
shopt -u nullglob

# Include hidden files with dotglob
shopt -s dotglob
for f in *; do
    echo "$f"
done
shopt -u dotglob 
```

### Solution 2: Use nullglob to Handle No Matches Gracefully

Enable `nullglob` so that globs expand to nothing (instead of the literal pattern) when there are no matches. This prevents the 'no match' error.

```bash
#!/bin/bash

# Without nullglob — literal pattern used
echo *.nonexistent
# Output: bash: *.nonexistent: no match found

# With nullglob
shopt -s nullglob
files=(*.nonexistent)
echo "Found ${#files} files"  # Output: Found 0 files
shopt -u nullglob

# Safe file processing
shopt -s nullglob
for file in *.log; do
    process_log "$file"
done
shopt -u nullglob 
```

## Prevention Tips

- Use `shopt -s nullglob` to avoid errors on non-matching globs
- Use `ls` to preview files before processing them with globs
- Use `shopt -s dotglob` to include hidden files in glob expansion

## Related Errors

- [No Such File]({< relref "/languages/bash/no-such-file-error" >})
- [Command Not Found]({< relref "/languages/bash/command-not-found-error" >})
