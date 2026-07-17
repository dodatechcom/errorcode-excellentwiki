---
title: "[Solution] PowerShell FormatError Fix"
description: "Fix 'FormatError' when PowerShell encounters invalid format string syntax."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell FormatError Fix

This error occurs when PowerShell encounters a malformed format string in cmdlets like `Write-Host`, `-f` operator, or format specifiers. The error message reads: `FormatException: Input string was not in a correct format.`

## Description

PowerShell uses format strings (similar to C#'s `String.Format`) with placeholder syntax like `{0}`, `{1}`, etc. When these placeholders are malformed, mismatched, or reference non-existent indexes, a `FormatException` is thrown during string interpolation.

## Common Causes

- **Mismatched braces** — missing or extra `{` or `}` in the format string.
- **Invalid index reference** — referencing `{5}` when only 3 arguments are provided.
- **Incorrect format specifier** — using invalid format codes like `{0:ZZZ}`.
- **Nested brace issues** — literal braces must be escaped as `{{` and `}}`.

## How to Fix

### Fix 1: Validate format string syntax

```powershell
# Check for balanced braces
$template = "Hello {0}, you are {1} years old"
$matches = [regex]::Matches($template, '\{(\d+)(?::\w+)?\}')
Write-Host "Found $($matches.Count) placeholders"

# Test the format string
try {
    $result = $template -f "Alice", 30
    Write-Host $result
} catch [System.FormatException] {
    Write-Warning "Invalid format string"
}
```

### Fix 2: Escape literal braces

```powershell
# Wrong — {0} is treated as a placeholder
$result = "Price: {0}" -f '$100'

# Correct — escape literal braces with double braces
$result = "Price: {{0}}" -f '$100'
# Output: Price: {0}

# Or use single quotes (no interpolation)
$result = 'Price: {0}'
```

### Fix 3: Ensure argument count matches placeholders

```powershell
# Wrong — 2 placeholders but only 1 argument
$result = "Hello {0}, welcome to {1}" -f "Alice"

# Correct — provide all arguments
$result = "Hello {0}, welcome to {1}" -f "Alice", "Wonderland"
```

### Fix 4: Use format specifiers correctly

```powershell
# Correct format specifiers
"{0:N2}" -f 1234.5678    # 1,234.57 (number with 2 decimals)
"{0:P0}" -f 0.856        # 86% (percentage)
"{0:yyyy-MM-dd}" -f (Get-Date)  # 2026-07-16

# Wrong — invalid format specifier
"{0:ZZZ}" -f 42  # FormatException
```

## Examples

```powershell
PS> "Hello {0" -f "World"
FormatException: Input string was not in a correct format.

PS> "{0} and {1}" -f "only_one_arg"
FormatException: Index (zero based) must be greater than or equal to zero...

PS> "{0:N2}" -f "not_a_number"
FormatException: Input string was not in a correct format.
```

## Related Errors

- [ScriptSyntaxException](script-syntax.md) — broader syntax parsing errors.
- [ParseException](parse-error.md) — script-level parse failures.
- [ParameterBindingException](parameter-binding.md) — parameter binding failure.
