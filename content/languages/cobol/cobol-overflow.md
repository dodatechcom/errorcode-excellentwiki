---
title: "Overflow in COBOL"
description: "Overflow errors in COBOL occur when arithmetic results exceed the capacity of the receiving field."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["overflow", "arithmetic", "numeric", "size", "cobol"]
weight: 5
---

## What This Error Means

COBOL overflow errors occur when the result of an arithmetic operation doesn't fit in the destination field's size. The ON SIZE ERROR clause catches these situations.

## Common Causes

- Result field too small for computation
- Multiplication producing large results
- Addition causing carry overflow
- Missing SIZE ERROR handling

## How to Fix

```cobol
       * WRONG: No overflow check
       COMPUTE WS-SMALL = WS-LARGE * WS-BIG.
       * S0C8 if result exceeds PIC 9(5)
```

```cobol
       * CORRECT: Use ON SIZE ERROR
       COMPUTE WS-SMALL = WS-LARGE * WS-BIG
           ON SIZE ERROR
               DISPLAY 'Overflow: result too large'
               MOVE 0 TO WS-SMALL
       END-COMPUTE.
```

```cobol
       * CORRECT: Use larger receiving field
       01 WS-SMALL    PIC 9(5).
       01 WS-RESULT   PIC 9(10).
       COMPUTE WS-RESULT = WS-LARGE * WS-BIG.
```

## Examples

```cobol
       MOVE 99999 TO WS-A.
       MOVE 99999 TO WS-B.
       COMPUTE WS-C = WS-A * WS-B.
       * Overflow: 99999 * 99999 = 9999800001
       * doesn't fit in PIC 9(5)
```

## Related Errors

- [Division by Zero](/languages/cobol/division-error2) - arithmetic errors
- [Decimal Error](/languages/cobol/decimal-error) - precision errors
