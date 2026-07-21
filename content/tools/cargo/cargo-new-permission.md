---
title: "[Solution] Cargo New Permission -- Fix Directory Permission Denied"
description: "Fix cargo new permission errors when cargo cannot create files in the target directory. Fix filesystem permissions."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `cargo new` failed because it does not have write permission to create the project directory.

## Common Causes

- Target directory is owned by root
- Parent directory has restrictive permissions
- Filesystem is read-only
- You are creating in a system directory

## How to Fix

### 1. Choose a Different Directory

```bash
cargo new ~/projects/my-project
```

### 2. Fix Directory Permissions

```bash
sudo chown -R $(whoami) ~/projects/
```

### 3. Create in Current Directory

```bash
mkdir my-project && cd my-project
cargo init
```

### 4. Check Filesystem

```bash
touch ~/test-write-access && rm ~/test-write-access
```

## Examples

```bash
$ cargo new /opt/my-project
error: failed to create directory: Permission denied (os error 13)

$ cargo new ~/my-project
     Created binary (application) `my-project` package
```
