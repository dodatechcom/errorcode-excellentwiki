---
title: "[Solution] VBA PivotTable Error"
description: "PivotTable creation and manipulation errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA PivotTable Error

PivotTable creation and manipulation errors.

### Common Causes
Wrong source; field not found; not refreshed

### How to Fix
```vba
Dim pt As PivotTable
Set pt = ws.PivotTables("PivotTable1")
pt.RefreshTable
```

### Examples
```vba
Dim pf As PivotField
Set pf = pt.PivotFields("Category")
pf.Orientation = xlRowField
```
