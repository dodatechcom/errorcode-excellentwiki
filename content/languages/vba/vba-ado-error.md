---
title: "[Solution] VBA ADO Error"
description: "ActiveX Data Objects errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA ADO Error

ActiveX Data Objects errors.

### Common Causes
Wrong connection string; provider missing

### How to Fix
```vba
Dim conn As Object
Set conn = CreateObject("ADODB.Connection")
conn.Open "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=C:\data\db.accdb"
```

### Examples
```vba
Dim rs As Object
Set rs = CreateObject("ADODB.Recordset")
rs.Open "SELECT * FROM Table1", conn, 3, 3
```
