---
title: "[Solution] VBA Chart Error"
description: "Chart creation and formatting errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Chart Error

Chart creation and formatting errors.

### Common Causes
Wrong source; wrong chart type; missing series

### How to Fix
```vba
Dim cht As Chart
Set cht = ws.ChartObjects.Add(100, 100, 400, 300).Chart
cht.SetSourceData ws.Range("A1:B10")
cht.ChartType = xlXYScatter
```

### Examples
```vba
cht.HasTitle = True
cht.ChartTitle.Text = "My Chart"
```
