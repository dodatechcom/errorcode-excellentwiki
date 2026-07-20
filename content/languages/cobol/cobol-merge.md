---
title: "[Solution] COBOL MERGE — File Merge Operations"
description: "Fix COBOL MERGE statement errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1103
---

MERGE combines multiple sorted files into one sorted output. Errors involve unsorted input files, wrong merge key, or mismatched record structures.

## Common Causes

- Input files are not pre-sorted on the merge key
- Merge key does not match across all input files
- Missing USING or GIVING clause
- Record structures differ between input files

## How to Fix

### 1. Ensure input files are sorted

```cobol
SORT SORT-FILE1 ON ASCENDING KEY WS-KEY USING FILE1 GIVING FILE1-SORTED.
SORT SORT-FILE2 ON ASCENDING KEY WS-KEY USING FILE2 GIVING FILE2-SORTED.
```

### 2. Use MERGE with correct syntax

```cobol
MERGE MERGE-FILE
    ON ASCENDING KEY WS-KEY
    USING FILE1-SORTED FILE2-SORTED
    GIVING OUTPUT-FILE.
```

### 3. Match record structures

```cobol
SD  MERGE-FILE.
01  MERGE-RECORD.
    05 MR-KEY       PIC 9(5).
    05 MR-DATA      PIC X(75).
```

### 4. Use INPUT/OUTPUT PROCEDURE for transformation

```cobol
MERGE MERGE-FILE
    ON ASCENDING KEY WS-KEY
    INPUT PROCEDURE IS READ-MERGE
    OUTPUT PROCEDURE IS WRITE-MERGE.
```

### 5. Test with two files first

```cobol
MERGE MERGE-FILE
    ON ASCENDING KEY MR-KEY
    USING SORTED-FILE-A SORTED-FILE-B
    GIVING MERGED-OUTPUT.
```

## Examples

Merging two customer files:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. MERGE-DEMO.

DATA DIVISION.
FILE SECTION.
SD  MERGE-FILE.
01  MERGE-REC.
    05 MR-ID        PIC 9(5).
    05 MR-NAME      PIC X(30).
    05 MR-BALANCE   PIC 9(7)V99.

PROCEDURE DIVISION.
    MERGE MERGE-FILE
        ON ASCENDING KEY MR-ID
        USING FILE-A FILE-B
        GIVING MERGED-OUTPUT.
    STOP RUN.
```

## Related Errors

- [COBOL SORT Statement](../cobol-sort-statement)
- [COBOL File Status Error](../cobol-file-status)
- [COBOL File Section Error](../cobol-file-section)
