---
title: "[Solution] Git fatal: unknown option"
description: "Fix 'unknown option' error. Resolve Git command failures when an invalid or misspelled command-line option is provided."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: unknown option

fatal: unknown option `<option>`

This error occurs when you provide a command-line option to Git that does not exist or is not valid for the specific Git subcommand.

## Common Causes

- Typo in the option name
- Using a single dash `-` instead of double dash `--`
- Option does not exist for the specific subcommand
- Using an alias that includes invalid arguments
- Outdated Git version missing the option

## How to Fix

### Check Available Options

```bash
git <command> --help
```

### Use Correct Dash Style

```bash
# Wrong: git commit -message "test"
# Correct: git commit -m "test"

# Wrong: git log -oneline
# Correct: git log --oneline
```

### Check Git Version

```bash
git --version
```

### Use Full Option Names

```bash
# Instead of short option
git diff --cached
# Instead of git diff -c
```

## Examples

```bash
# Example 1: Typo in option
git commit --mesage "test"
# fatal: unknown option `mesage'
# Fix: git commit --message "test"

# Example 2: Wrong dash
git log -oneline
# fatal: unknown option `oneline'
# Fix: git log --oneline

# Example 3: Option not valid for subcommand
git status --all
# fatal: unknown option `all'
# Fix: git status (or git log --all)
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
