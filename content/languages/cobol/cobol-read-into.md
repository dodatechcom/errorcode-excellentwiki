---
title: "[Solution] COBOL READ INTO — Read to Variable"
description: "Fix COBOL READ INTO errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1110
---

READ INTO reads a record into a different variable than the file record. Errors involve size mismatch, or using READ INTO when READ should be used instead.

## Common Causes

- Target variable smaller than the record (truncation)
- Target variable larger than the record (garbage in extra bytes)
- Using READ INTO without proper error handling
- Reading past end of file

## How to Fix

### 1. Ensure target is large enough

```cobol
FD  DATA-FILE.
01  FILE-RECORD       PIC X(100).

WORKING-STORAGE SECTION.
01  WS-RECORD-BUFFER  PIC X(100).

READ DATA-FILE INTO WS-RECORD-BUFFER
    AT END MOVE 'Y' TO WS-EOF
END-READ
```

### 2. Use READ for direct access to file record

```cobol
READ DATA-FILE
    AT END MOVE 'Y' TO WS-EOF
    NOT AT END
        DISPLAY FILE-RECORD
END-READ
```

### 3. Check file status after READ INTO

```cobol
READ DATA-FILE INTO WS-BUFFER
    AT END MOVE 'Y' TO WS-EOF
END-READ
IF WS-STATUS NOT = '00' AND NOT = '10'
    DISPLAY 'Read error: ' WS-STATUS
END-IF
```

### 4. Use KEY IS with READ INTO for indexed files

```cobol
READ CUSTOMER-FILE INTO WS-CUST-BUFFER
    KEY IS WS-CUST-ID
    INVALID KEY DISPLAY 'Not found'
END-READ
```

### 5. Handle different record layouts

```cobol
FD  DATA-FILE.
01  DATA-RECORD.
    05 DR-ID      PIC 9(5).
    05 DR-NAME    PIC X(30).

01  ALT-RECORD    REDEFINES DATA-RECORD.
    05 AR-ID      PIC X(5).
    05 AR-DATA    PIC X(30).
```

## Examples

Reading records with READ INTO:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. READ-INTO-DEMO.

DATA DIVISION.
FILE SECTION.
FD  INVENTORY-FILE.
01  INV-RECORD.
    05 INV-ITEM    PIC X(8).
    05 INV-QTY     PIC 9(5).
    05 INV-PRICE   PIC 9(5)V99.

WORKING-STORAGE SECTION.
01 WS-BUFFER      PIC X(18).
01 WS-EOF         PIC X(1) VALUE 'N'.

PROCEDURE DIVISION.
    OPEN INPUT INVENTORY-FILE
    PERFORM UNTIL WS-EOF = 'Y'
        READ INVENTORY-FILE INTO WS-BUFFER
            AT END MOVE 'Y' TO WS-EOF
            NOT AT END
                DISPLAY 'Read: ' WS-BUFFER
        END-READ
    END-PERFORM
    CLOSE INVENTORY-FILE
    STOP RUN.
```

## Related Errors

- [COBOL File Section Error](../cobol-file-section)
- [COBOL File Status Error](../cobol-file-status)
- [COBOL WRITE FROM Error](../cobol-write-from)
