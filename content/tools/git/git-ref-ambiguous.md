---
title: "[Solution] Git Reference Ambiguous Error"
description: "Fix Git ambiguous reference errors. Resolve when a ref name matches multiple refs like branches and tags."
tools: ["git"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Git reports an ambiguous reference when a name matches multiple refs — for example, a branch and a tag share the same name. Git cannot determine which one you meant, so it blocks the operation until you disambiguate.

## Common Causes

- A branch and tag have the same name (e.g., `v1.0` branch and `v1.0` tag)
- A branch name matches a remote-tracking branch prefix
- A ref name matches a commit hash prefix
- Legacy refs in `.git/refs/` that conflict with packed refs

## How to Fix

### List Ambiguous Refs

```bash
git show-ref | grep <ref-name>
```

### Use Full Ref Path

```bash
# Use the full refs/heads/ or refs/tags/ prefix
git checkout refs/heads/v1.0
git checkout refs/tags/v1.0
```

### Rename the Branch or Tag

```bash
# Rename the branch
git branch -m v1.0 release/v1.0

# Or delete and recreate the tag
git tag -d v1.0
git tag v1.0-legacy abc1234
```

### Use `--no-verify` for Ambiguous Hashes

```bash
git log abc1234
# warning: refname 'abc1234' is ambiguous
# Fix: use more characters from the hash
git log abc1234def
```

## Examples

```bash
# Example 1: Ambiguous branch and tag
git checkout v2.0
# warning: refname 'v2.0' is ambiguous
# Switching to 'v2.0'

# Fix: use full ref
git checkout refs/tags/v2.0

# Example 2: Ambiguous commit hash
git log 1234abcd
# warning: refname '1234abcd' is ambiguous

# Fix: use more characters
git log 1234abcd567890

# Example 3: List all refs with a name
git show-ref | grep v2.0
# abc1234 refs/heads/v2.0
# def5678 refs/tags/v2.0
```

## Related Errors

- [Git Branch Error]({{< relref "/tools/git/git-branch-error" >}}) — branch operation error
- [Git Tag Error]({{< relref "/tools/git/git-tag-error" >}}) — tag creation error
- [Git Fetch Error]({{< relref "/tools/git/git-fetch-error" >}}) — fetch failed
