---
title: "[Solution] COBOL ACCEPT FROM TIME — Time Retrieval"
description: "Fix COBOL ACCEPT FROM TIME errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1118
---

ACCEPT FROM TIME returns the current time as HHMMSSHH. Errors involve wrong PIC format, or not handling the two-digit hundredths correctly.

## Common Causes

- Wrong PIC size (needs PIC 9(8) for full time)
- Confusing HHMMSS with HHMMSSHH format
- Not extracting individual time components
- Time zone issues on some systems

## How to Fix

### 1. Use PIC 9(8) for time

```cobol
01 WS-TIME         PIC 9(8).
ACCEPT WS-TIME FROM TIME.
*> Format: HHMMSSHH
```

### 2. Extract individual components

```cobol
01 WS-TIME         PIC 9(8).
01 WS-HH           PIC 9(2).
01 WS-MM           PIC 9(2).
01 WS-SS           PIC 9(2).
01 WS-HH2          PIC 9(2).

ACCEPT WS-TIME FROM TIME.
MOVE WS-TIME(1:2) TO WS-HH.
MOVE WS-TIME(3:2) TO WS-MM.
MOVE WS-TIME(5:2) TO WS-SS.
MOVE WS-TIME(7:2) TO WS-HH2.
```

### 3. Format for display

```cobol
DISPLAY WS-HH ':' WS-MM ':' WS-SS '.' WS-HH2.
```

### 4. Use CURRENT-DATE for full timestamp (COBOL 2002+)

```cobol
01 WS-TIMESTAMP    PIC X(21).
ACCEPT WS-TIMESTAMP FROM CURRENT-DATE.
```

### 5. Calculate elapsed time

```cobol
01 WS-START-TIME   PIC 9(8).
01 WS-END-TIME     PIC 9(8).
01 WS-ELAPSED      PIC 9(8).

ACCEPT WS-START-TIME FROM TIME.
*> ... do work ...
ACCEPT WS-END-TIME FROM TIME.
COMPUTE WS-ELAPSED = WS-END-TIME - WS-START-TIME.
```

## Examples

Timing a operation:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. TIME-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-START        PIC 9(8).
01 WS-END          PIC 9(8).
01 WS-ELAPSED      PIC 9(8).

PROCEDURE DIVISION.
    ACCEPT WS-START FROM TIME
    PERFORM SLOW-OPERATION
    ACCEPT WS-END FROM TIME
    COMPUTE WS-ELAPSED = WS-END - WS-START
    DISPLAY 'Elapsed: ' WS-ELAPSED ' centiseconds'
    STOP RUN.
```

## Related Errors

- [COBOL ACCEPT FROM DATE Error](../cobol-accept-from-date)
- [COBOL DISPLAY UPON Error](../cobol-display-upon)
- [COBOL PIC Clause Error](../cobol-pic-clause)
