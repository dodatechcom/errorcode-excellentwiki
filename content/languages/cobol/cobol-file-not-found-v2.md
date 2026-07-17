---
title: "[Solution] COBOL: file not found - status 05"
description: "Fix COBOL errors when files cannot be found, including status code 05 and file allocation issues."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["file", "not-found", "status", "allocation", "open", "cobol"]
weight: 5
---

## What This Error Means

COBOL file status 05 indicates that the file was not found or cannot be opened because the file doesn't exist at the expected location.

## Common Causes

- File name incorrect in FILE-CONTROL
- File not created before reading
- DD statement missing (mainframe)
- Incorrect file path
- File was deleted

## How to Fix

```cobol
       * WRONG: File not found
       IDENTIFICATION DIVISION.
       PROGRAM-ID. FILE-MISSING.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-RECORD PIC X(80).
       PROCEDURE DIVISION.
           OPEN INPUT DATA-FILE.
           * File doesn't exist
           READ DATA-FILE INTO WS-RECORD.
           CLOSE DATA-FILE.
```

```cobol
       * CORRECT: Check file exists first
       IDENTIFICATION DIVISION.
       PROGRAM-ID. FILE-CHECK.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-FILE-STATUS PIC XX VALUE SPACES.
       PROCEDURE DIVISION.
           OPEN INPUT DATA-FILE
           IF WS-FILE-STATUS = '00'
               PERFORM PROCESS-FILE
           ELSE IF WS-FILE-STATUS = '05'
               DISPLAY 'File not found'
               PERFORM CREATE-DEFAULT-FILE
           END-IF
           CLOSE DATA-FILE.
```

```cobol
       * CORRECT: Use proper file assignment
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT DATA-FILE ASSIGN TO 'C:\DATA\FILE.TXT'
               FILE STATUS IS WS-FILE-STATUS.
```

```cobol
       * CORRECT: Handle missing file
       IDENTIFICATION DIVISION.
       PROGRAM-ID. FILE-HANDLE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-FILE-STATUS PIC XX VALUE SPACES.
       PROCEDURE DIVISION.
           OPEN INPUT DATA-FILE
           IF WS-FILE-STATUS NOT = '00'
               DISPLAY 'Cannot open file'
               DISPLAY 'Status: ' WS-FILE-STATUS
               STOP RUN
           END-IF
           READ DATA-FILE
               AT END DISPLAY 'End of file'
           END-READ
           CLOSE DATA-FILE.
```

```cobol
       * CORRECT: Mainframe DD statement
       * In JCL:
       * //SYSIN DD DSN=USER.DATA.FILE,DISP=SHR
       IDENTIFICATION DIVISION.
       PROGRAM-ID. MAINFRAME-FILE.
       DATA DIVISION.
       FILE SECTION.
       FD  DATA-FILE
           RECORD CONTAINS 80 CHARACTERS.
       01  DATA-RECORD PIC X(80).
       PROCEDURE DIVISION.
           OPEN INPUT DATA-FILE
           READ DATA-FILE
               AT END DISPLAY 'EOF'
           END-READ
           CLOSE DATA-FILE.
```

## Related Errors

- [Runtime Error](cobol-runtime-error-v2) - file status errors
- [Duplicate Key](cobol-duplicate-key-v2) - key errors
- [Record Error](cobol-record-error-v2) - record errors
