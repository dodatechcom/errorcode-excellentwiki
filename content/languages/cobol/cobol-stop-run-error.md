---
title: "[Solution] COBOL STOP Error"
description: "Fix COBOL STOP RUN errors including missing status codes and improper termination in subprograms."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

STOP RUN errors occur when programs terminate without proper status codes, or when subprograms use STOP RUN instead of GOBACK.

## Common Causes

- STOP RUN in a called subprogram
- Missing RETURN-CODE after STOP RUN
- Program falls through to STOP RUN unexpectedly
- STOP RUN with invalid return value

## How to Fix

### 1. Use GOBACK in subprograms

```cobol
*> WRONG: STOP RUN in subprogram
PROGRAM-ID. SUB-PROG.
PROCEDURE DIVISION.
    DISPLAY 'Done'.
    STOP RUN.
*> WRONG: Stops entire runtime

*> CORRECT
PROCEDURE DIVISION.
    DISPLAY 'Done'.
    GOBACK.
```

### 2. Set RETURN-CODE before stopping

```cobol
MOVE 0 TO RETURN-CODE.
STOP RUN.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. STOP-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-STATUS  PIC 9(4) VALUE 0.

PROCEDURE DIVISION.
    MOVE 0 TO WS-STATUS.
    DISPLAY 'Program complete with status: ' WS-STATUS.
    STOP RUN.
```

## Related Errors

- [COBOL Go Back Error](../cobol-go-back)
- [COBOL Exit Program Error](../cobol-exit-program)
- [COBOL Runtime Error](../cobol-runtime-error)
