---
title: "[Solution] COBOL ACCEPT FROM DATE — Date Handling"
description: "Fix COBOL ACCEPT FROM DATE errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1117
---

ACCEPT FROM DATE gets the current date in YYYYDDD (year + day-of-year) format. Errors involve wrong PIC format or misunderstanding the returned format.

## Common Causes

- Using PIC X(8) instead of PIC 9(7) for date
- Confusing YYYYDDD with YYYYMMDD format
- Date not available from the system (embedded systems)
- Century window issues with 2-digit year formats

## How to Fix

### 1. Use correct PIC for YYYYDDD

```cobol
01 WS-DATE         PIC 9(7).
ACCEPT WS-DATE FROM DATE.
*> WS-DATE contains YYYYDDD (e.g., 2026001 for Jan 1, 2026)
```

### 2. Extract year and day

```cobol
01 WS-DATE         PIC 9(7).
01 WS-YEAR         PIC 9(4).
01 WS-DAY          PIC 9(3).

ACCEPT WS-DATE FROM DATE.
MOVE WS-DATE(1:4) TO WS-YEAR.
MOVE WS-DATE(5:3) TO WS-DAY.
```

### 3. Use DATE YYYYMMDD for full date (COBOL 2002+)

```cobol
01 WS-FULL-DATE    PIC 9(8).
ACCEPT WS-FULL-DATE FROM DATE YYYYMMDD.
```

### 4. Use DAY for day-of-week

```cobol
01 WS-DAY-OF-WEEK  PIC 9(1).
ACCEPT WS-DAY-OF-WEEK FROM DAY.
```

### 5. Use TIME for current time

```cobol
01 WS-TIME         PIC 9(8).
ACCEPT WS-TIME FROM TIME.
*> WS-TIME contains HHMMSSHH (hour, minute, second, hundredths)
```

## Examples

Complete date/time usage:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. DATE-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-DATE         PIC 9(7).
01 WS-YEAR         PIC 9(4).
01 WS-DAY          PIC 9(3).
01 WS-TIME         PIC 9(8).
01 WS-HOURS        PIC 9(2).
01 WS-MINUTES      PIC 9(2).
01 WS-SECONDS      PIC 9(2).

PROCEDURE DIVISION.
    ACCEPT WS-DATE FROM DATE.
    MOVE WS-DATE(1:4) TO WS-YEAR.
    MOVE WS-DATE(5:3) TO WS-DAY.
    DISPLAY 'Year: ' WS-YEAR ' Day: ' WS-DAY.

    ACCEPT WS-TIME FROM TIME.
    MOVE WS-TIME(1:2) TO WS-HOURS.
    MOVE WS-TIME(3:2) TO WS-MINUTES.
    MOVE WS-TIME(5:2) TO WS-SECONDS.
    DISPLAY 'Time: ' WS-HOURS ':' WS-MINUTES ':' WS-SECONDS.
    STOP RUN.
```

## Related Errors

- [COBOL ACCEPT FROM TIME Error](../cobol-accept-from-time)
- [COBOL PIC Clause Error](../cobol-pic-clause)
- [COBOL Data Movement Error](../cobol-data-movement-error)
