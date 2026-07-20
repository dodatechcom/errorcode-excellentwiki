---
title: "[Solution] COBOL REDEFINES — Memory Overlay Errors"
description: "Fix COBOL REDEFINES errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1084
---

REDEFINES lets the same memory be interpreted as different data types. Errors involve wrong size between original and redefined fields, or using REDEFINES on level 01 items incorrectly.

## Common Causes

- The REDEFINES field has a different size than the original
- Using REDEFINES on the same level with other clauses (CLauses not allowed)
- REDEFINES across different record types causes data corruption
- Forgetting that REDEFINES shares memory (changes affect both views)

## How to Fix

### 1. Ensure same size

```cobol
01 WS-RECORD.
    05 WS-NUMBER   PIC 9(5).
    05 WS-NAME     REDEFINES WS-NUMBER PIC X(5).
```

### 2. REDEFINES must follow immediately after the original

```cobol
01 WS-DATA.
    05 WS-INT     PIC 9(4).
    05 WS-CHARS   REDEFINES WS-INT PIC X(4).
    05 WS-NEXT    PIC 9(4).   *> new field, not REDEFINES
```

### 3. Use REDEFINES for variant records

```cobol
01 WS-RECORD.
    05 WS-TYPE    PIC X(1).
    05 WS-DETAIL  PIC X(50).
01 WS-RECORD-A    REDEFINES WS-RECORD.
    05 WS-TYPE-A  PIC X(1).
    05 WS-VALUE-A PIC 9(10).
    05 WS-FILLER  PIC X(40).
01 WS-RECORD-B    REDEFINES WS-RECORD.
    05 WS-TYPE-B  PIC X(1).
    05 WS-NAME-B  PIC X(20).
    05 WS-FILLER  PIC X(30).
```

### 4. Use REDEFINES for hex/binary inspection

```cobol
01 WS-HIGH-VALUE  PIC 9(4) COMP VALUE 255.
01 WS-HEX-VIEW    REDEFINES WS-HIGH-VALUE PIC X(2).
```

### 5. Initialize with care when using REDEFINES

```cobol
01 WS-BYTES.
    05 WS-BYTE-1  PIC X(1) VALUE 'A'.
    05 WS-BYTE-2  PIC X(1) VALUE 'B'.
01 WS-SHORT       REDEFINES WS-BYTES PIC X(2).
*> WS-SHORT is now 'AB'
```

## Examples

A variant record using REDEFINES:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. REDEF-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-MESSAGE.
    05 WS-CMD      PIC X(4).
    05 WS-PAYLOAD  PIC X(76).
01 WS-LOGIN-MESS  REDEFINES WS-MESSAGE.
    05 WS-CMD2     PIC X(4).
    05 WS-USER     PIC X(20).
    05 WS-PASS     PIC X(20).
    05 WS-FILLER   PIC X(36).

PROCEDURE DIVISION.
    MOVE 'AUTH' TO WS-CMD.
    MOVE 'admin' TO WS-USER.
    MOVE 'secret' TO WS-PASS.
    DISPLAY 'Command: ' WS-CMD.
    DISPLAY 'User: ' WS-USER.
    STOP RUN.
```

## Related Errors

- [COBOL RENAMES Error](../cobol-renames)
- [COBOL Data Movement Error](../cobol-data-movement-error)
- [COBOL Record Error](../cobol-record-error)
