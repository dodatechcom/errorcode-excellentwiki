---
title: "[Solution] COBOL STRING — String Concatenation"
description: "Fix COBOL STRING statement errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1104
---

STRING concatenates fields into a target variable. Errors involve wrong delimiter, insufficient target size, or missing DELIMITED BY clause.

## Common Causes

- Target field too small for concatenated result
- Missing DELIMITED BY clause
- DELIMITED BY SIZE vs DELIMITED BY SPACE mismatch
- Pointer overflow in STRING with POINTER

## How to Fix

### 1. Ensure target is large enough

```cobol
01 WS-FIRST   PIC X(10) VALUE 'JOHN'.
01 WS-LAST    PIC X(10) VALUE 'DOE'.
01 WS-FULL    PIC X(25).

STRING WS-FIRST DELIMITED BY SPACE
       ' '
       WS-LAST DELIMITED BY SPACE
       INTO WS-FULL
```

### 2. Use DELIMITED BY SIZE to keep trailing spaces

```cobol
STRING WS-NAME DELIMITED BY SIZE INTO WS-TARGET.
```

### 3. Use DELIMITED BY SPACE to trim

```cobol
STRING WS-FIRST DELIMITED BY SPACE
       ' '
       WS-LAST DELIMITED BY SPACE
       INTO WS-FULL
       WITH POINTER WS-PTR
```

### 4. Use POINTER for incremental concatenation

```cobol
MOVE 1 TO WS-PTR.
STRING WS-A DELIMITED BY SIZE
       INTO WS-RESULT
       WITH POINTER WS-PTR.
STRING WS-B DELIMITED BY SIZE
       INTO WS-RESULT
       WITH POINTER WS-PTR.
```

### 5. Check TALLYING for characters written

```cobol
STRING WS-A DELIMITED BY SPACE INTO WS-RESULT
       TALLYING WS-COUNT.
```

## Examples

A complete STRING example:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. STRING-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-FIRST    PIC X(15) VALUE 'HELLO'.
01 WS-LAST     PIC X(15) VALUE 'WORLD'.
01 WS-RESULT   PIC X(50).
01 WS-PTR      PIC 9(3) COMP VALUE 1.

PROCEDURE DIVISION.
    STRING WS-FIRST DELIMITED BY SPACE
           ', '
           WS-LAST DELIMITED BY SPACE
           '!'
           INTO WS-RESULT
           WITH POINTER WS-PTR.
    DISPLAY 'Result: ' WS-RESULT(1:WS-PTR - 1).
    STOP RUN.
```

## Related Errors

- [COBOL UNSTRING Error](../cobol-unstring)
- [COBOL INSPECT TALLYING Error](../cobol-inspect-tallying)
- [COBOL Data Movement Error](../cobol-data-movement-error)
