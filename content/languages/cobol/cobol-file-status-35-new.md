---
title: "[Solution] COBOL: file status 35 sequential file organization violation"
description: "Fix COBOL file status 35 by correcting file organization and verifying sequential access modes."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

COBOL file status 35 indicates a sequential file organization violation, meaning an operation was attempted that is not permitted for the file's declared organization. This error occurs when trying to perform random access on a sequential file, when record locking conflicts arise, or when the file's organization does not match the access mode specified in the environment division. The file status code 35 is returned in the FILE-STATUS field after an unsuccessful I/O operation, allowing the program to handle the error gracefully.

## Why It Happens

File status 35 errors arise from mismatched file organization and access mode declarations. Attempting to use RANDOM access on a file declared as ORGANIZATION IS SEQUENTIAL is the most common cause. Another scenario is trying to read a record by key from a file that was not defined with the appropriate record key. Accessing a file with the wrong mode after opening it, such as attempting DELETE on a file opened as INPUT, triggers this error. Record locking conflicts in multi-user environments, where another user has locked a record, can also produce status 35. Using REWRITE on a sequential file that was opened as INPUT instead of I-O is another frequent cause. The file may also have been defined with the wrong organization in the SELECT statement.

## How to Fix It

**Match access mode to file organization:**

```cobol
       * WRONG: RANDOM access on sequential file
       SELECT INFILE ASSIGN TO 'DATA.TXT'
           ORGANIZATION IS SEQUENTIAL
           ACCESS MODE IS RANDOM
           FILE STATUS IS WS-STATUS.

       * CORRECT: use SEQUENTIAL access for sequential files
       SELECT INFILE ASSIGN TO 'DATA.TXT'
           ORGANIZATION IS SEQUENTIAL
           ACCESS MODE IS SEQUENTIAL
           FILE STATUS IS WS-STATUS.
```

**Use correct file open modes:**

```cobol
       * WRONG: REWRITE with INPUT mode
       OPEN INPUT INFILE.
       REWRITE INFILE-RECORD.  *> Error: wrong mode

       * CORRECT: use I-O mode for modifications
       OPEN I-O INFILE.
       REWRITE INFILE-RECORD.
       CLOSE INFILE.
```

**Use indexed organization for random access:**

```cobol
       * CORRECT: RANDOM access requires indexed organization
       SELECT MASTER-FILE ASSIGN TO 'MASTER.DAT'
           ORGANIZATION IS INDEXED
           ACCESS MODE IS RANDOM
           RECORD KEY IS WS-KEY
           FILE STATUS IS WS-STATUS.

       OPEN I-O MASTER-FILE.
       MOVE '001' TO WS-KEY.
       READ MASTER-FILE
           KEY IS WS-KEY
           INVALID KEY
               DISPLAY 'Record not found'
       END-READ.
       CLOSE MASTER-FILE.
```

**Check record handling operations:**

```cobol
       * WRONG: DELETE on file opened as INPUT
       OPEN INPUT OUTFILE.
       DELETE OUTFILE-RECORD.  *> Error

       * CORRECT: DELETE requires I-O or EXTEND mode
       OPEN I-O OUTFILE.
       DELETE OUTFILE-RECORD.
       CLOSE OUTFILE.
```

**Handle file status after every I/O operation:**

```cobol
       OPEN I-O INFILE.
       READ INFILE
           AT END
               MOVE 'Y' TO WS-EOF
           NOT AT END
               PERFORM PROCESS-RECORD
       END-READ.

       IF WS-STATUS NOT = '00'
           DISPLAY 'Error on READ: ' WS-STATUS
           CLOSE INFILE
           STOP RUN
       END-IF.
       CLOSE INFILE.
```

## Common Mistakes

- Declaring SEQUENTIAL organization but using RANDOM access mode
- Opening a file as INPUT when modifications (WRITE, REWRITE, DELETE) are needed
- Not checking FILE-STATUS after every I/O operation
- Using EXTEND mode for random writes when I-O mode is required
- Confusing RECORD KEY requirements between sequential and indexed files

## Related Pages

- [File status 46 in COBOL](/languages/cobol/cobol-file-status-46-new)
- [File status 72 in COBOL](/languages/cobol/cobol-file-status-72-new)
- [File status 91 in COBOL](/languages/cobol/cobol-file-status-91-new)
- [Record error in COBOL](/languages/cobol/cobol-record-error-v2)
