---
title: "[Solution] Bash For Loop Syntax Error Near Token Fix"
description: "Fix 'for: syntax error near token' in Bash. Learn correct for loop syntax including C-style, list, and glob patterns."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

# Bash For Loop Syntax Error Near Token Fix

The `for: syntax error near unexpected token` error occurs when a `for` loop uses incorrect syntax, missing keywords, or malformed expressions.

## What This Error Means

Bash supports several `for` loop variants: list-based, C-style, and glob-based. Each has strict syntax requirements. When the parser encounters an unexpected token in the loop header, it reports a syntax error before execution begins.

A typical error:

```
script.sh: line 2: syntax error near unexpected token `;'
```

## Why It Happens

Common causes include:

- **Missing `in` keyword** — Writing `for i 1 2 3` instead of `for i in 1 2 3`.
- **Missing `do`/`done`** — Omitting the required block delimiters.
- **Wrong C-style syntax** — `for ((i=0; i<10; i++))` with incorrect parentheses or semicolons.
- **Unquoted glob patterns** — `for f in *.txt` failing when no files match.
- **Missing quotes around variables** — Word splitting causes unexpected tokens.

## How to Fix It

### Fix 1: List-based for loop

```bash
# WRONG: Missing 'in' keyword
for i 1 2 3; do
    echo "$i"
done

# RIGHT: Include 'in'
for i in 1 2 3; do
    echo "$i"
done
```

### Fix 2: Use proper do and done delimiters

```bash
# WRONG: Missing done
for i in 1 2 3; do
    echo "$i"

# RIGHT: Always close with done
for i in 1 2 3; do
    echo "$i"
done
```

### Fix 3: C-style for loop syntax

```bash
# WRONG: Missing parentheses or wrong syntax
for i=0; i<10; i++ do
    echo "$i"
done

# RIGHT: C-style with double parentheses
for ((i=0; i<10; i++)); do
    echo "$i"
done
```

### Fix 4: Iterate over files safely

```bash
# WRONG: Fails when no files match
for f in *.txt; do
    echo "$f"
done

# RIGHT: Handle no-match case
for f in *.txt; do
    [ -e "$f" ] || continue
    echo "$f"
done
```

### Fix 5: Use brace expansion correctly

```bash
# RIGHT: Brace expansion for ranges
for i in {1..10}; do
    echo "$i"
done

# RIGHT: With step value
for i in {0..20..2}; do
    echo "$i"
done
```

## Common Mistakes

- **Forgetting the `in` keyword** — Always include `in` even for single values.
- **Using `;` before `do` on separate lines** — On separate lines, `do` starts on its own line.
- **Not quoting variables** — `for f in $files` splits on whitespace unexpectedly.

## Related Pages

- [Bash While Syntax Error](bash-while-syntax-error) — While loop syntax issues
- [Bash Case Syntax Error](bash-case-syntax-error) — Case statement errors
- [Bash Arithmetic Error](arithmetic-error) — Arithmetic expression errors
