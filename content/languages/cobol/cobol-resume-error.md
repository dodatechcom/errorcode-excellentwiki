---
title: "[Solution] COBOL RESUME Statement Error"
description: "Fix COBOL RESUME statement errors when attempting to resume execution after an interrupt or exception."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

RESUME statement errors occur when trying to resume execution after an exception handler without a valid interrupt context.

## Common Causes

- RESUME used outside an ON EXCEPTION block
- No prior exception was caught
- RESUME with incorrect target paragraph
- Missing declarative paragraph context

## How to Fix

### 1. Use RESUME within ON EXCEPTION

```cobol
*> WRONG: RESUME outside exception handler
PROCEDURE DIVISION.
    PERFORM CHECK-DATA.
    RESUME CHECK-DATA.

*> CORRECT: Inside declarative
USE AFTER EXCEPTION PROCEDURE ON CHECK-DATA.
    DISPLAY 'Error occurred'.
    RESUME CHECK-DATA.
```

### 2. Use proper exception handling

```cobol
PROCEDURE DIVISION.
    PERFORM CHECK-DATA
    ON EXCEPTION
        DISPLAY 'Exception in CHECK-DATA'
    END-PERFORM.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. RESUME-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-VALUE  PIC 9(4) VALUE 0.

PROCEDURE DIVISION.
    MOVE 100 TO WS-VALUE.
    DISPLAY 'Value: ' WS-VALUE.
    STOP RUN.
```

## Related Errors

- [COBOL Runtime Error](../cobol-runtime-error)
- [COBOL Restart Error](../cobol-restart-error)
- [COBOL Perform Error](../cobol-perform-error)
