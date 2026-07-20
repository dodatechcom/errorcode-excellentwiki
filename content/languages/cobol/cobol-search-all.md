---
title: "[Solution] COBOL SEARCH ALL — Binary Table Search"
description: "Fix COBOL SEARCH ALL errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1101
---

SEARCH ALL performs a binary search on a sorted table. Errors involve unsorted tables, wrong key field, or missing INDEXED BY on the table.

## Common Causes

- Table is not sorted by the search key
- Missing INDEXED BY on the OCCURS declaration
- Wrong key field in the WHEN condition
- Table is too small for binary search (linear search is better)

## How to Fix

### 1. Declare table with INDEXED BY

```cobol
01 WS-TABLE.
    05 WS-ENTRY     OCCURS 100 TIMES
                     INDEXED BY WS-IDX.
        10 WS-KEY   PIC 9(5).
        10 WS-NAME  PIC X(20).
```

### 2. Ensure table is sorted by key

```cobol
SORT WS-TABLE ON ASCENDING KEY WS-KEY.
```

### 3. Use SEARCH ALL with correct key

```cobol
SET WS-IDX TO 1.
SEARCH ALL WS-ENTRY
    AT END
        DISPLAY 'Not found'
    WHEN WS-KEY(WS-IDX) = WS-SEARCH-KEY
        DISPLAY 'Found: ' WS-NAME(WS-IDX)
END-SEARCH
```

### 4. Set index to 1 before SEARCH ALL

```cobol
SET WS-IDX TO 1.
SEARCH ALL WS-ENTRY ...
```

### 5. Use SEARCH (linear) for unsorted tables

```cobol
SET WS-IDX TO 1.
SEARCH WS-ENTRY
    AT END
        DISPLAY 'Not found'
    WHEN WS-KEY(WS-IDX) = WS-SEARCH-KEY
        DISPLAY 'Found'
END-SEARCH
```

## Examples

Complete binary search example:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SEARCH-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-TABLE.
    05 WS-ENTRY OCCURS 10 TIMES INDEXED BY WS-IDX.
        10 WS-KEY    PIC 9(3).
        10 WS-VALUE  PIC X(10).
01  WS-SEARCH-KEY   PIC 9(3) VALUE 5.

PROCEDURE DIVISION.
    MOVE 1 TO WS-KEY(1). MOVE 'FIRST' TO WS-VALUE(1).
    MOVE 2 TO WS-KEY(2). MOVE 'SECOND' TO WS-VALUE(2).
    MOVE 5 TO WS-KEY(3). MOVE 'FIFTH' TO WS-VALUE(3).
    *> ... fill more entries ...

    SET WS-IDX TO 1.
    SEARCH ALL WS-ENTRY
        AT END
            DISPLAY 'Key ' WS-SEARCH-KEY ' not found'
        WHEN WS-KEY(WS-IDX) = WS-SEARCH-KEY
            DISPLAY 'Found: ' WS-VALUE(WS-IDX)
    END-SEARCH
    STOP RUN.
```

## Related Errors

- [COBOL OCCURS Error](../cobol-occurs)
- [COBOL SORT Statement](../cobol-sort-statement)
- [COBOL Table Error](../cobol-table-error)
