---
title: "[Solution] COBOL FILE-STATUS 39 — Record Length Mismatch Error"
description: "Fix COBOL FILE-STATUS 39 (record length mismatch). Learn why the program's record definition doesn't match the file's record length and how to align them."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["file-status", "record-length", "39", "open", "runtime"]
weight: 5
---

# FILE-STATUS 39 — Record Length Mismatch Error

A `FILE-STATUS 39` error occurs when the record length defined in the COBOL program doesn't match the actual record length in the file. The runtime rejects the open or read operation because the sizes are incompatible.

## Description

In COBOL, each file has a record layout defined in the FD (File Description) section. The file on disk also has a record length (either fixed or determined by line delimiters). If these two lengths don't match, the runtime sets FILE-STATUS to `39` when attempting to open or read the file.

Common scenarios:

- **FD definition changed** — a program was modified to add/remove fields but the file wasn't updated.
- **File created by different program** — the file was written with a different record layout.
- **Fixed-length records mismatch** — the file has 80-byte records but the FD defines 100 bytes.
- **Mixed record formats** — the file uses a different record format than expected.

## Common Causes

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. RECORD-ERROR.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT DATA-FILE ASSIGN TO "DATA.DAT"
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD  DATA-FILE.
       01  DATA-RECORD.
           05 RECORD-ID      PIC 9(5).
           05 RECORD-NAME    PIC X(30).
           05 RECORD-VALUE   PIC 9(10).
      *    Total: 45 bytes
      *    If DATA.DAT has records of different length => FILE-STATUS 39

       WORKING-STORAGE SECTION.
       01  WS-FILE-STATUS   PIC XX VALUE SPACES.

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           OPEN INPUT DATA-FILE
           IF WS-FILE-STATUS NOT = "00"
               DISPLAY "File open error: " WS-FILE-STATUS
               STOP RUN
           END-IF
           ...
```

## How to Fix

### Fix 1: Match FD record length to the actual file

```cobol
       FD  DATA-FILE.
       01  DATA-RECORD.
           05 RECORD-ID      PIC 9(5).
           05 RECORD-NAME    PIC X(30).
           05 RECORD-VALUE   PIC 9(10).
      *    Adjust fields so total matches the file's record length
      *    If file has 80-byte records, pad or restructure accordingly
```

### Fix 2: Use RECORD CONTAINS clause to verify

```cobol
       FD  DATA-FILE
           RECORD CONTAINS 45 CHARACTERS.
       01  DATA-RECORD.
           05 RECORD-ID      PIC 9(5).
           05 RECORD-NAME    PIC X(30).
           05 RECORD-VALUE   PIC 9(10).
      *    The RECORD CONTAINS clause makes the expected length explicit
```

### Fix 3: Check file format matches ORGANIZATION clause

```cobol
       FILE-CONTROL.
      *    If file is fixed-length, don't use LINE SEQUENTIAL
           SELECT DATA-FILE ASSIGN TO "DATA.DAT"
               ORGANIZATION IS RECORD SEQUENTIAL.

      *    If file is text/line-delimited, use LINE SEQUENTIAL
           SELECT DATA-FILE ASSIGN TO "DATA.DAT"
               ORGANIZATION IS LINE SEQUENTIAL.
```

### Fix 4: Add error handling for record mismatch

```cobol
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           OPEN INPUT DATA-FILE
           EVALUATE WS-FILE-STATUS
               WHEN "00"
                   CONTINUE
               WHEN "39"
                   DISPLAY "ERROR: Record length mismatch"
                   DISPLAY "Program expects: 45 bytes"
                   DISPLAY "File has different record size"
                   STOP RUN
               WHEN OTHER
                   DISPLAY "File error: " WS-FILE-STATUS
                   STOP RUN
           END-EVALUATE

           READ DATA-FILE
               AT END DISPLAY "End of file"
               NOT AT END
                   DISPLAY DATA-RECORD
           END-READ
           CLOSE DATA-FILE
           STOP RUN.
```

## Examples

```
File status 39: Record length mismatch

The program's FD defines a 45-byte record, but the file
'DATA.DAT' contains records of a different length. The
OPEN or READ operation cannot proceed.
```

## Related Errors

- [file-not-found] — FILE-STATUS 35, the file doesn't exist at the specified path.
- [FILE-STATUS 30] — permanent file error (hardware/media issue).
- [FILE-STATUS 48] — line too long for RECORD SEQUENTIAL file.
