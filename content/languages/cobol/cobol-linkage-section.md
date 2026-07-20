---
title: "[Solution] COBOL LINKAGE SECTION — Parameter Passing"
description: "Fix COBOL LINKAGE SECTION errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1091
---

The LINKAGE SECTION defines parameters passed to a subprogram via the CALL statement. Errors involve mismatched parameter definitions, wrong level numbers, or missing USING on the PROCEDURE DIVISION.

## Common Causes

- LINKAGE SECTION items do not match the caller's arguments
- Missing `PROCEDURE DIVISION USING` for the linkage items
- Using LINKAGE variables without moving them to WORKING-STORAGE
- Wrong PIC clause for passed parameters

## How to Fix

### 1. Define LINKAGE SECTION with matching structure

```cobol
LINKAGE SECTION.
01  LS-INPUT        PIC X(80).
01  LS-COUNT        PIC 9(5).
```

### 2. Use PROCEDURE DIVISION USING

```cobol
PROCEDURE DIVISION USING LS-INPUT LS-COUNT.
    DISPLAY 'Input: ' LS-INPUT.
    DISPLAY 'Count: ' LS-COUNT.
    GOBACK.
```

### 3. Copy linkage to working-storage for modification

```cobol
WORKING-STORAGE SECTION.
01  WS-INPUT-COPY   PIC X(80).

PROCEDURE DIVISION USING LS-INPUT.
    MOVE LS-INPUT TO WS-INPUT-COPY.
    *> work with WS-INPUT-COPY
```

### 4. Use LINKAGE for callable programs

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SUB-PROG.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-RESULT       PIC 9(5).

LINKAGE SECTION.
01  LS-NUMBER       PIC 9(5).
01  LS-OUTPUT       PIC 9(7).

PROCEDURE DIVISION USING LS-NUMBER LS-OUTPUT.
    COMPUTE WS-RESULT = LS-NUMBER * 2.
    MOVE WS-RESULT TO LS-OUTPUT.
    GOBACK.
```

### 5. Match data types between caller and callee

```cobol
*> Caller
CALL 'SUB-PROG' USING WS-NUM WS-OUT.

*> Callee
LINKAGE SECTION.
01  LS-NUM  PIC 9(5) COMP.  *> must match caller's WS-NUM
01  LS-OUT  PIC 9(7) COMP.
```

## Examples

A complete callable subprogram:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. CALCTAX.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-TAX-RATE     PIC 9(3)V99 VALUE 0.08.
01  WS-TAX-AMT      PIC 9(5)V99.

LINKAGE SECTION.
01  LS-AMOUNT       PIC 9(7)V99.
01  LS-TOTAL        PIC 9(7)V99.

PROCEDURE DIVISION USING LS-AMOUNT LS-TOTAL.
    COMPUTE WS-TAX-AMT = LS-AMOUNT * WS-TAX-RATE.
    COMPUTE LS-TOTAL = LS-AMOUNT + WS-TAX-AMT.
    GOBACK.
```

## Related Errors

- [COBOL CALL Statement Error](../cobol-call-statement)
- [COBOL PROCEDURE DIVISION USING Error](../cobol-procedure-division-using)
- [COBOL Nested Programs Error](../cobol-nested-programs)
