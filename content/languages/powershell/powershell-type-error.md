---
title: "[Solution] PowerShell PSTypeException — Type Mismatch"
description: "Fix PowerShell type errors when converting between incompatible types, or when cmdlets receive wrong data types."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell PSTypeException — Type Mismatch Fix

Type mismatch errors occur when PowerShell cannot convert a value from one type to another, or when a cmdlet receives a value of the wrong type.

## What This Error Means

PowerShell is strongly typed but supports automatic type conversion. When conversion fails (e.g., converting "abc" to int), it throws a type error. Cmdlets also validate parameter types.

## Common Causes

- Implicit conversion failure ("abc" to int)
- Passing wrong object type to cmdlet parameter
- Array type mismatch in typed arrays
- Null conversion (null to value type)
- JSON deserialization type mismatch

## How to Fix

### 1. Use explicit type conversion

```powershell
# WRONG: implicit conversion fails
$num = [int]"abc"

# RIGHT: validate first
if ("abc" -match '^[0-9]+$') {
    $num = [int]"abc"
}
```

### 2. Check object type before processing

```powershell
# Verify type
$obj.GetType()

# Get type name
$obj | Get-Member -MemberType NoteProperty | Select Name, TypeName
```

### 3. Use proper type casting

```powershell
# Safe conversion with error handling
try {
    $num = [int]$value
} catch {
    Write-Warning "Cannot convert '$value' to integer"
}
```

### 4. Convert collections properly

```powershell
# WRONG: can't convert string array to int array
$nums = @("1", "2", "abc") -as [int[]]

# RIGHT: convert individually
$nums = @("1", "2", "abc") | ForEach-Object {
    if ($_ -match '^[0-9]+$') { [int]$_ } else { $null }
} | Where-Object { $_ -ne $null }
```

## Related Errors

- [ArgumentException](powershell-argument-error) — argument validation errors
- [Type Mismatch (VBA)](/languages/vba/type-mismatch) — VBA type errors
- [Cast Error](/languages/groovy/cast-error) — Groovy cast errors
