---
title: "[Solution] Bash Glob Expansion Error"
description: "Fix glob expansion issues in Bash when wildcard patterns are expanded unexpectedly or cause errors."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["glob-expand", "filename-expansion", "wildcards"]
weight: 5
---

# Bash Glob Expansion Error Fix

This error occurs when Bash's filename expansion (globbing) behaves unexpectedly due to unquoted variables or incorrect patterns.

## Description

Bash automatically expands wildcard characters (`*`, `?`, `[...]`) into matching filenames. When these characters appear in variables that should be treated literally — or when patterns are malformed — errors and unintended behavior result.

## Common Causes

- **Unquoted variable containing glob characters** — `*` or `?` in a string gets expanded.
- **Malformed character class** — `[abc` missing closing bracket.
- **Glob in a directory with many files** — "argument list too long" error.
- **Noclobber issues** — trying to redirect to a file that already exists with `set -o noclobber`.

## How to Fix

### Fix 1: Quote variables to prevent glob expansion

```bash
# Wrong — if pattern="file.*", it expands to all files
ls $pattern

# Right — treated as literal string
ls "$pattern"
```

### Fix 2: Escape glob characters in strings

```bash
# Escape with backslash
echo "Price is \$5.00"
ls *.\*

# Or quote the string
echo "Price is $5.00"
```

### Fix 3: Use nullglob to handle no matches gracefully

```bash
shopt -s nullglob
for f in *.nonexistent; do
    echo "$f"
done
# Loop body never executes (no error, no literal "*.nonexistent")
```

### Fix 4: Use `printf %q` to safely display patterns

```bash
printf '%q\n' "$variable_with_special_chars"
# Shows the escaped/safe version
```

## Examples

```bash
$ ls *
file1.txt  file2.txt  my*

$ echo *.txt
file1.txt file2.txt

$ var="hello*world"
$ echo $var
# Expands to files matching hello*world

$ echo "$var"
hello*world

$ shopt -s failglob
$ echo *.xyz
bash: no matches found: *.xyz
```

## Related Errors

- [No Matches Found](no-matching) — glob pattern doesn't match anything.
- [Word Splitting](word-splitting) — unquoted variable splitting.
