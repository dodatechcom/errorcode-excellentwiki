---
title: "[Solution] COBOL: division by zero error"
description: "Fix COBOL errors when dividing by zero in COMPUTE or DIVIDE statements."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

COBOL division by zero occurs when a DIVIDE or COMPUTE statement attempts to divide by a zero value, which is undefined and causes an exception (ABEND S0C8).

## Common Causes

- Divisor variable is zero
- Uninitialized divisor
- Missing zero-check
- Data loaded from file contains zeros
- Incorrect calculation producing zero

## How to Fix

```cobol
       * WRONG: No zero check
       IDENTIFICATION DIVISION.
       PROGRAM-ID. DIV-BY-ZERO.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-A PIC 9(5) VALUE 100.
       01 WS-B PIC 9(5) VALUE 0.
       01 WS-RESULT PIC 9(5).
       PROCEDURE DIVISION.
           DIVIDE WS-A BY WS-B GIVING WS-RESULT.
           * ABEND S0C8: Division by zero
```

```cobol
       * CORRECT: Check before dividing
       IDENTIFICATION DIVISION.
       PROGRAM-ID. DIV-SAFE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-A PIC 9(5) VALUE 100.
       01 WS-B PIC 9(5) VALUE 0.
       01 WS-RESULT PIC 9(5).
       PROCEDURE DIVISION.
           IF WS-B NOT = 0
               DIVIDE WS-A BY WS-B GIVING WS-RESULT
           ELSE
               DISPLAY 'Cannot divide by zero'
           END-IF.
```

```cobol
       * CORRECT: Use ON SIZE ERROR
       IDENTIFICATION DIVISION.
       PROGRAM-ID. DIV-ERROR.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-A PIC 9(5) VALUE 100.
       01 WS-B PIC 9(5) VALUE 0.
       01 WS-RESULT PIC 9(5).
       PROCEDURE DIVISION.
           DIVIDE WS-A BY WS-B GIVING WS-RESULT
               ON SIZE ERROR
                   DISPLAY 'Division error'
               NOT ON SIZE ERROR
                   DISPLAY 'Result: ' WS-RESULT
           END-DIVIDE.
```

```cobol
       * CORRECT: Validate data from file
       IDENTIFICATION DIVISION.
       PROGRAM-ID. VALIDATE-DATA.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-DIVISOR PIC 9(5).
       01 WS-RESULT PIC 9(10).
       PROCEDURE DIVISION.
           READ DATA-FILE
               AT END DISPLAY 'EOF'
           END-READ
           IF WS-DIVISOR = 0
               DISPLAY 'Invalid divisor'
           ELSE
               COMPUTE WS-RESULT = 100 / WS-DIVISOR
           END-IF.
```

```cobol
       * CORRECT: Use COMPUTE with check
       IDENTIFICATION DIVISION.
       PROGRAM-ID. COMPUTE-SAFE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-A PIC 9(5) VALUE 100.
       01 WS-B PIC 9(5) VALUE 0.
       01 WS-RESULT PIC 9(10).
       PROCEDURE DIVISION.
           IF WS-B NOT = 0
               COMPUTE WS-RESULT = WS-A / WS-B
           ELSE
               MOVE 0 TO WS-RESULT
           END-IF.
```

## Related Errors

- [Overflow](cobol-overflow-v2) - arithmetic overflow
- [Undefined Variable](cobol-undefined-variable-v2) - variable errors
- [Runtime Error](cobol-runtime-error-v2) - file status errors
