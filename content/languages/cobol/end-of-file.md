---
title: "End of file"
description: "An end of file condition occurs when attempting to read past the last record in a file."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["end-of-file", "eof", "file", "cobol"]
weight: 5
---

## What This Error Means

An end of file (EOF) condition occurs when a READ statement attempts to read past the last record in a sequential file. This is indicated by FILE-STATUS 10 and the AT END clause.

## Common Causes

- Reading past last record
- Missing AT END handling
- Empty file
- Incorrect loop termination

## How to Fix

```cobol
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           OPEN INPUT EMPLOYEE-FILE
           PERFORM UNTIL WS-FILE-STATUS = "10"
               READ EMPLOYEE-FILE
                   AT END
                       MOVE "10" TO WS-FILE-STATUS
                   NOT AT END
                       DISPLAY EMPLOYEE-RECORD
               END-READ
           END-PERFORM
           CLOSE EMPLOYEE-FILE
```

```cobol
       PROCEDURE DIVISION.
      * Alternative: Use AT END flag
           OPEN INPUT EMPLOYEE-FILE
           MOVE "N" TO WS-EOF-FLAG
           PERFORM UNTIL WS-EOF-FLAG = "Y"
               READ EMPLOYEE-FILE
                   AT END
                       MOVE "Y" TO WS-EOF-FLAG
                   NOT AT END
                       PROCESS-RECORD
               END-READ
           END-PERFORM
```

## Examples

```cobol
      * Example 1: Missing AT END
       READ EMPLOYEE-FILE
      * May get FILE-STATUS 10

      * Example 2: Empty file
       OPEN INPUT EMPLOYEE-FILE
       READ EMPLOYEE-FILE
           AT END DISPLAY "File is empty"
       END-READ

      * Example 3: Loop without EOF check
       PERFORM UNTIL FALSE
           READ EMPLOYEE-FILE
           DISPLAY WS-RECORD
      * Infinite loop if no EOF handling
```

## Related Errors

- [File status error](/languages/cobol/file-status)
- [Record locked](/languages/cobol/locked-record)
