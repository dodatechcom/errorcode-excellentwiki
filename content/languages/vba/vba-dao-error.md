---
title: "[Solution] VBA DAO Error"
description: "Data Access Objects errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA DAO Error

Data Access Objects errors.

### Common Causes
Wrong connection; SQL syntax; no recordset

### How to Fix
```vba
Dim db As DAO.Database
Set db = CurrentDb
Dim rs As DAO.Recordset
Set rs = db.OpenRecordset("SELECT * FROM Table1")
```

### Examples
```vba
Do While Not rs.EOF
    Debug.Print rs.Fields("Name").Value
    rs.MoveNext
Loop
rs.Close
```
