---
title: "[Solution] Measure-Object Error"
description: "Measure-Object fails on non-numeric data."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Measure-Object Error

Measure-Object fails on non-numeric data.

### Common Causes
Wrong property; non-numeric input

### How to Fix
```powershell
Get-Process | Measure-Object CPU -Average
```

### Examples
```powershell
Get-Process | Measure-Object CPU -Average -Sum -Maximum
```
