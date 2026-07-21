---
title: "[Solution] COBOL REDEFINES Level Error"
description: "Fix COBOL REDEFINES errors when redefining data items at incorrect levels or with incompatible sizes."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

REDEFINES level errors occur when the REDEFINES clause is placed at the wrong level or when the redefining item has a different size than the original.

## Common Causes

- REDEFINES used on level 01 in FILE SECTION (not allowed)
- Redefining item larger than original item
- REDEFINES placed after PIC clause (must come first)
- Multiple REDEFINES on same level

## How to Fix

### 1. Place REDEFINES correctly

```cobol
*> WRONG: REDEFINES after PIC
01 WS-RECORD.
    05 WS-NUM   PIC 9(4).
    05 WS-TEXT  PIC X(4) REDEFINES WS-NUM.
*> WRONG order

*> CORRECT
01 WS-RECORD.
    05 WS-NUM   PIC 9(4).
    05 WS-TEXT  REDEFINES WS-NUM PIC X(4).
```

### 2. Match sizes

```cobol
*> WRONG: Different sizes
01 WS-A  PIC 9(4).
01 WS-B  REDEFINES WS-A PIC 9(6).

*> CORRECT: Same size
01 WS-A  PIC 9(4).
01 WS-B  REDEFINES WS-A PIC X(4).
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. REDEFINES-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-COMP-DATA.
    05 WS-NUMERIC   PIC 9(4) VALUE 1234.
    05 WS-ALPHA     REDEFINES WS-NUMERIC PIC X(4).

PROCEDURE DIVISION.
    DISPLAY 'Numeric: ' WS-NUMERIC.
    DISPLAY 'Alpha: ' WS-ALPHA.
    STOP RUN.
```

## Related Errors

- [COBOL Redefines Error](../cobol-redefines)
- [COBOL PIC Clause Error](../cobol-pic-clause)
- [COBOL Data Name Error](../cobol-data-name-error)
