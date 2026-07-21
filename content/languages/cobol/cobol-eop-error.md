---
title: "[Solution] COBOL EOP Error"
description: "Fix COBOL END-OF-PAGE errors when handling file end-of-page conditions during sequential writing."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

END-OF-PAGE errors occur when WRITE statements do not handle page overflow conditions properly or when AT END-OF-PAGE is missing.

## Common Causes

- WRITE without AT END-OF-PAGE for printer files
- Page size too small for record content
- Missing advance after reaching page bottom
- EOP condition ignored causing output loss

## How to Fix

### 1. Handle AT EOP in WRITE statements

```cobol
WRITE DETAIL-LINE
    AT END OF PAGE
        PERFORM NEW-PAGE.
```

### 2. Set appropriate page size

```cobol
RD  PRINT-REPORT
    PAGE SIZE 66 LINES
    FIRST DETAIL 7
    LAST DETAIL 60.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. EOP-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-COUNT  PIC 9(4) VALUE 0.

PROCEDURE DIVISION.
    PERFORM 10 TIMES
        ADD 1 TO WS-COUNT
        DISPLAY 'Line ' WS-COUNT
    END-PERFORM.
    STOP RUN.
```

## Related Errors

- [COBOL File Status Error](../cobol-file-status-error)
- [COBOL Write From Error](../cobol-write-from)
- [COBOL Runtime Error](../cobol-runtime-error)
