---
title: "[Solution] COBOL: runtime error - file status 35"
description: "Fix COBOL runtime errors when file operations fail with status code 35 (file not found or access denied)."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["runtime", "file", "status", "access", "open", "cobol"]
weight: 5
---

## What This Error Means

COBOL file status 35 indicates a file cannot be opened due to a missing file, incorrect file name, or access permission issues. This is one of the most common COBOL file status codes.

## Common Causes

- File doesn't exist at specified path
- Incorrect file name or DD statement
- Permission denied
- File locked by another process
- JCL errors (mainframe)
- Missing DD statement

## How to Fix

```cobol
       * WRONG: No file status checking
       IDENTIFICATION DIVISION.
       PROGRAM-ID. FILE-ERROR.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-RECORD PIC X(80).
       PROCEDURE DIVISION.
           OPEN INPUT DATA-FILE.
           READ DATA-FILE INTO WS-RECORD.
           CLOSE DATA-FILE.
       * May fail with status 35
```

```cobol
       * CORRECT: Check file status
       IDENTIFICATION DIVISION.
       PROGRAM-ID. FILE-SAFE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-RECORD PIC X(80).
       01 WS-STATUS PIC XX VALUE SPACES.
       PROCEDURE DIVISION.
           OPEN INPUT DATA-FILE
           IF WS-STATUS NOT = '00'
               DISPLAY 'File open error: ' WS-STATUS
               STOP RUN
           END-IF
           READ DATA-FILE INTO WS-RECORD
               AT END DISPLAY 'End of file'
           END-READ
           CLOSE DATA-FILE.
```

```cobol
       * CORRECT: Use FILE-STATUS clause
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT DATA-FILE ASSIGN TO 'data.txt'
               FILE STATUS IS WS-FILE-STATUS.
```

```cobol
       * CORRECT: Handle file errors
       IDENTIFICATION DIVISION.
       PROGRAM-ID. FILE-HANDLER.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-FILE-STATUS PIC XX VALUE SPACES.
       PROCEDURE DIVISION.
           OPEN INPUT DATA-FILE
           EVALUATE WS-FILE-STATUS
               WHEN '00'
                   PERFORM READ-RECORDS
               WHEN '35'
                   DISPLAY 'File not found'
               WHEN '30'
                   DISPLAY 'Permission denied'
               WHEN OTHER
                   DISPLAY 'Error: ' WS-FILE-STATUS
           END-EVALUATE
           CLOSE DATA-FILE.
```

## Related Errors

- [File Not Found](cobol-file-not-found-v2) - file errors
- [Duplicate Key](cobol-duplicate-key-v2) - key errors
- [Record Error](cobol-record-error-v2) - record errors
