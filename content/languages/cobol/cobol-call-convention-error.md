---
title: "[Solution] COBOL CALL CONVENTION Error"
description: "Fix COBOL CALL CONVENTION errors when calling programs from different dialects or languages."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

CALL CONVENTION errors occur when calling a program with an incompatible calling convention, causing parameter passing mismatches or stack corruption.

## Common Causes

- Default CALL CONVENTION differs between compiler and target
- Calling non-COBOL program without specifying convention
- STATIC vs DYNAMIC calling mismatch
- C linkage vs COBOL linkage mismatch

## How to Fix

### 1. Specify CALL CONVENTION explicitly

```cobol
*> WRONG: Assumed convention
CALL 'C-PROGRAM' USING WS-DATA.

*> CORRECT: Specify convention
CALL 'C-PROGRAM' USING BY VALUE WS-DATA.
```

### 2. Match static and dynamic calling

```cobol
CALL STATIC 'SUB-PROG' USING WS-INPUT.
CALL DYNAMIC WS-PROG-NAME USING WS-INPUT.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. CALL-CONVENTION-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-DATA  PIC 9(4) VALUE 42.

PROCEDURE DIVISION.
    DISPLAY 'Calling with convention...'.
    DISPLAY 'Data: ' WS-DATA.
    STOP RUN.
```

## Related Errors

- [COBOL Call Statement Error](../cobol-call-statement)
- [COBOL Nested Call Error](../cobol-nested-call-error)
- [COBOL Runtime Error](../cobol-runtime-error)
