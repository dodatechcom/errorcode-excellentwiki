---
title: "[Solution] Git Patch Application Error"
description: "Fix Git patch errors when applying patches with git apply or git am fails."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Patch Application Error

Git fails to apply a patch file due to conflicts or formatting issues.

```
error: patch failed: file.txt:10
error: file.txt: patch does not apply
```

## Common Causes

- Patch context does not match working tree
- File was modified since patch was created
- Wrong line endings in patch file
- Patch created for wrong branch
- Hunks overlapping

## How to Fix

### Apply Patch with Options

```bash
# Check if patch applies cleanly
git apply --check patch.diff

# Apply with fuzzy matching
git apply --3way patch.diff

# Apply in reverse
git apply -R patch.diff
```

### Use git am for Email Patches

```bash
# Apply mailbox-format patch
git am mailbox.patch

# Apply with 3-way merge
git am --3way mailbox.patch

# Skip rejected hunks
git am --reject mailbox.patch
```

### Fix Patch Conflicts

```bash
# Apply with reject files for manual fix
git apply --reject patch.diff

# Edit .rej files manually
# Then apply remaining
git apply *.rej
```

### Generate Correct Patches

```bash
# Create patch from commit
git format-patch -1 HEAD

# Create patch for last N commits
git format-patch -3

# Create diff patch
git diff HEAD~1 > changes.patch
```

## Examples

```bash
# Apply patch from email
curl -L https://example.com/patch.mbox | git am

# Apply patch with backup
git apply --backup --stat patch.diff

# Check patch content
git apply --stat patch.diff
git apply --summary patch.diff
```
