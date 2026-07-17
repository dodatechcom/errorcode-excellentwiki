---
title: "[Solution] COBOL: arithmetic overflow error"
description: "Fix COBOL overflow errors when arithmetic calculations exceed the data item's capacity."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

COBOL arithmetic overflow occurs when the result of a computation exceeds the size of the receiving data item, causing loss of significant digits or truncation.

## Common Causes

- Result exceeds PIC clause size
- Multiplication producing large numbers
- Missing ON SIZE ERROR clause
- Insufficient decimal places
- Accumulated values in loops

## How to Fix

```cobol
       * WRONG: No size error handling
       IDENTIFICATION DIVISION.
       PROGRAM-ID. OVERFLOW-ERROR.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-A PIC 9(5) VALUE 99999.
       01 WS-B PIC 9(5) VALUE 2.
       01 WS-RESULT PIC 9(5).
       PROCEDURE DIVISION.
           COMPUTE WS-RESULT = WS-A * WS-B.
           * Overflow: 99999 * 2 = 199999 > 99999
```

```cobol
       * CORRECT: Handle size error
       IDENTIFICATION DIVISION.
       PROGRAM-ID. OVERFLOW-SAFE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-A PIC 9(5) VALUE 99999.
       01 WS-B PIC 9(5) VALUE 2.
       01 WS-RESULT PIC 9(10).
       PROCEDURE DIVISION.
           COMPUTE WS-RESULT = WS-A * WS-B
               ON SIZE ERROR
                   DISPLAY 'Arithmetic overflow'
               NOT ON SIZE ERROR
                   DISPLAY 'Result: ' WS-RESULT
           END-COMPUTE.
```

```cobol
       * CORRECT: Use larger PIC clause
       IDENTIFICATION DIVISION.
       PROGRAM-ID. LARGER-PIC.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-A PIC 9(5) VALUE 99999.
       01 WS-B PIC 9(5) VALUE 2.
       01 WS-RESULT PIC 9(10).
       PROCEDURE DIVISION.
           COMPUTE WS-RESULT = WS-A * WS-B
           DISPLAY 'Result: ' WS-RESULT.
```

```cobol
       * CORRECT: Check before computing
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CHECK-BEFORE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-A PIC 9(5).
       01 WS-B PIC 9(5).
       01 WS-RESULT PIC 9(10).
       PROCEDURE DIVISION.
           MOVE 99999 TO WS-A
           MOVE 2 TO WS-B
           IF WS-A > 9999
               DISPLAY 'Warning: potential overflow'
           END-IF
           COMPUTE WS-RESULT = WS-A * WS-B
               ON SIZE ERROR
                   DISPLAY 'Overflow occurred'
           END-COMPUTE.
```

## Related Errors

- [Division by Zero](cobol-division-by-zero-v2) - arithmetic errors
- [Undefined Variable](cobol-undefined-variable-v2) - variable errors
- [Runtime Error](cobol-runtime-error-v2) - file status errors
