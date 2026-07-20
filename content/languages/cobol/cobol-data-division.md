---
title: "[Solution] COBOL DATA DIVISION — Data Declarations"
description: "Fix COBOL DATA DIVISION errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1124
---

DATA DIVISION contains all data declarations. Errors involve missing sections, wrong level numbers, or missing PIC clauses.

## Common Causes

- Missing WORKING-STORAGE SECTION for program variables
- Using level 01 for items that should be under a group
- Missing PIC clause on data items
- Using VALUE with OCCURS (not allowed in some dialects)

## How to Fix

### 1. Structure the DATA DIVISION properly

```cobol
DATA DIVISION.
FILE SECTION.
    FD  MY-FILE.
    01  MY-RECORD.
        05 MY-FIELD    PIC X(10).

WORKING-STORAGE SECTION.
01  WS-COUNTER       PIC 9(5) VALUE 0.
01  WS-NAME          PIC X(20) VALUE 'DEFAULT'.

LINKAGE SECTION.
01  LS-INPUT         PIC X(50).
```

### 2. Use correct level hierarchy

```cobol
WORKING-STORAGE SECTION.
01  WS-RECORD.
    05 WS-FIELD-1    PIC X(10).    *> level 05 under 01
    05 WS-FIELD-2    PIC 9(5).
```

### 3. Every data item needs a PIC (except 88 and 66)

```cobol
01  WS-VAR          PIC 9(5).     *> PIC required
    88 WS-END       VALUE 'Y'.    *> 88 has VALUE, no PIC
66  WS-ALIAS        RENAMES WS-VAR. *> 66 has RENAMES, no PIC
```

### 4. Use VALUE for initialization

```cobol
01  WS-AMOUNT       PIC 9(7)V99 VALUE 0.00.
01  WS-FLAG         PIC X(1) VALUE SPACES.
```

### 5. Check LOCAL-STORAGE for per-invocation data

```cobol
LOCAL-STORAGE SECTION.
01  WS-CALL-COUNT   PIC 9(5) VALUE 0.
```

## Examples

Complete DATA DIVISION:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. DATA-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-COUNT        PIC 9(5) COMP VALUE 0.
01  WS-NAME         PIC X(20) VALUE 'TEST'.
01  WS-TABLE.
    05 WS-ENTRY     PIC X(10) OCCURS 5 TIMES.
01  WS-RECORD.
    05 WS-ID        PIC 9(5).
    05 WS-VALUE     PIC X(15).
    88 WS-VALID     VALUE 'Y'.
66  WS-ID-VAL       RENAMES WS-ID THRU WS-VALUE.

PROCEDURE DIVISION.
    MOVE 'Y' TO WS-VALID.
    IF WS-VALID
        DISPLAY 'Valid record'
    END-IF
    STOP RUN.
```

## Related Errors

- [COBOL WORKING-STORAGE Error](../cobol-working-storage)
- [COBOL File Section Error](../cobol-file-section)
- [COBOL LINKAGE Section Error](../cobol-linkage-section-new)
