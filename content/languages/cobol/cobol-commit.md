---
title: "[Solution] COBOL COMMIT — Transaction Commit"
description: "Fix COBOL COMMIT statement errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1115
---

COMMIT saves all file operations since the last COMMIT or ROLLBACK. Errors involve missing COMMIT after batch operations, or COMMIT on files not opened with I-O.

## Common Causes

- Forgetting to COMMIT after batch updates (data loss on crash)
- COMMIT when no transaction is active (no-op or error)
- Files opened without proper mode for COMMIT
- COMMIT does not close files (need explicit CLOSE)

## How to Fix

### 1. COMMIT after batch updates

```cobol
PERFORM VARYING WS-I FROM 1 BY 1 UNTIL WS-I > WS-COUNT
    READ CUSTOMER-FILE
    ADD WS-AMOUNT TO CUST-BAL
    REWRITE CUST-RECORD
END-PERFORM
COMMIT
```

### 2. Use COMMIT for checkpointing

```cobol
PERFORM UNTIL WS-EOF = 'Y'
    READ DATA-FILE
    PROCESS RECORD
    ADD 1 TO WS-COUNTER
    IF WS-COUNTER MOD 100 = 0
        COMMIT
    END-IF
END-PERFORM
COMMIT
```

### 3. ROLLBACK on error

```cobol
PERFORM PROCESS-RECORDS
ON EXCEPTION
    ROLLBACK
    DISPLAY 'Transaction rolled back'
END-PERFORM
```

### 4. COMMIT does not close files

```cobol
COMMIT
*> Files remain open; CLOSE them explicitly
```

### 5. Use COMMIT with ROLLBACK for error recovery

```cobol
OPEN I-O CUSTOMER-FILE
PERFORM UPDATE-ALL
    ON EXCEPTION
        ROLLBACK
        DISPLAY 'Updates reversed'
    NOT ON EXCEPTION
        COMMIT
        DISPLAY 'Updates saved'
END-PERFORM
CLOSE CUSTOMER-FILE
```

## Examples

Transaction processing:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. COMMIT-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-TRANS-COUNT    PIC 9(5) VALUE 0.
01 WS-MAX-TRANS      PIC 9(5) VALUE 100.

PROCEDURE DIVISION.
    OPEN I-O ACCOUNT-FILE
    PERFORM UNTIL WS-EOF = 'Y'
        READ ACCOUNT-FILE
            AT END MOVE 'Y' TO WS-EOF
            NOT AT END
                PERFORM TRANSFER-FUNDS
                ADD 1 TO WS-TRANS-COUNT
                IF WS-TRANS-COUNT MOD 50 = 0
                    COMMIT
                END-IF
        END-READ
    END-PERFORM
    COMMIT
    CLOSE ACCOUNT-FILE
    STOP RUN.
```

## Related Errors

- [COBOL ROLLBACK Error](../cobol-rollback)
- [COBOL File Status Error](../cobol-file-status)
- [COBOL OPEN I-O Error](../cobol-open-io)
