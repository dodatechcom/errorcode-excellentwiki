---
title: "[Solution] Do-While Loop Error"
description: "Do-While loop errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Do-While Loop Error

Do-While loop errors.

### Common Causes
Missing while; wrong condition

### How to Fix
```powershell
do { $i++ } while ($i -lt 10)
```

### Examples
```powershell
do {
  $input = Read-Host "Enter q to quit"
} while ($input -ne "q")
```
