---
title: "[Solution] COBOL Condition Name Error"
description: "Fix COBOL condition name (LEVEL 88) errors including undefined values and incorrect usage in IF statements."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

Condition name errors occur when LEVEL 88 condition names are used incorrectly or when the parent field value does not match any defined condition.

## Common Causes

- Using condition names on the wrong parent field
- Setting a parent field value not covered by any 88-level
- Condition name values overlapping unexpectedly
- Forgetting to initialize the parent field before checking

## How to Fix

### 1. Define condition names with complete coverage

```cobol
*> WRONG: Missing common values
01 WS-STATUS     PIC X(1).
   88 WS-ACTIVE  VALUE 'A'.
   88 WS-CLOSED  VALUE 'C'.
   *> 'D' for deleted is not covered

*> CORRECT: Cover all expected values
01 WS-STATUS     PIC X(1).
   88 WS-ACTIVE  VALUE 'A'.
   88 WS-CLOSED  VALUE 'C'.
   88 WS-DELETED VALUE 'D'.
   88 WS-UNKNOWN VALUES ' ', LOW-VALUES.
```

### 2. Initialize before checking

```cobol
*> WRONG: Uninitialized check
01 WS-FLAG       PIC X.
IF WS-FLAG = 'Y'
    DISPLAY 'Yes'.

*> CORRECT: Use condition names
01 WS-FLAG       PIC X.
   88 WS-YES     VALUE 'Y'.
   88 WS-NO      VALUE 'N'.
MOVE 'N' TO WS-FLAG.
IF WS-YES
    DISPLAY 'Yes'.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. CONDITION-NAME-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ORDER-STATUS  PIC 9(1).
   88 WS-PENDING    VALUE 0.
   88 WS-PROCESSING VALUE 1.
   88 WS-COMPLETE   VALUE 2.
   88 WS-CANCELLED  VALUE 3.

PROCEDURE DIVISION.
    MOVE 1 TO WS-ORDER-STATUS.
    IF WS-PROCESSING
        DISPLAY 'Order is processing'.
    MOVE 9 TO WS-ORDER-STATUS.
    DISPLAY 'Status: ' WS-ORDER-STATUS.
    STOP RUN.
```

## Related Errors

- [COBOL Level88 Error](../cobol-level88)
- [COBOL Evaluate Error](../cobol-evaluate-error)
- [COBOL Undefined Variable](../cobol-undefined-variable)
