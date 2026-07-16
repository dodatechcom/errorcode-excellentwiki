---
title: "[Solution] PowerShell ParseException Fix"
description: "Fix 'ParseException' when PowerShell cannot parse a script or command."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ParseException", "parse", "syntax"]
weight: 5
---

# PowerShell ParseException Fix

This error occurs when PowerShell's parser completely fails to understand a script or command. The error message reads: `ParseException: The command or statement is not complete. Check for missing braces or parenthesis.`

## Description

A `ParseException` is thrown when the parser cannot form a valid abstract syntax tree from the input. Unlike a `ParserError` (which identifies a specific unexpected token), a `ParseException` indicates the overall structure of the command is broken — unclosed blocks, incomplete expressions, or fundamentally malformed input.

## Common Causes

- **Unclosed script blocks** — missing `}` to close a `scriptblock`, `if`, `foreach`, or `function`.
- **Incomplete expression** — the command ends abruptly with an operator or open parenthesis.
- **Nested construct mismatch** — inner blocks are closed but outer blocks are not (or vice versa).
- **Invalid encoding or BOM issues** — file encoding problems corrupt the script text.

## How to Fix

### Fix 1: Use the AST parser to find the exact location

```powershell
$errors = $null
$tokens = $null
$ast = [System.Management.Automation.Language.Parser]::ParseFile(
    "C:\Scripts\myscript.ps1",
    [ref]$tokens,
    [ref]$errors
)

# Each error has an Extent with line/column info
$errors | ForEach-Object {
    "Line $($_.Extent.StartLineNumber): $($_.Message)"
}
```

### Fix 2: Check for matching braces and parentheses

```powershell
# Count opening and closing braces
$code = Get-Content "myscript.ps1" -Raw
$openBraces = ([regex]::Matches($code, '\{')).Count
$closeBraces = ([regex]::Matches($code, '\}')).Count
Write-Host "Open: $openBraces, Close: $closeBraces"

# Same for parentheses
$openParens = ([regex]::Matches($code, '\(')).Count
$closeParens = ([regex]::Matches($code, '\)')).Count
Write-Host "Open: $openParens, Close: $closeParens"
```

### Fix 3: Ensure all blocks are properly closed

```powershell
# Wrong — missing closing brace
function Get-Data {
    if ($true) {
        return "data"
    }
# Missing closing brace for function

# Correct — all blocks properly closed
function Get-Data {
    if ($true) {
        return "data"
    }
}
```

### Fix 4: Check file encoding

```powershell
# Check file encoding
$bytes = [System.IO.File]::ReadAllBytes("myscript.ps1")
if ($bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
    Write-Host "File has UTF-8 BOM"
}

# Re-save as UTF-8 without BOM if needed
$content = Get-Content "myscript.ps1" -Raw
[System.IO.File]::WriteAllText("myscript_fixed.ps1", $content,
    [System.Text.UTF8Encoding]::new($false))
```

## Examples

```powershell
PS> .\myscript.ps1
ParseException: The command or statement is not complete. Check for missing braces or parenthesis.

PS> Invoke-Expression "if ($true) { Write-Host 'hello'"
ParseException: The command or statement is not complete.

PS> & { Write-Host "test"
ParseException: Missing closing '}' in statement block.
```

## Related Errors

- [ScriptSyntaxException](script-syntax.md) — specific syntax violations.
- [ParserError](command-syntax.md) — unexpected token during parsing.
- [FormatError](format-error.md) — format string syntax errors.
