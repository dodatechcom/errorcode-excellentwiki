---
title: "[Solution] Bash No Matches Found Error"
description: "Fix 'no matches found' in Bash when a glob pattern doesn't match any files."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Bash No Matches Found Error Fix

This error occurs when a glob pattern (wildcard) doesn't match any files or directories, and `failglob` is set.

## Description

Bash expands glob patterns like `*.txt` into matching filenames. By default, if no match exists, the pattern is passed as a literal string. With `shopt -s failglob`, Bash errors instead. This can also appear in zsh (where it's the default behavior).

## Common Causes

- **Pattern doesn't match anything** — `*.xyz` when no `.xyz` files exist.
- **Wrong directory** — globbing in a directory that doesn't contain the expected files.
- **zsh default behavior** — zsh errors on unmatched globs by default.
- **Case sensitivity** — `*.TXT` won't match `file.txt` on case-sensitive systems.

## How to Fix

### Fix 1: Check if files exist before globbing

```bash
shopt -s nullglob
files=(*.txt)
if [[ ${#files[@]} -gt 0 ]]; then
    for f in "${files[@]}"; do
        echo "$f"
    done
fi
```

### Fix 2: Disable failglob if you want the pattern as literal

```bash
shopt -u failglob
echo *.txt  # outputs "*.txt" if no match
```

### Fix 3: Verify the current directory

```bash
pwd
ls -la
# Confirm you're where you expect to be
```

### Fix 4: Use a conditional check in zsh

```bash
# In zsh, use (N) glob qualifier for nullglob behavior
files=(*.txt(N))
if (( ${#files} )); then
    echo "${files[@]}"
fi
```

## Examples

```bash
$ shopt -s failglob
$ echo *.xyz
bash: no matches found: *.xyz

$ ls *.log
zsh: no matches found: *.log

$ echo *.txt
*.txt
# (without failglob, pattern is passed literally)
```

## Related Errors

- [Glob Expansion Error](glob-expand) — unexpected glob behavior.
- [No Such File or Directory](no-such-file) — specific file reference doesn't exist.
