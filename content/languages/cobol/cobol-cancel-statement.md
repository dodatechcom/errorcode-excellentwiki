---
title: "[Solution] COBOL CANCEL Statement — Subprogram Release"
description: "Fix COBOL CANCEL statement errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1093
---

The CANCEL statement releases a dynamically called subprogram from memory. Errors involve calling CANCEL on a statically linked program or forgetting to CANCEL after dynamic calls.

## Common Causes

- CANCEL on a program that was never CALLed
- Forgetting to CANCEL after dynamic CALLs (memory leak)
- CANCEL on a program name that does not match the CALL
- Using CANCEL after STOP RUN in the callee (too late)

## How to Fix

### 1. CANCEL only after a dynamic CALL

```cobol
CALL WS-PROG-NAME USING WS-DATA.
*> ... process ...
CANCEL WS-PROG-NAME.
```

### 2. Match the program name exactly

```cobol
CALL 'MYPGM' USING WS-A.
CANCEL 'MYPGM'.  *> must match
```

### 3. Use CANCEL in a loop for repeated dynamic calls

```cobol
PERFORM VARYING WS-I FROM 1 BY 1 UNTIL WS-I > 10
    MOVE WS-PROG-TABLE(WS-I) TO WS-CURR-PROG
    CALL WS-CURR-PROG USING WS-DATA
    CANCEL WS-CURR-PROG
END-PERFORM.
```

### 4. CANCEL releases initial values

```cobol
CALL 'STATEFUL' USING WS-X.
CANCEL 'STATEFUL'.
*> next CALL starts with fresh initial values
```

### 5. Use CANCEL before a second call to the same program

```cobol
CALL 'MYPROG' USING WS-A.
CANCEL 'MYPROG'.
CALL 'MYPROG' USING WS-B.  *> fresh start
```

## Examples

Dynamic program loading:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. DYNAMIC-LOADER.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-PROG-NAME    PIC X(20).
01  WS-DATA         PIC X(100).

PROCEDURE DIVISION.
    MOVE 'PROC-1' TO WS-PROG-NAME
    CALL WS-PROG-NAME USING WS-DATA
    CANCEL WS-PROG-NAME

    MOVE 'PROC-2' TO WS-PROG-NAME
    CALL WS-PROG-NAME USING WS-DATA
    CANCEL WS-PROG-NAME

    STOP RUN.
```

## Related Errors

- [COBOL CALL Statement](../cobol-call-statement)
- [COBOL STOP RUN Error](../cobol-stop-run)
- [COBOL EXIT PROGRAM Error](../cobol-exit-program)
