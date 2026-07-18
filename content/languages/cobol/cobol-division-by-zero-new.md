---
title: "[Solution] COBOL: division by zero runtime error"
description: "Fix COBOL division by zero by validating divisors before DIVIDE and using ON SIZE ERROR."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A COBOL division by zero error occurs when a DIVIDE statement has a divisor of zero, causing an S0C8 (fixed-point divide exception) ABEND on mainframe systems. This is one of the most common runtime errors in COBOL and immediately terminates the program. The error can occur with integer, decimal, or packed decimal divisors. COBOL provides the ON SIZE ERROR clause to handle this condition gracefully, preventing the program abend.

## Why It Happens

Division by zero in COBOL occurs when divisor variables are not properly initialized or validated. A WORKING-STORAGE variable used as a divisor defaults to spaces or zeros depending on its definition, and if not MOVE'd a proper value, will be zero. Computed divisors from SUBTRACT or MULTIPLY operations may yield zero under certain conditions. User input that is not validated may contain zero or space values. Counting variables used as divisors may be zero before any records are processed. Conditional calculations that set a divisor under some conditions may leave it as zero in other paths. Packed decimal fields with all zero bytes also cause division by zero exceptions.

## How to Fix It

**Check divisor before dividing:**

```cobol
       DIVISION-BY-ZERO-CHECK.
           IF WS-DENOMINATOR NOT = 0
               DIVIDE WS-NUMERATOR BY WS-DENOMINATOR
                   GIVING WS-QUOTIENT
           ELSE
               DISPLAY 'Error: Division by zero'
               MOVE 0 TO WS-QUOTIENT
               ADD 1 TO WS-ERROR-COUNT
           END-IF.
```

**Use ON SIZE ERROR clause:**

```cobol
       SAFE-DIVIDE.
           DIVIDE WS-A BY WS-B
               GIVING WS-C
               ON SIZE ERROR
                   DISPLAY 'Division error or by zero'
                   DISPLAY 'WS-A=' WS-A ' WS-B=' WS-B
                   MOVE 0 TO WS-C
                   ADD 1 TO WS-ERROR-COUNT
           END-DIVIDE.
```

**Validate before COMPUTE statements:**

```cobol
       SAFE-COMPUTE.
           IF WS-DIVISOR NOT = 0
               COMPUTE WS-RESULT =
                   WS-NUMERATOR / WS-DIVISOR
           ELSE
               MOVE 0 TO WS-RESULT
           END-IF.

       *> Or using ON SIZE ERROR with COMPUTE
           COMPUTE WS-RESULT =
               WS-NUMERATOR / WS-DIVISOR
               ON SIZE ERROR
                   MOVE 0 TO WS-RESULT
               NOT ON SIZE ERROR
                   CONTINUE
           END-COMPUTE.
```

**Initialize divisor variables properly:**

```cobol
       WORKING-STORAGE SECTION.
       01  WS-NUMERATOR      PIC 9(7)V99 VALUE 100.
       01  WS-DENOMINATOR    PIC 9(7)V99 VALUE 0.
       01  WS-QUOTIENT       PIC 9(7)V99 VALUE 0.

       PROCEDURE DIVISION.
       CALCULATE-RATIO.
           MOVE 0 TO WS-DENOMINATOR.
           *> This will cause S0C8 without ON SIZE ERROR
           DIVIDE WS-NUMERATOR BY WS-DENOMINATOR
               GIVING WS-QUOTIENT
               ON SIZE ERROR
                   DISPLAY 'Cannot divide by zero'
           END-DIVIDE.
```

**Handle packed decimal division safely:**

```cobol
       WORKING-STORAGE SECTION.
       01  WS-DECIMAL-NUM    PIC 9(5)V99 PACKED-DECIMAL.
       01  WS-DECIMAL-DEN    PIC 9(5)V99 PACKED-DECIMAL.
       01  WS-DECIMAL-RES    PIC 9(7)V99 PACKED-DECIMAL.

       PROCEDURE DIVISION.
       SAFE-PACKED-DIVIDE.
           MOVE 100.00 TO WS-DECIMAL-NUM.
           MOVE 0.00 TO WS-DECIMAL-DEN.
           DIVIDE WS-DECIMAL-NUM BY WS-DECIMAL-DEN
               GIVING WS-DECIMAL-RES
               ON SIZE ERROR
                   MOVE 0 TO WS-DECIMAL-RES
                   DISPLAY 'Packed decimal division error'
           END-DIVIDE.
```

## Common Mistakes

- Not using ON SIZE ERROR on every DIVIDE statement
- Assuming that initialized WORKING-STORAGE variables are non-zero
- Forgetting that SPACES in a numeric field evaluates to zero
- Not checking divisors that result from COMPUTE or arithmetic operations
- Using integer DIVIDE when decimal division would be more appropriate

## Related Pages

- [Numeric overflow in COBOL](/languages/cobol/cobol-overflow-error-new)
- [File status 35 in COBOL](/languages/cobol/cobol-file-status-35-new)
- [Runtime error in COBOL](/languages/cobol/cobol-runtime-error-v2)
- [Linkage section error in COBOL](/languages/cobol/cobol-linkage-section-new)
