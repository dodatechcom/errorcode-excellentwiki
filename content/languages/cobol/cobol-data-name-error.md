---
title: "[Solution] COBOL Data Name Error"
description: "Fix COBOL data name errors caused by reserved word usage, invalid naming, or undeclared variables."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

Data name errors occur when variables use reserved words, contain invalid characters, or are referenced before being declared in the WORKING-STORAGE or LINKAGE SECTION.

## Common Causes

- Using COBOL reserved words as data names
- Data names exceeding 30 characters
- Referencing a variable not declared in any section
- Duplicate data names in nested programs

## How to Fix

### 1. Avoid reserved words

```cobol
*> WRONG: 'DATE' is reserved
01 DATE        PIC 9(8).

*> CORRECT: Use descriptive non-reserved name
01 WS-DATE     PIC 9(8).
```

### 2. Keep names under 30 characters

```cobol
*> WRONG: Too long
01 VERY-LONG-DATA-NAME-EXCEEDING-THIRTY-CHARS  PIC X(10).

*> CORRECT: Shorten the name
01 VL-DATA-NAME  PIC X(10).
```

### 3. Declare before use

```cobol
PROCEDURE DIVISION.
    MOVE 1 TO WS-UNDECLARED.
    *> WRONG: WS-UNDECLARED not declared in WORKING-STORAGE

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-UNDECLARED  PIC 9(4).
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. DATA-NAME-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-COUNTER    PIC 9(4) VALUE 0.
01 WS-MAX-VAL    PIC 9(4) VALUE 100.
01 WS-RESULT     PIC 9(8).

PROCEDURE DIVISION.
    PERFORM VARYING WS-COUNTER FROM 1 BY 1
        UNTIL WS-COUNTER > WS-MAX-VAL
        ADD WS-COUNTER TO WS-RESULT
    END-PERFORM.
    DISPLAY 'Sum: ' WS-RESULT.
    STOP RUN.
```

## Related Errors

- [COBOL Syntax Error](../cobol-syntax-error-new)
- [COBOL Undefined Variable](../cobol-undefined-variable)
- [COBOL Working Storage Error](../cobol-working-storage)
