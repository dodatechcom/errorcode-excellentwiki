---
title: "[Solution] COBOL SORT Statement — Internal Sort"
description: "Fix COBOL SORT statement errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1102
---

The SORT statement sorts records in a file. Errors involve missing INPUT/OUTPUT PROCEDURE, wrong sort key, or mismatched record layouts.

## Common Causes

- Missing INPUT PROCEDURE or USING clause
- Sort key does not match the record structure
- OUTPUT PROCEDURE does not RELEASE records properly
- Sort file and input file have different record sizes

## How to Fix

### 1. Use SORT with USING/OUTPUT for simple cases

```cobol
SORT SORT-FILE
    ON ASCENDING KEY WS-KEY
    USING INPUT-FILE
    OUTPUT PROCEDURE IS WRITE-SORTED.
```

### 2. Use INPUT PROCEDURE for data transformation

```cobol
SORT SORT-FILE
    ON ASCENDING KEY WS-KEY
    INPUT PROCEDURE IS READ-AND-PROCESS
    GIVING OUTPUT-FILE.
```

### 3. RELEASE records in INPUT PROCEDURE

```cobol
READ-AND-PROCESS.
    PERFORM UNTIL WS-EOF = 'Y'
        READ INPUT-FILE
            AT END MOVE 'Y' TO WS-EOF
            NOT AT END
                MOVE WS-RECORD TO WS-SORT-REC
                RELEASE WS-SORT-REC
        END-READ
    END-PERFORM.
```

### 4. RETURN records in OUTPUT PROCEDURE

```cobol
WRITE-SORTED.
    RETURN SORT-FILE
        AT END MOVE 'Y' TO WS-EOF
        NOT AT END
            WRITE OUTPUT-REC FROM WS-SORT-REC
    END-RETURN.
```

### 5. Define the sort file correctly

```cobol
SD  SORT-FILE.
01  SORT-RECORD.
    05 SORT-KEY     PIC 9(5).
    05 SORT-DATA    PIC X(75).
```

## Examples

A complete SORT example:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SORT-DEMO.

DATA DIVISION.
FILE SECTION.
FD  INPUT-FILE.
01  INPUT-RECORD.
    05 IN-KEY       PIC 9(5).
    05 IN-DATA      PIC X(75).

SD  SORT-FILE.
01  SORT-RECORD.
    05 SR-KEY       PIC 9(5).
    05 SR-DATA      PIC X(75).

FD  OUTPUT-FILE.
01  OUTPUT-RECORD.
    05 OUT-KEY      PIC 9(5).
    05 OUT-DATA     PIC X(75).

PROCEDURE DIVISION.
    SORT SORT-FILE
        ON ASCENDING KEY SR-KEY
        USING INPUT-FILE
        GIVING OUTPUT-FILE.
    STOP RUN.
```

## Related Errors

- [COBOL MERGE Error](../cobol-merge-error)
- [COBOL File Status Error](../cobol-file-status)
- [COBOL File Section Error](../cobol-file-section)
