---
title: "[Solution] COBOL 66 Level — RENAMES Level"
description: "Fix COBOL 66 level errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1088
---

Level 66 is the RENAMES level, used to give alternative names to groups of fields. Errors involve incorrect syntax, using 66 where 88 would be appropriate, or missing the THRU clause.

## Common Causes

- Missing THRU keyword in RENAMES declaration
- Using 66 level where 88 (condition name) is needed
- 66 level items placed incorrectly in the data structure
- Using 66 for a single field instead of a group

## How to Fix

### 1. Use proper RENAMES syntax

```cobol
01 WS-RECORD.
    05 WS-A        PIC X(10).
    05 WS-B        PIC X(10).
    05 WS-C        PIC X(10).
66 WS-GROUP        RENAMES WS-A THRU WS-C.
```

### 2. RENAMES without THRU for single field alias

```cobol
01 WS-DATA.
    05 WS-ORIG     PIC X(20).
66 WS-ALIAS        RENAMES WS-ORIG.
```

### 3. Place 66 levels after all 01-level items

```cobol
01 WS-RECORD.
    05 WS-FIELD-1  PIC X(10).
    05 WS-FIELD-2  PIC X(20).
66 WS-ALL          RENAMES WS-FIELD-1 THRU WS-FIELD-2.
```

### 4. Use 66 for flexible field access

```cobol
01 WS-NAME.
    05 WS-FIRST    PIC X(15).
    05 WS-LAST     PIC X(15).
66 WS-FULL-NAME    RENAMES WS-FIRST THRU WS-LAST.
```

### 5. Do not confuse with 88 level

```cobol
*> 88: condition name (boolean)
01 WS-FLAG   PIC X(1).
    88 WS-YES VALUE 'Y'.

*> 66: group alias
66 WS-ALIAS  RENAMES WS-FLAG.
```

## Examples

Level 66 in a data structure:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. LEVEL66-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-EMPLOYEE.
    05 WS-EMP-ID      PIC 9(5).
    05 WS-EMP-NAME    PIC X(30).
    05 WS-EMP-DEPT    PIC X(10).
    05 WS-EMP-SALARY  PIC 9(7)V99.
66 WS-NAME-DEPT       RENAMES WS-EMP-NAME THRU WS-EMP-DEPT.
66 WS-ID-SALARY       RENAMES WS-EMP-ID THRU WS-EMP-SALARY.

PROCEDURE DIVISION.
    MOVE 10001 TO WS-EMP-ID.
    MOVE 'JOHN DOE' TO WS-EMP-NAME.
    MOVE 'ACCOUNTING' TO WS-EMP-DEPT.
    MOVE 75000.00 TO WS-EMP-SALARY.
    DISPLAY 'Name/Dept: ' WS-NAME-DEPT.
    STOP RUN.
```

## Related Errors

- [COBOL RENAMES Error](../cobol-renames)
- [COBOL REDEFINES Error](../cobol-redefines)
- [COBOL 88 Level Error](../cobol-level88)
