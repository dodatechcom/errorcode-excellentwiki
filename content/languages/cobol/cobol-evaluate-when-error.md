---
title: "[Solution] COBOL EVALUATE WHEN Error"
description: "Fix COBOL EVALUATE WHEN errors including missing END-EVALUATE and incorrect condition matching."
languages: ["cobol"]
error-types: ["syntax-error"]
severities: ["error"]
---

EVALUATE WHEN errors occur when the EVALUATE statement is missing its END-EVALUATE delimiter, WHEN conditions are malformed, or WHEN OTHER is misplaced.

## Common Causes

- Missing END-EVALUATE statement
- WHEN OTHER placed before regular WHEN clauses
- EVALUATE subject and WHEN conditions type mismatch
- Nested EVALUATE missing inner END-EVALUATE

## How to Fix

### 1. Always close with END-EVALUATE

```cobol
*> WRONG: Missing END-EVALUATE
EVALUATE WS-STATUS
    WHEN 'A' DISPLAY 'Active'
    WHEN 'C' DISPLAY 'Closed'.
*> ERROR

*> CORRECT
EVALUATE WS-STATUS
    WHEN 'A' DISPLAY 'Active'
    WHEN 'C' DISPLAY 'Closed'
END-EVALUATE.
```

### 2. Put WHEN OTHER last

```cobol
EVALUATE WS-STATUS
    WHEN OTHER DISPLAY 'Unknown'
    WHEN 'A' DISPLAY 'Active'
END-EVALUATE.
*> WRONG: WHEN OTHER should be last
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. EVALUATE-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-GRADE  PIC X(1) VALUE 'B'.

PROCEDURE DIVISION.
    EVALUATE WS-GRADE
        WHEN 'A' DISPLAY 'Excellent'
        WHEN 'B' DISPLAY 'Good'
        WHEN 'C' DISPLAY 'Average'
        WHEN OTHER DISPLAY 'Other'
    END-EVALUATE.
    STOP RUN.
```

## Related Errors

- [COBOL Evaluate Error](../cobol-evaluate-error)
- [COBOL Evaluate Custom Error](../cobol-evaluate-custom)
- [COBOL Syntax Error](../cobol-syntax-error-new)
