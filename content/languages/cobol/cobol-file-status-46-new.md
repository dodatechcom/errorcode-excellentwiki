---
title: "[Solution] COBOL: file status 46 read error on indexed file"
description: "Fix COBOL file status 46 by verifying record keys and handling indexed file read operations."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

COBOL file status 46 indicates a read error on an indexed file, specifically that a READ operation could not find a matching record for the specified key value. This error occurs when the record key being searched for does not exist in the indexed file, or when the key structure does not match the file's alternate key definitions. The status 46 is distinct from status 23 (record not found) in that it may indicate structural issues with the key rather than simply an absent record.

## Why It Happens

File status 46 errors occur when a READ KEY IS statement references a key value that does not exist in the indexed file. The key value may have been misspelled, incorrectly formatted, or the record may have been deleted without the program knowing. Using an alternate key that was not properly defined in the file's SD (Sort Description) or FD (File Description) section triggers this error. Reading with a key that does not match the data type or length defined for the record key causes mismatches. Accessing an indexed file that has become corrupted, where the index structure does not match the actual data, produces status 46. Attempting sequential reads on an indexed file opened in RANDOM mode with an invalid key also triggers this condition.

## How to Fix It

**Validate key values before reading:**

```cobol
       * WRONG: reading with potentially empty key
       MOVE WS-INPUT-KEY TO MASTER-KEY.
       READ MASTER-FILE
           KEY IS MASTER-KEY
           INVALID KEY
               DISPLAY 'Key not found: ' WS-INPUT-KEY
       END-READ.

       * CORRECT: validate key first
       IF WS-INPUT-KEY NOT = SPACES
           MOVE WS-INPUT-KEY TO MASTER-KEY
           READ MASTER-FILE
               KEY IS MASTER-KEY
               INVALID KEY
                   DISPLAY 'Record not found: ' WS-INPUT-KEY
               NOT INVALID KEY
                   PERFORM PROCESS-DATA
           END-READ
       ELSE
           DISPLAY 'Key is empty'
       END-IF.
```

**Verify record key definitions in the FD:**

```cobol
       FD  MASTER-FILE
           RECORD CONTAINS 100 CHARACTERS
           LABEL RECORDS ARE STANDARD.

       01  MASTER-RECORD.
           05 MASTER-ID        PIC X(10).
           05 MASTER-NAME      PIC X(30).
           05 MASTER-AMOUNT    PIC 9(7)V99.

       * In SELECT statement, key must match FD structure
       SELECT MASTER-FILE ASSIGN TO 'MASTER.DAT'
           ORGANIZATION IS INDEXED
           ACCESS MODE IS RANDOM
           RECORD KEY IS MASTER-ID
           FILE STATUS IS WS-STATUS.
```

**Handle alternate keys properly:**

```cobol
       SELECT EMPLOYEE-FILE ASSIGN TO 'EMP.DAT'
           ORGANIZATION IS INDEXED
           ACCESS MODE IS RANDOM
           RECORD KEY IS EMP-ID
           ALTERNATE RECORD KEY IS EMP-NAME
               WITH DUPLICATES
           FILE STATUS IS WS-STATUS.
```

**Check for corrupted indexed files:**

```cobol
       * Rebuild indexed file if corruption suspected
       OPEN INPUT MASTER-FILE.
       OPEN OUTPUT NEW-FILE.

       PERFORM UNTIL WS-EOF = 'Y'
           READ MASTER-FILE
               AT END
                   MOVE 'Y' TO WS-EOF
               NOT AT END
                   WRITE NEW-RECORD FROM MASTER-RECORD
           END-READ
       END-PERFORM.

       CLOSE MASTER-FILE NEW-FILE.
```

## Common Mistakes

- Not validating that the key field is populated before attempting a READ KEY IS
- Mixing up RECORD KEY and ALTERNATE RECORD KEY usage
- Using a key value with the wrong data type or length compared to the FD definition
- Not handling INVALID KEY conditions in every READ statement
- Assuming indexed files cannot become corrupted after power failures or system crashes

## Related Pages

- [File status 35 in COBOL](/languages/cobol/cobol-file-status-35-new)
- [File status 72 in COBOL](/languages/cobol/cobol-file-status-72-new)
- [File status 91 in COBOL](/languages/cobol/cobol-file-status-91-new)
- [Record error in COBOL](/languages/cobol/cobol-record-error-v2)
