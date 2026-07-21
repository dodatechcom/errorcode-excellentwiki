---
title: "[Solution] COBOL Subprogram Error"
description: "Fix COBOL subprogram errors including missing PROGRAM-ID, incorrect CALL syntax, and linkage issues."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

Subprogram errors occur when called COBOL programs have missing PROGRAM-ID declarations, incorrect USING clauses, or linkage section mismatches.

## Common Causes

- Missing PROGRAM-ID in called program
- CALL USING arguments not matching LINKAGE SECTION
- RETURNING clause used with wrong data type
- Circular CALL between subprograms

## How to Fix

### 1. Ensure proper LINKAGE SECTION

```cobol
*> CALLED program
IDENTIFICATION DIVISION.
PROGRAM-ID. SUB-PROG.
DATA DIVISION.
LINKAGE SECTION.
01 LS-INPUT    PIC 9(4).
01 LS-OUTPUT   PIC X(20).
PROCEDURE DIVISION USING LS-INPUT LS-OUTPUT.
    MOVE 'DONE' TO LS-OUTPUT.
    GOBACK.
```

### 2. Match CALL arguments

```cobol
*> CALLER
CALL 'SUB-PROG' USING WS-COUNT WS-RESULT.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SUBPROGRAM-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-INPUT   PIC 9(4) VALUE 42.
01 WS-OUTPUT  PIC X(20) VALUE SPACES.

PROCEDURE DIVISION.
    DISPLAY 'Calling subprogram...'.
    DISPLAY 'Result: ' WS-OUTPUT.
    STOP RUN.
```

## Related Errors

- [COBOL Call Statement Error](../cobol-call-statement)
- [COBOL Linkage Section Error](../cobol-linkage-section)
- [COBOL Nested Call Error](../cobol-nested-call-error)
