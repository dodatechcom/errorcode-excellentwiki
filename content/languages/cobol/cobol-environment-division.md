---
title: "[Solution] COBOL ENVIRONMENT DIVISION — Environment Configuration"
description: "Fix COBOL ENVIRONMENT DIVISION errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1123
---

ENVIRONMENT DIVISION configures file-to-device mappings and compiler options. Errors involve wrong section names, missing FILE-CONTROL, or invalid configuration.

## Common Causes

- Missing FILE-CONTROL section for file-using programs
- Wrong SECTION name (must be ENVIRONMENT DIVISION then CONFIGURATION SECTION)
- ASSIGN TO clause does not match runtime environment
- Special-names clause has syntax errors

## How to Fix

### 1. Use proper structure

```cobol
ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
SOURCE-COMPUTER. IBM-ZSERIES.
OBJECT-COMPUTER. IBM-ZSERIES.

INPUT-OUTPUT SECTION.
FILE-CONTROL.
    SELECT DATA-FILE ASSIGN TO 'data.txt'
        ORGANIZATION IS LINE SEQUENTIAL.
```

### 2. Use ASSIGN for file mapping

```cobol
SELECT IN-FILE ASSIGN TO 'input.dat'.
SELECT OUT-FILE ASSIGN TO SYSOUT.
```

### 3. Use SPECIAL-NAMES for device mapping

```cobol
SPECIAL-NAMES.
    C01 IS TOP-OF-PAGE.
    CONSOLE IS WS-CONSOLE.
```

### 4. Handle missing ENVIRONMENT DIVISION

```cobol
*> If no files are used, ENVIRONMENT DIVISION can be omitted
IDENTIFICATION DIVISION.
PROGRAM-ID. SIMPLE.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-X PIC 9(5) VALUE 42.
PROCEDURE DIVISION.
    DISPLAY WS-X.
    STOP RUN.
```

### 5. Check runtime file assignment

```cobol
SELECT SORT-FILE ASSIGN TO 'sortwork.dat'.
```

## Examples

Complete ENVIRONMENT DIVISION:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. ENV-DEMO.

ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
SOURCE-COMPUTER. LINUX.
OBJECT-COMPUTER. LINUX.

INPUT-OUTPUT SECTION.
FILE-CONTROL.
    SELECT INPUT-FILE ASSIGN TO 'input.txt'
        ORGANIZATION IS LINE SEQUENTIAL.
    SELECT OUTPUT-FILE ASSIGN TO 'output.txt'
        ORGANIZATION IS LINE SEQUENTIAL.
    SELECT SORT-FILE ASSIGN TO 'sort.tmp'.

DATA DIVISION.
FILE SECTION.
FD  INPUT-FILE.
01  INPUT-REC       PIC X(80).
FD  OUTPUT-FILE.
01  OUTPUT-REC      PIC X(80).
SD  SORT-FILE.
01  SORT-REC        PIC X(80).

PROCEDURE DIVISION.
    DISPLAY 'Environment configured'.
    STOP RUN.
```

## Related Errors

- [COBOL IDENTIFICATION DIVISION Error](../cobol-identification-division)
- [COBOL DATA DIVISION Error](../cobol-data-division)
- [COBOL File Section Error](../cobol-file-section)
