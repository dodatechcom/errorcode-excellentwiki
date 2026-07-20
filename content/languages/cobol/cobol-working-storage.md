---
title: "[Solution] COBOL WORKING-STORAGE — Variable Declarations"
description: "Fix WORKING-STORAGE section errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1090
---

WORKING-STORAGE declares variables used during program execution. Errors involve missing PIC clauses, wrong level numbers, or invalid VALUE clauses.

## Common Causes

- Missing PIC clause on data items
- Wrong level number hierarchy (01 for records, 05 for fields)
- VALUE clause incompatible with PIC format
- Mixing WORKING-STORAGE and LOCAL-STORAGE incorrectly

## How to Fix

### 1. Declare variables with proper level hierarchy

```cobol
WORKING-STORAGE SECTION.
01  WS-COUNTER      PIC 9(5) COMP VALUE 0.
01  WS-RECORD.
    05 WS-FIELD-A   PIC X(10).
    05 WS-FIELD-B   PIC 9(5).
```

### 2. Use VALUE for initialization

```cobol
01  WS-NAME         PIC X(20) VALUE 'DEFAULT'.
01  WS-AMOUNT       PIC 9(7)V99 VALUE 0.00.
01  WS-FLAG         PIC X(1) VALUE 'N'.
    88 WS-DONE      VALUE 'Y'.
```

### 3. Use OCCURS for arrays

```cobol
01  WS-TABLE.
    05 WS-ENTRY     PIC X(20) OCCURS 100 TIMES.
```

### 4. Use REDEFINES for variant data

```cobol
01  WS-DATA.
    05 WS-INT       PIC 9(5).
    05 WS-CHAR      REDEFINES WS-INT PIC X(5).
```

### 5. Use FILLER for padding

```cobol
01  WS-LINE.
    05 WS-TITLE     PIC X(20).
    05 FILLER       PIC X(5) VALUE SPACES.
    05 WS-VALUE     PIC X(10).
```

## Examples

A complete WORKING-STORAGE section:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. WSCHEMA-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-LOOP-IDX     PIC 9(3) COMP.
01  WS-LOOP-MAX     PIC 9(3) COMP VALUE 10.
01  WS-TOTAL        PIC 9(9)V99 COMP VALUE 0.
01  WS-COUNT        PIC 9(5) COMP VALUE 0.
01  WS-INPUT-LINE   PIC X(80).
01  WS-RESPONSE     PIC X(1).
    88 WS-YES       VALUE 'Y'.
    88 WS-NO        VALUE 'N'.

PROCEDURE DIVISION.
    PERFORM VARYING WS-LOOP-IDX FROM 1 BY 1
            UNTIL WS-LOOP-IDX > WS-LOOP-MAX
        ADD 1 TO WS-COUNT
        COMPUTE WS-TOTAL = WS-TOTAL + WS-LOOP-IDX
    END-PERFORM.
    DISPLAY 'Total: ' WS-TOTAL.
    STOP RUN.
```

## Related Errors

- [COBOL File Section Error](../cobol-file-section)
- [COBOL LINKAGE Section Error](../cobol-linkage-section-new)
- [COBOL PIC Clause Error](../cobol-pic-clause)
