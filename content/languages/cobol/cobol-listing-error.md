---
title: "[Solution] COBOL Compiler Listing Error"
description: "Fix errors shown in COBOL compiler listings including warning counts and fatal compilation failures."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

Listing errors appear in the COBOL compiler output listing, indicating warnings, severe errors, or fatal conditions that prevent compilation.

## Common Causes

- Ignoring warning messages that indicate real bugs
- Fatal syntax errors stopping compilation early
- Missing required sections (ENVIRONMENT, DATA DIVISION)
- Inconsistent compiler flags producing unexpected warnings

## How to Fix

### 1. Treat warnings as errors

```cobol
*> Warning: Implicit usage of WS-TEMP
PROCEDURE DIVISION.
    ADD 1 TO WS-TEMP.

*> Fix: Declare WS-TEMP in WORKING-STORAGE
WORKING-STORAGE SECTION.
01 WS-TEMP PIC 9(4) VALUE 0.
```

### 2. Review listing for all severity levels

Compiler listings group messages by severity. Address severity 8+ first (fatal), then severity 4 (warnings).

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. LISTING-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-VALUE  PIC 9(4) VALUE 10.

PROCEDURE DIVISION.
    DISPLAY 'Value: ' WS-VALUE.
    STOP RUN.
```

## Related Errors

- [COBOL Syntax Error](../cobol-syntax-error-new)
- [COBOL Compiler Option Error](../cobol-compiler-option)
- [COBOL Compiler Directive Error](../cobol-compiler-directive)
