---
title: "[Solution] VBA JSON Error"
description: "JSON parsing without library errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA JSON Error

JSON parsing without library errors.

### Common Causes
Manual parsing; missing library

### How to Fix
```vba
' Use VBA-JSON library or manual parsing
Dim jsonStr As String
jsonStr = "{\"key\": \"value\"}"
```

### Examples
```vba
' Use a JSON parser library
Dim parsed As Object
Set parsed = JsonConverter.ParseJson(jsonStr)
Debug.Print parsed("key")
```
