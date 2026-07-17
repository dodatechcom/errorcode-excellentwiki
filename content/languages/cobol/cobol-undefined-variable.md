---
title: "Undefined variable in COBOL"
description: "Undefined variable errors in COBOL occur when referencing a variable not declared in the Working-Storage or Linkage Section."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["undefined", "variable", "declaration", "working-storage", "cobol"]
weight: 5
---

## What This Error Means

COBOL requires all variables to be declared in the DATA DIVISION before use. An undefined variable causes a compile-time error or runtime ABEND if the variable name is wrong.

## Common Causes

- Typo in variable name
- Variable declared in different program section
- Missing WORKING-STORAGE declaration
- Variable used before declaration

## How to Fix

```cobol
       * WRONG: Variable not declared
       PROCEDURE DIVISION.
           MOVE 42 TO WS-UNDEFINED-VAR.
       * Compile error: undefined variable
```

```cobol
       * CORRECT: Declare in WORKING-STORAGE
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-UNDEFINED-VAR PIC 9(5) VALUE 0.
       PROCEDURE DIVISION.
           MOVE 42 TO WS-UNDEFINED-VAR.
```

```cobol
       * CORRECT: Check naming conventions
       01 WS-CUSTOMER-NAME PIC X(30).
       * Reference as WS-CUSTOMER-NAME, not WS-CUSTNAME
```

## Examples

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. UNDEF.
       PROCEDURE DIVISION.
           MOVE 'Hello' TO WS-MSG.
       * WS-MSG not declared - compile error
```

## Related Errors

- [Record Error](/languages/cobol/record-error) - record structure errors
- [Subscript Error](/languages/cobol/subscript-error) - index errors
