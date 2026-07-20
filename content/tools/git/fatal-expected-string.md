---
title: "[Solution] Git fatal: Expected string"
description: "Fix 'Expected string' error. Resolve Git rebase, merge, or config parsing failures when an unexpected value type is encountered."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Expected string

fatal: Expected string value for '<key>'

This error occurs when Git expects a string value for a configuration key but receives a non-string value, or when a command receives an unexpected argument type.

## Common Causes

- Configuration file has a numeric value where string is required
- Boolean value used instead of string in config
- Empty value provided for a required parameter
- Incorrect YAML or INI syntax in Git config
- Malformed environment variable

## How to Fix

### Check and Fix Config Value

```bash
git config --global --unset <key>
git config --global <key> "<correct-string-value>"
```

### Edit Config File Directly

```bash
git config --global --edit
```

### Remove Invalid Config

```bash
git config --global --unset <key>
```

## Examples

```bash
# Example 1: Numeric instead of string
git config --global user.name 123
# fatal: Expected string value for 'user.name'
# Fix: git config --global user.name "John Doe"

# Example 2: Empty value
git config --global user.email ""
# Fix: git config --global user.email "john@example.com"

# Example 3: Edit config file
git config --global --edit
# Fix the offending line manually
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
