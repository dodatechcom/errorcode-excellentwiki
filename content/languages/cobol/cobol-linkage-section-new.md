---
title: "[Solution] COBOL: linkage section error or parameter mismatch"
description: "Fix COBOL linkage section errors by matching parameter definitions and CALL USING conventions."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A COBOL linkage section error occurs when there is a mismatch between the parameters passed by a calling program and the LINKAGE SECTION definitions in the called program. This can cause data corruption, incorrect calculations, or runtime abends. The error manifests when the calling program's data items do not match the called program's LINKAGE SECTION in size, type, or position. Proper parameter passing in COBOL requires that the data definitions match exactly, as COBOL does not perform automatic type conversion between programs.

## Why It Happens

Linkage section errors occur when the CALL statement's USING parameters do not match the called program's LINKAGE SECTION declarations. Mismatched PIC clauses between the caller's WORKING-STORAGE and the callee's LINKAGE SECTION cause data misalignment. Using CALL BY VALUE when the called program expects BY REFERENCE, or vice versa, leads to incorrect data passing. The number of parameters may differ between the call and the receiving program. Group items with different elementary field layouts between caller and callee cause data corruption. Using the wrong data types (numeric vs alphanumeric) for the same logical parameter causes conversion errors. Not initializing parameters before calling can pass garbage data. Forgetting that COBOL passes by reference by default means modifications in the called program affect the caller's data.

## How to Fix It

**Match parameter definitions exactly between caller and callee:**

```cobol
       * CALLING PROGRAM
       WORKING-STORAGE SECTION.
       01  WS-CUST-ID       PIC X(10) VALUE 'CUST001'.
       01  WS-AMOUNT        PIC 9(7)V99 VALUE 100.00.
       01  WS-STATUS        PIC X(1).

       PROCEDURE DIVISION.
       CALL 'SUB-PROGRAM'
           USING WS-CUST-ID WS-AMOUNT WS-STATUS
       END-CALL.
```

```cobol
       * CALLED PROGRAM - SUB-PROGRAM.COB
       IDENTIFICATION DIVISION.
       PROGRAM-ID. SUB-PROGRAM.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-LOCAL-STATUS  PIC X(1).

       LINKAGE SECTION.
       01  LS-CUST-ID       PIC X(10).    *> Must match caller
       01  LS-AMOUNT        PIC 9(7)V99. *> Must match caller
       01  LS-STATUS        PIC X(1).     *> Must match caller

       PROCEDURE DIVISION USING LS-CUST-ID LS-AMOUNT LS-STATUS.
           DISPLAY 'Customer: ' LS-CUST-ID
           DISPLAY 'Amount: ' LS-AMOUNT
           MOVE 'Y' TO LS-STATUS
           EXIT PROGRAM.
```

**Use BY VALUE for value passing:**

```cobol
       * Caller: pass by value (copy of data)
       CALL 'CALC-TAX' USING BY VALUE WS-TAX-RATE
                              BY REFERENCE WS-PRICE
       END-CALL.

       * Called program
       LINKAGE SECTION.
       01  LS-TAX-RATE      PIC 9(3)V99.
       01  LS-PRICE         PIC 9(7)V99.

       PROCEDURE DIVISION USING
           BY VALUE LS-TAX-RATE
           BY REFERENCE LS-PRICE.
           COMPUTE LS-PRICE =
               LS-PRICE * (1 + LS-TAX-RATE / 100)
           EXIT PROGRAM.
```

**Verify parameter count matches:**

```cobol
       * WRONG: passing 2 parameters to program expecting 3
       CALL 'PROCESS' USING WS-A WS-B
       * But PROCESS expects: USING WS-A WS-B WS-C

       * CORRECT: pass all required parameters
       CALL 'PROCESS' USING WS-A WS-B WS-C
```

**Check RETURN-CODE for called program status:**

```cobol
       CALL 'SUB-PROGRAM' USING WS-DATA.
       IF RETURN-CODE NOT = 0
           DISPLAY 'Called program failed: ' RETURN-CODE
       END-IF.


## Common Mistakes

- Passing parameters in a different order than the called program expects
- Not matching PIC clause sizes exactly between caller and callee
- Forgetting that CALL BY REFERENCE means the called program can modify the caller's data
- Using CALL BY VALUE for large group items (only the address is passed, not a copy)
- Not defining a RETURN-CODE or using it to detect called program failures

## Related Pages

- [Syntax error in COBOL](/languages/cobol/cobol-syntax-error-new)
- [Undefined paragraph in COBOL](/languages/cobol/cobol-undefined-paragraph-new)
- [Numeric overflow in COBOL](/languages/cobol/cobol-overflow-error-new)
- [Division by zero in COBOL](/languages/cobol/cobol-division-by-zero-new)
