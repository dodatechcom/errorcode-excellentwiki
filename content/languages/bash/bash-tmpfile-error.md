---
title: "[Solution] Bash Tmpfile Error -- Insecure Temporary File Creation"
description: "Fix bash tmpfile errors when creating temporary files insecurely with predictable names."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Tmpfile Error

This error occurs when temporary files are created with predictable names, leading to security vulnerabilities.

## Common Causes

- Using hardcoded temp file names like `/tmp/myfile`
- Race condition between file creation and use
- Not removing temp files on exit
- Temp file permissions too permissive

## How to Fix

### Use mktemp for secure temp files

```bash
# WRONG: predictable temp file
TEMP="/tmp/myapp_data"
echo "data" > "$TEMP"

# CORRECT: use mktemp
TEMP=$(mktemp)
echo "data" > "$TEMP"
trap 'rm -f "$TEMP"' EXIT
```

### Create temp directory

```bash
TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT
```

## Examples

```bash
#!/bin/bash
TEMP_FILE=$(mktemp "${TMPDIR:-/tmp}/myapp.XXXXXX")
trap 'rm -f "$TEMP_FILE"' EXIT

echo "Working in $TEMP_FILE"
```
