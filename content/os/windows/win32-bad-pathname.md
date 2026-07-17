---
title: "ERROR_BAD_PATHNAME (161) - How to Fix"
description: "Fix Windows ERROR_BAD_PATHNAME (161). Resolve malformed path errors, fix invalid path characters, and troubleshoot path format issues on Windows."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["win32", "error-161", "bad-pathname", "invalid-path"]
weight: 5
---

# ERROR_BAD_PATHNAME (Win32 Error 161)

This Win32 API error occurs when a path string is malformed or contains invalid characters. The error code is `ERROR_BAD_PATHNAME` (value 161). The full message reads:

> "The filename, directory name, or volume label syntax is incorrect."

Unlike Error 2 (file not found) or Error 3 (path not found), this error means the path format itself is wrong.

## Common Causes

- **Invalid characters** — Path contains `*`, `?`, `"`, `<`, `>`, `|`, or other illegal characters.
- **Trailing spaces or dots** — Path ends with spaces or periods.
- **Double backslashes** — Unintended `\\` in path.
- **Colon in filename** — Filename contains `:` (reserved for drive letters).
- **UNC path malformed** — Network path missing leading `\\`.

## How to Fix

### Validate Path Characters

```powershell
$invalid = [System.IO.Path]::GetInvalidPathChars()
$path = "C:\Path\With*Invalid"
$hasInvalid = $path.ToCharArray() | Where-Object { $_ -in $invalid }
if ($hasInvalid) { Write-Host "Path contains invalid characters: $($hasInvalid -join ', ')" }
```

### Check for Trailing Characters

```powershell
$path.TrimEnd('.', ' ')
```

### Fix Double Backslashes

```powershell
$path -replace '\\{2,}', '\'
```

### Validate Path Format

```powershell
try {
    [System.IO.Path]::GetFullPath($path)
    Write-Host "Path is valid"
} catch {
    Write-Host "Invalid path: $_"
}
```

### Sanitize Path in Script

```powershell
function Sanitize-Path {
    param([string]$Path)
    $invalid = [System.IO.Path]::GetInvalidFileNameChars()
    $sanitized = $invalid | ForEach-Object { $Path = $Path.Replace($_, '_') }
    return $Path.TrimEnd('.', ' ')
}
```

### Check UNC Path Format

```powershell
# Valid UNC path
$uncPath = "\\ServerName\ShareName\Folder"
$uncPath -match "^\\\\[^\\]+\\[^\\]+"
```

### Check for Reserved Names

```powershell
$reserved = @("CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9")
$filename = [System.IO.Path]::GetFileNameWithoutExtension($path)
if ($filename -in $reserved) { Write-Host "Path uses reserved name: $filename" }
```

## Related Errors

- [ERROR_PATH_NOT_FOUND (3)]({{< relref "/os/windows/win32-path-not-found" >}}) — Path directory doesn't exist
- [ERROR_FILE_NOT_FOUND (2)]({{< relref "/os/windows/win32-file-not-found" >}}) — File not found at path
- [ERROR_INVALID_NAME (123)]({{< relref "/os/windows/win32-invalid-name" >}}) — Invalid filename or extension
