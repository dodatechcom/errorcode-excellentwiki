---
title: "[Solution] PowerShell ParserError Unexpected Token Fix"
description: "Fix 'ParserError: Unexpected token' when PowerShell cannot parse a command."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ParserError", "syntax", "unexpected-token"]
weight: 5
---

# PowerShell ParserError Unexpected Token Fix

This error occurs when PowerShell's parser encounters a token it doesn't expect at a given position. The error message reads: `ParserError: Unexpected token 'X' in expression or statement.`

## Description

PowerShell parses commands before executing them. If the structure of a command doesn't match expected syntax (missing operators, unclosed quotes, misplaced parentheses), the parser raises this error before any code runs.

## Common Causes

- **Missing closing quote or parenthesis** — unterminated string or expression.
- **Unexpected character** — special characters like `&`, `|`, `;` in wrong positions.
- **C# code in PowerShell** — using C# syntax like `foreach(var x in y)` instead of PowerShell's `foreach`.
- **Wrong string interpolation** — missing `$` before variable names in double-quoted strings or using single quotes with variables.

## How to Fix

### Fix 1: Check for unmatched quotes and parentheses

```powershell
# Wrong — missing closing quote
Write-Host "Hello world

# Correct
Write-Host "Hello world"
```

### Fix 2: Use PowerShell syntax, not C#

```powershell
# Wrong (C# syntax)
foreach(var x in $items) { }

# Correct (PowerShell syntax)
foreach ($x in $items) { }
```

### Fix 3: Proper string interpolation

```powershell
# Wrong — single quotes don't interpolate
$name = "Alice"
Write-Host 'Hello $name'

# Correct — double quotes interpolate
Write-Host "Hello $name"

# Correct — curly braces for complex expressions
Write-Host "Hello $($name.ToUpper())"
```

### Fix 4: Escape special characters

```powershell
# Wrong — unescaped parenthesis
echo (Get-Date).ToString("yyyy-MM-dd")

# Correct (if needed, though this example is valid PowerShell)
# The issue is usually when operators appear inside strings unexpectedly
$date = Get-Date
Write-Host ($date.ToString("yyyy-MM-dd"))
```

## Examples

```powershell
PS> Write-Host "Hello
ParserError: Unexpected token in expression or statement.

PS> foreach(var x in 1..5) { Write-Host $x }
ParserError: Unexpected token 'var' in expression or statement.

PS> echo "Count: $count"
# Works — double quotes interpolate

PS> echo 'Count: $count'
Count: $count
# Works but shows literal $count
```

## Related Errors

- [CommandNotFoundException](command-not-found.md) — command name not recognized.
