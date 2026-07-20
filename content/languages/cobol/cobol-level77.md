---
title: "[Solution] COBOL 77 Level — Independent Variables"
description: "Fix COBOL 77 level errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1087
---

Level 77 declares independent (non-group) variables. Errors involve using level 77 where level 01 is required, or misunderstanding that 77 items cannot be part of a group.

## Common Causes

- Using level 77 for fields that need to be part of a group structure
- Mix of level 77 and level 01 inappropriately
- Level 77 items cannot have subordinates (no level 02+ under 77)
- Confusing level 77 with level 01 (both are independent)

## How to Fix

### 1. Use 77 for standalone variables

```cobol
77 WS-COUNTER      PIC 9(5) COMP.
77 WS-TEMP-NAME    PIC X(30).
77 WS-RESULT       PIC 9(7)V99.
```

### 2. Use 01 for record-level fields

```cobol
01 WS-RECORD.
    05 WS-FIELD-1  PIC X(10).
    05 WS-FIELD-2  PIC 9(5).
```

### 3. Level 77 cannot have subordinates

```cobol
77 WS-VAR          PIC X(10).
*> 77 WS-SUB      PIC X(5).  *> WRONG: cannot subordinate under 77
```

### 4. Use 77 for file record counters

```cobol
77 WS-RECORD-COUNT PIC 9(6) COMP VALUE 0.
77 WS-EOF-FLAG     PIC X(1) VALUE 'N'.
    88 WS-EOF       VALUE 'Y'.
```

### 5. Modern style: prefer 01 for clarity

```cobol
*> Legacy
77 WS-X            PIC 9(5).

*> Modern (equivalent but clearer)
01 WS-X            PIC 9(5).
```

## Examples

Level 77 usage in a simple program:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. LEVEL77-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
77 WS-LOOP-COUNT   PIC 9(3) COMP.
77 WS-TOTAL        PIC 9(7)V99 COMP VALUE 0.
77 WS-INPUT        PIC X(20).
77 WS-EOF          PIC X(1) VALUE 'N'.
    88 WS-DONE     VALUE 'Y'.

PROCEDURE DIVISION.
    PERFORM VARYING WS-LOOP-COUNT FROM 1 BY 1
            UNTIL WS-LOOP-COUNT > 10
        COMPUTE WS-TOTAL = WS-TOTAL + WS-LOOP-COUNT
    END-PERFORM.
    DISPLAY 'Total: ' WS-TOTAL.
    STOP RUN.
```

## Related Errors

- [COBOL PIC Clause Error](../cobol-pic-clause)
- [COBOL 88 Level Error](../cobol-level88)
- [COBOL WORKING-STORAGE Error](../cobol-working-storage)
