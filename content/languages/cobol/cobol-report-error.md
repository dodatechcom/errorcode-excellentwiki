---
title: "[Solution] COBOL REPORT Writer Error"
description: "Fix COBOL REPORT WRITER errors including invalid control fields, missing GROUP clauses, and page overflow issues."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

REPORT WRITER errors occur when REPORT SECTION definitions have invalid control breaks, missing DETAIL/GROUP sections, or incorrect page overflow handling.

## Common Causes

- Missing CONTROL clause in RD entry
- DETAIL line referenced but not defined
- Page overflow without adequate page size
- RESET FINAL on wrong control field

## How to Fix

### 1. Define complete report structure

```cobol
*> WRONG: Missing DETAIL section
RD  SALES-REPORT
    CONTROLS ARE FINAL
    PAGE SIZE 60 LINES.

*> CORRECT: Include all required sections
RD  SALES-REPORT
    CONTROLS ARE FINAL
    PAGE SIZE 60 LINES.
01  DETAIL-LINE TYPE DETAIL.
```

### 2. Use GENERATE correctly

```cobol
GENERATE SALES-DETAIL.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. REPORT-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-COUNT  PIC 9(4) VALUE 0.

PROCEDURE DIVISION.
    PERFORM 5 TIMES
        ADD 1 TO WS-COUNT
        DISPLAY 'Processing record ' WS-COUNT
    END-PERFORM.
    DISPLAY 'Report complete'.
    STOP RUN.
```

## Related Errors

- [COBOL Sort Error](../cobol-sort-error)
- [COBOL Record Error](../cobol-record-error)
- [COBOL Runtime Error](../cobol-runtime-error)
