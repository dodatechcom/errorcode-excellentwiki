---
title: "[Solution] COBOL: duplicate key error - status 22"
description: "Fix COBOL duplicate key errors when attempting to write or add a record with a key that already exists."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

COBOL status 22 indicates an attempt to add a record with a duplicate key to an indexed file. The key value already exists in the file, and duplicates are not allowed.

## Common Causes

- Duplicate key value in indexed file
- Attempting to WRITE instead of REWRITE
- Data not properly sorted
- Key definition incorrect
- Missing duplicate key handling

## How to Fix

```cobol
       * WRONG: No duplicate key handling
       IDENTIFICATION DIVISION.
       PROGRAM-ID. DUPLICATE-ERROR.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-RECORD.
           05 WS-KEY PIC X(10).
           05 WS-DATA PIC X(70).
       PROCEDURE DIVISION.
           MOVE 'KEY001' TO WS-KEY.
           MOVE 'Data' TO WS-DATA.
           WRITE WS-RECORD.
           * May fail with status 22 if key exists
```

```cobol
       * CORRECT: Check for duplicate before writing
       IDENTIFICATION DIVISION.
       PROGRAM-ID. DUPLICATE-SAFE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-FILE-STATUS PIC XX VALUE SPACES.
       01 WS-RECORD.
           05 WS-KEY PIC X(10).
           05 WS-DATA PIC X(70).
       PROCEDURE DIVISION.
           MOVE 'KEY001' TO WS-KEY.
           MOVE 'Data' TO WS-DATA.
           WRITE WS-RECORD
               INVALID KEY
                   DISPLAY 'Duplicate key: ' WS-KEY
                   REWRITE WS-RECORD
           END-WRITE.
```

```cobol
       * CORRECT: Use REWRITE for updates
       IDENTIFICATION DIVISION.
       PROGRAM-ID. UPDATE-RECORD.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-FILE-STATUS PIC XX VALUE SPACES.
       01 WS-RECORD.
           05 WS-KEY PIC X(10).
           05 WS-DATA PIC X(70).
       PROCEDURE DIVISION.
           MOVE 'KEY001' TO WS-KEY.
           READ DATA-FILE
               KEY IS WS-KEY
               INVALID KEY
                   MOVE 'New data' TO WS-DATA
                   WRITE WS-RECORD
               NOT INVALID KEY
                   MOVE 'Updated data' TO WS-DATA
                   REWRITE WS-RECORD
           END-READ.
```

```cobol
       * CORRECT: Handle status 22 explicitly
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HANDLE-DUPLICATE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-FILE-STATUS PIC XX VALUE SPACES.
       PROCEDURE DIVISION.
           WRITE WS-RECORD
           EVALUATE WS-FILE-STATUS
               WHEN '00'
                   DISPLAY 'Record written'
               WHEN '22'
                   DISPLAY 'Duplicate key'
                   REWRITE WS-RECORD
               WHEN OTHER
                   DISPLAY 'Error: ' WS-FILE-STATUS
           END-EVALUATE.
```

## Related Errors

- [Invalid Key](cobol-invalid-key-v2) - key errors
- [Runtime Error](cobol-runtime-error-v2) - file status errors
- [Record Error](cobol-record-error-v2) - record errors
