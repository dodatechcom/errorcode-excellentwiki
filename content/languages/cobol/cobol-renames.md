---
title: "[Solution] COBOL RENAMES — Group Renaming Errors"
description: "Fix COBOL RENAMES errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1085
---

The RENAMES clause (level 66) creates an alternative name for a group of fields. Errors involve overlapping RENAMES, incorrect level numbers, or using RENAMES where REDEFINES would be more appropriate.

## Common Causes

- Using RENAMES where REDEFINES is needed (RENAMES is for aliasing groups)
- RENAMES field overlaps with another RENAMES on the same level
- Using RENAMES on level 01 (not allowed)
- Missing RENAMES clause syntax

## How to Fix

### 1. Use level 66 for RENAMES

```cobol
01 WS-RECORD.
    05 WS-FIELD-1  PIC X(10).
    05 WS-FIELD-2  PIC X(10).
    05 WS-FIELD-3  PIC X(10).
66 WS-ALL-FIELDS  RENAMES WS-FIELD-1 THRU WS-FIELD-3.
```

### 2. Use RENAMES to alias subgroups

```cobol
01 WS-ADDRESS.
    05 WS-STREET   PIC X(30).
    05 WS-CITY     PIC X(20).
    05 WS-STATE    PIC X(2).
    05 WS-ZIP      PIC X(10).
66 WS-LOCAL       RENAMES WS-CITY THRU WS-ZIP.
```

### 3. Do not use RENAMES on level 01

```cobol
01 WS-RECORD.
    05 WS-A        PIC X(10).
66 WS-B            RENAMES WS-A.  *> level 66, not 01
```

### 4. Use RENAMES for conditional testing

```cobol
01 WS-INPUT.
    05 WS-CODE     PIC X(5).
    05 WS-DATA     PIC X(20).
66 WS-CODE-DATA    RENAMES WS-CODE THRU WS-DATA.

IF WS-CODE-DATA = SPACES
    DISPLAY 'Empty record'
END-IF.
```

### 5. Understand RENAMES vs REDEFINES

```cobol
*> REDEFINES: same memory, different interpretation
01 WS-ORIG  PIC X(10).
01 WS-ALT   REDEFINES WS-ORIG PIC 9(10).

*> RENAMES: same memory, different name/group
66 WS-GROUP RENAMES WS-ORIG THRU WS-ALT.  *> not useful here
```

## Examples

RENAMES for flexible data access:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. RENAMES-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-CUSTOMER.
    05 WS-FIRST    PIC X(15).
    05 WS-LAST     PIC X(15).
    05 WS-AGE      PIC 9(3).
    05 WS-BALANCE  PIC 9(7)V99.
66 WS-NAME         RENAMES WS-FIRST THRU WS-LAST.
66 WS-FINANCIAL    RENAMES WS-AGE THRU WS-BALANCE.

PROCEDURE DIVISION.
    MOVE 'JOHN' TO WS-FIRST.
    MOVE 'DOE' TO WS-LAST.
    MOVE 30 TO WS-AGE.
    MOVE 1500.50 TO WS-BALANCE.
    DISPLAY 'Name: ' WS-NAME.
    DISPLAY 'Financial: ' WS-FINANCIAL.
    STOP RUN.
```

## Related Errors

- [COBOL REDEFINES Error](../cobol-redefines)
- [COBOL Data Movement Error](../cobol-data-movement-error)
- [COBOL Record Error](../cobol-record-error)
