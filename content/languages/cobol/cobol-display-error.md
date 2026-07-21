---
title: "[Solution] COBOL DISPLAY Error"
description: "Fix COBOL DISPLAY errors including unsupported output targets and incorrect USING clause usage."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

DISPLAY errors occur when the DISPLAY verb is used with unsupported output targets or incorrect UPON/USING clauses.

## Common Causes

- DISPLAY UPON SYSPRINT on unsupported compilers
- DISPLAY with too many items exceeding buffer
- Missing DELIMITED SIZE on string items
- DISPLAY in a PROGRAM-USING subprogram

## How to Fix

### 1. Use standard DISPLAY syntax

```cobol
*> WRONG: Invalid UPON target
DISPLAY 'Hello' UPON INVALID-DEVICE.

*> CORRECT: Use standard output
DISPLAY 'Hello'.
```

### 2. Limit display buffer size

```cobol
*> WRONG: Oversized display
DISPLAY WS-HUGE-RECORD-1000-BYTES.

*> CORRECT: Display portions
DISPLAY WS-RECORD(1:80).
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. DISPLAY-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-MESSAGE   PIC X(50) VALUE 'Error code: '.
01 WS-CODE      PIC 9(4) VALUE 4012.
01 WS-OUTPUT    PIC X(60).

PROCEDURE DIVISION.
    STRING WS-MESSAGE DELIMITED BY SIZE
           WS-CODE DELIMITED BY SIZE
           INTO WS-OUTPUT.
    DISPLAY WS-OUTPUT.
    STOP RUN.
```

## Related Errors

- [COBOL Display Upon Error](../cobol-display-upon)
- [COBOL String Error](../cobol-string-error)
- [COBOL Procedure Division Error](../cobol-procedure-division-using)
