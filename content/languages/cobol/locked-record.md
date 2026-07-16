---
title: "Record locked"
description: "A record locked error occurs when attempting to access a record that is locked by another process."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["record", "locked", "concurrency", "cobol"]
weight: 5
---

## What This Error Means

A record locked error (FILE-STATUS 42) occurs when a program tries to access a record that has been locked by another process. This is common in multi-user environments where multiple programs access the same file.

## Common Causes

- Another process has locked the record
- Missing unlock operation
- Transaction not completed
- Deadlock between processes

## How to Fix

```cobol
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           OPEN I-O EMPLOYEE-FILE
           READ EMPLOYEE-FILE
               RECORD IS LOCKED
               DISPLAY "Record locked by another user"
               CLOSE EMPLOYEE-FILE
               STOP RUN
           END-READ
           ...
           WRITE EMPLOYEE-RECORD
           UNLOCK EMPLOYEE-FILE
```

```cobol
       PROCEDURE DIVISION.
      * Retry with delay
           MOVE 0 TO WS-RETRY-COUNT
           PERFORM UNTIL WS-RETRY-COUNT > 3
               READ EMPLOYEE-FILE
                   RECORD IS LOCKED
                   ADD 1 TO WS-RETRY-COUNT
                   CALL "C$SLEEP" USING 1
               NOT RECORD IS LOCKED
                   EXIT PERFORM
               END-READ
           END-PERFORM
```

## Examples

```cobol
      * Example 1: Lock conflict
       OPEN I-O EMPLOYEE-FILE
       READ EMPLOYEE-FILE
      * FILE-STATUS = 42 (locked)

      * Example 2: Missing unlock
       OPEN I-O EMPLOYEE-FILE
       READ EMPLOYEE-FILE
       WRITE EMPLOYEE-RECORD
      * Record still locked

      * Example 3: Deadlock
      * Program A locks record 1, waits for record 2
      * Program B locks record 2, waits for record 1
```

## Related Errors

- [File status error](/languages/cobol/file-status)
- [End of file](/languages/cobol/end-of-file)
