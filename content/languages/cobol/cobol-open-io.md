---
title: "[Solution] COBOL OPEN I-O — Indexed File Access"
description: "Fix COBOL OPEN I-O errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1109
---

OPEN I-O opens a file for both input and output (random access). Errors involve using I-O on sequential files, or not having an indexed file organization.

## Common Causes

- OPEN I-O requires an indexed (ISAM/VSAM) file
- Using I-O on a sequential file (use INPUT or OUTPUT instead)
- Missing organization clause in the FD
- File does not exist when opening with I-O

## How to Fix

### 1. Use I-O for indexed files only

```cobol
FD  CUSTOMER-FILE
    RECORD CONTAINS 100 CHARACTERS
    ORGANIZATION IS INDEXED
    ACCESS MODE IS RANDOM
    RECORD KEY IS WS-CUST-ID.

OPEN I-O CUSTOMER-FILE.
```

### 2. Use INPUT for read-only access

```cobol
OPEN INPUT DATA-FILE.
```

### 3. Use OUTPUT for write-only access

```cobol
OPEN OUTPUT REPORT-FILE.
```

### 4. Use EXTEND to append

```cobol
OPEN EXTEND LOG-FILE.
```

### 5. Handle file status after open

```cobol
OPEN I-O CUSTOMER-FILE
IF WS-STATUS NOT = '00'
    DISPLAY 'Cannot open: ' WS-STATUS
END-IF
```

## Examples

Random access on indexed file:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. OPEN-IO-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-FILE-STATUS    PIC XX.
01 WS-CUST-ID        PIC 9(5) VALUE 10001.

FILE SECTION.
FD  CUSTOMER-FILE
    FILE STATUS IS WS-FILE-STATUS
    ORGANIZATION IS INDEXED
    ACCESS MODE IS RANDOM
    RECORD KEY IS CUST-ID.
01  CUST-RECORD.
    05 CUST-ID      PIC 9(5).
    05 CUST-NAME    PIC X(30).
    05 CUST-BAL     PIC 9(7)V99.

PROCEDURE DIVISION.
    OPEN I-O CUSTOMER-FILE
    MOVE 10001 TO CUST-ID
    READ CUSTOMER-FILE
        KEY IS CUST-ID
        INVALID KEY
            DISPLAY 'Customer not found'
        NOT INVALID KEY
            DISPLAY CUST-NAME
    END-READ
    CLOSE CUSTOMER-FILE
    STOP RUN.
```

## Related Errors

- [COBOL File Status Error](../cobol-file-status)
- [COBOL File Section Error](../cobol-file-section)
- [COBOL READ INTO Error](../cobol-read-into)
