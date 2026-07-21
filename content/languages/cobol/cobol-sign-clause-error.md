---
title: "[Solution] COBOL SIGN Clause Error"
description: "Fix COBOL SIGN clause errors when specifying leading or trailing sign positions for signed numeric fields."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

SIGN clause errors occur when the sign representation for signed numeric fields is incorrectly specified, causing data to be read with wrong sign values.

## Common Causes

- SIGN LEADING vs SIGN TRAILING confusion
- SIGN SEPARATE used with compact formats
- Missing SIGN clause on signed COMP-3 fields
- Sign nibble corrupted by data movement

## How to Fix

### 1. Use explicit SIGN clause

```cobol
*> WRONG: Implicit sign may differ across systems
01 WS-AMOUNT     PIC S9(5)V99.

*> CORRECT: Explicit SIGN clause
01 WS-AMOUNT     PIC S9(5)V99 SIGN LEADING SEPARATE.
```

### 2. Match sign format to file layout

```cobol
*> For mainframe files
01 WS-FIELD       PIC S9(7) SIGN TRAILING.

*> For PC files
01 WS-FIELD       PIC S9(7) SIGN LEADING SEPARATE.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SIGN-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-POSITIVE   PIC S9(4) SIGN LEADING SEPARATE VALUE +123.
01 WS-NEGATIVE   PIC S9(4) SIGN LEADING SEPARATE VALUE -456.
01 WS-RESULT     PIC S9(5) SIGN LEADING.

PROCEDURE DIVISION.
    COMPUTE WS-RESULT = WS-POSITIVE + WS-NEGATIVE.
    DISPLAY 'Result: ' WS-RESULT.
    STOP RUN.
```

## Related Errors

- [COBOL COMP3 Error](../cobol-comp3-packed-error)
- [COBOL PIC Clause Error](../cobol-pic-clause)
- [COBOL Decimal Error](../cobol-decimal-error)
