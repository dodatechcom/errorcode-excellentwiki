---
title: "File status error"
description: "A file status error occurs when a file operation fails, indicated by the FILE-STATUS field."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A file status error in COBOL is indicated when the FILE-STATUS field contains a non-zero value after a file operation. Different status codes indicate different error conditions, such as file not found, record locked, or end of file.

## Common Causes

- File doesn't exist (status 35)
- File already open (status 41)
- End of file reached (status 10)
- Record locked by another process (status 42)

## How to Fix

```cobol
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           OPEN INPUT EMPLOYEE-FILE
           IF WS-FILE-STATUS NOT = "00"
               EVALUATE WS-FILE-STATUS
                   WHEN "10"
                       DISPLAY "End of file"
                   WHEN "35"
                       DISPLAY "File not found"
                   WHEN "41"
                       DISPLAY "File already open"
                   WHEN OTHER
                       DISPLAY "File error: " WS-FILE-STATUS
               END-EVALUATE
               STOP RUN
           END-IF
           ...
```

## Examples

```cobol
      * Example 1: File not found
       OPEN INPUT EMPLOYEE-FILE
      * FILE-STATUS = 35 (file not found)

      * Example 2: End of file
       READ EMPLOYEE-FILE
           AT END
               DISPLAY "No more records"
      * FILE-STATUS = 10 (end of file)

      * Example 3: Record locked
       READ EMPLOYEE-FILE
      * FILE-STATUS = 42 (record locked)
```

## Related Errors

- [File not found](/languages/cobol/file-not-found)
- [Record locked](/languages/cobol/locked-record)
