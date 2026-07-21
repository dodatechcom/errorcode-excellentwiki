---
title: "[Solution] VBA Shape Error"
description: "Shape object errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Shape Error

Shape object errors.

### Common Causes
Wrong type; positioning; name not found

### How to Fix
```vba
Dim shp As Shape
Set shp = ws.Shapes.AddShape(msoShapeRectangle, 10, 10, 100, 50)
shp.TextFrame2.TextRange.Text = "Hello"
```

### Examples
```vba
ws.Shapes("Rectangle 1").Fill.ForeColor.RGB = vbRed
```
