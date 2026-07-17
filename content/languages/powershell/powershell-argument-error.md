---
title: "[Solution] PowerShell ArgumentException in PowerShell"
description: "Fix ArgumentException in PowerShell when invalid arguments are passed to cmdlets, functions, or .NET methods."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ArgumentException", "argument", "parameter", "invalid", "value"]
weight: 5
---

# PowerShell ArgumentException Fix

ArgumentExceptions occur when a method or cmdlet receives an argument that doesn't meet its expected type, range, or format requirements.

## What This Error Means

.NET methods and PowerShell cmdlets validate their arguments. An ArgumentException means the value is within the correct type but outside the valid range or doesn't meet constraints.

## Common Causes

- Numeric value out of allowed range
- String value doesn't match expected format (e.g., path, regex)
- Null passed where a non-null value is required
- Enum value not in the allowed set
- Collection count doesn't match expected size

## How to Fix

### 1. Validate argument ranges

```powershell
# Check parameter constraints
Get-Help Some-Command -Parameter ParameterName

# Example: port must be 1-65535
$port = 99999  # ArgumentException
$port = 8080   # Valid
```

### 2. Check argument type

```powershell
# Verify type matches
$value.GetType()

# Convert if needed
$number = [int]"42"          # String to int
$date = [DateTime]"2024-01-01"  # String to DateTime
```

### 3. Handle null values

```powershell
# WRONG: null argument
$nullValue = $null
[System.IO.File]::ReadAllText($nullValue)

# RIGHT: validate first
if ($null -ne $path -and (Test-Path $path)) {
    [System.IO.File]::ReadAllText($path)
}
```

### 4. Use valid enum values

```powershell
# Check allowed values
[enum]::GetValues([System.ConsoleColor])

# Use valid value
[Console]::ForegroundColor = [ConsoleColor]::Red  # Valid
```

## Related Errors

- [Type Mismatch](powershell-type-error) — type conversion errors
- [ParameterBindingException](powershell-parameter-binding) — parameter issues
- [InvalidOperation](invalid-operation) — operation errors
