---
title: "[Solution] COBOL File Status — File Operation Status Codes"
description: "Fix COBOL file status errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1108
---

File status codes report the result of file I/O operations. Common codes include 00 (success), 10 (end of file), 22 (duplicate key), 23 (record not found), 35 (file not found).

## Common Causes

- File status 35: file does not exist or wrong path
- File status 22: duplicate key in indexed file
- File status 23: key not found in indexed file
- File status 91: file not available

## How to Fix

### 1. Check file status after every I/O operation

```cobol
READ FILE-NAME
    AT END MOVE 'Y' TO WS-EOF
    INVALID KEY DISPLAY 'INVALID KEY'
END-READ
IF WS-FILE-STATUS NOT = '00'
    DISPLAY 'Error: ' WS-FILE-STATUS
END-IF
```

### 2. Handle file not found (status 35)

```cobol
OPEN INPUT DATA-FILE
IF WS-FILE-STATUS = '35'
    DISPLAY 'File not found'
    STOP RUN
END-IF
```

### 3. Handle duplicate key (status 22)

```cobol
WRITE RECORD-NAME FROM WS-REC
    INVALID KEY
        DISPLAY 'Duplicate key: ' WS-KEY
END-WRITE
```

### 4. Handle record not found (status 23)

```cobol
READ FILE-NAME KEY IS WS-SEARCH-KEY
    INVALID KEY
        DISPLAY 'Record not found'
END-READ
```

### 5. Use FILE STATUS clause in FD

```cobol
FD  DATA-FILE
    FILE STATUS IS WS-FILE-STATUS.
```

## Examples

Complete file status handling:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. FILE-STATUS-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-FILE-STATUS    PIC XX VALUE SPACES.
01 WS-EOF            PIC X(1) VALUE 'N'.

FILE SECTION.
FD  DATA-FILE
    FILE STATUS IS WS-FILE-STATUS.
01  DATA-RECORD.
    05 DR-ID    PIC 9(5).
    05 DR-NAME  PIC X(30).

PROCEDURE DIVISION.
    OPEN INPUT DATA-FILE
    EVALUATE WS-FILE-STATUS
        WHEN '00'
            CONTINUE
        WHEN '35'
            DISPLAY 'File not found'
            STOP RUN
        WHEN OTHER
            DISPLAY 'Open error: ' WS-FILE-STATUS
            STOP RUN
    END-EVALUATE

    PERFORM UNTIL WS-EOF = 'Y'
        READ DATA-FILE
            AT END MOVE 'Y' TO WS-EOF
            NOT AT END
                DISPLAY DR-ID ' ' DR-NAME
        END-READ
    END-PERFORM
    CLOSE DATA-FILE
    STOP RUN.
```

## Related Errors

- [COBOL File Section Error](../cobol-file-section)
- [COBOL OPEN I-O Error](../cobol-open-io)
- [COBOL READ INTO Error](../cobol-read-into)
