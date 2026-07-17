---
title: "[Solution] COBOL: sort error - insufficient memory"
description: "Fix COBOL sort errors when sorting operations fail due to memory limitations or configuration issues."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

COBOL sort errors occur when the SORT or MERGE statement fails, often due to insufficient memory for work files, incorrect SORT configuration, or data issues.

## Common Causes

- Insufficient memory for sort work files
- Work file space exhausted
- Invalid sort keys
- Data too large for available memory
- Missing WORK-FIELD declarations

## How to Fix

```cobol
       * WRONG: Missing sort configuration
       IDENTIFICATION DIVISION.
       PROGRAM-ID. SORT-ERROR.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-RECORD PIC X(80).
       PROCEDURE DIVISION.
           SORT SORT-FILE
               ON ASCENDING KEY WS-KEY
               INPUT PROCEDURE IS 100-INPUT
               OUTPUT PROCEDURE IS 200-OUTPUT.
           * May fail without proper work files
```

```cobol
       * CORRECT: Proper sort setup
       IDENTIFICATION DIVISION.
       PROGRAM-ID. SORT-SAFE.
       DATA DIVISION.
       FILE SECTION.
       SD  SORT-FILE
           RECORD CONTAINS 80 CHARACTERS.
       01  SORT-RECORD.
           05 SORT-KEY PIC X(10).
           05 SORT-DATA PIC X(70).
       WORKING-STORAGE SECTION.
       01 WS-EOF PIC X VALUE 'N'.
       PROCEDURE DIVISION.
           OPEN INPUT DATA-FILE
           SORT SORT-FILE
               ON ASCENDING KEY SORT-KEY
               INPUT PROCEDURE IS 100-INPUT
               OUTPUT PROCEDURE IS 200-OUTPUT
           CLOSE DATA-FILE.
       100-INPUT SECTION.
       100-INPUT-RTN.
           READ DATA-FILE
               AT END MOVE 'Y' TO WS-EOF
           END-READ
           PERFORM UNTIL WS-EOF = 'Y'
               RELEASE SORT-RECORD
               READ DATA-FILE
                   AT END MOVE 'Y' TO WS-EOF
               END-READ
           END-PERFORM.
       200-OUTPUT SECTION.
       200-OUTPUT-RTN.
           RETURN SORT-FILE
               AT END DISPLAY 'No records'
           END-RETURN
           PERFORM UNTIL WS-EOF = 'Y'
               DISPLAY SORT-RECORD
               RETURN SORT-FILE
                   AT END MOVE 'Y' TO WS-EOF
               END-RETURN
           END-PERFORM.
```

```cobol
       * CORRECT: Add work file space (mainframe)
       * In JCL:
       * //SORTWK01 DD SPACE=(CYL,(10,10))
       * //SORTWK02 DD SPACE=(CYL,(10,10))
       * //SORTWK03 DD SPACE=(CYL,(10,10))
```

```cobol
       * CORRECT: Check sort return code
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CHECK-SORT.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-SORT-RC PIC 9(4) VALUE 0.
       PROCEDURE DIVISION.
           SORT SORT-FILE
               ON ASCENDING KEY SORT-KEY
               INPUT PROCEDURE IS 100-INPUT
               OUTPUT PROCEDURE IS 200-OUTPUT
           IF WS-SORT-RC NOT = 0
               DISPLAY 'Sort error: ' WS-SORT-RC
           END-IF.
```

```cobol
       * CORRECT: Validate data before sort
       IDENTIFICATION DIVISION.
       PROGRAM-ID. VALIDATE-SORT.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-RECORD.
           05 WS-KEY PIC X(10).
           05 WS-DATA PIC X(70).
       PROCEDURE DIVISION.
           READ DATA-FILE INTO WS-RECORD
           IF WS-KEY = SPACES
               DISPLAY 'Invalid key for sorting'
           ELSE
               PERFORM SORT-PROCESS
           END-IF.
```

## Related Errors

- [Runtime Error](cobol-runtime-error-v2) - file status errors
- [File Not Found](cobol-file-not-found-v2) - file errors
- [Record Error](cobol-record-error-v2) - record errors
