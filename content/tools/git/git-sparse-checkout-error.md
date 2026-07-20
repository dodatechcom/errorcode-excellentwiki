---
title: "[Solution] Git sparse checkout error"
description: "Fix Git sparse checkout errors. Resolve issues when using partial or sparse checkout to work with a subset of repository files."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git sparse checkout error

fatal: Sparse checkout leaves no entry on working directory

This error occurs when sparse checkout patterns exclude all files, leaving an empty working directory.

## Common Causes

- Sparse checkout patterns match nothing
- Cone mode excludes all directories
- Incorrect path patterns
- No patterns configured after enabling sparse checkout

## How to Fix

### Initialize Sparse Checkout

```bash
git sparse-checkout init --cone
```

### Set Directory to Include

```bash
git sparse-checkout set src/
```

### Add Multiple Directories

```bash
git sparse-checkout add src/ docs/ tests/
```

### Disable Sparse Checkout

```bash
git sparse-checkout disable
```

### List Current Patterns

```bash
git sparse-checkout list
```

## Examples

```bash
# Example 1: Clone only src directory
git clone --filter=blob:none <url>
cd repo
git sparse-checkout init --cone
git sparse-checkout set src/

# Example 2: Add more directories
git sparse-checkout add docs/ tests/

# Example 3: Disable and get everything
git sparse-checkout disable
git checkout main -- .
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
