---
title: "[Solution] COBOL Alphanumeric MOVE Error"
description: "Fix COBOL alphanumeric MOVE errors when transferring data between PIC X fields of different lengths."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

An alphanumeric MOVE error occurs when moving data between PIC X fields of incompatible sizes, resulting in truncation or unexpected padding.

## Common Causes

- Moving a longer PIC X field into a shorter one (truncation)
- Unexpected space padding on shorter targets
- Moving numeric data to alphanumeric fields without conversion
- Mixing PIC X and PIC 9 without proper conversion clauses

## How to Fix

### 1. Ensure target field is large enough

```cobol
*> WRONG: Target too short
01 WS-SOURCE     PIC X(20) VALUE 'HELLO WORLD'.
01 WS-TARGET     PIC X(5).
MOVE WS-SOURCE TO WS-TARGET.
*> WS-TARGET contains 'HELLO' -- truncation

*> CORRECT: Match sizes
01 WS-SOURCE     PIC X(20) VALUE 'HELLO WORLD'.
01 WS-TARGET     PIC X(20).
MOVE WS-SOURCE TO WS-TARGET.
```

### 2. Use STRING for controlled concatenation

```cobol
*> WRONG: Multiple moves cause confusion
MOVE WS-FIRST TO WS-FULL.
MOVE WS-SECOND TO WS-FULL.

*> CORRECT: Use STRING
STRING WS-FIRST DELIMITED BY SPACE
       ' ' DELIMITED BY SIZE
       WS-SECOND DELIMITED BY SPACE
       INTO WS-FULL.
```

### 3. Use UNSTRING for splitting

```cobol
UNSTRING WS-FULL-NAME
    DELIMITED BY ','
    INTO WS-LAST-NAME
         WS-FIRST-NAME.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. ALPHANUMERIC-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-SOURCE     PIC X(30) VALUE 'ERRORCODE123'.
01 WS-TARGET     PIC X(10).
01 WS-RESULT     PIC X(30).

PROCEDURE DIVISION.
    MOVE WS-SOURCE TO WS-TARGET.
    DISPLAY 'Truncated: ' WS-TARGET.

    STRING 'CODE:' DELIMITED BY SIZE
           WS-SOURCE(10:5) DELIMITED BY SIZE
           INTO WS-RESULT.
    DISPLAY 'Result: ' WS-RESULT.
    STOP RUN.
```

## Related Errors

- [COBOL Data Movement Error](../cobol-data-movement-error)
- [COBOL PIC Clause Error](../cobol-pic-clause)
- [COBOL String Error](../cobol-string-error)
