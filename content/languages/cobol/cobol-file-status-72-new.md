---
title: "[Solution] COBOL: file status 72 disk storage limit exceeded"
description: "Fix COBOL file status 72 by managing disk space and implementing file cleanup routines."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

COBOL file status 72 indicates that disk storage limit has been exceeded during a file operation. The operating system cannot write additional records to the file because the storage device is full, the file has reached its maximum allowed size, or the disk volume has insufficient free space. This error is returned in the FILE-STATUS field after an unsuccessful WRITE or REWRITE operation. In batch processing environments, this can halt an entire job stream if not properly handled.

## Why It Happens

Disk storage exhaustion occurs when output files grow beyond available disk space. In batch processing programs that generate large reports or data files, the disk may fill up before the program completes. Log files that accumulate over time without rotation consume increasing space. Temporary files created during SORT operations or intermediate processing may not be cleaned up, gradually filling the disk. In multi-user environments, multiple programs writing to the same disk simultaneously can collectively exhaust space. Files with incorrectly specified record sizes that are larger than necessary waste storage. Not compressing or archiving old data files before writing new ones contributes to the problem. System administrators may have set quotas that limit individual file or user storage.

## How to Fix It

**Monitor disk space before writing:**

```cobol
       * Check available space (platform-dependent)
       * Most COBOL environments provide system routines

       OPEN OUTPUT OUTFILE.
       PERFORM WRITE-RECORDS
           AT END OF FILE
               DISPLAY 'Warning: disk space may be low'
       END-PERFORM.
       CLOSE OUTFILE.

       * Alternative: estimate file size before creation
       COMPUTE WS-ESTIMATED-SIZE =
           WS-RECORD-COUNT * WS-RECORD-SIZE
       IF WS-ESTIMATED-SIZE > WS-AVAILABLE-SPACE
           DISPLAY 'Insufficient disk space'
           STOP RUN
       END-IF.
```

**Implement file cleanup routines:**

```cobol
       * Before writing new output, check and clean old files
       CALL 'C$DELETE' USING 'OLD_REPORT.TXT'
       CALL 'C$DELETE' USING 'TEMP_FILE.DAT'

       OPEN OUTPUT REPORT-FILE.
       WRITE REPORT-LINE FROM HEADER-RECORD.
       * Write report...
       CLOSE REPORT-FILE.
```

**Set file size limits and handle status 72:**

```cobol
       OPEN OUTPUT DATA-FILE.
       PERFORM UNTIL WS-EOF = 'Y'
           READ INPUT-FILE
               AT END
                   MOVE 'Y' TO WS-EOF
               NOT AT ENd
                   WRITE DATA-RECORD
                       FROM INPUT-RECORD
                   END-WRITE

                   IF WS-FILE-STATUS = '72'
                       DISPLAY 'Disk full, writing stopped'
                       CLOSE DATA-FILE
                       STOP RUN
                   END-IF
           END-READ
       END-PERFORM.
       CLOSE DATA-FILE.
```

**Split large outputs across multiple files:**

```cobol
       MOVE 0 TO WS-FILE-COUNT.
       MOVE 0 TO WS-RECORDS-IN-FILE.

       OPEN OUTPUT DATA-FILE.
       PERFORM UNTIL WS-EOF = 'Y'
           READ INPUT-FILE
               AT END
                   MOVE 'Y' TO WS-EOF
               NOT AT END
                   IF WS-RECORDS-IN-FILE >= 100000
                       CLOSE DATA-FILE
                       ADD 1 TO WS-FILE-COUNT
                       OPEN OUTPUT DATA-FILE
                       MOVE 0 TO WS-RECORDS-IN-FILE
                   END-IF

                   WRITE DATA-RECORD FROM INPUT-RECORD
                   ADD 1 TO WS-RECORDS-IN-FILE
           END-READ
       END-PERFORM.
       CLOSE DATA-FILE.
```

**Use compressed output when possible:**

```cobol
       * For sequential files, consider using record compression
       * if supported by your COBOL implementation

       SELECT COMPRESSED-FILE ASSIGN TO 'OUTPUT.DAT'
           ORGANIZATION IS SEQUENTIAL
           RECORD DELIMITED BY SIZE
           FILE STATUS IS WS-STATUS.
```

## Common Mistakes

- Not monitoring disk space in long-running batch jobs
- Allowing log files and temporary files to accumulate without cleanup
- Creating output files without estimating required space first
- Not implementing file rotation for programs that generate daily output
- Assuming the disk will always have enough space without checking quotas

## Related Pages

- [File status 35 in COBOL](/languages/cobol/cobol-file-status-35-new)
- [File status 46 in COBOL](/languages/cobol/cobol-file-status-46-new)
- [File status 91 in COBOL](/languages/cobol/cobol-file-status-91-new)
- [Runtime error in COBOL](/languages/cobol/cobol-runtime-error-v2)
