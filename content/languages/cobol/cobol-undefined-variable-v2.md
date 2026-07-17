---
title: "[Solution] COBOL: undefined variable reference"
description: "Fix COBOL errors when variables are referenced before being defined or initialized."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["undefined", "variable", "declaration", "working-storage", "cobol"]
weight: 5
---

## What This Error Means

COBOL undefined variable errors occur when a variable is referenced without being properly declared in the DATA DIVISION or before being initialized.

## Common Causes

- Variable not in WORKING-STORAGE
- Variable name misspelled
- Variable declared after use
- MOVE before value assigned
- Missing DATA DIVISION section

## How to Fix

```cobol
       * WRONG: Variable not declared
       IDENTIFICATION DIVISION.
       PROGRAM-ID. UNDEF-VAR.
       PROCEDURE DIVISION.
           MOVE 'Hello' TO WS-GREETING.
           * WS-GREETING not declared
```

```cobol
       * CORRECT: Declare variables properly
       IDENTIFICATION DIVISION.
       PROGRAM-ID. DEFINED-VAR.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-GREETING PIC X(20).
       PROCEDURE DIVISION.
           MOVE 'Hello' TO WS-GREETING.
           DISPLAY WS-GREETING.
```

```cobol
       * CORRECT: Initialize before use
       IDENTIFICATION DIVISION.
       PROGRAM-ID. INIT-VAR.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-COUNTER PIC 9(5) VALUE 0.
       01 WS-NAME PIC A(20) VALUE SPACES.
       PROCEDURE DIVISION.
           ADD 1 TO WS-COUNTER
           MOVE 'John' TO WS-NAME
           DISPLAY WS-COUNTER ' ' WS-NAME.
```

```cobol
       * CORRECT: Check variable scope
       IDENTIFICATION DIVISION.
       PROGRAM-ID. VAR-SCOPE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-GLOBAL PIC X(20) VALUE 'Global'.
       PROCEDURE DIVISION.
           DISPLAY WS-GLOBAL
           PERFORM LOCAL-VARS
           DISPLAY WS-GLOBAL.
       LOCAL-VARS SECTION.
       LOCAL-VARS-RTN.
           DISPLAY WS-GLOBAL.
```

```cobol
       * CORRECT: Use COPY for common definitions
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       COPY 'COMMON.CPY'.
```

## Related Errors

- [Record Error](cobol-record-error-v2) - record errors
- [Index Error](cobol-index-error-v2) - subscript errors
- [Runtime Error](cobol-runtime-error-v2) - file status errors
