---
title: "[Solution] COBOL INITIALIZE Error"
description: "Fix COBOL INITIALIZE errors when resetting data items to default values across different data types."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

INITIALIZE errors occur when the INITIALIZE statement is used on data items with incompatible types or when it clears fields that should retain values.

## Common Causes

- Using INITIALIZE on group items containing COMP-3 fields
- INITIALIZE clearing essential configuration data
- Unexpected behavior with FILLER items
- Forgetting INITIALIZE replaces with spaces, not zeros

## How to Fix

### 1. Be explicit about what to initialize

```cobol
*> WRONG: Initializes everything including config
01 WS-CONFIG.
    05 WS-TIMEOUT  PIC 9(4) VALUE 30.
    05 WS-RETRIES  PIC 9(2) VALUE 3.
INITIALIZE WS-CONFIG.
*> Both reset to spaces/zeros

*> CORRECT: Move specific values
MOVE 0 TO WS-TIMEOUT.
MOVE 0 TO WS-RETRIES.
```

### 2. Use REPLACING with INITIALIZE

```cobol
INITIALIZE WS-DATA REPLACING NUMERIC DATA BY 0
    ALPHANUMIC DATA BY SPACES.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. INITIALIZE-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-RECORD.
    05 WS-ID     PIC 9(6).
    05 WS-NAME   PIC X(20).
    05 WS-AMOUNT PIC S9(7)V99 COMP-3.

PROCEDURE DIVISION.
    MOVE 123456 TO WS-ID.
    MOVE 'TEST' TO WS-NAME.
    INITIALIZE WS-RECORD.
    DISPLAY 'ID after init: ' WS-ID.
    STOP RUN.
```

## Related Errors

- [COBOL Working Storage Error](../cobol-working-storage)
- [COBOL Data Movement Error](../cobol-data-movement-error)
- [COBOL COMP3 Error](../cobol-comp3-packed-error)
