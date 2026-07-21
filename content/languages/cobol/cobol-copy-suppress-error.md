---
title: "[Solution] COBOL COPY Suppress Error"
description: "Fix COBOL COPY SUPPRESS errors when suppressing copybook output or warnings in the listing."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

COPY SUPPRESS errors occur when the SUPPRESS clause is used incorrectly to hide copybook content from the listing, or when it interferes with debugging.

## Common Causes

- SUPPRESS hiding essential copybook definitions
- SUPPRESS preventing debugging of copybook issues
- SUPPRESS on COPY with PRINT NO conflicting with listing options
- SUPPRESS not supported by target compiler

## How to Fix

### 1. Use SUPPRESS only when necessary

```cobol
*> WRONG: Suppressing all output hides errors
COPY ERROR-DEFS
    SUPPRESS ALL.

*> CORRECT: Suppress only listing, keep compilation
COPY ERROR-DEFS
    SUPPRESS PRINTING.
```

### 2. Remove SUPPRESS during debugging

```cobol
*> Temporary: Remove SUPPRESS to debug
COPY ERROR-DEFS.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SUPPRESS-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-VALUE  PIC 9(4) VALUE 100.

PROCEDURE DIVISION.
    DISPLAY 'Suppress demo: ' WS-VALUE.
    STOP RUN.
```

## Related Errors

- [COBOL Copy Error](../cobol-copy-error-new)
- [COBOL Compiler Directive Error](../cobol-compiler-directive)
- [COBOL Copybook Error](../cobol-copybook-error)
