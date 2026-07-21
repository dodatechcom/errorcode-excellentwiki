---
title: "[Solution] Compression Error"
description: "Compression/decompression errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Compression Error

Compression/decompression errors.

### Common Causes
Wrong format; corrupted archive; path issues

### How to Fix
```powershell
Compress-Archive -Path "C:\temp\*" -DestinationPath "archive.zip"
```

### Examples
```powershell
Expand-Archive -Path "archive.zip" -DestinationPath "C:\temp\extracted" -Force
```
