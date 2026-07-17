---
title: "Division by zero in COBOL"
description: "Division by zero in COBOL occurs when a DIVIDE statement has a divisor of zero, causing an S0C8 ABEND."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["division", "zero", "abend", "arithmetic", "cobol"]
weight: 5
---

## What This Error Means

COBOL division by zero causes an S0C8 (fixed-point divide exception) ABEND. The DIVIDE statement must have its divisor checked before execution.

## Common Causes

- Divisor variable not initialized
- Computed divisor resulting in zero
- User input resulting in zero divisor
- Missing ZERO-CHECK before DIVIDE

## How to Fix

```cobol
       * WRONG: No check before divide
       DIVIDE WS-A BY WS-B GIVING WS-C.
       * S0C8 ABEND if WS-B = 0
```

```cobol
       * CORRECT: Check divisor first
       IF WS-B NOT = 0
           DIVIDE WS-A BY WS-B GIVING WS-C
       ELSE
           DISPLAY 'Error: Division by zero'
           MOVE 0 TO WS-C
       END-IF.
```

```cobol
       * CORRECT: Use ON SIZE ERROR
       DIVIDE WS-A BY WS-B
           GIVING WS-C
           ON SIZE ERROR
               DISPLAY 'Division error'
               MOVE 0 TO WS-C
       END-DIVIDE.
```

## Examples

```cobol
       MOVE 100 TO WS-NUMERATOR.
       MOVE 0 TO WS-DENOMINATOR.
       DIVIDE WS-NUMERATOR BY WS-DENOMINATOR
           GIVING WS-QUOTIENT.
       * S0C8 ABEND: Division by zero
```

## Related Errors

- [Overflow](/languages/cobol/overflow-error2) - arithmetic overflow
- [Runtime Error](/languages/cobol/runtime-error) - general errors
