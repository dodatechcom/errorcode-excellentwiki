---
title: "Division error"
description: "A division error occurs when performing division by zero or an arithmetic operation that produces an invalid result."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A division error in COBOL occurs when you attempt to divide by zero or when an arithmetic operation produces a result that exceeds the capacity of the receiving field. This is a runtime error that terminates the program.

## Common Causes

- Dividing by zero
- Result too large for receiving field
- Invalid arithmetic on packed decimal
- Missing numeric validation

## How to Fix

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. DIV-ERROR.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-NUMERATOR    PIC 9(5) VALUE 100.
       01  WS-DENOMINATOR  PIC 9(5) VALUE 0.
       01  WS-RESULT       PIC 9(5).

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           IF WS-DENOMINATOR = 0
               DISPLAY "Cannot divide by zero"
               STOP RUN
           END-IF
           DIVIDE WS-NUMERATOR BY WS-DENOMINATOR
               GIVING WS-RESULT
           END-DIVIDE
           DISPLAY "Result: " WS-RESULT
           STOP RUN.
```

```cobol
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
      *    Check before dividing
           IF WS-DENOMINATOR NOT = 0
               COMPUTE WS-RESULT = WS-NUMERATOR / WS-DENOMINATOR
           ELSE
               MOVE 0 TO WS-RESULT
               DISPLAY "Warning: Division by zero"
           END-IF
```

## Examples

```cobol
       PROCEDURE DIVISION.
      * Example 1: Division by zero
           MOVE 100 TO WS-NUMERATOR
           MOVE 0 TO WS-DENOMINATOR
           DIVIDE WS-NUMERATOR BY WS-DENOMINATOR
               GIVING WS-RESULT
      *    Runtime error: Division by zero

      * Example 2: Overflow
           MOVE 99999 TO WS-NUMERATOR
           MOVE 1 TO WS-DENOMINATOR
           DIVIDE WS-NUMERATOR BY WS-DENOMINATOR
               GIVING WS-RESULT
      *    WS-RESULT too small (only 5 digits)
```

## Related Errors

- [Overflow error](/languages/cobol/overflow-error2)
- [File status error](/languages/cobol/file-status)
