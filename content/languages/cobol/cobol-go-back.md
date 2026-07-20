---
title: "[Solution] COBOL GO BACK — Subprogram Return"
description: "Fix COBOL GO BACK errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1096
---

GO BACK returns control from a subprogram to its caller. Errors involve using GO BACK in the main program, or forgetting that GO BACK terminates the entire call chain if used in the wrong context.

## Common Causes

- Using GO BACK in the main program (should use STOP RUN)
- GO BACK in a nested program returns to the enclosing program
- Not returning data through linkage before GO BACK
- Confusing GO BACK with EXIT PARAGRAPH

## How to Fix

### 1. Use GO BACK in subprograms

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SUB.

PROCEDURE DIVISION.
    DISPLAY 'Sub'.
    GOBACK.  *> returns to caller
```

### 2. Return data before GO BACK

```cobol
PROCEDURE DIVISION USING LS-INPUT LS-OUTPUT.
    COMPUTE LS-OUTPUT = LS-INPUT * 2.
    GOBACK.
```

### 3. Use GO BACK with return code

```cobol
PROCEDURE DIVISION.
    IF WS-ERROR
        GOBACK RETURNING 12
    END-IF
    GOBACK RETURNING 0.
```

### 4. Use STOP RUN in the main program

```cobol
PROCEDURE DIVISION.
    CALL 'SUB'.
    STOP RUN.  *> NOT GO BACK
```

### 5. GO BACK in nested programs

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. OUTER.

IDENTIFICATION DIVISION.
PROGRAM-ID. INNER.
PROCEDURE DIVISION.
    DISPLAY 'Inner'.
    GOBACK.  *> returns to OUTER
END PROGRAM INNER.

PROCEDURE DIVISION.
    CALL 'INNER'.
    STOP RUN.
END PROGRAM OUTER.
```

## Examples

A complete GO BACK usage:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. MAIN-PROG.

PROCEDURE DIVISION.
    CALL 'SUB-PROG' USING WS-DATA
    STOP RUN.

IDENTIFICATION DIVISION.
PROGRAM-ID. SUB-PROG.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-DATA         PIC X(50).

LINKAGE SECTION.
01  LS-DATA         PIC X(50).

PROCEDURE DIVISION USING LS-DATA.
    MOVE 'HELLO FROM SUB' TO LS-DATA.
    GOBACK.
END PROGRAM SUB-PROG.
```

## Related Errors

- [COBOL EXIT PROGRAM Error](../cobol-exit-program)
- [COBOL STOP RUN Error](../cobol-stop-run)
- [COBOL Nested Programs](../cobol-nested-programs)
