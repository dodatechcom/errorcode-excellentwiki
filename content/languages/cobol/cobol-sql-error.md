---
title: "[Solution] COBOL Embedded SQL Error"
description: "Fix COBOL embedded SQL errors including SQLCODE checks, cursor handling, and missing EXEC SQL END-EXEC."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

Embedded SQL errors occur when EXEC SQL statements contain syntax errors, missing END-EXEC markers, or SQL operations that return non-zero SQLCODE values.

## Common Causes

- Missing EXEC SQL END-EXEC terminator
- Not checking SQLCODE after SQL operations
- Cursor used without proper DECLARE/FETCH/CLOSE cycle
- SQLCA not declared before SQL operations

## How to Fix

### 1. Always include SQLCA

```cobol
EXEC SQL
    INCLUDE SQLCA
END-EXEC.
```

### 2. Check SQLCODE after operations

```cobol
EXEC SQL
    SELECT NAME INTO :WS-NAME
    FROM CUSTOMERS
    WHERE ID = :WS-ID
END-EXEC.

IF SQLCODE NOT = 0
    DISPLAY 'SQL Error: ' SQLCODE.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SQL-DEMO.

EXEC SQL INCLUDE SQLCA END-EXEC.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ID     PIC 9(6) VALUE 100001.
01 WS-NAME   PIC X(30).

PROCEDURE DIVISION.
    EXEC SQL
        SELECT CUST_NAME INTO :WS-NAME
        FROM CUSTOMERS
        WHERE CUST_ID = :WS-ID
    END-EXEC.
    IF SQLCODE = 0
        DISPLAY 'Name: ' WS-NAME
    ELSE
        DISPLAY 'SQL Error: ' SQLCODE.
    STOP RUN.
```

## Related Errors

- [COBOL Runtime Error](../cobol-runtime-error)
- [COBOL Record Error](../cobol-record-error)
- [COBOL File Status Error](../cobol-file-status-error)
