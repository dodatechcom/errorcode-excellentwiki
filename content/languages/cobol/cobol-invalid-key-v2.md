---
title: "[Solution] COBOL: invalid key error - status 23"
description: "Fix COBOL invalid key errors when accessing records with invalid keys in indexed files."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["invalid", "key", "indexed", "access", "status", "cobol"]
weight: 5
---

## What This Error Means

COBOL status 23 indicates an attempt to access a record with a key that doesn't exist in the indexed file, or an invalid key reference.

## Common Causes

- Key value doesn't exist in file
- Reading with non-existent key
- File not properly indexed
- Key area overflow
- Corrupted index

## How to Fix

```cobol
       * WRONG: No key validation
       IDENTIFICATION DIVISION.
       PROGRAM-ID. INVALID-KEY.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-KEY PIC X(10) VALUE 'NONEXIST'.
       01 WS-RECORD PIC X(80).
       PROCEDURE DIVISION.
           READ DATA-FILE
               KEY IS WS-KEY
               INTO WS-RECORD.
           * May fail with status 23
```

```cobol
       * CORRECT: Handle invalid key
       IDENTIFICATION DIVISION.
       PROGRAM-ID. INVALID-KEY-SAFE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-FILE-STATUS PIC XX VALUE SPACES.
       01 WS-KEY PIC X(10) VALUE 'KEY001'.
       01 WS-RECORD PIC X(80).
       PROCEDURE DIVISION.
           READ DATA-FILE
               KEY IS WS-KEY
               INTO WS-RECORD
               INVALID KEY
                   DISPLAY 'Key not found: ' WS-KEY
               NOT INVALID KEY
                   DISPLAY 'Record found'
           END-READ.
```

```cobol
       * CORRECT: Validate key before access
       IDENTIFICATION DIVISION.
       PROGRAM-ID. VALIDATE-KEY.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-FILE-STATUS PIC XX VALUE SPACES.
       01 WS-KEY PIC X(10).
       PROCEDURE DIVISION.
           MOVE 'KEY001' TO WS-KEY.
           IF WS-KEY = SPACES
               DISPLAY 'Invalid key'
               STOP RUN
           END-IF
           READ DATA-FILE
               KEY IS WS-KEY
               INVALID KEY
                   DISPLAY 'Key not found'
           END-READ.
```

```cobol
       * CORRECT: Check file status after operation
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CHECK-STATUS.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-FILE-STATUS PIC XX VALUE SPACES.
       PROCEDURE DIVISION.
           READ DATA-FILE
               KEY IS WS-KEY
           IF WS-FILE-STATUS = '23'
               DISPLAY 'Key does not exist'
           ELSE IF WS-FILE-STATUS = '00'
               DISPLAY 'Record read successfully'
           END-IF.
```

## Related Errors

- [Duplicate Key](cobol-duplicate-key-v2) - duplicate keys
- [Runtime Error](cobol-runtime-error-v2) - file status errors
- [Index Error](cobol-index-error-v2) - subscript errors
