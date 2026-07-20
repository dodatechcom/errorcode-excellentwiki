---
title: "[Solution] Git fatal: bad config line"
description: "Fix 'bad config line' error. Resolve Git configuration file parsing errors caused by malformed config entries."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: bad config line

fatal: bad config line <number> in file <path>

This error occurs when Git encounters a syntax error while parsing a configuration file. The config file is malformed or contains invalid entries.

## Common Causes

- Manual editing of .git/config or ~/.gitconfig
- Copy-paste introduced invisible characters
- Encoding issues in config file
- Missing or extra quotes in configuration values
- Corrupted config file

## How to Fix

### Locate the Config File

```bash
git config --list --show-origin
```

### Open Config File for Editing

```bash
git config --global --edit
# or
vim ~/.gitconfig
```

### Fix Specific Line

```bash
git config --global --unset <key>
```

### Remove and Recreate

```bash
mv ~/.gitconfig ~/.gitconfig.bak
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

## Examples

```bash
# Example 1: Missing quote in config
git status
# fatal: bad config line 5 in file /home/user/.gitconfig
# Fix: git config --global --edit (fix the line)

# Example 2: Invalid key
git config --global --unset user.emal
# Instead of 'email' -> 'emal' typo

# Example 3: Backup and recreate
mv ~/.gitconfig ~/.gitconfig.bak
git config --global user.name "John Doe"
git config --global user.email "john@example.com"
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
