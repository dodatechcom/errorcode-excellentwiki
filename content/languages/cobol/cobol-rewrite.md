---
title: "[Solution] COBOL REWRITE — Update Record"
description: "Fix COBOL REWRITE errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1112
---

REWRITE replaces the current record in an indexed file. Errors involve REWRITE after READ without proper key handling, or REWRITE on a non-indexed file.

## Common Causes

- REWRITE requires a prior successful READ
- File not opened with I-O
- Key changed during REWRITE (not allowed directly)
- Wrong record size in REWRITE

## How to Fix

### 1. READ before REWRITE

```cobol
READ CUSTOMER-FILE
    INVALID KEY DISPLAY 'Not found'
    NOT INVALID KEY
        MOVE WS-NEW-BAL TO CUST-BAL
        REWRITE CUST-RECORD
            INVALID KEY DISPLAY 'Rewrite failed'
        END-REWRITE
END-READ
```

### 2. Open with I-O for REWRITE

```cobol
OPEN I-O CUSTOMER-FILE.
```

### 3. Do not change the key during REWRITE

```cobol
*> WRONG: cannot change key
MOVE NEW-KEY TO CUST-ID.
REWRITE CUST-RECORD.

*> CORRECT: delete then write
DELETE CUSTOMER-FILE.
MOVE NEW-KEY TO CUST-ID.
WRITE CUST-RECORD.
```

### 4. Use REWRITE from a different variable

```cobol
READ CUSTOMER-FILE.
MOVE WS-UPDATED-REC TO CUST-RECORD.
REWRITE CUST-RECORD.
```

### 5. Check file status after REWRITE

```cobol
REWRITE CUST-RECORD
    INVALID KEY
        DISPLAY 'REWRITE error: ' WS-STATUS
END-REWRITE
```

## Examples

Updating a record:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. REWRITE-DEMO.

DATA DIVISION.
FILE SECTION.
FD  CUSTOMER-FILE
    ORGANIZATION IS INDEXED
    RECORD KEY IS CUST-ID.
01  CUST-RECORD.
    05 CUST-ID      PIC 9(5).
    05 CUST-NAME    PIC X(30).
    05 CUST-BAL     PIC 9(7)V99.

WORKING-STORAGE SECTION.
01 WS-SEARCH-ID     PIC 9(5) VALUE 10001.
01 WS-NEW-BAL       PIC 9(7)V99 VALUE 5000.00.

PROCEDURE DIVISION.
    OPEN I-O CUSTOMER-FILE
    MOVE WS-SEARCH-ID TO CUST-ID
    READ CUSTOMER-FILE KEY IS CUST-ID
        INVALID KEY DISPLAY 'Not found'
        NOT INVALID KEY
            MOVE WS-NEW-BAL TO CUST-BAL
            REWRITE CUST-RECORD
            DISPLAY 'Updated: ' CUST-NAME
    END-READ
    CLOSE CUSTOMER-FILE
    STOP RUN.
```

## Related Errors

- [COBOL READ INTO Error](../cobol-read-into)
- [COBOL DELETE Error](../cobol-delete)
- [COBOL File Status Error](../cobol-file-status)
