---
title: "[Solution] Git Shallow Clone Error — fetch depth insufficient"
description: "Fix Git shallow clone errors. Resolve issues with limited history and missing commits in shallow clones."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git Shallow Clone Error — fetch depth insufficient

Shallow clones contain only a limited number of commits. Errors occur when operations require history that wasn't fetched, such as rebasing, blame, or finding merge bases.

## Common Causes

- Cloned with `--depth=1` which only fetches the latest commit
- CI/CD pipelines use shallow clones for speed
- Operations like `git blame` need full history
- Merge or rebase requires common ancestor not in shallow history

## How to Fix

### Fetch Full History

```bash
git fetch --unshallow
```

### Fetch More History

```bash
git fetch --deepen=100
```

### Clone with Full History

```bash
git clone <repo-url>
```

### Clone with Specific Depth

```bash
git clone --depth=50 <repo-url>
```

### Check Shallow Status

```bash
git rev-parse --is-shallow-repository
```

## Examples

```bash
# Example 1: Blame fails on shallow clone
git blame src/app.js
# fatal: cannot do a partial blame during a squash merge
# Fix: git fetch --unshallow

# Example 2: Rebase fails
git rebase main
# error: could not find common ancestor
# Fix: git fetch --unshallow && git rebase main

# Example 3: Check if repository is shallow
git rev-parse --is-shallow-repository
# true
```

## Related Errors

- [Submodule Error]({{< relref "/tools/git/submodule-error" >}}) — submodule not initialized
- [Branch Not Found]({{< relref "/tools/git/branch-not-found" >}}) — branch does not exist
