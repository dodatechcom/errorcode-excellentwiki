---
title: "[Solution] COBOL COMP/COMP-3 — Binary and Packed Decimal"
description: "Fix COBOL COMP and COMP-3 errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1082
---

COMP (binary) and COMP-3 (packed decimal) specify how data is stored. Errors involve display fields used in arithmetic expecting COMP fields, or wrong COMP type for the target system.

## Common Causes

- Using a COMP field with DISPLAY I/O without conversion
- Wrong byte size for COMP (varies by compiler)
- Arithmetic overflow in COMP fields
- COMP-3 with odd number of digits causing storage issues

## How to Fix

### 1. Use COMP for binary arithmetic

```cobol
01 WS-BINARY    PIC 9(5) COMP.   *> 2 or 4 bytes depending on compiler
01 WS-PACKED    PIC 9(7) COMP-3. *> 4 bytes (7 digits)
```

### 2. Convert between COMP and DISPLAY

```cobol
MOVE WS-COMP-FIELD TO WS-DISPLAY-FIELD.
COMPUTE WS-DISPLAY-FIELD = WS-COMP-FIELD.
```

### 3. Check storage size

```cobol
01 WS-COMP1     PIC 9(4) COMP.    *> typically 2 bytes
01 WS-COMP2     PIC 9(9) COMP.    *> typically 4 bytes
01 WS-COMP3     PIC 9(5) COMP-3.  *> 3 bytes (ceil(5/2))
```

### 4. Use REDEFINES to inspect COMP storage

```cobol
01 WS-PACKED    PIC 9(5) COMP-3.
01 WS-REDEF     REDEFINES WS-PACKED PIC X(3).
```

### 5. Test for COMP-3 sign encoding

```cobol
01 WS-SIGNED    PIC S9(5) COMP-3.
MOVE -12345 TO WS-SIGNED.
*> The sign is encoded in the last nibble
```

## Examples

Arithmetic with COMP fields:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. COMP-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-A         PIC 9(5) COMP     VALUE 1000.
01 WS-B         PIC 9(5) COMP     VALUE 2000.
01 WS-RESULT    PIC 9(9) COMP     VALUE 0.
01 WS-PACKED    PIC 9(7) COMP-3   VALUE 0.

PROCEDURE DIVISION.
    COMPUTE WS-RESULT = WS-A + WS-B.
    DISPLAY 'Result: ' WS-RESULT.
    MOVE WS-RESULT TO WS-PACKED.
    DISPLAY 'Packed: ' WS-PACKED.
    STOP RUN.
```

## Related Errors

- [COBOL PIC Clause Error](../cobol-pic-clause)
- [COBOL Decimal Error](../cobol-decimal-error)
- [COBOL Overflow Error](../cobol-overflow)
