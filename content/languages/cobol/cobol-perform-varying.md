---
title: "[Solution] COBOL PERFORM VARYING — Loop Control"
description: "Fix COBOL PERFORM VARYING errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1099
---

PERFORM VARYING loops through a range. Errors involve wrong BY value, infinite loops from wrong UNTIL condition, or modifying the loop variable inside the loop body.

## Common Causes

- Loop variable modified inside the loop body
- BY 0 causing an infinite loop
- UNTIL condition never becomes true
- Wrong initial value or direction (counting up when you should count down)

## How to Fix

### 1. Do not modify the loop variable inside the loop

```cobol
PERFORM VARYING WS-I FROM 1 BY 1 UNTIL WS-I > 10
    DISPLAY WS-I
    *> Do NOT modify WS-I here
END-PERFORM
```

### 2. Check BY value is not zero

```cobol
PERFORM VARYING WS-I FROM 1 BY 1 UNTIL WS-I > 100
    *> BY 0 would loop forever
END-PERFORM
```

### 3. Use correct comparison in UNTIL

```cobol
PERFORM VARYING WS-I FROM 1 BY 1 UNTIL WS-I > 10
    DISPLAY WS-I
END-PERFORM
```

### 4. Count backwards when needed

```cobol
PERFORM VARYING WS-I FROM 10 BY -1 UNTIL WS-I < 1
    DISPLAY WS-I
END-PERFORM
```

### 5. Use AFTER INITIALIZING / BEFORE TERMINATING (OOCobol)

```cobol
PERFORM VARYING WS-I FROM 1 BY 1
        AFTER INITIALIZING
        UNTIL WS-I > 10
        BEFORE TERMINATING
    DISPLAY WS-I
END-PERFORM
```

## Examples

A nested loop example:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. VARYING-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-I            PIC 9(3) COMP.
01  WS-J            PIC 9(3) COMP.
01  WS-PRODUCT     PIC 9(6) COMP.

PROCEDURE DIVISION.
    PERFORM VARYING WS-I FROM 1 BY 1 UNTIL WS-I > 5
        PERFORM VARYING WS-J FROM 1 BY 1 UNTIL WS-J > 5
            COMPUTE WS-PRODUCT = WS-I * WS-J
            DISPLAY WS-I ' * ' WS-J ' = ' WS-PRODUCT
        END-PERFORM
    END-PERFORM
    STOP RUN.
```

## Related Errors

- [COBOL PERFORM UNTIL Error](../cobol-perform-until)
- [COBOL PERFORM THRU Error](../cobol-perform-thru)
- [COBOL PERFORM Error](../cobol-perform-error)
