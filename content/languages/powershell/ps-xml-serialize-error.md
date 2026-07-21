---
title: "[Solution] XML Serialization Error"
description: "XML serialization errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# XML Serialization Error

XML serialization errors.

### Common Causes
Wrong element names; attribute errors

### How to Fix
```powershell
$xml = [xml]@"<root><item>text</item></root>"@
```

### Examples
```powershell
$doc = New-Object System.Xml.XmlDocument
$root = $doc.CreateElement("root")
$doc.AppendChild($root)
```
