---
title: "[Solution] PowerShell ScriptSyntaxException Fix"
description: "Fix 'ScriptSyntaxException' when PowerShell encounters invalid syntax in a script block."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell ScriptSyntaxException Fix

This error occurs when PowerShell's script parser encounters syntax it cannot understand. The error message typically reads: `ScriptSyntaxException: The syntax of 'X' is incorrect.`

## Description

PowerShell parses script blocks into an abstract syntax tree before execution. A `ScriptSyntaxException` is thrown when the parser encounters malformed expressions, invalid operators, or structurally incorrect code that prevents compilation.

## Common Causes

- **Invalid expression syntax** — mismatched braces, brackets, or parentheses in complex expressions.
- **Incorrect operator usage** — using operators like `-eq`, `+=`, or `..` in wrong contexts.
- **Missing statement separator** — multiple statements on one line without `;` separation.
- **Invalid here-string syntax** — malformed `@"..."@` or `@'...'@` constructs.

## How to Fix

### Fix 1: Validate script syntax before running

```powershell
# Parse a script file without executing it
$errors = $null
[System.Management.Automation.Language.Parser]::ParseFile(
    "C:\Scripts\myscript.ps1",
    [ref]$null,
    [ref]$errors
)

# Show any syntax errors
$errors | ForEach-Object { $_.ToString() }
```

### Fix 2: Fix common expression issues

```powershell
# Wrong — invalid nested expression
$result = @(Get-Process | Where-Object { $_.CPU -gt 10

# Correct — properly closed expression
$result = @(Get-Process | Where-Object { $_.CPU -gt 10 })
```

### Fix 3: Correct here-string formatting

```powershell
# Wrong — closing tag on wrong line or indented
$text = @"Hello
World
  "@

# Correct — closing tag must be at the start of the line
$text = @"
Hello
World
"@
```

### Fix 4: Separate statements properly

```powershell
# Wrong — missing separator
$x = 1 $y = 2

# Correct — use semicolons
$x = 1; $y = 2

# Or use separate lines
$x = 1
$y = 2
```

## Examples

```powershell
PS> Invoke-Expression "1 + * 2"
ScriptSyntaxException: The syntax of '1 + * 2' is incorrect.

PS> $text = @"Hello
  "@
ScriptSyntaxException: The syntax of the here-string is incorrect.

PS> .\myscript.ps1
ScriptSyntaxException: Missing closing '}' in statement block.
```

## Related Errors

- [ParserError](command-syntax.md) — unexpected token during parsing.
- [ParseException](parse-error.md) — script cannot be parsed at all.
- [FormatError](format-error.md) — error in format string syntax.
