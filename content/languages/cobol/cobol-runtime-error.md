---
title: "Runtime error in COBOL"
description: "Runtime errors in COBOL occur during program execution due to invalid operations, data exceptions, or resource limitations."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

COBOL runtime errors (abends) occur when the program encounters an invalid operation during execution. Common codes include S0C7 (data exception), S0C1 (operation exception), and S0C4 (protection exception).

## Common Causes

- Division by zero (ABEND S0C8)
- Data not numeric when expected (ABEND S0C7)
- Invalid subscript or index (ABEND S0C6)
- Uninitialized variables
- File I/O failures

## How to Fix

```cobol
       * WRONG: No error handling
       IDENTIFICATION DIVISION.
       PROGRAM-ID. RUNTIME-ERR.
       PROCEDURE DIVISION.
           MOVE 'ABC' TO WS-NUMBER.
           COMPUTE WS-RESULT = WS-NUMBER / 0.
       * S0C7 or S0C8 ABEND
```

```cobol
       * CORRECT: Check before operations
       IDENTIFICATION DIVISION.
       PROGRAM-ID. RUNTIME-SAFE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-NUMBER    PIC 9(5).
       01 WS-DIVISOR   PIC 9(5) VALUE 0.
       01 WS-RESULT    PIC 9(10).
       PROCEDURE DIVISION.
           IF WS-DIVISOR NOT = 0
               DIVIDE WS-NUMBER BY WS-DIVISOR
                   GIVING WS-RESULT
           ELSE
               DISPLAY 'ERROR: Division by zero'
           END-IF.
           STOP RUN.
```

## Examples

```cobol
       * Example 1: Data exception
       MOVE 'HELLO' TO WS-NUMERIC-VAR.
       * S0C7: HELLO is not numeric

       * Example 2: Division by zero
       DIVIDE A BY B GIVING C.
       * S0C8 if B = 0
```

## Related Errors

- [Division by Zero](/languages/cobol/division-error2) - arithmetic errors
- [File Not Found](/languages/cobol/file-not-found) - file errors
- [Decimal Error](/languages/cobol/decimal-error) - precision errors
