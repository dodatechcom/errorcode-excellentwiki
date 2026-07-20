---
title: "[Solution] COBOL CALL Statement — Subprogram Invocation"
description: "Fix COBOL CALL statement errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1092
---

The CALL statement invokes another program. Errors involve wrong parameter count, mismatched data types, or calling a program that does not exist.

## Common Causes

- Parameter count or types do not match the callee's LINKAGE SECTION
- Calling a program not compiled or in the library path
- Missing CANCEL after a dynamic CALL to free resources
- Not using GOBACK in the callee (uses STOP RUN instead)

## How to Fix

### 1. Match parameters between caller and callee

```cobol
CALL 'SUBPROG' USING WS-DATA WS-COUNT.
*> callee must have matching LINKAGE SECTION
```

### 2. Use CANCEL for dynamic calls

```cobol
CALL WS-PROG-NAME USING WS-DATA.
*> ... later ...
CANCEL WS-PROG-NAME.
```

### 3. Use GOBACK, not STOP RUN, in subprograms

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SUBPROG.

PROCEDURE DIVISION USING LS-DATA.
    DISPLAY LS-DATA.
    GOBACK.  *> NOT STOP RUN
```

### 4. Check program existence

```cobol
CALL 'NONEXIST' ON EXCEPTION
    DISPLAY 'Program not found'
END-CALL.
```

### 5. Use nested CALL carefully

```cobol
PROCEDURE DIVISION.
    CALL 'PROG-A' USING WS-A.
    *> PROG-A may call PROG-B
    CALL 'PROG-C' USING WS-C.
```

## Examples

A complete CALL scenario:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. MAIN-PROG.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-NUM          PIC 9(5) VALUE 100.
01  WS-RESULT       PIC 9(7) VALUE 0.

PROCEDURE DIVISION.
    CALL 'DOUBLER' USING WS-NUM WS-RESULT.
    DISPLAY 'Result: ' WS-RESULT.
    STOP RUN.

IDENTIFICATION DIVISION.
PROGRAM-ID. DOUBLER.

DATA DIVISION.
LINKAGE SECTION.
01  LS-NUM          PIC 9(5).
01  LS-RESULT       PIC 9(7).

PROCEDURE DIVISION USING LS-NUM LS-RESULT.
    COMPUTE LS-RESULT = LS-NUM * 2.
    GOBACK.
```

## Related Errors

- [COBOL CANCEL Statement](../cobol-cancel-statement)
- [COBOL STOP RUN Error](../cobol-stop-run)
- [COBOL Nested Programs](../cobol-nested-programs)
