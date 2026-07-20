---
title: "[Solution] COBOL OCCURS — Table and Array Declarations"
description: "Fix COBOL OCCURS clause errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1083
---

The OCCURS clause declares repeating data elements (arrays/tables). Errors involve wrong subscript ranges, missing OCCURS on multi-dimensional tables, or using undeclared indices.

## Common Causes

- Subscript out of range (starts at 1, not 0 in most compilers)
- Missing OCCURS for nested table dimensions
- Using the wrong index in a table reference
- Referencing a table element without a subscript

## How to Fix

### 1. Declare tables with OCCURS

```cobol
01 WS-TABLE.
    05 WS-ITEM    PIC X(10) OCCURS 10 TIMES.
01 WS-MATRIX.
    05 WS-ROW     OCCURS 5 TIMES.
        10 WS-COL PIC 9(4) OCCURS 5 TIMES.
```

### 2. Use correct subscripts

```cobol
MOVE 'HELLO' TO WS-ITEM(1).   *> first element
MOVE 'WORLD' TO WS-ITEM(10).  *> last element
```

### 3. Use OCCURS with DEPENDING ON for variable length

```cobol
01 WS-LIST.
    05 WS-COUNT    PIC 9(3).
    05 WS-ENTRY    PIC X(20) OCCURS 0 TO 100
                      DEPENDING ON WS-COUNT.
```

### 4. Use index with OCCURS

```cobol
01 WS-TABLE.
    05 WS-ITEM    PIC X(10) OCCURS 10 TIMES.
       89 END-OF-TABLE VALUE 11.

PROCEDURE DIVISION.
    SET IDX TO 1.
    PERFORM VARYING IDX FROM 1 BY 1
            UNTIL IDX > 10
        DISPLAY WS-ITEM(IDX)
    END-PERFORM.
```

### 5. Initialize tables

```cobol
01 WS-TABLE.
    05 WS-NUM     PIC 9(3) OCCURS 5 TIMES
                      VALUE ALL ZERO.
```

## Examples

A complete table example:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. TABLE-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-SCORES.
    05 WS-SCORE   PIC 9(3) OCCURS 5 TIMES.
01 WS-IDX        PIC 9(3) COMP.
01 WS-AVG        PIC 9(5)V99.

PROCEDURE DIVISION.
    MOVE 85 TO WS-SCORE(1).
    MOVE 90 TO WS-SCORE(2).
    MOVE 78 TO WS-SCORE(3).
    MOVE 92 TO WS-SCORE(4).
    MOVE 88 TO WS-SCORE(5).
    COMPUTE WS-AVG =
        (WS-SCORE(1) + WS-SCORE(2) + WS-SCORE(3)
       + WS-SCORE(4) + WS-SCORE(5)) / 5.
    DISPLAY 'Average: ' WS-AVG.
    STOP RUN.
```

## Related Errors

- [COBOL Subscript Error](../cobol-subscript-error)
- [COBOL Table Error](../cobol-table-error)
- [COBOL SEARCH ALL Error](../cobol-search-all)
