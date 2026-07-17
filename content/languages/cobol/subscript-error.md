---
title: "Subscript out of range"
description: "A subscript error occurs when accessing an array element with an index outside its declared bounds."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A subscript out of range error occurs when you try to access an array element using an index that is less than the lower bound or greater than the upper bound declared in the OCCURS clause.

## Common Causes

- Index below lower bound
- Index above upper bound
- Off-by-one errors in loops
- Incorrect subscript calculation

## How to Fix

```cobol
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-ARRAY.
           05 WS-ITEMS PIC X(20) OCCURS 10 TIMES.
       01  WS-INDEX    PIC 9(2) VALUE 1.

       PROCEDURE DIVISION.
      * WRONG: No bounds check
           MOVE "data" TO WS-ITEMS(WS-INDEX)

      * CORRECT: Check bounds
           IF WS-INDEX >= 1 AND WS-INDEX <= 10
               MOVE "data" TO WS-ITEMS(WS-INDEX)
           ELSE
               DISPLAY "Index out of range: " WS-INDEX
           END-IF
```

```cobol
       PROCEDURE DIVISION.
      * Use proper loop bounds
           PERFORM VARYING WS-INDEX FROM 1 BY 1
               UNTIL WS-INDEX > 10
               MOVE WS-INDEX TO WS-ITEMS(WS-INDEX)
           END-PERFORM
```

## Examples

```cobol
      * Example 1: Index too high
       01  WS-ARR PIC X(5) OCCURS 5 TIMES.
       MOVE "x" TO WS-ARR(10)  * subscript out of range

      * Example 2: Index too low
       MOVE "x" TO WS-ARR(0)   * subscript out of range

      * Example 3: Dynamic index
       COMPUTE WS-INDEX = WS-COUNT + 1
       MOVE "x" TO WS-ITEMS(WS-INDEX)  * may be out of range
```

## Related Errors

- [Overflow error](/languages/cobol/overflow-error2)
- [Syntax error](/languages/cobol/syntax-error7)
