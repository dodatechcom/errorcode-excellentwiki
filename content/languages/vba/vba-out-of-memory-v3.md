---
title: "[Solution] VBA Out of Memory Cannot Allocate Error Fix"
description: "Fix VBA 'Out of memory' errors when VBA cannot allocate memory. Learn why memory allocation fails and how to reduce VBA memory usage."
languages: ["vba"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

The VBA Out of Memory error occurs when the Visual Basic runtime cannot allocate enough memory for a new variable, array, or string. VBA runs in a 32-bit address space limited to approximately 2 GB (or 4 GB with Large Address Aware). Even on 64-bit systems, VBA modules are constrained by this limit.

## Why It Happens

- Declaring arrays that are too large for available memory
- Loading entire worksheets into VBA arrays at once
- Creating too many string variables or concatenating strings in loops
- Leaking memory by not releasing object references
- Running multiple large VBA projects in the same Office instance
- Exceeding the 64 KB string size limit in some contexts
- Module code size approaching the VBA project limit

## How to Fix It

### Process data in chunks instead of all at once

```vba
' WRONG: Loading entire column into memory
Sub ProcessAll()
    Dim arr As Variant
    arr = Range("A1:A1000000").Value  ' 1M rows, may exhaust memory
End Sub

' CORRECT: Process in batches
Sub ProcessAll()
    Dim batchSize As Long
    batchSize = 10000
    Dim lastRow As Long
    lastRow = Cells(Rows.Count, 1).End(xlUp).Row
    
    Dim i As Long
    For i = 1 To lastRow Step batchSize
        Dim endRow As Long
        endRow = Application.Min(i + batchSize - 1, lastRow)
        Dim chunk As Variant
        chunk = Range("A" & i & ":A" & endRow).Value
        ProcessChunk chunk
    Next i
End Sub
```

### Release object references promptly

```vba
' WRONG: Objects not released
Sub CreateReports()
    Dim xlApp As Excel.Application
    Set xlApp = New Excel.Application
    ' ... work ...
    xlApp.Quit  ' but reference still held
End Sub

' CORRECT: Release all references
Sub CreateReports()
    Dim xlApp As Excel.Application
    Set xlApp = New Excel.Application
    ' ... work ...
    xlApp.Quit
    Set xlApp = Nothing  ' release reference
End Sub
```

### Use arrays instead of cell-by-cell operations

```vba
' WRONG: Cell-by-cell is slow and memory-intensive
Sub SlowWrite()
    Dim i As Long
    For i = 1 To 100000
        Cells(i, 1).Value = i * 2
    Next i
End Sub

' CORRECT: Use array for bulk operations
Sub FastWrite()
    Dim arr() As Variant
    ReDim arr(1 To 100000, 1 To 1)
    Dim i As Long
    For i = 1 To 100000
        arr(i, 1) = i * 2
    Next i
    Range("A1:A100000").Value = arr
End Sub
```

### Avoid string concatenation in loops

```vba
' WRONG: String concatenation creates many temp strings
Sub BuildReport()
    Dim result As String
    Dim i As Long
    For i = 1 To 10000
        result = result & "Line " & i & vbCrLf  ' memory grows
    Next i
End Sub

' CORRECT: Use StringBuilder pattern
Sub BuildReport()
    Dim parts() As String
    ReDim parts(1 To 10000)
    Dim i As Long
    For i = 1 To 10000
        parts(i) = "Line " & i
    Next i
    Dim result As String
    result = Join(parts, vbCrLf)
End Sub
```

### Monitor memory usage

```vba
' CORRECT: Check available memory before large operations
Sub CheckMemory()
    Dim freeMemory As LongPtr
    freeMemory = GetAvailableMemory()  ' custom function using API
    
    If freeMemory < 100 * 1024 * 1024 Then  ' less than 100 MB
        MsgBox "Low memory warning. Consider closing other applications."
    End If
End Sub
```

## Common Mistakes

- Not setting objects to `Nothing` after use
- Using `ReDim Preserve` in a loop, which copies the entire array each time
- Storing large strings in module-level variables that persist across calls
- Not closing external connections (ADO, files) which hold memory
- Assuming 64-bit Office gives VBA access to more than 2 GB of memory

## Related Pages

- [VBA Subscript Out of Range](vba-subscript-out-of-range) - array index error
- [VBA Application-Defined Error](vba-application-defined-error) - application error
- [VBA Out of Memory V2](vba-out-of-memory-v2) - related memory error
- [VBA Runtime Error](vba-runtime-error) - general runtime issue
