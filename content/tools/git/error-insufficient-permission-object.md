---
title: "[Solution] Git error: insufficient permission for adding an object"
description: "Fix 'insufficient permission for adding an object' error. Resolve Git permission issues when writing to the repository database."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git error: insufficient permission for adding an object

error: insufficient permission for adding an object to repository database

This error occurs when Git does not have write permissions to the `.git/objects` directory or its subdirectories. The object database cannot be modified.

## Common Causes

- Repository owned by a different user
- Wrong file permissions on .git directory
- sudo used for git init but not for subsequent commands
- Shared repository with multiple users
- NFS or network filesystem permission issues

## How to Fix

### Fix Ownership

```bash
sudo chown -R $USER:$USER .git
```

### Fix Permissions

```bash
chmod -R u+w .git
```

### For Shared Repositories

```bash
git init --shared=group
chmod -R g+ws .git
```

### Run Git as Correct User

```bash
whoami
# Verify you own the repository
ls -la .git/objects
```

## Examples

```bash
# Example 1: Repository owned by root
sudo chown -R $(whoami):$(whoami) .git
git add . && git commit -m "Fix permissions"

# Example 2: Group-shared repository
sudo chgrp -R developers .git
chmod -R g+ws .git
git config core.sharedRepository group

# Example 3: Fix read-only .git
ls -la .git/objects
# drwx------  # too restrictive
chmod -R u+w .git
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
