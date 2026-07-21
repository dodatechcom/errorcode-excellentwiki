---
title: "[Solution] COBOL Configuration Section Error"
description: "Fix COBOL CONFIGURATION SECTION errors including missing INPUT-OUTPUT and bad SPECIAL-NAMES entries."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

Configuration section errors occur when the CONFIGURATION SECTION contains missing or malformed entries in the ENVIRONMENT DIVISION.

## Common Causes

- Missing INPUT-OUTPUT SECTION after CONFIGURATION SECTION
- Invalid SPECIAL-NAMES entries
- Referencing undefined ASSIGN-TO names
- Incorrect SOURCE-COMPUTER or OBJECT-COMPUTER entries

## How to Fix

### 1. Include all required sections

```cobol
ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
SOURCE-COMPUTER. IBM-Z-SERIES.
OBJECT-COMPUTER. IBM-Z-SERIES.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
    SELECT OUTFILE ASSIGN TO 'output.dat'.
```

### 2. Define SPECIAL-NAMES correctly

```cobol
*> WRONG: Invalid SPECIAL-NAMES
SPECIAL-NAMES.
    PRINTER IS BAD-PRINTER.

*> CORRECT: Valid SPECIAL-NAMES
SPECIAL-NAMES.
    PRINTER IS SYSOUT.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. CONFIG-DEMO.

ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
SOURCE-COMPUTER. COMPILER-NAME.
OBJECT-COMPUTER. COMPILER-NAME.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-OUTPUT  PIC X(20) VALUE 'Configuration OK'.

PROCEDURE DIVISION.
    DISPLAY WS-OUTPUT.
    STOP RUN.
```

## Related Errors

- [COBOL Environment Division Error](../cobol-environment-division)
- [COBOL File Not Found](../cobol-file-not-found)
- [COBOL File Status Error](../cobol-file-status-error)
