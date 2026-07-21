---
title: "[Solution] VBA File Already Open Error"
description: "File is already open by another process."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA File Already Open Error

File is already open by another process.

### Common Causes
Not closed; another application has lock

### How to Fix
```vba
Close #1  ' Close before reopening
Open filePath For Output As #1
```

### Examples
```vba
Dim fNum As Integer
fNum = FreeFile
Open filePath For Input As #fNum
Close #fNum
```
