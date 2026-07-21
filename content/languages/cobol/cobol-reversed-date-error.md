---
title: "[Solution] COBOL REVERSED-DATE Error"
description: "Fix COBOL reversed date format errors when converting between YYYYMMDD, MMDDYYYY, and DDMMYYYY formats."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

Reversed date format errors occur when date fields are interpreted in the wrong order, causing incorrect date calculations or invalid calendar operations.

## Common Causes

- Confusing MMDDYYYY with DDMMYYYY order
- Using DATE YYYYMMDD when system returns YYYYDDD
- Month and day swapped in date comparison
- Date arithmetic across month boundaries

## How to Fix

### 1. Document date format explicitly

```cobol
*> WRONG: Assumed format
01 WS-DATE     PIC 9(8).
ACCEPT WS-DATE FROM DATE YYYYMMDD.
*> Is it YYYYMMDD or DDMMYYYY?

*> CORRECT: Match your system locale
01 WS-DATE-YYYYMMDD  PIC 9(8).
ACCEPT WS-DATE-YYYYMMDD FROM DATE YYYYMMDD.
```

### 2. Extract components correctly

```cobol
01 WS-DATE     PIC 9(8).
ACCEPT WS-DATE FROM DATE YYYYMMDD.
01 WS-YEAR     REDEFINES WS-DATE PIC 9(4).
01 WS-MONTH    REDEFINES WS-DATE PIC 9(2).
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. DATE-FORMAT-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-FULL-DATE  PIC 9(8).
01 WS-YEAR       PIC 9(4).
01 WS-MONTH      PIC 9(2).
01 WS-DAY        PIC 9(2).

PROCEDURE DIVISION.
    ACCEPT WS-FULL-DATE FROM DATE YYYYMMDD.
    MOVE WS-FULL-DATE(1:4) TO WS-YEAR.
    MOVE WS-FULL-DATE(5:2) TO WS-MONTH.
    MOVE WS-FULL-DATE(7:2) TO WS-DAY.
    DISPLAY 'Date: ' WS-YEAR '/' WS-MONTH '/' WS-DAY.
    STOP RUN.
```

## Related Errors

- [COBOL Accept From Date Error](../cobol-accept-from-date)
- [COBOL Compute Error](../cobol-compute-error)
- [COBOL PIC Clause Error](../cobol-pic-clause)
