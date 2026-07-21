---
title: "[Solution] VBA Activate Error"
description: "Activate method errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Activate Error

Activate method errors.

### Common Causes
Sheet not found; wrong workbook

### How to Fix
```vba
ws.Activate
ws.Range("A1").Select
```

### Examples
```vba
ThisWorkbook.Sheets("Sheet1").Activate
ActiveSheet.Range("A1").Select
```
