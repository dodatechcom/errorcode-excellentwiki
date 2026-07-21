---
title: "[Solution] VBA SQL Syntax Error"
description: "SQL in VBA has syntax errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA SQL Syntax Error

SQL in VBA has syntax errors.

### Common Causes
Wrong SQL; quotes in strings; reserved words

### How to Fix
```vba
Dim sql As String
sql = "SELECT * FROM [Table] WHERE [Name] = '" & nameVal & "'"
```

### Examples
```vba
sql = "INSERT INTO Table1 (Col1, Col2) VALUES (" & val1 & ", '" & val2 & "')"
```
