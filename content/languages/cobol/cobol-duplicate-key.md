---
title: "Duplicate key error in COBOL"
description: "Duplicate key errors in COBOL occur when attempting to write a record with a key that already exists in an indexed file."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["duplicate-key", "indexed", "write", "file-status", "cobol"]
weight: 5
---

## What This Error Means

When writing to an indexed (ISAM/VSAM) file, a duplicate key error (file status '22') occurs if the new record's key matches an existing record's key.

## Common Causes

- Writing record with existing key value
- Duplicate primary key in indexed file
- Not reading/rewriting to update existing record
- Missing duplicate key handling in WRITE

## How to Fix

```cobol
       * WRONG: No duplicate key check
       WRITE CUSTOMER-REC
           INVALID KEY DISPLAY 'Duplicate key'.
```

```cobol
       * CORRECT: Check file status after write
       WRITE CUSTOMER-REC
           INVALID KEY
               IF FILE-STATUS = '22'
                   DISPLAY 'Duplicate key - record exists'
                   REWRITE CUSTOMER-REC
               ELSE
                   DISPLAY 'Write error: ' FILE-STATUS
               END-IF
       END-WRITE.
```

```cobol
       * CORRECT: Read before write to update
       READ CUSTOMER-FILE
           KEY IS CUSTOMER-ID
           INVALID KEY
               WRITE CUSTOMER-REC
           NOT INVALID KEY
               REWRITE CUSTOMER-REC
       END-READ.
```

## Examples

```cobol
       * Writing duplicate record
       MOVE 'CUST001' TO CUSTOMER-ID.
       WRITE CUSTOMER-REC.
       * If CUST001 already exists: file status 22
```

## Related Errors

- [File Not Found](/languages/cobol/file-not-found) - file errors
- [Invalid Key](/languages/cobol/invalid-key) - key access errors
