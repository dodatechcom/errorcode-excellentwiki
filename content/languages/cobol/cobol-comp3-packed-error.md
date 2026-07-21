---
title: "[Solution] COBOL COMP-3 Packed Decimal Error"
description: "Fix COBOL COMP-3 packed decimal errors when numeric fields contain invalid bit patterns."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

A COMP-3 packed decimal error occurs when a packed decimal field contains an invalid hex nibble, causing arithmetic operations to fail at runtime.

## Common Causes

- Uninitialized COMP-3 fields used in arithmetic
- Data imported with incorrect packing
- Partial byte fields not aligned to even nibble boundaries
- Moving non-numeric data into COMP-3 fields

## How to Fix

### 1. Always initialize COMP-3 fields

```cobol
*> WRONG: Uninitialized COMP-3
01 WS-AMOUNT     PIC S9(7)V99 COMP-3.
ADD 100 TO WS-AMOUNT.
*> May trigger invalid decimal if WS-AMOUNT has garbage

*> CORRECT: Initialize
01 WS-AMOUNT     PIC S9(7)V99 COMP-3 VALUE 0.
ADD 100 TO WS-AMOUNT.
```

### 2. Validate before use

```cobol
IF FUNCTION NUMVAL(WS-COMP3-TEXT) NOT NUMERIC
    DISPLAY 'Invalid packed decimal data'
ELSE
    MOVE WS-COMP3-TEXT TO WS-OUTPUT.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. COMP3-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-TOTAL      PIC S9(9)V99 COMP-3 VALUE 0.
01 WS-ITEM-PRICE PIC S9(5)V99 COMP-3 VALUE 0.
01 WS-QTY        PIC 9(5) COMP-3 VALUE 0.

PROCEDURE DIVISION.
    MOVE 25.99 TO WS-ITEM-PRICE.
    MOVE 3 TO WS-QTY.
    COMPUTE WS-TOTAL = WS-ITEM-PRICE * WS-QTY.
    DISPLAY 'Total: ' WS-TOTAL.
    STOP RUN.
```

## Related Errors

- [COBOL COMP COMP3 Error](../cobol-comp-comp3)
- [COBOL Compute Error](../cobol-compute-error)
- [COBOL Decimal Error](../cobol-decimal-error)
