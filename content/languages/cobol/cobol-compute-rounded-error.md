---
title: "[Solution] COBOL COMPUTE ROUNDED Error"
description: "Fix COBOL COMPUTE ROUNDED errors when rounding results do not match expected precision."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

COMPUTE ROUNDED errors occur when the ROUNDED phrase is missing or when rounding behavior differs from expected decimal precision.

## Common Causes

- Missing ROUNDED in COMPUTE causing truncation
- Target PIC clause has fewer decimal places than result
- Rounding mode not matching business requirements
- Mixed integer and decimal precision in expression

## How to Fix

### 1. Add ROUNDED when precision matters

```cobol
*> WRONG: Truncation
COMPUTE WS-RESULT = WS-A / WS-B.
*> WS-RESULT may lose decimal places

*> CORRECT: Round properly
COMPUTE WS-RESULT ROUNDED = WS-A / WS-B.
```

### 2. Ensure target has enough decimal places

```cobol
*> WRONG: Target too short
01 WS-RESULT     PIC 9(5).
COMPUTE WS-RESULT ROUNDED = 123.456 + 789.012.

*> CORRECT: Enough decimal places
01 WS-RESULT     PIC 9(5)V999.
COMPUTE WS-RESULT ROUNDED = 123.456 + 789.012.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. ROUNDED-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-NUMERATOR   PIC 9(5)V99 VALUE 100.00.
01 WS-DENOMINATOR PIC 9(3)    VALUE 3.
01 WS-RESULT      PIC 9(5)V999.

PROCEDURE DIVISION.
    COMPUTE WS-RESULT ROUNDED = WS-NUMERATOR / WS-DENOMINATOR.
    DISPLAY 'Result: ' WS-RESULT.
    STOP RUN.
```

## Related Errors

- [COBOL Compute Error](../cobol-compute-error)
- [COBOL Decimal Error](../cobol-decimal-error)
- [COBOL COMP3 Error](../cobol-comp3-packed-error)
