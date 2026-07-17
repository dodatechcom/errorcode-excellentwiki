---
title: "File not found in COBOL"
description: "File not found errors in COBOL occur when OPEN statement cannot locate the specified file."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["file", "not-found", "open", "file-status", "cobol"]
weight: 5
---

## What This Error Means

COBOL file not found errors occur when the OPEN INPUT or OPEN I-O statement cannot find the file. The FILE-STATUS field will contain '35' (file not found).

## Common Causes

- File path incorrect in DD statement
- File doesn't exist on disk
- JCL DD assignment missing
- File was deleted or moved
- Case sensitivity in file name

## How to Fix

```cobol
       * Check file status after open
       OPEN INPUT CUSTOMER-FILE
           IF FILE-STATUS NOT = '00'
               DISPLAY 'File open error: ' FILE-STATUS
               STOP RUN
           END-IF.
```

```cobol
       * CORRECT: Verify file exists before opening
       OPEN INPUT CUSTOMER-FILE
       IF FILE-STATUS = '35'
           DISPLAY 'File not found'
           STOP RUN
       END-IF.
       * Process file
       CLOSE CUSTOMER-FILE.
```

## Examples

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. FILE-CHECK.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 FILE-STATUS    PIC XX VALUE SPACES.
       01 WS-RECORD      PIC X(80).
       FILE SECTION.
       FD  CUSTOMER-FILE
           RECORD CONTAINS 80 CHARACTERS.
       01  CUSTOMER-REC  PIC X(80).
       PROCEDURE DIVISION.
           OPEN INPUT CUSTOMER-FILE
           IF FILE-STATUS NOT = '00'
               DISPLAY 'File error: ' FILE-STATUS
               STOP RUN
           END-IF.
           READ CUSTOMER-FILE
               AT END DISPLAY 'End of file'
           END-READ.
           CLOSE CUSTOMER-FILE.
           STOP RUN.
```

## Related Errors

- [File Status Error](/languages/cobol/file-status) - file operation errors
- [Locked Record](/languages/cobol/locked-record) - record locking errors
