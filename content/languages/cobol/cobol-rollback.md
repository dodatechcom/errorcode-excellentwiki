---
title: "[Solution] COBOL ROLLBACK — Transaction Rollback"
description: "Fix COBOL ROLLBACK statement errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1116
---

ROLLBACK reverts all file operations since the last COMMIT. Errors involve ROLLBACK when no transaction is active, or forgetting to ROLLBACK on error.

## Common Causes

- ROLLBACK without an active transaction (no-op or error)
- Not using ROLLBACK on error paths
- ROLLBACK closes files on some implementations
- Mixing ROLLBACK with file CLOSE

## How to Fix

### 1. Use ROLLBACK on error paths

```cobol
OPEN I-O CUSTOMER-FILE
PERFORM UPDATE-RECORDS
    ON EXCEPTION
        ROLLBACK
        DISPLAY 'Reverted changes'
        CLOSE CUSTOMER-FILE
        STOP RUN
END-PERFORM
COMMIT
CLOSE CUSTOMER-FILE
```

### 2. ROLLBACK undoes since last COMMIT

```cobol
COMMIT
*> Start new transaction
UPDATE-1
UPDATE-2
ROLLBACK
*> Only updates 1 and 2 are undone
```

### 3. Check if ROLLBACK closes files (compiler-dependent)

```cobol
ROLLBACK
*> Reopen files if needed
OPEN I-O CUSTOMER-FILE
```

### 4. Use ROLLBACK with proper error handling

```cobol
ON EXCEPTION
    ROLLBACK
    DISPLAY 'Error: changes reverted'
    GOBACK
END-CALL
```

### 5. Combine COMMIT and ROLLBACK for safety

```cobol
COMMIT *> checkpoint
UPDATE-A
UPDATE-B
ON ERROR
    ROLLBACK
    DISPLAY 'Failed'
    GOBACK
COMMIT *> save A and B
```

## Examples

Error recovery with ROLLBACK:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. ROLLBACK-DEMO.

PROCEDURE DIVISION.
    OPEN I-O ACCOUNT-FILE
    PERFORM DEBIT-ACCOUNT
    ON EXCEPTION
        ROLLBACK
        DISPLAY 'Debit failed, rolling back'
        CLOSE ACCOUNT-FILE
        STOP RUN
    END-PERFORM

    PERFORM CREDIT-ACCOUNT
    ON EXCEPTION
        ROLLBACK
        DISPLAY 'Credit failed, rolling back'
        CLOSE ACCOUNT-FILE
        STOP RUN
    END-PERFORM

    COMMIT
    DISPLAY 'Transfer complete'
    CLOSE ACCOUNT-FILE
    STOP RUN.
```

## Related Errors

- [COBOL COMMIT Error](../cobol-commit)
- [COBOL File Status Error](../cobol-file-status)
- [COBOL OPEN I-O Error](../cobol-open-io)
