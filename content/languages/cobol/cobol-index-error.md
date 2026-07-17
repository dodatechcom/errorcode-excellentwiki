---
title: "Index error in COBOL"
description: "Index errors in COBOL occur when using invalid subscript values or index registers that are out of range."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

COBOL indexes and subscripts must be within the range defined by OCCURS clauses. An out-of-range index causes an S0C6 ABEND (fixed-point performance monitor).

## Common Causes

- Subscript exceeds OCCURS count
- Index register not initialized
- Subscript is negative or zero
- Using wrong index for wrong table

## How to Fix

```cobol
       * WRONG: Subscript out of range
       01 WS-TABLE.
           05 WS-ITEM OCCURS 10 TIMES PIC X(20).
       MOVE WS-ITEM(15) TO WS-OUTPUT.
       * Error: subscript 15 > OCCURS 10
```

```cobol
       * CORRECT: Check subscript bounds
       IF WS-INDEX > 0 AND WS-INDEX <= 10
           MOVE WS-ITEM(WS-INDEX) TO WS-OUTPUT
       ELSE
           DISPLAY 'Index out of range: ' WS-INDEX
       END-IF.
```

```cobol
       * CORRECT: Use SET for index operations
       SET IDX TO 1.
       PERFORM VARYING IDX FROM 1 BY 1
           UNTIL IDX > 10
           DISPLAY WS-ITEM(IDX)
       END-PERFORM.
```

## Examples

```cobol
       01 TABLE-DATA.
           05 ENTRY OCCURS 5 TIMES PIC 9(5).
       MOVE 0 TO WS-IDX.
       MOVE ENTRY(WS-IDX) TO WS-VAL.
       * Error: subscript is 0 (below lower bound)
```

## Related Errors

- [Subscript Error](/languages/cobol/subscript-error) - subscript errors
- [Runtime Error](/languages/cobol/runtime-error) - general errors
