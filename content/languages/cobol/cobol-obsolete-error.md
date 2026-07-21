---
title: "[Solution] COBOL Obsolete Feature Error"
description: "Fix COBOL errors caused by using obsolete features like STOP RETURN, ALTER, or COMPUTE verb variations."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

Obsolete feature errors occur when code uses COBOL-74 or earlier constructs that are no longer supported in COBOL-85 and later standards.

## Common Causes

- Using STOP RETURN instead of GOBACK
- Using ALTER verb for self-modifying code
- COMPUTE with unsupported operators
- Using EJECT or SKIPPAGE in source listing

## How to Fix

### 1. Replace STOP RETURN with GOBACK

```cobol
*> WRONG: Obsolete
STOP RETURN.

*> CORRECT
GOBACK.
```

### 2. Remove ALTER statements

```cobol
*> WRONG: Self-modifying code
ALTER PARA-1 TO PROCEED TO PARA-3.

*> CORRECT: Use normal flow control
IF WS-FLAG = 'Y'
    PERFORM PARA-3
ELSE
    PERFORM PARA-1.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. OBSOLETE-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-FLAG  PIC X VALUE 'N'.

PROCEDURE DIVISION.
    IF WS-FLAG = 'Y'
        DISPLAY 'Flag is set'
    ELSE
        DISPLAY 'Flag not set'.
    GOBACK.
```

## Related Errors

- [COBOL Syntax Error](../cobol-syntax-error-new)
- [COBOL Compiler Option Error](../cobol-compiler-option)
- [COBOL Go Back Error](../cobol-go-back)
