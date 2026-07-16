---
title: "Overflow error"
description: "An overflow error occurs when a numeric value exceeds the capacity of its receiving field."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["overflow", "numeric", "size", "cobol"]
weight: 5
---

## What This Error Means

An overflow error in COBOL occurs when an arithmetic operation produces a result that is too large to fit in the receiving field. This is a runtime error that occurs when numeric fields are too small for their values.

## Common Causes

- Result field too small for calculation
- Multiplying large numbers
- Accumulating values without sufficient field size
- packed decimal overflow

## How to Fix

```cobol
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-SMALL    PIC 9(3) VALUE 0.
       01  WS-LARGE    PIC 9(9) VALUE 0.

       PROCEDURE DIVISION.
      * WRONG: WS-SMALL too small
           COMPUTE WS-SMALL = 1000 * 1000
      * Overflow error

      * CORRECT: Use larger field
           COMPUTE WS-LARGE = 1000 * 1000
```

```cobol
       PROCEDURE DIVISION.
      * Check before operation
           IF WS-NUMBER1 * WS-NUMBER2 > 99999
               DISPLAY "Result would overflow"
           ELSE
               COMPUTE WS-RESULT = WS-NUMBER1 * WS-NUMBER2
           END-IF
```

## Examples

```cobol
      * Example 1: Field too small
       01  WS-RESULT    PIC 9(3).
       COMPUTE WS-RESULT = 500 + 600
      * Overflow: 1100 doesn't fit in 3 digits

      * Example 2: Multiplication overflow
       01  WS-RESULT    PIC 9(5).
       COMPUTE WS-RESULT = 999 * 999
      * Overflow: 998001 doesn't fit in 5 digits

      * Example 3: Packed decimal
       01  WS-RESULT    PIC 9(3)V99 COMP-3.
       COMPUTE WS-RESULT = 999.99 * 999.99
      * May overflow packed decimal field
```

## Related Errors

- [Division error](/languages/cobol/division-error2)
- [Subscript out of range](/languages/cobol/subscript-error)
