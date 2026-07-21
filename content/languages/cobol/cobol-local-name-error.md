---
title: "[Solution] COBOL LOCAL Storage Error"
description: "Fix COBOL LOCAL storage errors in nested programs when variables conflict between parent and child programs."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

LOCAL storage errors occur in nested programs when variable names conflict or LOCAL storage sections are misconfigured.

## Common Causes

- Same variable name used in parent and child programs without GLOBAL
- LOCAL storage section missing for nested program
- LOCAL-STORAGE SECTION placed after DATA DIVISION items
- Reinitializing LOCAL variables unexpectedly

## How to Fix

### 1. Use distinct names or GLOBAL/LOCAL

```cobol
PROGRAM-ID. PARENT-PROG.
WORKING-STORAGE SECTION.
01 WS-COUNT PIC 9(4) VALUE 0.

PROGRAM-ID. CHILD-PROG.
LOCAL-STORAGE SECTION.
01 WS-COUNT PIC 9(4) VALUE 0.
*> This is distinct from parent's WS-COUNT
```

### 2. Use GLOBAL when sharing is needed

```cobol
PROGRAM-ID. PARENT.
WORKING-STORAGE SECTION.
01 WS-SHARED PIC X(10) GLOBAL.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. LOCAL-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-VALUE  PIC 9(4) VALUE 100.

PROCEDURE DIVISION.
    DISPLAY 'Parent value: ' WS-VALUE.
    STOP RUN.
```

## Related Errors

- [COBOL Nested Programs Error](../cobol-nested-programs)
- [COBOL Global Clause Error](../cobol-global-clause-error)
- [COBOL Working Storage Error](../cobol-working-storage)
