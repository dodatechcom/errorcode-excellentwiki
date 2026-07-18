---
title: "[Solution] COBOL: numeric overflow error"
description: "Fix COBOL numeric overflow by expanding PIC clause sizes and using ON SIZE ERROR handling."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A COBOL numeric overflow error occurs when an arithmetic operation produces a result that exceeds the capacity of the receiving field. On mainframe systems, this triggers an S0C8 ABEND or is caught by the ON SIZE ERROR clause. The error means the result has more integer digits than the PIC clause can hold, or the decimal precision exceeds the receiving field's Vnn places. COBOL does not automatically truncate numeric results with overflow detection; it requires explicit ON SIZE ERROR handling.

## Why It Happens

Numeric overflow in COBOL occurs when the receiving field's PIC clause is too small for the calculated result. For example, storing the result of 99999 * 99 in a PIC 9(5) field overflows because the result (999901) requires six digits. Adding accumulated totals without checking the PIC size is a frequent source of overflow. Multiplication results grow quickly: a 5-digit number multiplied by a 3-digit number can produce up to 8 digits. SUBTRACT operations that produce negative results stored in unsigned numeric fields also cause overflow. When COMPUTE statements evaluate complex expressions, intermediate results may overflow even if the final result would fit. Packed decimal fields with insufficient size for large computed values trigger decimal overflow.

## How to Fix It

**Size receiving fields appropriately:**

```cobol
       WORKING-STORAGE SECTION.
       * WRONG: PIC too small for result
       01  WS-SMALL-TOTAL    PIC 9(5).
       01  WS-VALUE-A        PIC 9(5) VALUE 50000.
       01  WS-VALUE-B        PIC 9(3) VALUE 999.

       * CORRECT: ensure result field is large enough
       01  WS-LARGE-TOTAL    PIC 9(9).
       01  WS-PRODUCT        PIC 9(8).

       PROCEDURE DIVISION.
       CALCULATE-PRODUCT.
           MULTIPLY WS-VALUE-A BY WS-VALUE-B
               GIVING WS-PRODUCT
               ON SIZE ERROR
                   DISPLAY 'Product overflow'
               NOT ON SIZE ERROR
                   DISPLAY 'Product: ' WS-PRODUCT
           END-MULTIPLY.
```

**Use ON SIZE ERROR on every arithmetic statement:**

```cobol
       ADD-SAFE.
           ADD WS-A TO WS-B
               GIVING WS-C
               ON SIZE ERROR
                   DISPLAY 'ADD overflow: ' WS-A ' + ' WS-B
                   MOVE 99999999 TO WS-C
               NOT ON SIZE ERROR
                   CONTINUE
           END-ADD.

       SUBTRACT-SAFE.
           SUBTRACT WS-B FROM WS-A
               GIVING WS-C
               ON SIZE ERROR
                   DISPLAY 'SUBTRACT overflow'
               NOT ON SIZE ERROR
                   CONTINUE
           END-SUBTRACT.

       MULTIPLY-SAFE.
           MULTIPLY WS-A BY WS-B
               GIVING WS-C
               ON SIZE ERROR
                   DISPLAY 'MULTIPLY overflow'
           END-MULTIPLY.

       DIVIDE-SAFE.
           DIVIDE WS-A BY WS-B
               GIVING WS-C
               ON SIZE ERROR
                   DISPLAY 'DIVIDE error'
           END-DIVIDE.
```

**Use larger PIC clauses for accumulation:**

```cobol
       WORKING-STORAGE SECTION.
       01  WS-CUMULATIVE   PIC 9(15)V99 VALUE 0.
       01  WS-TRANSACTION  PIC 9(9)V99.

       PROCEDURE DIVISION.
       ACCUMULATE-TOTALS.
           PERFORM UNTIL WS-EOF = 'Y'
               READ TRANSACTION-FILE
                   AT END
                       MOVE 'Y' TO WS-EOF
                   NOT AT END
                       ADD WS-TRANSACTION TO WS-CUMULATIVE
                           ON SIZE ERROR
                               DISPLAY 'Total overflow at record '
                                   WS-RECORD-COUNT
                       END-ADD
               END-READ
           END-PERFORM.


## Common Mistakes

- Not using ON SIZE ERROR on ADD, SUBTRACT, MULTIPLY, and DIVIDE statements
- Using PIC 9(5) for totals that can easily exceed 99999
- Forgetting that multiplication results grow rapidly in size
- Not considering that negative SUBTRACT results overflow unsigned fields
- Assuming intermediate COMPUTE results will fit in the final receiving field

## Related Pages

- [Division by zero in COBOL](/languages/cobol/cobol-division-by-zero-new)
- [Copybook not found in COBOL](/languages/cobol/cobol-copy-error-new)
- [Runtime error in COBOL](/languages/cobol/cobol-runtime-error-v2)
- [File status 72 in COBOL](/languages/cobol/cobol-file-status-72-new)
