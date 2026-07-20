---
title: "[Solution] Bash No Such File or Directory Error"
description: "Fix 'bash: No such file or directory' when a file, script, or path does not exist."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "command", "file", "path", "not-found", "directory"]
severity: "error"
---

# No Such File

## Error Message

```
bash: ./script.sh: No such file or directory
```

## Common Causes

- The file or directory specified does not exist at the given path
- The filename has a typo or wrong extension
- The working directory is different from where the file is located
- A symbolic link points to a non-existent target (broken symlink)

## Solutions

### Solution 1: Verify the File Exists at the Specified Path

Use `ls`, `file`, or test operators to confirm the file exists before trying to use it. Check for typos in the path.

```bash
# Check if the file exists
ls -la /path/to/file.sh

# Check with test operator
if [ -f "/path/to/file.sh" ]; then
    echo "File exists"
else
    echo "File not found"
fi

# Search for the file
find /home -name "script.sh" 2>/dev/null

# Check for broken symlinks
ls -la script.sh
file script.sh 
```

### Solution 2: Use Absolute Paths or Check Your Working Directory

Relative paths depend on the current working directory. Use `pwd` to verify your location, or use absolute paths for reliable file access.

```bash
# Check current directory
pwd

# Use absolute path
/home/user/scripts/deploy.sh

# Change to the correct directory first
cd /path/to/project
./script.sh

# Use the script's directory for relative paths
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/config.sh" 
```

## Prevention Tips

- Always verify file existence with `[ -f file ]` before using it
- Use `pwd` to confirm your working directory
- Use `find` to search for files when you're unsure of their location

## Related Errors

- [Permission Denied]({< relref "/languages/bash/permission-denied-error" >})
- [Command Not Found]({< relref "/languages/bash/command-not-found-error" >})
