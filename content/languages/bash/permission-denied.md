---
title: "[Solution] Bash Permission Denied Error Fix"
description: "Fix 'bash: ./script.sh: Permission denied' when you lack execute or read permissions."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["permission-denied", "chmod", "execute"]
weight: 5
---

# Bash Permission Denied Error Fix

This error occurs when Bash cannot execute a script or access a file because the current user lacks the necessary file permissions.

## Description

Linux/macOS file permissions control who can read, write, and execute files. If a script lacks the execute bit, or if a file/directory lacks read permission, Bash will refuse to run or access it.

## Common Causes

- **Missing execute permission** — the script file doesn't have `+x` set.
- **Running a file downloaded from the internet** — downloaded files often lose execute permissions.
- **Wrong user ownership** — file is owned by another user with restrictive permissions.
- **Directory lacks read/execute** — trying to `cd` into or list a directory you can't access.

## How to Fix

### Fix 1: Add execute permission

```bash
chmod +x script.sh
./script.sh
```

### Fix 2: Run with bash explicitly (no +x needed)

```bash
bash script.sh
```

### Fix 3: Check and fix file permissions

```bash
# View permissions
ls -la script.sh

# Make readable and executable for owner
chmod 755 script.sh
```

### Fix 4: Change file ownership

```bash
sudo chown $(whoami) script.sh
chmod +x script.sh
```

## Examples

```bash
$ ./deploy.sh
bash: ./deploy.sh: Permission denied

$ ls -la deploy.sh
-rw-r--r-- 1 user user 1024 deploy.sh
#     ^ no execute bit

$ chmod +x deploy.sh
$ ./deploy.sh
# Now works
```

## Related Errors

- [Command Not Found](command-not-found) — command doesn't exist in PATH.
