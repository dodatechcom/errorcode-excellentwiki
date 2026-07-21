---
title: "[Solution] VBA XML Parsing Error"
description: "MSXML parsing errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA XML Parsing Error

MSXML parsing errors.

### Common Causes
Wrong document method; namespace issues

### How to Fix
```vba
Dim xmlDoc As Object
Set xmlDoc = CreateObject("MSXML2.DOMDocument")
xmlDoc.Load "file.xml"
```

### Examples
```vba
Dim node As Object
Set node = xmlDoc.SelectSingleNode("//root/item")
Debug.Print node.Text
```
