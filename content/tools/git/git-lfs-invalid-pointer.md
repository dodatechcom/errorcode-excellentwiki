---
title: "[Solution] Git LFS: Invalid pointer file"
description: "Fix Git LFS 'invalid pointer' error. Resolve LFS pointer file issues when the pointer does not match the expected format."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git LFS: Invalid pointer file

Error: Invalid Git LFS pointer: <file>

This error occurs when Git LFS encounters a pointer file that does not match the expected LFS pointer format. The file contains LFS metadata but is malformed.

## Common Causes

- Pointer file was manually edited
- File was corrupted during transfer
- LFS tracked pattern was changed after files were committed
- Mixed content: both LFS pointer and actual file content
- Migration from other VCS with different pointer format

## How to Fix

### Recreate the Pointer

```bash
git lfs track <pattern>
git add --renormalize <file>
```

### Check Pointer Content

```bash
git show HEAD:<file> | head -5
```

### Migrate Pointers

```bash
git lfs migrate import --include="<pattern>" --everything
```

### Re-clone the Repository

```bash
cd ..
rm -rf repo
git clone <url>
cd repo
git lfs pull
```

## Examples

```bash
# Example 1: Manual edit broke pointer
git lfs track "*.psd"
git add file.psd
# Error: Invalid Git LFS pointer
# Fix: git add --renormalize file.psd

# Example 2: Migrate pointers
git lfs migrate import --include="*.zip" --everything
git push origin --force

# Example 3: Re-clone to get correct pointers
cd .. && rm -rf repo
git clone <url>
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
