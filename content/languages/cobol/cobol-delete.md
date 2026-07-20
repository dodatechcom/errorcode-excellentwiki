---
title: "[Solution] COBOL DELETE — Remove Record"
description: "Fix COBOL DELETE statement errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1113
---

DELETE removes the current record from an indexed file. Errors involve DELETE without prior READ, or DELETE on sequential files.

## Common Causes

- DELETE requires a prior successful READ
- File not opened with I-O
- DELETE on a sequential file (not supported)
- Key not set before DELETE

## How to Fix

### 1. READ before DELETE

```cobol
READ CUSTOMER-FILE KEY IS WS-KEY
    INVALID KEY DISPLAY 'Not found'
    NOT INVALID KEY
        DELETE CUSTOMER-FILE
            INVALID KEY DISPLAY 'Delete failed'
        END-DELETE
END-READ
```

### 2. Open with I-O

```cobol
OPEN I-O CUSTOMER-FILE.
```

### 3. Check file status after DELETE

```cobol
DELETE CUSTOMER-FILE
    INVALID KEY
        DISPLAY 'Delete error: ' WS-STATUS
END-DELETE
```

### 4. Use INVALID KEY for safety

```cobol
DELETE CUSTOMER-FILE
    INVALID KEY
        DISPLAY 'Cannot delete: ' WS-CUST-ID
END-DELETE
```

### 5. Verify deletion

```cobol
READ CUSTOMER-FILE KEY IS WS-KEY
    INVALID KEY DISPLAY 'Record deleted successfully'
    NOT INVALID KEY DISPLAY 'Record still exists'
END-READ
```

## Examples

Deleting a record:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. DELETE-DEMO.

DATA DIVISION.
FILE SECTION.
FD  CUSTOMER-FILE
    ORGANIZATION IS INDEXED
    RECORD KEY IS CUST-ID.
01  CUST-RECORD.
    05 CUST-ID      PIC 9(5).
    05 CUST-NAME    PIC X(30).

WORKING-STORAGE SECTION.
01 WS-DELETE-ID     PIC 9(5) VALUE 10001.

PROCEDURE DIVISION.
    OPEN I-O CUSTOMER-FILE
    MOVE WS-DELETE-ID TO CUST-ID
    READ CUSTOMER-FILE KEY IS CUST-ID
        INVALID KEY
            DISPLAY 'Record not found'
        NOT INVALID KEY
            DISPLAY 'Deleting: ' CUST-NAME
            DELETE CUSTOMER-FILE
                INVALID KEY DISPLAY 'Delete failed'
                NOT INVALID KEY DISPLAY 'Deleted'
            END-DELETE
    END-READ
    CLOSE CUSTOMER-FILE
    STOP RUN.
```

## Related Errors

- [COBOL REWRITE Error](../cobol-rewrite)
- [COBOL START Error](../cobol-start)
- [COBOL File Status Error](../cobol-file-status)
