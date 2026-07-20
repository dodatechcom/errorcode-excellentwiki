---
title: "[Solution] Git fatal: Not a git repository"
description: "Fix 'fatal: not a git repository' error. Resolve cases where Git commands fail because the current directory is not a Git repository."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Not a git repository

fatal: Not a git repository (or any of the parent directories): .git

This error occurs when you run a Git command in a directory that is not part of a Git repository. Git cannot find a `.git` directory in the current path or any parent directory.

## Common Causes

- Running Git commands outside a repository
- The `.git` directory was deleted or corrupted
- Working in a subdirectory that was not initialized
- The repository was cloned but you changed directories
- Wrong working directory in terminal

## How to Fix

### Initialize a New Repository

```bash
git init
```

### Clone an Existing Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### Check for .git Directory

```bash
ls -la .git
```

If missing, the repository metadata has been lost.

### Navigate to Repository Root

```bash
git rev-parse --show-toplevel
cd $(git rev-parse --show-toplevel)
```

## Examples

```bash
# Example 1: Running git log outside a repo
cd /tmp
git log
# fatal: not a git repository (or any of the parent directories): .git
# Fix: cd into your repository first

# Example 2: Deleted .git directory
rm -rf .git
git status
# fatal: not a git repository (or any of the parent directories): .git
# Fix: git init (loses history) or git clone fresh copy

# Example 3: Initialize a new project
mkdir myproject && cd myproject
git init
# Initialized empty Git repository in /path/to/myproject/.git/
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
