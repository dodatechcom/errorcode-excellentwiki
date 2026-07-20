---
title: "[Solution] COBOL EVALUATE — Multi-Way Branch"
description: "Fix COBOL EVALUATE statement errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1097
---

EVALUATE is COBOL's switch/case construct. Errors involve mismatched WHEN conditions, missing END-EVALUATE, or using EVALUATE with incompatible data types.

## Common Causes

- WHEN conditions do not match the EVALUATE subject type
- Missing END-EVALUATE terminator
- WHEN OTHER is not the last WHEN clause
- Using EVALUATE with numeric and character subjects together

## How to Fix

### 1. Match WHEN to the subject type

```cobol
EVALUATE WS-STATUS
    WHEN 'A'
        DISPLAY 'Active'
    WHEN 'I'
        DISPLAY 'Inactive'
    WHEN OTHER
        DISPLAY 'Unknown'
END-EVALUATE
```

### 2. Use multiple conditions in one WHEN

```cobol
EVALUATE WS-GRADE
    WHEN 'A' WHEN 'B'
        DISPLAY 'Pass'
    WHEN 'F'
        DISPLAY 'Fail'
    WHEN OTHER
        DISPLAY 'Incomplete'
END-EVALUATE
```

### 3. Use TRUE/FALSE for boolean conditions

```cobol
EVALUATE TRUE
    WHEN WS-AGE >= 18
        DISPLAY 'Adult'
    WHEN WS-AGE >= 13
        DISPLAY 'Teen'
    WHEN OTHER
        DISPLAY 'Child'
END-EVALUATE
```

### 4. Use EVALUATE with ranges

```cobol
EVALUATE WS-SCORE ALSO WS-LEVEL
    WHEN 90 ALSO 1
        DISPLAY 'Excellent beginner'
    WHEN 90 ALSO 2
        DISPLAY 'Excellent intermediate'
    WHEN OTHER ALSO ANY
        DISPLAY 'Other'
END-EVALUATE
```

### 5. Always include END-EVALUATE

```cobol
EVALUATE WS-COMMAND
    WHEN 'ADD'
        DISPLAY 'Adding'
    WHEN 'DELETE'
        DISPLAY 'Deleting'
END-EVALUATE
```

## Examples

Complete EVALUATE usage:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. EVALUATE-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-MONTH       PIC 9(2) VALUE 6.
01  WS-SEASON      PIC X(10).

PROCEDURE DIVISION.
    EVALUATE WS-MONTH
        WHEN 12 WHEN 1 WHEN 2
            MOVE 'WINTER' TO WS-SEASON
        WHEN 3 WHEN 4 WHEN 5
            MOVE 'SPRING' TO WS-SEASON
        WHEN 6 WHEN 7 WHEN 8
            MOVE 'SUMMER' TO WS-SEASON
        WHEN OTHER
            MOVE 'FALL' TO WS-SEASON
    END-EVALUATE
    DISPLAY 'Season: ' WS-SEASON
    STOP RUN.
```

## Related Errors

- [COBOL PERFORM Error](../cobol-perform-error)
- [COBOL 88 Level Error](../cobol-level88)
- [COBOL SEARCH ALL Error](../cobol-search-all)
