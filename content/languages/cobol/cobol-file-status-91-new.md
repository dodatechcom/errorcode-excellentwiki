---
title: "[Solution] COBOL: file status 91 file not available"
description: "Fix COBOL file status 91 by verifying file assignment and checking dataset availability."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

COBOL file status 91 indicates that the file is not available for the requested operation. This error occurs when the operating system cannot access the file because it has not been allocated, the DSN (Data Set Name) does not exist, the file is locked by another process, or the file's physical storage is inaccessible. On mainframe systems, this often relates to JCL allocation issues. On distributed systems, it may indicate file permission problems or missing files.

## Why It Happens

File status 91 errors have multiple causes. The most common is attempting to open a file that was not properly allocated in the JCL (Job Control Language) on mainframe systems. A misspelled DD name or DSN in the JCL that does not match the program's SELECT statement triggers this error. The file may have been deleted by another job or user before the current program accesses it. In distributed environments, the file path may be incorrect or the file may not exist at the specified location. Permission restrictions may prevent access, especially when running under different user IDs. File locking by concurrent processes, particularly in CICS or IMS regions, can make the file temporarily unavailable. Storage volumes that are unmounted or offline cause physical access failures.

## How to Fix It

**Verify JCL allocation matches SELECT statement:**

```cobol
       * In the COBOL program:
       SELECT MASTER-FILE ASSIGN TO 'MSTFILE'
           ORGANIZATION IS SEQUENTIAL
           ACCESS MODE IS SEQUENTIAL
           FILE STATUS IS WS-STATUS.

       * In the JCL, ensure DD name matches:
       * //MSTFILE DD DSN=MY.DATA.MASTER,DISP=SHR
```

**Check file existence before opening:**

```cobol
       OPEN INPUT MASTER-FILE.
       IF WS-STATUS NOT = '00'
           DISPLAY 'File not available, status: ' WS-STATUS
           DISPLAY 'Check file allocation and permissions'
           STOP RUN
       END-IF.
```

**Handle file locking in multi-user environments:**

```cobol
       * Use OPEN with appropriate sharing options
       OPEN INPUT MASTER-FILE
           WITH LOCK    *> Exclusive lock
       * or
       OPEN INPUT MASTER-FILE
           WITH NO LOCK *> Allow concurrent access

       IF WS-STATUS = '91'
           DISPLAY 'File locked by another process'
           PERFORM RETRY-OPEN
       END-IF.
```

**Use error handling for dynamic file access:**

```cobol
       PROCEDURE DIVISION.
       MAIN-PARAGRAPH.
           OPEN I-O INVENTORY-FILE
           EVALUATE WS-STATUS
               WHEN '00'
                   PERFORM PROCESS-INVENTORY
               WHEN '91'
                   DISPLAY 'Inventory file unavailable'
                   DISPLAY 'Status: ' WS-STATUS
                   PERFORM NOTIFY-OPERATOR
               WHEN OTHER
                   DISPLAY 'Unexpected error: ' WS-STATUS
           END-EVALUATE
           CLOSE INVENTORY-FILE
           STOP RUN.
```

**Validate file paths on distributed systems:**

```cobol
       * On Unix/Linux/Windows systems
       SELECT INFILE ASSIGN TO '/home/cobol/data/input.dat'
           ORGANIZATION IS LINE SEQUENTIAL
           FILE STATUS IS WS-STATUS.

       * Verify the directory exists
       CALL 'C$FILEOP' USING 'EXISTS'
           '/home/cobol/data/input.dat'
           RETURNING WS-RESULT

       IF WS-RESULT = 0
           DISPLAY 'File does not exist'
           STOP RUN
       END-IF.
```

## Common Mistakes

- Not verifying that DD names in JCL match SELECT ASSIGN TO values
- Assuming a file exists without checking after job restarts
- Not handling status 91 in program error routines
- Forgetting that file permissions change when running under different user IDs
- Not accounting for temporary file allocation failures in batch chains

## Related Pages

- [File status 35 in COBOL](/languages/cobol/cobol-file-status-35-new)
- [File status 46 in COBOL](/languages/cobol/cobol-file-status-46-new)
- [File status 72 in COBOL](/languages/cobol/cobol-file-status-72-new)
- [Syntax error in COBOL](/languages/cobol/cobol-syntax-error-new)
