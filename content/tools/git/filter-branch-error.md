---
title: "[Solution] Git Filter Branch Error"
description: "Fix Git filter-branch errors when rewriting history with git filter-branch or git filter-repo."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Filter Branch Error

Git filter-branch fails to rewrite repository history correctly.

```
WARNING: git-filter-branch is not supported
```

## Common Causes

- filter-branch deprecated in newer Git versions
- Rewrite affects too many refs
- Large repository causing memory issues
- Script errors in filter commands
- Missing backup before rewrite

## How to Fix

### Use git filter-repo Instead

```bash
# Install git-filter-repo
pip install git-filter-repo

# Remove a file from all history
git filter-repo --invert-paths --path secret.txt

# Remove directory from all history
git filter-repo --invert-paths --path-glob '*.env'
```

### Remove Large Files

```bash
# Find large files
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  sed -n 's/^blob //p' | sort -rnk2 | head -10

# Remove specific large file
git filter-repo --path big-file.zip --invert-paths
```

### Replace Text in History

```bash
# Replace email in all commits
git filter-repo --replace-text expressions.txt

# expressions.txt format:
# old@email.com=>new@email.com
```

### Backup Before Rewriting

```bash
# Always backup first
cp -r .git .git.backup

# Or create a bare clone
git clone --mirror repo.git repo-backup.git
```

## Examples

```bash
# Remove passwords from history
git filter-repo --replace-text <<'EOF'
password123==>***REDACTED***
secret_key==>***REDACTED***
EOF

# Prune empty commits after filter
git filter-repo --prune-degenerate always
```
