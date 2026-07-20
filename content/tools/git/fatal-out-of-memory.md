---
title: "[Solution] Git fatal: Out of memory"
description: "Fix Git 'out of memory' error. Resolve memory exhaustion failures when processing large repositories or files."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Out of memory

fatal: Out of memory? mmap failed: Cannot allocate memory

This error occurs when Git runs out of available memory while processing large files, big repositories, or complex operations like diffing or packing.

## Common Causes

- Very large files in the repository
- Large number of commits or objects
- System memory limits or swap disabled
- Processing large diffs with many changes
- Running multiple memory-intensive operations

## How to Fix

### Increase Swap Space

```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Use Shallow Clone

```bash
git clone --depth 1 <repo-url>
```

### Limit Git Memory Usage

```bash
git config --global core.deltaBaseCacheLimit 2g
git config --global pack.threads 1
```

### Use Sparse Checkout

```bash
git clone --filter=blob:none <repo>
git sparse-checkout set <path>
```

## Examples

```bash
# Example 1: Large repo clone
git clone https://github.com/user/large-repo.git
# fatal: Out of memory? mmap failed
# Fix: git clone --depth 1 https://github.com/user/large-repo.git

# Example 2: Increase swap
sudo fallocate -l 4G /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile

# Example 3: Sparse checkout
git clone --filter=blob:none https://github.com/user/repo.git
cd repo
git sparse-checkout set src/
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
