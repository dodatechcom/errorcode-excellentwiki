---
title: "[Solution] COBOL EXIT PROGRAM — Subprogram Return"
description: "Fix COBOL EXIT PROGRAM errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1095
---

EXIT PROGRAM returns control from a subprogram to its caller. Errors involve using EXIT PROGRAM where GOBACK is needed, or mixing EXIT PROGRAM and STOP RUN in the same program.

## Common Causes

- Using EXIT PROGRAM in the main program (should use STOP RUN)
- Missing EXIT PROGRAM causing fall-through to next paragraph
- Using EXIT PROGRAM without returning modified linkage data
- Mixing EXIT PROGRAM and STOP RUN in a subprogram

## How to Fix

### 1. Use EXIT PROGRAM in subprograms

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. CALLED.

PROCEDURE DIVISION.
    DISPLAY 'Called program'.
    EXIT PROGRAM.
```

### 2. Ensure linkage data is returned before EXIT

```cobol
PROCEDURE DIVISION USING LS-DATA.
    MOVE 'RESULT' TO LS-DATA.
    EXIT PROGRAM.
```

### 3. Use GOBACK as alternative (preferred in modern COBOL)

```cobol
PROCEDURE DIVISION USING LS-DATA.
    MOVE 'RESULT' TO LS-DATA.
    GOBACK.  *> preferred over EXIT PROGRAM
```

### 4. Multiple EXIT points

```cobol
PROCEDURE DIVISION.
    IF WS-ERROR
        DISPLAY 'Error'
        EXIT PROGRAM
    END-IF
    DISPLAY 'Normal'
    EXIT PROGRAM.
```

### 5. Do not use EXIT PROGRAM in the main program

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. MAIN.

PROCEDURE DIVISION.
    CALL 'SUB'.
    STOP RUN.  *> NOT EXIT PROGRAM
```

## Examples

Subprogram with EXIT PROGRAM:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. VALIDATOR.

DATA DIVISION.
LINKAGE SECTION.
01  LS-INPUT        PIC X(50).
01  LS-VALID        PIC X(1).

PROCEDURE DIVISION USING LS-INPUT LS-VALID.
    IF LS-INPUT = SPACES
        MOVE 'N' TO LS-VALID
    ELSE
        MOVE 'Y' TO LS-VALID
    END-IF
    EXIT PROGRAM.
```

## Related Errors

- [COBOL GO BACK Error](../cobol-go-back)
- [COBOL STOP RUN Error](../cobol-stop-run)
- [COBOL CALL Statement](../cobol-call-statement)
