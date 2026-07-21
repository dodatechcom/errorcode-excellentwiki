---
title: "[Solution] VBA ComboBox Error"
description: "ComboBox errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA ComboBox Error

ComboBox errors.

### Common Causes
No items; wrong value; RowSource issues

### How to Fix
```vba
ComboBox1.RowSource = "Sheet1!A1:A10"
```

### Examples
```vba
ComboBox1.Clear
ComboBox1.AddItem "Option A"
ComboBox1.AddItem "Option B"
ComboBox1.ListIndex = 0
```
