---
title: "[Solution] COBOL Intrinsic Function Error"
description: "Fix COBOL intrinsic function errors including incorrect argument types and missing FUNCTION keyword."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

Intrinsic function errors occur when COBOL built-in functions are called with wrong argument types or missing the FUNCTION keyword.

## Common Causes

- Missing FUNCTION keyword before function name
- Passing string to a numeric function
- Using wrong number of arguments
- FUNCTION not supported by target compiler

## How to Fix

### 1. Always use FUNCTION keyword

```cobol
*> WRONG: Missing FUNCTION keyword
COMPUTE WS-RESULT = SQRT(WS-VALUE).

*> CORRECT
COMPUTE WS-RESULT = FUNCTION SQRT(WS-VALUE).
```

### 2. Match argument types

```cobol
*> WRONG: String argument to numeric function
COMPUTE WS-RESULT = FUNCTION SQRT(WS-TEXT).

*> CORRECT: Use numeric field
COMPUTE WS-RESULT = FUNCTION SQRT(WS-NUMERIC-VALUE).
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. FUNCTION-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-VALUE    PIC 9(4) VALUE 16.
01 WS-RESULT   PIC 9(4)V99.
01 WS-MIN      PIC 9(4) VALUE 5.
01 WS-MAX      PIC 9(4) VALUE 20.

PROCEDURE DIVISION.
    COMPUTE WS-RESULT = FUNCTION SQRT(WS-VALUE).
    DISPLAY 'Square root: ' WS-RESULT.
    COMPUTE WS-RESULT = FUNCTION MIN(WS-MIN, WS-MAX).
    DISPLAY 'Minimum: ' WS-RESULT.
    STOP RUN.
```

## Related Errors

- [COBOL Compute Error](../cobol-compute-error)
- [COBOL Syntax Error](../cobol-syntax-error-new)
- [COBOL Data Name Error](../cobol-data-name-error)
