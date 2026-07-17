---
title: "ERROR_INVALID_NAME (123) - How to Fix"
description: "Fix Windows ERROR_INVALID_NAME (123). Resolve invalid filename, extension, and naming errors on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["win32", "error-123", "invalid-name", "filename"]
weight: 5
---

# ERROR_INVALID_NAME (Win32 Error 123)

This Win32 API error occurs when a filename, directory name, or volume label is invalid. The error code is `ERROR_INVALID_NAME` (value 123). The full message reads:

> "The filename, directory name, or volume label syntax is incorrect."

This differs from ERROR_BAD_PATHNAME (161) by focusing specifically on the name component rather than the full path.

## Common Causes

- **Invalid filename characters** — Characters like `*`, `?`, `"`, `<`, `>`, `|`, `:` are prohibited.
- **Reserved filenames** — Names like `CON`, `PRN`, `AUX`, `NUL` are reserved by Windows.
- **Filename too long** — Exceeds 255 characters for the name component.
- **Name starts or ends with space/period** — Trailing or leading whitespace and periods.
- **Extension issues** — Double extensions or empty extensions.

## How to Fix

### Validate Filename

```powershell
function Test-FileName {
    param([string]$Name)
    $invalid = [System.IO.Path]::GetInvalidFileNameChars()
    $hasInvalid = $Name.ToCharArray() | Where-Object { $_ -in $invalid }
    return -not $hasInvalid -and $Name.Trim().Length -gt 0 -and $Name.TrimEnd('.') -eq $Name.Trim()
}
Test-FileName -Name "MyFile.txt"
```

### Check Reserved Names

```powershell
$reserved = @("CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5",
    "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5",
    "LPT6", "LPT7", "LPT8", "LPT9")
$name = [System.IO.Path]::GetFileNameWithoutExtension("CON.txt").ToUpper()
if ($name -in $reserved) { Write-Host "Reserved name: $name" }
```

### Sanitize Filename

```powershell
function Sanitize-FileName {
    param([string]$Name)
    $invalid = [System.IO.Path]::GetInvalidFileNameChars()
    $sanitized = $invalid | ForEach-Object { $Name = $Name.Replace($_, '_') }
    return $Name.Trim().TrimEnd('.')
}
Sanitize-FileName -Name "My File: with (invalid) chars?.txt"
```

### Check Filename Length

```powershell
$name = "MyFileName.txt"
if ($name.Length -gt 255) { Write-Host "Filename too long: $($name.Length) characters" }
```

### Use Valid Extensions

```powershell
# Ensure extension is valid
$ext = [System.IO.Path]::GetExtension("file.txt")
if ([string]::IsNullOrEmpty($ext)) { Write-Host "No extension found" }
```

### Fix Double Extensions

```powershell
$name = "file.tar.gz"
# This is valid but check if intended
$extensions = [System.IO.Path]::GetExtension($name)
```

## Related Errors

- [ERROR_BAD_PATHNAME (161)]({{< relref "/os/windows/win32-bad-pathname" >}}) — Full path format invalid
- [ERROR_FILE_NOT_FOUND (2)]({{< relref "/os/windows/win32-file-not-found" >}}) — File not found
- [ERROR_ALREADY_EXISTS (183)]({{< relref "/os/windows/win32-already-exists" >}}) — File already exists
