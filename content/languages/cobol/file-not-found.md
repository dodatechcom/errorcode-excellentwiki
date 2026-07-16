---
title: "[Solution] COBOL FILE-STATUS 35 — File Not Found Error"
description: "Fix COBOL FILE-STATUS 35 (file not found). Learn why the runtime can't locate the file and how to verify paths and open modes."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["file-status", "file-not-found", "35", "open", "runtime"]
weight: 5
---

# FILE-STATUS 35 — File Not Found Error

A `FILE-STATUS 35` error occurs when the COBOL runtime attempts to open a file that doesn't exist at the specified path, or the path is incorrect. This is one of the most common file-related errors in COBOL programs.

## Description

In COBOL, file operations are managed through the File Status field. When an `OPEN` statement is executed and the runtime cannot find the file (for INPUT or I-O mode) or create it (for OUTPUT mode), FILE-STATUS is set to `35`. This is typically a configuration or path issue rather than a code logic problem.

Common scenarios:

- **File doesn't exist** — attempting to open a file for INPUT that hasn't been created.
- **Wrong path** — the file exists but the directory path in the SELECT clause is incorrect.
- **Permission denied** — the runtime lacks read/write permissions on the file path.
- **File name mismatch** — the actual filename differs from what the program expects.
- **Environment variable issue** — file names in COBOL often rely on environment variable resolution.

## Common Causes

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. FILE-ERROR.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT EMPLOYEE-FILE ASSIGN TO "EMPLOYEES.DAT"
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD  EMPLOYEE-FILE.
       01  EMPLOYEE-RECORD.
           05 EMP-ID        PIC 9(5).
           05 EMP-NAME      PIC X(20).

       WORKING-STORAGE SECTION.
       01  WS-FILE-STATUS   PIC XX VALUE SPACES.

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           OPEN INPUT EMPLOYEE-FILE
           IF WS-FILE-STATUS NOT = "00"
               DISPLAY "File open error: " WS-FILE-STATUS
               STOP RUN
           END-IF
           READ EMPLOYEE-FILE
               AT END DISPLAY "End of file"
           END-READ
           CLOSE EMPLOYEE-FILE
           STOP RUN.
```

## How to Fix

### Fix 1: Verify the file exists before opening

```cobol
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
      *    Check file status after OPEN
           OPEN INPUT EMPLOYEE-FILE
           IF WS-FILE-STATUS = "35"
               DISPLAY "ERROR: File not found - EMPLOYEES.DAT"
               DISPLAY "Please ensure the file exists in the "
                       "working directory"
               STOP RUN
           END-IF
           ...
```

### Fix 2: Use OUTPUT mode to create the file first

```cobol
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
      *    Create the file if it doesn't exist
           OPEN OUTPUT EMPLOYEE-FILE
           WRITE EMPLOYEE-RECORD FROM INITIAL-RECORD
           CLOSE EMPLOYEE-FILE

      *    Now reopen for input
           OPEN INPUT EMPLOYEE-FILE
           ...
```

### Fix 3: Verify file assignment paths

```cobol
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
      *    Make sure the path is correct
           SELECT EMPLOYEE-FILE ASSIGN TO "./data/EMPLOYEES.DAT"
               ORGANIZATION IS LINE SEQUENTIAL.

      *    Or use environment variable
           SELECT EMPLOYEE-FILE ASSIGN TO EMP-DATA-FILE
               ORGANIZATION IS LINE SEQUENTIAL.
```

### Fix 4: Add error handling with OPEN INPUT/OUTPUT

```cobol
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           OPEN I-O EMPLOYEE-FILE
           EVALUATE WS-FILE-STATUS
               WHEN "00"
                   CONTINUE
               WHEN "35"
                   DISPLAY "File not found, creating new file"
                   CLOSE EMPLOYEE-FILE
                   OPEN OUTPUT EMPLOYEE-FILE
                   CLOSE EMPLOYEE-FILE
                   OPEN I-O EMPLOYEE-FILE
               WHEN OTHER
                   DISPLAY "File error: " WS-FILE-STATUS
                   STOP RUN
           END-EVALUATE
           ...
```

## Examples

```
File not found: EMPLOYEES.DAT (FILE-STATUS 35)

The OPEN INPUT statement could not locate the file
'EMPLOYEES.DAT' in the current working directory.
```

## Related Errors

- [file-status-39] — record length mismatch between file and program definition.
- [FILE-STATUS 30] — permanent file error (hardware/media issue).
- [FILE-STATUS 41] — file already open.
