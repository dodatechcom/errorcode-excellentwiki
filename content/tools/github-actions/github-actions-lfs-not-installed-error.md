---
title: "[Solution] GitHub Actions LFS Not Installed Error"
description: "Fix GitHub Actions LFS not installed errors when working with Git LFS files."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

LFS errors occur when the runner does not have Git LFS installed or configured:

```
Error: This repository is configured for Git LFS but 'git-lfs' was not found
```

## Common Causes

- Git LFS is not pre-installed on the runner.
- `actions/checkout` does not have `lfs: true` set.

## How to Fix

**Enable LFS in checkout:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      lfs: true
```

**Install LFS manually:**

```yaml
steps:
  - name: Install Git LFS
    run: |
      sudo apt-get update
      sudo apt-get install -y git-lfs
      git lfs install
  - uses: actions/checkout@v4
    with:
      lfs: true
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      lfs: true
  - run: git lfs ls-files
```
