---
title: "[Solution] COBOL Nested Programs — Program Containment"
description: "Fix COBOL nested program errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1125
---

Nested programs allow subprograms within a main program. Errors involve missing END PROGRAM markers, wrong scope for shared data, or calling nested programs incorrectly.

## Common Causes

- Missing END PROGRAM for the nested program
- Nested program does not share parent's WORKING-STORAGE
- Calling a nested program from outside the parent (unsupported)
- Overlapping names between parent and nested program

## How to Fix

### 1. Use proper nesting syntax

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. MAIN.

PROCEDURE DIVISION.
    CALL 'NESTED'.
    STOP RUN.

IDENTIFICATION DIVISION.
PROGRAM-ID. NESTED.

PROCEDURE DIVISION.
    DISPLAY 'Nested'.
    GOBACK.

END PROGRAM NESTED.
END PROGRAM MAIN.
```

### 2. Use COMMON for shared data

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. PARENT.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-SHARED       PIC X(10) COMMON.
01  WS-LOCAL        PIC X(10) LOCAL.
```

### 3. End each nested program

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. CHILD.
PROCEDURE DIVISION.
    DISPLAY 'Child'.
    GOBACK.
END PROGRAM CHILD.
```

### 4. Call nested programs with CALL

```cobol
CALL 'NESTED-PROG'.
```

### 5. Keep END PROGRAM order matching

```cobol
PROGRAM-ID. OUTER.
  PROGRAM-ID. INNER.
  END PROGRAM INNER.
END PROGRAM OUTER.
```

## Examples

A nested program structure:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. MAIN-PROG.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-MAIN-DATA    PIC X(20) VALUE 'MAIN DATA'.

PROCEDURE DIVISION.
    DISPLAY WS-MAIN-DATA
    CALL 'SUB-PROG'
    STOP RUN.

IDENTIFICATION DIVISION.
PROGRAM-ID. SUB-PROG.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-SUB-DATA     PIC X(20) VALUE 'SUB DATA'.

PROCEDURE DIVISION.
    DISPLAY WS-SUB-DATA
    GOBACK.

END PROGRAM SUB-PROG.
END PROGRAM MAIN-PROG.
```

## Related Errors

- [COBOL CALL Statement](../cobol-call-statement)
- [COBOL GO BACK Error](../cobol-go-back)
- [COBOL STOP RUN Error](../cobol-stop-run)
