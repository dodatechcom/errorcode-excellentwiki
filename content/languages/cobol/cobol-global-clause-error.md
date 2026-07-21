---
title: "[Solution] COBOL GLOBAL Clause Error"
description: "Fix COBOL GLOBAL clause errors when used on FD entries or variable declarations in nested programs."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

GLOBAL clause errors occur when the GLOBAL keyword is used inappropriately on FD entries or variables that cannot be shared across nested programs.

## Common Causes

- Using GLOBAL on non-FD entries
- GLOBAL variables not declared in the parent program
- Conflicting GLOBAL and LOCAL declarations
- Using GLOBAL on REDEFINES items

## How to Fix

### 1. Apply GLOBAL only to valid items

```cobol
*> WRONG: GLOBAL on WORKING-STORAGE
WORKING-STORAGE SECTION.
GLOBAL 01 WS-ERROR PIC X(1).

*> CORRECT: GLOBAL on FD in parent program
FD  SHARED-FILE
    GLOBAL
    LABEL RECORDS ARE STANDARD.
```

### 2. Ensure parent declares GLOBAL items

```cobol
PROGRAM-ID. PARENT-PROG.
DATA DIVISION.
FILE SECTION.
FD  SHARED-FILE GLOBAL.
01  SHARED-RECORD PIC X(80).

PROCEDURE DIVISION.
    CALL 'CHILD-PROG'.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. GLOBAL-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-FLAG  PIC X VALUE 'N'.

PROCEDURE DIVISION.
    DISPLAY 'Global clause demo'.
    STOP RUN.
```

## Related Errors

- [COBOL Nested Programs Error](../cobol-nested-programs)
- [COBOL Linkage Section Error](../cobol-linkage-section)
- [COBOL Working Storage Error](../cobol-working-storage)
