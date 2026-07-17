---
title: "[Solution] COBOL: record format error"
description: "Fix COBOL errors when record formats don't match, record lengths are incorrect, or record operations fail."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

COBOL record format errors occur when the record structure doesn't match the file format, record length is incorrect, or record operations encounter issues.

## Common Causes

- Record length mismatch with file
- FD description doesn't match actual file
- Variable-length records handled incorrectly
- Record contains invalid data
- Record already locked

## How to Fix

```cobol
       * WRONG: Record length mismatch
       IDENTIFICATION DIVISION.
       PROGRAM-ID. RECORD-ERROR.
       DATA DIVISION.
       FILE SECTION.
       FD  DATA-FILE
           RECORD CONTAINS 80 CHARACTERS.
       01  DATA-RECORD PIC X(100).
           * Mismatch: FD says 80, record is 100
```

```cobol
       * CORRECT: Match record length
       IDENTIFICATION DIVISION.
       PROGRAM-ID. RECORD-MATCH.
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

```cobol
       * CORRECT: Handle variable-length records
       IDENTIFICATION DIVISION.
       PROGRAM-ID. VARIABLE-RECORD.
       DATA DIVISION.
       FILE SECTION.
       FD  DATA-FILE
           RECORD IS VARYING IN SIZE
               FROM 10 TO 100 CHARACTERS
           CONTAINS 0 CHARACTERS.
       01  DATA-RECORD PIC X(100).
       PROCEDURE DIVISION.
           OPEN INPUT DATA-FILE
           READ DATA-FILE
               AT END DISPLAY 'EOF'
           END-READ
           CLOSE DATA-FILE.
```

```cobol
       * CORRECT: Check record after read
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CHECK-RECORD.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-FILE-STATUS PIC XX VALUE SPACES.
       PROCEDURE DIVISION.
           READ DATA-FILE
               AT END DISPLAY 'EOF'
           END-READ
           IF WS-FILE-STATUS = '00'
               DISPLAY 'Record read successfully'
           ELSE
               DISPLAY 'Record error: ' WS-FILE-STATUS
           END-IF.
```

```cobol
       * CORRECT: Validate record content
       IDENTIFICATION DIVISION.
       PROGRAM-ID. VALIDATE-RECORD.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-RECORD.
           05 WS-KEY PIC X(10).
           05 WS-NAME PIC A(20).
           05 WS-VALUE PIC 9(5).
       PROCEDURE DIVISION.
           READ DATA-FILE INTO WS-RECORD
           IF WS-KEY = SPACES
               DISPLAY 'Invalid record: empty key'
           END-IF.
```

## Related Errors

- [File Not Found](cobol-file-not-found-v2) - file errors
- [Duplicate Key](cobol-duplicate-key-v2) - key errors
- [Index Error](cobol-index-error-v2) - subscript errors
