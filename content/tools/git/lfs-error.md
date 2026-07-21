---
title: "[Solution] Git Large File Storage Error"
description: "Fix Git LFS errors when tracking, pushing, or pulling large files with Git LFS."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Large File Storage Error

Git LFS operations fail when tracking or transferring large files.

```
error: failed to push some objects
Git LFS: (0 files, 0/1 files)
```

## Common Causes

- Git LFS not installed
- LFS pointer files corrupted
- Server does not support LFS
- Storage quota exceeded
- LFS objects not properly fetched

## How to Fix

### Install Git LFS

```bash
# Install LFS
git lfs install

# Track file patterns
git lfs track "*.zip"
git lfs track "*.psd"
git lfs track "*.mp4"
```

### Fix Corrupted LFS Objects

```bash
# Re-clone with LFS
GIT_LFS_SKIP_SMUDGE=1 git clone url repo
cd repo
git lfs pull

# Or force re-download
git lfs fetch --all
git lfs checkout
```

### Check LFS Configuration

```bash
# List tracked patterns
git lfs track

# Show LFS objects
git lfs ls-files

# Check LFS status
git lfs status
```

### Fix LFS Push Issues

```bash
# Push with LFS objects
git lfs push --all origin main

# Push specific files
git lfs push origin main --include="*.zip"
```

### Migrate to LFS

```bash
# Migrate existing large files to LFS
git lfs migrate import --include="*.zip,*.psd,*.mp4" --everything
```

## Examples

```bash
# Track specific large files
git lfs track "*.psd"
git add .gitattributes
git add *.psd
git commit -m "Track PSD files with LFS"

# Force re-download LFS objects
git lfs fetch --all
git lfs checkout
```
