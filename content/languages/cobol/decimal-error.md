---
title: "Decimal precision error"
description: "A decimal precision error occurs when a numeric operation loses precision due to field size limitations."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["decimal", "precision", "numeric", "cobol"]
weight: 5
---

## What This Error Means

A decimal precision error occurs when a numeric operation produces a result with more decimal places than the receiving field can hold, or when precision is lost during packed decimal operations.

## Common Causes

- Insufficient decimal places in receiving field
- Division producing more decimals than field allows
- Packed decimal rounding errors
- Mixed numeric types with different precision

## How to Fix

```cobol
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-NUM1      PIC 9(5)V99 VALUE 123.45.
       01  WS-NUM2      PIC 9(5)V99 VALUE 678.90.
       01  WS-RESULT    PIC 9(7)V99.

       PROCEDURE DIVISION.
      * CORRECT: Sufficient field size
           COMPUTE WS-RESULT = WS-NUM1 + WS-NUM2
           DISPLAY "Result: " WS-RESULT
```

```cobol
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-NUM       PIC 9(5)V99 VALUE 100.00.
       01  WS-DIV       PIC 9(5)V9999.

       PROCEDURE DIVISION.
      * WRONG: WS-DIV has 4 decimal places
           DIVIDE 3 INTO WS-NUM
               GIVING WS-DIV
      * Precision may be lost

      * CORRECT: Use larger decimal field
           DIVIDE 3 INTO WS-NUM
               GIVING WS-DIV
```

## Examples

```cobol
      * Example 1: Division precision
       01  WS-A     PIC 9(3) VALUE 10.
       01  WS-B     PIC 9(3) VALUE 3.
       01  WS-C     PIC 9(3)V9.
       DIVIDE WS-A BY WS-B GIVING WS-C
      * Result: 3.3 (lost precision)

      * Example 2: Packed decimal
       01  WS-PACKED PIC 9(5)V99 COMP-3.
       COMPUTE WS-PACKED = 123.456 + 789.012
      * May round to fit packed decimal

      * Example 3: Mixed precision
       COMPUTE WS-RESULT = WS-INT + WS-DECIMAL
      * Different precision types
```

## Related Errors

- [Overflow error](/languages/cobol/overflow-error2)
- [Division error](/languages/cobol/division-error2)
