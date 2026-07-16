---
title: "[Solution] PowerShell NullReferenceException Fix"
description: "Fix 'Object reference not set to an instance of an object' when PowerShell accesses a null object."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["NullReferenceException", "null", "object-reference"]
weight: 5
---

# PowerShell NullReferenceException Fix

This error occurs when code tries to access a member or method on a null object. The error message reads: `You cannot call a method on a null-valued expression.` or `Object reference not set to an instance of an object.`

## Description

In PowerShell, when an expression evaluates to `$null` and you attempt to access a property, method, or index on it, the runtime throws a null reference error. This is one of the most common runtime errors in PowerShell scripting.

## Common Causes

- **Command returned no output** — a cmdlet returned `$null` instead of an object.
- **Failed lookup or filter** — `Where-Object` or hash table lookup didn't match anything.
- **Uninitialized property** — accessing a property on an object that doesn't have it.
- **Pipeline produced empty result** — the pipeline before the current operation yielded nothing.

## How to Fix

### Fix 1: Check for null before accessing members

```powershell
# Wrong — will fail if Get-Process returns nothing
$proc = Get-Process -Name "nonexistent"
Write-Host $proc.Id

# Correct — check for null first
$proc = Get-Process -Name "nonexistent" -ErrorAction SilentlyContinue
if ($null -ne $proc) {
    Write-Host $proc.Id
}
```

### Fix 2: Use optional chaining (PowerShell 7+)

```powershell
# PowerShell 7+ supports the ?. operator
$proc = Get-Process -Name "nonexistent" -ErrorAction SilentlyContinue
Write-Host $proc?.Id
# Returns $null instead of throwing an error
```

### Fix 3: Handle empty pipelines

```powershell
# Wrong — pipeline may produce nothing
$results = Get-ChildItem "C:\Nonexistent" | Where-Object { $_.Length -gt 1MB }
Write-Host $results.Count

# Correct — ensure $results is not null
$results = @(Get-ChildItem "C:\Nonexistent" -ErrorAction SilentlyContinue |
    Where-Object { $_.Length -gt 1MB })
Write-Host $results.Count
```

### Fix 4: Use the null-coalescing operator (PowerShell 7+)

```powershell
# Use ?? to provide a default value
$value = $null ?? "default"
Write-Host $value

# Or with ??= to assign only if null
$settings = @{}
$settings["key"] ??= "default_value"
```

## Examples

```powershell
PS> $obj = $null
PS> $obj.ToString()
You cannot call a method on a null-valued expression.

PS> $hash = @{}
PS> $hash["missing_key"].Property
You cannot call a method on a null-valued expression.

PS> $list = Get-ChildItem "C:\Nonexistent"
PS> $list.GetType()
You cannot call a method on a null-valued expression.
```

## Related Errors

- [InvalidOperation](invalid-operation.md) — operation not valid on the object's current state.
- [VariableNotFound](variable-not-found.md) — variable has not been set.
- [ParameterBindingException](parameter-binding.md) — parameter binding failure.
