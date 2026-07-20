---
title: "[Solution] COBOL File Section — File Record Declarations"
description: "Fix COBOL file section errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1089
---

The FILE SECTION declares file records and their structure. Errors involve mismatched record layouts, missing FD entries, or incorrect record definitions.

## Common Causes

- FD (File Description) entry does not match the actual file format
- Record size does not match the physical file record length
- Missing RECORD CONTAINS clause when needed
- Mixing sequential and indexed file record layouts

## How to Fix

### 1. Define FD correctly

```cobol
FILE SECTION.
FD  CUSTOMER-FILE
    RECORD CONTAINS 80 CHARACTERS
    BLOCK CONTAINS 10 RECORDS.
01  CUSTOMER-RECORD.
    05 CUST-ID       PIC 9(5).
    05 CUST-NAME     PIC X(30).
    05 CUST-BALANCE  PIC 9(7)V99.
    05 CUST-FILLER   PIC X(36).
```

### 2. Match record size to file

```cobol
FD  DATA-FILE
    RECORD CONTAINS 100 CHARACTERS.
01  DATA-RECORD PIC X(100).
```

### 3. Use record variants for indexed files

```cobol
FD  ORDER-FILE
    RECORD CONTAINS 120 CHARACTERS.
01  ORDER-RECORD.
    05 ORDER-TYPE    PIC X(1).
    88 ORDER-ADD     VALUE 'A'.
    88 ORDER-DELETE  VALUE 'D'.
    05 ORDER-DATA    PIC X(119).
01  ORDER-ADD-REC    REDEFINES ORDER-RECORD.
    05 ORDER-TYPE2   PIC X(1).
    05 ORDER-ID      PIC 9(8).
    05 ORDER-DETAIL  PIC X(111).
```

### 4. Use LINAGE for print files

```cobol
FD  REPORT-FILE
    RECORD CONTAINS 132 CHARACTERS
    LINAGE IS 60 LINES
    WITH FOOTING AT 55
    LINES AT TOP 3
    LINES AT BOTTOM 5.
```

### 5. Check block size for optimized I/O

```cobol
FD  BATCH-FILE
    RECORD CONTAINS 200 CHARACTERS
    BLOCK CONTAINS 50 RECORDS.
```

## Examples

A complete FILE SECTION:

```cobol
DATA DIVISION.
FILE SECTION.
FD  INVENTORY-FILE
    RECORD CONTAINS 100 CHARACTERS
    BLOCK CONTAINS 25 RECORDS.
01  INV-RECORD.
    05 INV-ITEM-NO   PIC X(8).
    05 INV-DESC      PIC X(30).
    05 INV-QTY       PIC 9(5).
    05 INV-PRICE     PIC 9(5)V99.
    05 INV-FILLER    PIC X(47).
```

## Related Errors

- [COBOL WORKING-STORAGE Error](../cobol-working-storage)
- [COBOL OPEN I-O Error](../cobol-open-io)
- [COBOL File Status Error](../cobol-file-status)
