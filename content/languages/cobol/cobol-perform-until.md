---
title: "[Solution] COBOL PERFORM UNTIL — Conditional Loop"
description: "Fix COBOL PERFORM UNTIL errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1100
---

PERFORM UNTIL loops until a condition is true. Errors involve the condition being true from the start (loop never executes), or the condition never becoming true (infinite loop).

## Common Causes

- Condition is already true when PERFORM UNTIL is reached
- Loop body does not change the condition variable
- Wrong logical operator (AND vs OR in the condition)
- Using = instead of NOT = for the termination check

## How to Fix

### 1. Check that the condition can become true

```cobol
MOVE 0 TO WS-COUNT.
PERFORM UNTIL WS-COUNT >= 10
    ADD 1 TO WS-COUNT
END-PERFORM
```

### 2. Ensure the loop variable changes

```cobol
PERFORM UNTIL WS-EOF = 'Y'
    READ FILE-NAME
        AT END MOVE 'Y' TO WS-EOF
        NOT AT END
            PROCESS THE RECORD
    END-READ
END-PERFORM
```

### 3. Use correct comparison operators

```cobol
PERFORM UNTIL WS-VALUE = 0
    COMPUTE WS-VALUE = WS-VALUE - 1
END-PERFORM
```

### 4. Test with a small case first

```cobol
MOVE 0 TO WS-COUNT.
PERFORM UNTIL WS-COUNT > 5
    ADD 1 TO WS-COUNT
    DISPLAY WS-COUNT
END-PERFORM
```

### 5. Use PERFORM ... WITH TEST AFTER for do-while behavior

```cobol
PERFORM WITH TEST AFTER
    UNTIL WS-VALUE = 0
    COMPUTE WS-VALUE = WS-VALUE - 1
END-PERFORM
```

## Examples

File reading loop:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. UNTIL-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-EOF         PIC X(1) VALUE 'N'.
01  WS-COUNT       PIC 9(5) VALUE 0.

PROCEDURE DIVISION.
    OPEN INPUT DATA-FILE
    PERFORM UNTIL WS-EOF = 'Y'
        READ DATA-FILE
            AT END
                MOVE 'Y' TO WS-EOF
            NOT AT END
                ADD 1 TO WS-COUNT
        END-READ
    END-PERFORM
    CLOSE DATA-FILE
    DISPLAY 'Records read: ' WS-COUNT
    STOP RUN.
```

## Related Errors

- [COBOL PERFORM VARYING Error](../cobol-perform-varying)
- [COBOL PERFORM THRU Error](../cobol-perform-thru)
- [COBOL PERFORM Error](../cobol-perform-error)
