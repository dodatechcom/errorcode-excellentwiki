---
title: "[Solution] VBA ADO: connection error - provider not found"
description: "Fix VBA ADO/DAO connection errors when database connections fail, provider not found, or ODBC errors occur."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

ADO connection errors occur when VBA cannot establish a database connection. "Provider not found" means the OLE DB provider for the database type isn't installed or configured properly.

## Common Causes

- Missing OLE DB provider
- Wrong connection string
- Database file doesn't exist
- Network path inaccessible
- 32-bit vs 64-bit provider mismatch
- Database password required

## How to Fix

```vba
' WRONG: Hardcoded connection string
Sub Example1()
    Dim conn As Object
    Set conn = CreateObject("ADODB.Connection")
    conn.Open "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=C:\data\db.accdb"
    ' May fail if provider not installed
End Sub

' CORRECT: Check provider availability
Sub Example1()
    Dim conn As Object
    Dim connStr As String
    
    On Error GoTo ErrHandler
    
    ' Try ACE provider first
    connStr = "Provider=Microsoft.ACE.OLEDB.12.0;" & _
              "Data Source=C:\data\db.accdb;" & _
              "Persist Security Info=False;"
    
    Set conn = CreateObject("ADODB.Connection")
    conn.Open connStr
    
    ' Use connection
    Dim rs As Object
    Set rs = CreateObject("ADODB.Recordset")
    rs.Open "SELECT * FROM MyTable", conn
    
    ' Cleanup
    rs.Close
    conn.Close
    Set rs = Nothing
    Set conn = Nothing
    Exit Sub
    
ErrHandler:
    MsgBox "Connection error: " & Err.Description
End Sub
```

```vba
' CORRECT: Fallback to different providers
Sub Example2()
    Dim conn As Object
    Set conn = CreateObject("ADODB.Connection")
    
    On Error Resume Next
    
    ' Try ACE provider
    conn.Open "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=C:\data\db.mdb"
    
    If conn.State = 0 Then
        ' Try JET provider
        conn.Open "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\data\db.mdb"
    End If
    
    On Error GoTo 0
    
    If conn.State = 1 Then
        MsgBox "Connected successfully"
        conn.Close
    Else
        MsgBox "Failed to connect"
    End If
End Sub
```

```vba
' CORRECT: Use DAO for Access databases
Sub Example3()
    Dim db As DAO.Database
    Set db = OpenDatabase("C:\data\db.accdb")
    
    Dim rs As DAO.Recordset
    Set rs = db.OpenRecordset("SELECT * FROM MyTable")
    
    ' Process records
    Do While Not rs.EOF
        Debug.Print rs!Name
        rs.MoveNext
    Loop
    
    rs.Close
    db.Close
End Sub
```

## Related Errors

- [Access Error](vba-access-error) - Access-specific errors
- [File Not Found](vba-file-not-found-v2) - missing files
- [Permission Denied](vba-permission-denied-v2) - access issues
