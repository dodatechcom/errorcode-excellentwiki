---
title: "[Solution] Bash While Loop Syntax Error Near Unexpected Token Fix"
description: "Fix 'while: syntax error near unexpected token' in Bash. Correct common while loop syntax mistakes in shell scripts."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

# Bash While Loop Syntax Error Near Unexpected Token Fix

The `while: syntax error near unexpected token` error occurs when a `while` loop is constructed with incorrect syntax, missing `do`/`done` keywords, or improper condition formatting.

## What This Error Means

Bash expects a very specific structure for `while` loops: the keyword `while`, followed by a condition, then `do`, the loop body, and `done`. Any deviation from this structure causes a parse error before the script even runs.

A typical error:

```
script.sh: line 3: syntax error near unexpected token `done'
```

## Why It Happens

Common causes include:

- **Missing `do` keyword** — Writing `while [ condition ]; echo "hi"; done` without `do`.
- **Missing `done` keyword** — Forgetting to close the loop block.
- **Wrong condition syntax** — Using `==` inside `[ ]` or `(( ))` incorrectly.
- **Unquoted variables in condition** — `while [ $var == "test" ]` fails when `$var` is empty.
- **Mixing single and double brackets** — `while [[ condition ]]` vs `while [ condition ]`.
- **Placing commands on the same line without semicolons** — Missing `;` before `do`.

## How to Fix It

### Fix 1: Always use proper while loop structure

```bash
# WRONG: Missing do
while [ "$count" -lt 5 ]
    echo "$count"
done

# RIGHT: Complete structure
while [ "$count" -lt 5 ]; do
    echo "$count"
    count=$((count + 1))
done
```

### Fix 2: Use semicolons correctly on one-line loops

```bash
# WRONG: Missing semicolons
while true do echo "hello" done

# RIGHT: Semicolons required on same line
while true; do echo "hello"; done

# RIGHT: Multi-line format (no semicolons needed)
while true
do
    echo "hello"
done
```

### Fix 3: Fix condition syntax

```bash
# WRONG: Using == in single brackets (POSIX)
while [ $count == 5 ]; do
    echo "found"
done

# RIGHT: Use -eq for numeric comparison in single brackets
while [ "$count" -eq 5 ]; do
    echo "found"
done

# RIGHT: Or use double brackets for string comparison
while [[ "$count" == "5" ]]; do
    echo "found"
done
```

### Fix 4: Quote variables to prevent empty string errors

```bash
# WRONG: Fails if variable is empty
while [ $var != "stop" ]; do
    read var
done

# RIGHT: Quote all variables
while [ "$var" != "stop" ]; do
    read var
done
```

### Fix 5: Use read in while loops correctly

```bash
# WRONG: Classic read-in-while bug
while read line; do
    echo "$line"
done < file.txt  # Subshell issue with variables

# RIGHT: Use process substitution
while read -r line; do
    echo "$line"
done < <(cat file.txt)

# RIGHT: Or use pipe with lastpipe
shopt -s lastpipe
while read -r line; do
    echo "$line"
done < file.txt
```

### Fix 6: Handle infinite loops properly

```bash
# RIGHT: Infinite loop with proper break
while true; do
    read -p "Enter command: " cmd
    case "$cmd" in
        quit) break ;;
        *) echo "Unknown: $cmd" ;;
    esac
done
```

## Common Mistakes

- **Forgetting the semicolon before `do` on the same line** — `while condition do` is invalid.
- **Using `=` instead of `-eq` for numeric comparison** — `=` is for strings in single brackets.
- **Not quoting `$var` in the condition** — Causes syntax errors when the variable is unset.
- **Using `while [ ]` without spaces** — `while []` is not valid syntax.

## Related Pages

- [Bash For Syntax Error](bash-for-syntax-error) — For loop syntax issues
- [Bash Case Syntax Error](bash-case-syntax-error) — Case statement syntax errors
- [Bash Arithmetic Error](arithmetic-error) — Arithmetic expression errors
