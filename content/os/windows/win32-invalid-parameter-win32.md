---
title: "ERROR_INVALID_PARAMETER (87) - How to Fix"
description: "Fix Windows ERROR_INVALID_PARAMETER (87). Resolve invalid parameter errors, fix function argument issues, and troubleshoot Win32 API parameter validation."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["win32", "error-87", "invalid-parameter", "parameter"]
weight: 5
---

# ERROR_INVALID_PARAMETER (Win32 Error 87)

This Win32 API error occurs when a function receives a parameter that is invalid, null, or out of range. The error code is `ERROR_INVALID_PARAMETER` (value 87). The full message reads:

> "The parameter is incorrect."

This is a common Win32 error in applications, scripts, and system utilities when function arguments don't meet expected requirements.

## Common Causes

- **Null or empty parameter** — Required argument not provided.
- **Out of range value** — Numeric parameter exceeds valid range.
- **Wrong data type** — Parameter type doesn't match expected type.
- **Structural mismatch** — Structure size or alignment incorrect.
- **Invalid combination** — Parameter combination not supported.

## How to Fix

### Validate Parameters Before Use

```powershell
function Invoke-WithValidation {
    param(
        [Parameter(Mandatory)]
        [string]$Path,
        [ValidateRange(1, 100)]
        [int]$Count
    )
    if (-not (Test-Path $Path)) { throw "Invalid path: $Path" }
    # Use validated parameters
}
```

### Check Parameter Types

```powershell
$param = "123"
if ($param -notmatch '^\d+$') { Write-Host "Parameter must be numeric" }
```

### Check Null/Empty Parameters

```powershell
if ([string]::IsNullOrEmpty($param)) { Write-Host "Parameter cannot be null or empty" }
if ($null -eq $param) { Write-Host "Parameter is null" }
```

### Verify Function Parameters

Check the function documentation for expected parameter types and ranges:

```powershell
Get-Help Function-Name -Parameter *
```

### Validate Struct Fields

```powershell
$struct = New-Object SomeStruct
$struct.Size = [System.Runtime.InteropServices.Marshal]::SizeOf($struct)
```

### Check Array/Collection Bounds

```powershell
$arr = @(1, 2, 3)
$index = 0
if ($index -ge 0 -and $index -lt $arr.Length) {
    $value = $arr[$index]
}
```

### Debug with Detailed Error

```powershell
try {
    # Failing operation
} catch {
    Write-Host "Error: $($_.Exception.Message)"
    Write-Host "Parameter: $($_.TargetObject)"
}
```

## Related Errors

- [ERROR_INVALID_HANDLE (6)]({{< relref "/os/windows/win32-invalid-handle" >}}) — Invalid handle parameter
- [ERROR_BAD_PATHNAME (161)]({{< relref "/os/windows/win32-bad-pathname" >}}) — Invalid path parameter
- [ERROR_INVALID_NAME (123)]({{< relref "/os/windows/win32-invalid-name" >}}) — Invalid name parameter
