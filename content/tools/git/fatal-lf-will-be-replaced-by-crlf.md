---
title: "[Solution] Git fatal: LF will be replaced by CRLF"
description: "Fix 'LF will be replaced by CRLF' warning. Resolve Git line ending normalization issues across Windows and Unix systems."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: LF will be replaced by CRLF

warning: LF will be replaced by CRLF in <file>.

This warning (or error with `--strict`) occurs when Git detects that a file uses Unix-style line endings (LF) but the repository or working directory expects Windows-style (CRLF).

## Common Causes

- Collaborating across Windows and Unix/macOS systems
- `core.autocrlf` set inconsistently across team
- File with mixed line endings committed
- Text file detected as binary or vice versa

## How to Fix

### Configure autocrlf (Windows)

```bash
git config --global core.autocrlf true
```

### Configure autocrlf (Unix/macOS)

```bash
git config --global core.autocrlf input
```

### Normalize Line Endings for Repository

```bash
git add --renormalize .
git commit -m "Normalize line endings"
```

### Use .gitattributes

```properties
*.js text eol=lf
*.bat text eol=crlf
*.png binary
```

## Examples

```bash
# Example 1: Windows developer
git config --global core.autocrlf true
git checkout -- .

# Example 2: Linux/macOS developer
git config --global core.autocrlf input

# Example 3: Using .gitattributes
echo "*.sh text eol=lf" >> .gitattributes
echo "*.ps1 text eol=crlf" >> .gitattributes
git add .gitattributes
git commit -m "Add line ending normalization"
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
