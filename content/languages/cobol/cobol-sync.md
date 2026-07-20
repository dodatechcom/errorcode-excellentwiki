---
title: "[Solution] COBOL SYNC — Synchronization Directive"
description: "Fix COBOL SYNC clause errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["warning"]
weight: 1120
---

SYNC aligns data items to machine word boundaries for efficient access. Errors involve SYNC on the wrong level, or SYNC causing unexpected gaps in records.

## Common Causes

- SYNC creates padding that changes record layout
- SYNC on COMP fields may be redundant (already word-aligned)
- SYNC on PIC X fields may waste storage
- SYNC affects record size for file I/O

## How to Fix

### 1. Use SYNC with numeric fields

```cobol
01 WS-RECORD.
    05 WS-NAME     PIC X(10).
    05 FILLER      PIC X(2).     *> padding for alignment
    05 WS-COUNT    PIC 9(5) SYNC.
```

### 2. Be aware of record size changes

```cobol
01 WS-REC.
    05 WS-A        PIC X(3).
    05 WS-B        PIC 9(5) SYNC.
    *> WS-B may start at offset 4 or 8 depending on SYNC
```

### 3. Use SYNC to optimize access

```cobol
01 WS-BIG-REC.
    05 WS-FLAG     PIC X(1).
    05 FILLER      PIC X(3).     *> align to word boundary
    05 WS-AMOUNT   PIC 9(9) SYNC.
```

### 4. Avoid SYNC for sequential record layouts

```cobol
01 WS-FILE-REC.
    05 WS-FIELD-1  PIC X(5).     *> no SYNC for file records
    05 WS-FIELD-2  PIC 9(3).
```

### 5. Test with and without SYNC

```cobol
01 WS-WITH-SYNC.
    05 WS-A        PIC 9(5) SYNC.
    05 WS-B        PIC X(10).

01 WS-WITHOUT-SYNC.
    05 WS-C        PIC 9(5).
    05 WS-D        PIC X(10).
```

## Examples

SYNC in a record layout:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SYNC-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-EMPLOYEE.
    05 WS-EMP-ID      PIC 9(5) SYNC.
    05 WS-EMP-NAME    PIC X(20).
    05 WS-EMP-SALARY  PIC 9(7)V99 SYNC.
    05 WS-EMP-STATUS  PIC X(1).

PROCEDURE DIVISION.
    MOVE 10001 TO WS-EMP-ID.
    MOVE 'JOHN DOE' TO WS-EMP-NAME.
    MOVE 75000.00 TO WS-EMP-SALARY.
    DISPLAY 'ID: ' WS-EMP-ID.
    STOP RUN.
```

## Related Errors

- [COBOL PIC Clause Error](../cobol-pic-clause)
- [COBOL COMP/COMP-3 Error](../cobol-comp-comp3)
- [COBOL Record Error](../cobol-record-error)
