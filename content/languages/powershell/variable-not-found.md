---
title: "[Solution] PowerShell VariableNotFoundException Fix"
description: "Fix 'Variable cannot be retrieved' when PowerShell cannot access a variable."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["VariableNotFoundException", "variable", "scope"]
weight: 5
---

# PowerShell VariableNotFoundException Fix

This error occurs when PowerShell tries to access a variable that doesn't exist in the current scope. The error message reads: `The variable 'X' cannot be retrieved because it has not been set.`

## Description

PowerShell variables must be assigned a value before they can be read. Unlike some languages, PowerShell does not initialize variables to a default value. Accessing an unset variable in strict mode or when `$ErrorActionPreference = 'Stop'` triggers this exception.

## Common Causes

- **Variable never assigned** — the variable was referenced before being given a value.
- **Scope mismatch** — the variable was set in a child scope but accessed in a parent scope.
- **Strict mode enabled** — `Set-StrictMode -Version Latest` causes errors on unset variables.
- **Typo in variable name** — misspelled variable name doesn't match the intended variable.

## How to Fix

### Fix 1: Initialize variables before use

```powershell
# Wrong — variable not initialized
Write-Host $result

# Correct — initialize first
$result = $null
Write-Host $result
```

### Fix 2: Check if the variable exists before accessing it

```powershell
# Use Test-Path to check for the variable
if (Test-Path variable:result) {
    Write-Host $result
} else {
    Write-Host "Variable not set"
}

# Or use the $null -ne check pattern
if ($null -ne $myVar) {
    # Use $myVar
}
```

### Fix 3: Fix scope issues

```powershell
# Variables in functions are local by default
function MyFunction {
    $localVar = "hello"
}
MyFunction
# $localVar is not accessible here

# Use $script: scope to make it accessible
function MyFunction {
    $script:sharedVar = "hello"
}
MyFunction
Write-Host $script:sharedVar
```

### Fix 4: Disable strict mode if needed

```powershell
# Check current strict mode
Get-StrictMode

# Disable strict mode
Set-StrictMode -Off
```

## Examples

```powershell
PS> Write-Host $undefinedVar
The variable '$undefinedVar' cannot be retrieved because it has not been set.

PS> Set-StrictMode -Version 2
PS> Write-Host $missing
VariableIsNotInitialized: The variable '$missing' cannot be retrieved because it has not been set.

PS> $missing = "initialized"
PS> Write-Host $missing
initialized
```

## Related Errors

- [InvalidOperation](invalid-operation.md) — operation not valid on current object.
- [ObjectReference](object-reference.md) — null reference when accessing object members.
- [ParseException](parse-error.md) — script parsing failure.
