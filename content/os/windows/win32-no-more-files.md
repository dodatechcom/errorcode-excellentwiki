---
title: "ERROR_NO_MORE_FILES (18) - How to Fix"
description: "Fix Windows ERROR_NO_MORE_FILES (18). Resolve file enumeration errors, fix directory listing issues, and troubleshoot FindFirstFile/FindNextFile errors."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["win32", "error-18", "no-more-files", "enumeration"]
weight: 5
---

# ERROR_NO_MORE_FILES (Win32 Error 18)

This Win32 API error occurs when a file enumeration operation reaches the end of the directory listing, or when the enumeration fails. The error code is `ERROR_NO_MORE_FILES` (value 18). The full message reads:

> "There are no more files."

This is normally returned by `FindFirstFile`/`FindNextFile` when enumeration is complete, but it becomes an error when expected files are missing.

## Common Causes

- **Directory is empty** — No files match the search criteria.
- **Files were deleted during enumeration** — Race condition between listing and accessing.
- **Access denied on subdirectories** — Some entries cannot be enumerated.
- **Junction/symlink points to empty location** — Symbolic links resolve to nothing.
- **Wrong directory** — Enumeration target is not the expected directory.

## How to Fix

### Verify Directory Contents

```powershell
Get-ChildItem "C:\Path\To\Directory" -ErrorAction SilentlyContinue
```

### Check for Hidden Files

```powershell
Get-ChildItem "C:\Path\To\Directory" -Force -ErrorAction SilentlyContinue
```

### Enumerate Files Recursively

```powershell
Get-ChildItem "C:\Path\To\Directory" -Recurse -ErrorAction SilentlyContinue | Select-Object FullName
```

### Check File Attributes

```powershell
Get-ChildItem "C:\Path\To\Directory" | Select-Object Name, Attributes, Length
```

### Verify Search Pattern

```powershell
# Check with specific filter
Get-ChildItem "C:\Path\To\Directory" -Filter "*.txt" -ErrorAction SilentlyContinue
```

### Check Junction/Symlink Targets

```powershell
Get-Item "C:\Path\To\Junction" | Select-Object Target, LinkType
```

### Use Robocopy to Verify

```cmd
robocopy "C:\Path\To\Dir" C:\NUL /L /s
```

## Related Errors

- [ERROR_FILE_NOT_FOUND (2)]({{< relref "/os/windows/win32-file-not-found" >}}) — Specific file not found
- [ERROR_PATH_NOT_FOUND (3)]({{< relref "/os/windows/win32-path-not-found" >}}) — Directory path doesn't exist
- [ERROR_DIR_NOT_EMPTY (145)]({{< relref "/os/windows/win32-directory-not-empty" >}}) — Directory not empty during deletion
