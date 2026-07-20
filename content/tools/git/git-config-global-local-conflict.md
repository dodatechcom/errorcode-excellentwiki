---
title: "[Solution] Git config global/local conflict"
description: "Fix Git configuration conflicts between global and local config settings that override expected behavior."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git config global/local conflict

warning: user.name is set in multiple configuration files

This occurs when you have conflicting Git configuration values set at different levels (system, global, local). The local value takes precedence.

## Common Causes

- Different user.name or user.email in global vs local config
- Local repo has different signing key than global config
- Proxy settings differ between global and local
- Conflicting alias definitions

## How to Fix

### List All Config Values

```bash
git config --list --show-origin
```

### Check Specific Key

```bash
git config --global user.name
git config --local user.name
```

### Unset Local Config

```bash
git config --local --unset user.name
```

### Unset Global Config

```bash
git config --global --unset user.name
```

## Examples

```bash
# Example 1: Different user names
git config --global user.name "John Doe"
git config --local user.name "Jane Doe"
# Fix: git config --local --unset user.name

# Example 2: View all origins
git config --list --show-origin

# Example 3: Check which config is winning
git config user.name
# Shows the effective value
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
