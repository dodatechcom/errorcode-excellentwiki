---
title: "[Solution] XML Parsing Error"
description: "PowerShell XML parsing errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# XML Parsing Error

PowerShell XML parsing errors.

### Common Causes
Malformed XML; namespace issues; encoding

### How to Fix
```powershell
[xml]$xml = Get-Content "file.xml"
```

### Examples
```powershell
$xml = [xml](Get-Content "file.xml")
$xml.root.item
```
