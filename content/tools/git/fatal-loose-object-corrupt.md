---
title: "[Solution] Git fatal: loose object is corrupt"
description: "Fix 'loose object is corrupt' error. Resolve Git repository object corruption causing data integrity failures."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: loose object is corrupt

fatal: loose object <hash> is corrupt

This error occurs when Git encounters a loose object file that is damaged, truncated, or has a checksum mismatch. The object cannot be read.

## Common Causes

- Disk write cache failure during commit
- File system errors
- Manual modification of .git/objects files
- Incomplete copy or backup restoration
- Storage hardware issues

## How to Fix

### Remove the Corrupt Object

```bash
rm -f .git/objects/<xx>/<hash>
```

### Restore from Remote

```bash
git fetch origin
git reset --hard origin/main
```

### Run Git Fsck

```bash
git fsck --full
```

### Clone Fresh Copy

```bash
cd ..
rm -rf repo
git clone <url>
```

## Examples

```bash
# Example 1: Single corrupt object
git fsck --full
# corrupt loose object
# Fix: rm .git/objects/ab/cdef123... && git fetch origin

# Example 2: Multiple corrupt objects
git fsck --full
# Fix: cd .. && rm -rf repo && git clone <url> repo

# Example 3: Restore from backup
cp -a backup/.git/objects/* .git/objects/
git fsck --full
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
