---
title: "[Solution] COBOL File Description (FD) Error"
description: "Fix COBOL FD errors caused by mismatched record definitions, missing labels, or invalid file modes."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

File Description errors occur when FD entries contain invalid clauses, mismatched record layouts, or missing required sections for the target file system.

## Common Causes

- FD with missing RECORD CONTAINS clause
- Label records misconfigured for sequential files
- RECORD DELIMITER clause incompatible with file type
- Conflicting BLOCK CONTAINS and RECORD CONTAINS

## How to Fix

### 1. Provide complete FD definition

```cobol
*> WRONG: Missing essential clauses
FD  CUSTOMER-FILE.
01  CUSTOMER-RECORD.
    05 CUST-ID    PIC 9(6).
    05 CUST-NAME  PIC X(30).

*> CORRECT: Include LABEL and RECORD clauses
FD  CUSTOMER-FILE
    LABEL RECORDS ARE STANDARD
    RECORD CONTAINS 36 CHARACTERS.
01  CUSTOMER-RECORD.
    05 CUST-ID    PIC 9(6).
    05 CUST-NAME  PIC X(30).
```

### 2. Match record layout to actual file

```cobol
FD  INVENTORY-FILE
    LABEL RECORDS ARE STANDARD
    RECORD CONTAINS 80 CHARACTERS
    BLOCK CONTAINS 0 RECORDS.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. FD-DEMO.

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
    SELECT OUTFILE ASSIGN TO 'cust.dat'
        ORGANIZATION IS SEQUENTIAL.

DATA DIVISION.
FILE SECTION.
FD  OUTFILE
    LABEL RECORDS ARE STANDARD
    RECORD CONTAINS 36 CHARACTERS.
01  CUSTOMER-RECORD.
    05 CUST-ID    PIC 9(6).
    05 CUST-NAME  PIC X(30).

WORKING-STORAGE SECTION.
01 WS-EOF  PIC X VALUE 'N'.

PROCEDURE DIVISION.
    OPEN OUTPUT OUTFILE.
    MOVE 100001 TO CUST-ID.
    MOVE 'JOHN DOE' TO CUST-NAME.
    WRITE CUSTOMER-RECORD.
    CLOSE OUTFILE.
    STOP RUN.
```

## Related Errors

- [COBOL File Section Error](../cobol-file-section)
- [COBOL File Status Error](../cobol-file-status-error)
- [COBOL Record Error](../cobol-record-error)
