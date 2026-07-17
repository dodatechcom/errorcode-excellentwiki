---
title: "[Solution] Bash For Loop Error"
description: "Fix for loop errors in Bash when loops have syntax errors, unexpected word splitting, or glob expansion issues."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["for", "loop", "word-splitting", "glob", "range"]
weight: 5
---

# Bash For Loop Error Fix

For loop errors include unexpected word splitting on variable values, glob patterns expanding unexpectedly, incorrect range syntax, or missing `in` keyword.

## What This Error Means

The `for` loop iterates over a word list. Bash splits unquoted variables on whitespace and expands unquoted globs, which can produce unexpected iterations.

## Common Causes

- Unquoted variable with spaces splits into multiple words
- Glob in unquoted variable expands to filenames
- Incorrect range syntax (`{1..10}` vs `seq`)
- Missing `in` keyword
- Array iteration syntax error

## How to Fix

### 1. Quote variables to prevent splitting

```bash
# WRONG: word splitting
files="file1.txt file2.txt"
for f in $files; do
    echo "$f"
done

# RIGHT: use array
files=("file1.txt" "file2.txt")
for f in "${files[@]}"; do
    echo "$f"
done
```

### 2. Use proper range syntax

```bash
# WRONG: seq syntax in for
for i in $(seq 1 10)

# RIGHT: brace expansion
for i in {1..10}; do
    echo $i
done
```

### 3. Iterate over array properly

```bash
arr=("a" "b" "c")

# WRONG: iterates over string "a b c"
for item in $arr; do echo "$item"; done

# RIGHT: iterate over array elements
for item in "${arr[@]}"; do echo "$item"; done
```

### 4. Include the in keyword

```bash
# WRONG: missing in
for i 1 2 3; do echo $i; done

# RIGHT:
for i in 1 2 3; do echo $i; done
```

## Related Errors

- [While Error](bash-while-error) — while loop issues
- [Array Error](bash-array-error) — array handling problems
