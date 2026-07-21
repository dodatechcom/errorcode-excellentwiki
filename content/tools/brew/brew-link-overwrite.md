---
title: "[Solution] Brew Link Overwrite -- Fix Symlink Overwrite Error"
description: "Fix brew link overwrite errors when symlinks conflict with existing files. Use --overwrite flag or remove conflicting files."
tools: ["brew"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `brew link` cannot create symlinks because files already exist at the target locations.

## Common Causes

- Formula was previously installed manually
- Another formula provides the same files
- macOS ships files in the same location
- A previous brew install left orphan files

## How to Fix

### 1. Overwrite Existing Files

```bash
brew link --overwrite <formula>
```

### 2. Force Link

```bash
brew link --force <formula>
```

### 3. Uninstall Old Version

```bash
brew uninstall --force <formula>
brew install <formula>
```

### 4. Check Overwriting Files

```bash
brew link --overwrite --dry-run <formula>
```

## Examples

```bash
$ brew link wget
Error: Could not symlink bin/wget
/usr/local/bin/wget already exists

$ brew link --overwrite wget
Linking /usr/local/Cellar/wget/1.21.3... 12 symlinks created
```
