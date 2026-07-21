---
title: "[Solution] COBOL Debugging Error"
description: "Fix COBOL debugging issues including missing DEBUG-ITEM and incorrect use of READY TRACE."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

Debugging errors occur when COBOL debugging features are misconfigured or when the DEBUG-ITEM is used incorrectly during runtime tracing.

## Common Causes

- Missing READY TRACE before using debug features
- DEBUG-ITEM not declared in WORKING-STORAGE
- Using TRACE in production code accidentally
- Conflicting DEBUG and optimization options

## How to Fix

### 1. Declare DEBUG-ITEM properly

```cobol
WORKING-STORAGE SECTION.
DEBUG-ITEM.
    DEBUG-SUB-1   PIC 9(4).
    DEBUG-SUB-2   PIC 9(4).
```

### 2. Use READY TRACE in appropriate scope

```cobol
READY TRACE.
PERFORM CHECK-ALL-RECORDS.
RESET TRACE.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. DEBUG-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-COUNT  PIC 9(4) VALUE 0.

PROCEDURE DIVISION.
    READY TRACE.
    PERFORM 10 TIMES
        ADD 1 TO WS-COUNT
        DISPLAY 'Count: ' WS-COUNT
    END-PERFORM.
    RESET TRACE.
    STOP RUN.
```

## Related Errors

- [COBOL Runtime Error](../cobol-runtime-error)
- [COBOL Syntax Error](../cobol-syntax-error-new)
- [COBOL Working Storage Error](../cobol-working-storage)
