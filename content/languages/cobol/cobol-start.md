---
title: "[Solution] COBOL START — Position Indexed File"
description: "Fix COBOL START statement errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1114
---

START positions an indexed file for sequential reading from a specific key. Errors involve wrong key value, file not opened with I-O, or key field mismatch.

## Common Causes

- Key value does not exist in the file
- File not opened with I-O access mode
- Key field does not match the record key definition
- START on a non-indexed file

## How to Fix

### 1. Open with I-O and use START

```cobol
OPEN I-O CUSTOMER-FILE.
START CUSTOMER-FILE KEY IS >= WS-SEARCH-KEY
    INVALID KEY DISPLAY 'Key not found'
END-START
```

### 2. Use correct comparison operator

```cobol
START CUSTOMER-FILE KEY IS = WS-KEY.        *> exact match
START CUSTOMER-FILE KEY IS >= WS-KEY.       *> greater or equal
START CUSTOMER-FILE KEY IS > WS-KEY.        *> greater than
START CUSTOMER-FILE KEY IS NOT > WS-KEY.    *> not greater (<=)
```

### 3. Handle INVALID KEY

```cobol
START CUSTOMER-FILE KEY IS >= WS-KEY
    INVALID KEY
        DISPLAY 'No matching key'
    NOT INVALID KEY
        PERFORM READ-NEXT
END-START
```

### 4. Read sequentially after START

```cobol
PERFORM UNTIL WS-EOF = 'Y'
    READ CUSTOMER-FILE NEXT
        AT END MOVE 'Y' TO WS-EOF
        NOT AT END
            DISPLAY CUST-ID ' ' CUST-NAME
    END-READ
END-PERFORM
```

### 5. Use START for partial key access

```cobol
START CUSTOMER-FILE KEY IS = WS-DEPT-ID
    INVALID KEY DISPLAY 'Department not found'
END-START
```

## Examples

Random access with START:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. START-DEMO.

DATA DIVISION.
FILE SECTION.
FD  CUSTOMER-FILE
    ORGANIZATION IS INDEXED
    ACCESS MODE IS RANDOM
    RECORD KEY IS CUST-ID.
01  CUST-RECORD.
    05 CUST-ID      PIC 9(5).
    05 CUST-NAME    PIC X(30).
    05 CUST-BAL     PIC 9(7)V99.

WORKING-STORAGE SECTION.
01 WS-START-KEY     PIC 9(5) VALUE 10010.
01 WS-EOF           PIC X(1) VALUE 'N'.

PROCEDURE DIVISION.
    OPEN I-O CUSTOMER-FILE
    START CUSTOMER-FILE KEY IS >= WS-START-KEY
        INVALID KEY DISPLAY 'No records >= ' WS-START-KEY
        NOT INVALID KEY
            PERFORM UNTIL WS-EOF = 'Y'
                READ CUSTOMER-FILE NEXT
                    AT END MOVE 'Y' TO WS-EOF
                    NOT AT END
                        DISPLAY CUST-ID ' ' CUST-NAME
                END-READ
            END-PERFORM
    END-START
    CLOSE CUSTOMER-FILE
    STOP RUN.
```

## Related Errors

- [COBOL READ INTO Error](../cobol-read-into)
- [COBOL REWRITE Error](../cobol-rewrite)
- [COBOL File Status Error](../cobol-file-status)
