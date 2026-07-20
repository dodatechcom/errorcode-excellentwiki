---
title: "[Solution] COBOL PROCEDURE DIVISION USING — Entry Parameters"
description: "Fix COBOL PROCEDURE DIVISION USING errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1126
---

PROCEDURE DIVISION USING declares the parameters a program accepts via CALL. Errors involve mismatched parameter count, wrong data types, or missing USING when parameters are passed.

## Common Causes

- PROCEDURE DIVISION USING items do not match caller's arguments
- Missing USING when the caller passes parameters
- Parameter types do not match between caller and callee
- USING with RETURNING for function-style subprograms

## How to Fix

### 1. Match USING parameters to caller

```cobol
*> Caller
CALL 'MYSUB' USING WS-A WS-B.

*> Callee
PROCEDURE DIVISION USING WS-A WS-B.
    DISPLAY WS-A WS-B.
    GOBACK.
```

### 2. Match data types exactly

```cobol
*> Caller
01 WS-NUM    PIC 9(5) COMP.
CALL 'SUB' USING WS-NUM.

*> Callee
PROCEDURE DIVISION USING LS-NUM.
01 LS-NUM    PIC 9(5) COMP.
```

### 3. Use RETURNING for return values

```cobol
PROCEDURE DIVISION USING LS-INPUT RETURNING LS-OUTPUT.
    COMPUTE LS-OUTPUT = LS-INPUT * 2.
    GOBACK.
```

### 4. Handle optional parameters

```cobol
PROCEDURE DIVISION USING LS-A LS-B LS-C.
    IF LS-C NOT OMITTED
        DISPLAY LS-C
    END-IF
```

### 5. Use LINKAGE SECTION for parameter declarations

```cobol
DATA DIVISION.
LINKAGE SECTION.
01  LS-PARAM-1    PIC X(10).
01  LS-PARAM-2    PIC 9(5).

PROCEDURE DIVISION USING LS-PARAM-1 LS-PARAM-2.
```

## Examples

A complete parameter passing example:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. CALLER.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-NAME    PIC X(20) VALUE 'JOHN'.
01  WS-AGE     PIC 9(3) VALUE 30.

PROCEDURE DIVISION.
    CALL 'DISPLAY-INFO' USING WS-NAME WS-AGE
    STOP RUN.

IDENTIFICATION DIVISION.
PROGRAM-ID. DISPLAY-INFO.

DATA DIVISION.
LINKAGE SECTION.
01  LS-NAME    PIC X(20).
01  LS-AGE     PIC 9(3).

PROCEDURE DIVISION USING LS-NAME LS-AGE.
    DISPLAY 'Name: ' LS-NAME.
    DISPLAY 'Age: ' LS-AGE.
    GOBACK.
END PROGRAM DISPLAY-INFO.
```

## Related Errors

- [COBOL CALL Statement](../cobol-call-statement)
- [COBOL LINKAGE Section Error](../cobol-linkage-section-new)
- [COBOL Nested Programs](../cobol-nested-programs)
