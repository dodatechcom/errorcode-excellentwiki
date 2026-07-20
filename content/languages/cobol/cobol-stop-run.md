---
title: "[Solution] COBOL STOP RUN — Program Termination"
description: "Fix COBOL STOP RUN errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1094
---

STOP RUN terminates the entire run unit. Errors involve using STOP RUN in a subprogram (should use GOBACK), or missing STOP RUN at the end of the main program.

## Common Causes

- Using STOP RUN in a subprogram terminates the entire job
- Missing STOP RUN causing the program to fall through to the next program
- STOP RUN in a paragraph that should return to a caller
- Not returning a return code with STOP RUN

## How to Fix

### 1. Use STOP RUN only in the main program

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. MAIN.

PROCEDURE DIVISION.
    DISPLAY 'Hello'.
    STOP RUN.  *> correct in main
```

### 2. Use GOBACK in subprograms

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SUB.

PROCEDURE DIVISION.
    DISPLAY 'Sub'.
    GOBACK.  *> correct in subprogram
```

### 3. Return a return code

```cobol
STOP RUN RETURNING WS-RETURN-CODE.
```

### 4. Check for STOP RUN in called programs

```cobol
CALL 'SUBPROG' ON EXCEPTION
    DISPLAY 'CALL FAILED'
    STOP RUN RETURNING 12
END-CALL.
```

### 5. Use EXIT PROGRAM as alternative to GOBACK

```cobol
PROCEDURE DIVISION.
    DISPLAY 'done'.
    EXIT PROGRAM.
```

## Examples

Main program with return codes:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. MAIN-PROG.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-RETURN-CODE  PIC 9(2) VALUE 0.

PROCEDURE DIVISION.
    CALL 'PROCESS' USING WS-RETURN-CODE
    IF WS-RETURN-CODE NOT = 0
        DISPLAY 'Error in PROCESS'
    END-IF
    STOP RUN RETURNING WS-RETURN-CODE.
```

## Related Errors

- [COBOL GO BACK Error](../cobol-go-back)
- [COBOL EXIT PROGRAM Error](../cobol-exit-program)
- [COBOL Nested Programs](../cobol-nested-programs)
