---
title: "[Solution] While Loop Error"
description: "While loop errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# While Loop Error

While loop errors.

### Common Causes
Infinite loop; wrong condition

### How to Fix
```powershell
$i = 0
while ($i -lt 10) { $i++; Write-Output $i }
```

### Examples
```powershell
$reader = [System.IO.StreamReader]::new("file.txt")
while ($null -ne ($line = $reader.ReadLine())) { $line }
$reader.Close()
```
