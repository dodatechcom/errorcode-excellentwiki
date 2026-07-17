---
title: "[Solution] Bash Word Splitting Issue"
description: "Fix word splitting issues in Bash when unquoted variables cause unexpected argument splitting."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Bash Word Splitting Issue Fix

This error occurs when unquoted variable expansions are split on whitespace and glob characters, causing unexpected behavior.

## Description

Bash splits unquoted variable expansions on `$IFS` (Internal Field Separator, default: space, tab, newline) and also performs filename expansion (globbing) on the results. This is a common source of bugs in scripts.

## Common Causes

- **Unquoted `$var` in a loop** — `for f in $files` splits on spaces.
- **Unquoted in conditional tests** — `[ $var = "yes" ]` breaks when `$var` is empty.
- **Path with spaces** — `rm $path` deletes multiple arguments if path has spaces.
- **Glob characters in variables** — `*`, `?`, `[` get expanded.

## How to Fix

### Fix 1: Always quote variable expansions

```bash
# Wrong
rm $file
echo $var

# Right
rm "$file"
echo "$var"
```

### Fix 2: Use arrays for lists of items

```bash
# Wrong — breaks on spaces
files="file 1.txt file2.txt"
rm $files  # Tries to delete "file", "1.txt", "file2.txt"

# Right
files=("file 1.txt" "file2.txt")
rm "${files[@]}"
```

### Fix 3: Quote in test expressions

```bash
# Wrong
[ -z $var ]
[ $count -gt 0 ]

# Right
[[ -z "$var" ]]
[[ "$count" -gt 0 ]]
```

### Fix 4: Use `read -r` safely to handle whitespace

```bash
while IFS= read -r line; do
    echo "$line"
done < file.txt
```

## Examples

```bash
$ var="hello world"
$ echo $var
hello world
# Split into two arguments

$ echo "$var"
hello world
# Treated as one argument

$ rm $path_with_spaces
# Removes multiple files unexpectedly

$ for f in *.txt; do
    echo "Processing: $f"
done
# If no .txt files: Processing: *.txt (literal)
```

## Related Errors

- [Too Many Arguments](too-many-arguments) — caused by unquoted expansions.
- [Glob Expansion Error](glob-expand) — unintended glob expansion.
- [No Matches Found](no-matching) — glob pattern doesn't match anything.
