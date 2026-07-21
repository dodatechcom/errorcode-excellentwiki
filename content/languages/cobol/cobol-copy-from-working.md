---
title: "[Solution] COBOL COPY FROM WORKING Error"
description: "Fix COBOL COPY FROM errors when importing structures from one section to another."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

COPY FROM errors occur when the COPY ... FROM statement references invalid source sections or when the imported structure conflicts with existing declarations.

## Common Causes

- COPY FROM referencing nonexistent SECTION
- Naming conflicts with existing declarations
- COPY FROM used on items with incompatible levels
- Missing copy library path for FROM source

## How to Fix

### 1. Verify source exists

```cobol
*> WRONG: Source not defined
COPY WS-RECORD FROM WORKING-STORAGE.

*> CORRECT: Reference valid copybook
COPY CUSTOMER-REC FROM COPYLIB.
```

### 2. Avoid naming conflicts

```cobol
COPY ERROR-RECORD.
*> If 'ERROR-RECORD' conflicts with existing item, rename the copy
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. COPY-FROM-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-DATA  PIC X(50) VALUE 'Copy from demo'.

PROCEDURE DIVISION.
    DISPLAY WS-DATA.
    STOP RUN.
```

## Related Errors

- [COBOL Copy Error](../cobol-copy-error-new)
- [COBOL Copybook Error](../cobol-copybook-error)
- [COBOL Compiler Directive Error](../cobol-compiler-directive)
