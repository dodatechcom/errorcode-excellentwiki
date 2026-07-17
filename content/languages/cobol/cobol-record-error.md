---
title: "Record error in COBOL"
description: "Record errors in COBOL occur when record layout mismatches, record size is incorrect, or record operations fail."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Record errors occur when the record structure defined in the FD doesn't match the actual data, or when record operations (READ, WRITE, REWRITE) encounter size or structure issues.

## Common Causes

- FD record size doesn't match actual file record size
- Moving data between incompatible record layouts
- RECORD CONTAINS clause wrong
- Group item alignment issues

## How to Fix

```cobol
       * WRONG: Record size mismatch
       FD  CUSTOMER-FILE
           RECORD CONTAINS 80 CHARACTERS.
       01  CUSTOMER-REC  PIC X(100).
       * Error: FD says 80 but record is 100
```

```cobol
       * CORRECT: Match FD to actual record size
       FD  CUSTOMER-FILE
           RECORD CONTAINS 100 CHARACTERS.
       01  CUSTOMER-REC.
           05 CUST-ID      PIC X(10).
           05 CUST-NAME    PIC X(30).
           05 CUST-ADDR    PIC X(60).
```

## Examples

```cobol
       01  WS-RECORD.
           05 FIELD-A PIC X(10).
           05 FIELD-B PIC X(20).
       * Moving PIC X(30) to WS-RECORD requires
       * exactly 30 characters
```

## Related Errors

- [File Not Found](/languages/cobol/file-not-found) - file errors
- [Locked Record](/languages/cobol/locked-record) - record locking
