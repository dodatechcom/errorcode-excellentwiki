---
title: "[Solution] COBOL WRITE FROM — Write Record"
description: "Fix COBOL WRITE FROM errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1111
---

WRITE FROM writes a record to a file from a source variable. Errors involve size mismatch, writing to a file not opened for OUTPUT, or wrong record structure.

## Common Causes

- Source variable larger than record (truncation)
- File not opened for OUTPUT or EXTEND
- After START for indexed files, WRITE FROM may not work
- Missing INVALID KEY handling for indexed files

## How to Fix

### 1. Open the file for OUTPUT

```cobol
OPEN OUTPUT REPORT-FILE.
WRITE REPORT-RECORD FROM WS-DATA.
```

### 2. Match source and record sizes

```cobol
FD  REPORT-FILE.
01  REPORT-RECORD    PIC X(80).

WORKING-STORAGE SECTION.
01 WS-LINE           PIC X(80).

WRITE REPORT-RECORD FROM WS-LINE.
```

### 3. Handle INVALID KEY for indexed files

```cobol
WRITE WS-RECORD FROM WS-DATA
    INVALID KEY
        DISPLAY 'Write error: ' WS-STATUS
END-WRITE
```

### 4. Use AFTER ADVANCING for line control

```cobol
WRITE REPORT-RECORD FROM WS-LINE
    AFTER ADVANCING 1 LINE.
```

### 5. Write to print files with page control

```cobol
WRITE REPORT-RECORD FROM WS-LINE
    AFTER ADVANCING PAGE.
```

## Examples

Report writing:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. WRITE-FROM-DEMO.

DATA DIVISION.
FILE SECTION.
FD  REPORT-FILE.
01  REPORT-LINE       PIC X(80).

WORKING-STORAGE SECTION.
01 WS-HEADER          PIC X(80) VALUE
    '=============================================='.
01 WS-DATA-LINE       PIC X(80).

PROCEDURE DIVISION.
    OPEN OUTPUT REPORT-FILE
    WRITE REPORT-LINE FROM WS-HEADER
        AFTER ADVANCING 1 LINE
    MOVE 'Name: JOHN DOE     Balance: $1000.00'
        TO WS-DATA-LINE
    WRITE REPORT-LINE FROM WS-DATA-LINE
        AFTER ADVANCING 1 LINE
    CLOSE REPORT-FILE
    STOP RUN.
```

## Related Errors

- [COBOL READ INTO Error](../cobol-read-into)
- [COBOL REWRITE Error](../cobol-rewrite)
- [COBOL File Status Error](../cobol-file-status)
