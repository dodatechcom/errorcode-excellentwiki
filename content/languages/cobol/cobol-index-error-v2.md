---
title: "[Solution] COBOL: subscript out of range"
description: "Fix COBOL errors when array subscripts or table indices exceed their declared bounds."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["index", "subscript", "table", "array", "bounds", "cobol"]
weight: 5
---

## What This Error Means

COBOL subscript out of range occurs when accessing a table element with an index that exceeds the declared OCCURS clause bounds.

## Common Causes

- Subscript exceeds OCCURS limit
- Index not properly initialized
- Off-by-one error in loops
- Subscript is zero or negative
- Table overflow

## How to Fix

```cobol
       * WRONG: Subscript out of bounds
       IDENTIFICATION DIVISION.
       PROGRAM-ID. INDEX-ERROR.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-TABLE.
           05 WS-ITEM OCCURS 10 TIMES PIC X(10).
       01 WS-INDEX PIC 9(2).
       PROCEDURE DIVISION.
           MOVE 15 TO WS-INDEX.
           DISPLAY WS-ITEM(WS-INDEX).
           * Error: 15 > 10
```

```cobol
       * CORRECT: Check bounds before access
       IDENTIFICATION DIVISION.
       PROGRAM-ID. INDEX-SAFE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-TABLE.
           05 WS-ITEM OCCURS 10 TIMES PIC X(10).
       01 WS-INDEX PIC 9(2).
       PROCEDURE DIVISION.
           MOVE 5 TO WS-INDEX.
           IF WS-INDEX > 0 AND WS-INDEX <= 10
               DISPLAY WS-ITEM(WS-INDEX)
           ELSE
               DISPLAY 'Index out of range'
           END-IF.
```

```cobol
       * CORRECT: Use proper loop bounds
       IDENTIFICATION DIVISION.
       PROGRAM-ID. LOOP-BOUNDS.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-TABLE.
           05 WS-ITEM OCCURS 10 TIMES PIC X(10).
       01 WS-INDEX PIC 9(2).
       PROCEDURE DIVISION.
           PERFORM VARYING WS-INDEX FROM 1 BY 1
               UNTIL WS-INDEX > 10
               DISPLAY WS-ITEM(WS-INDEX)
           END-PERFORM.
```

```cobol
       * CORRECT: Initialize index properly
       IDENTIFICATION DIVISION.
       PROGRAM-ID. INIT-INDEX.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-TABLE.
           05 WS-ITEM OCCURS 10 TIMES PIC X(10).
       01 WS-INDEX PIC 9(2) VALUE 1.
       PROCEDURE DIVISION.
           MOVE 1 TO WS-INDEX
           DISPLAY WS-ITEM(WS-INDEX).
```

```cobol
       * CORRECT: Check subscript source
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CHECK-SUBSCRIPT.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-TABLE.
           05 WS-ITEM OCCURS 10 TIMES PIC X(10).
       01 WS-SUB PIC 9(3).
       PROCEDURE DIVISION.
           READ INPUT-FILE
           IF WS-SUB < 1 OR WS-SUB > 10
               DISPLAY 'Invalid subscript: ' WS-SUB
           ELSE
               DISPLAY WS-ITEM(WS-SUB)
           END-IF.
```

## Related Errors

- [Invalid Key](cobol-invalid-key-v2) - key errors
- [Record Error](cobol-record-error-v2) - record errors
- [Runtime Error](cobol-runtime-error-v2) - file status errors
