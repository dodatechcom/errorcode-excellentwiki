---
title: "[Solution] VBA Access: record not updatable error"
description: "Fix VBA Access errors when records cannot be updated, edited, or deleted in tables or queries."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Access "record not updatable" errors occur when you try to modify data in a table or query that doesn't support updates. This is common with multi-table queries, calculated fields, or locked records.

## Common Causes

- Query with aggregate functions (SUM, COUNT)
- Multiple tables without unique key
- Calculated fields in query
- Record locked by another user
- Table opened as read-only
- ODBC connection limitations

## How to Fix

```vba
' WRONG: Direct update of multi-table query
Sub Example1()
    Dim db As DAO.Database
    Dim rs As DAO.Recordset
    
    Set db = CurrentDb
    Set rs = db.OpenRecordset("SELECT * FROM Orders INNER JOIN Customers ON Orders.CustID = Customers.ID")
    rs.Edit  ' Error: not updatable
    rs!OrderDate = Date
    rs.Update
End Sub

' CORRECT: Update single table directly
Sub Example1()
    Dim db As DAO.Database
    Dim rs As DAO.Recordset
    
    Set db = CurrentDb
    Set rs = db.OpenRecordset("Orders")
    rs.Edit
    rs!OrderDate = Date
    rs.Update
    rs.Close
End Sub
```

```vba
' WRONG: Update with aggregates
Sub Example2()
    Dim rs As DAO.Recordset
    Set rs = CurrentDb.OpenRecordset("SELECT Sum(Amount) AS Total FROM Sales")
    rs.Edit  ' Error: not updatable
    rs!Total = 0
    rs.Update
End Sub

' CORRECT: Use temp table or direct update
Sub Example2()
    CurrentDb.Execute "UPDATE Sales SET Amount = 0 WHERE Region = 'West'"
End Sub
```

```vba
' CORRECT: Check if recordset is updatable
Sub Example3()
    Dim rs As DAO.Recordset
    Set rs = CurrentDb.OpenRecordset("MyQuery")
    
    If rs.Updatable Then
        rs.Edit
        ' Make changes
        rs.Update
    Else
        MsgBox "Recordset is not updatable"
    End If
    
    rs.Close
End Sub
```

## Related Errors

- [ADO Connection Error](vba-adodb-connection-error) - database connections
- [Runtime Error 70](vba-permission-denied-v2) - permission issues
- [File Not Found](vba-file-not-found-v2) - file access
