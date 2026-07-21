---
title: "[Solution] COBOL PHONE Number Error"
description: "Fix COBOL PHONE NUMBER clause errors in ENVIRONMENT DIVISION for telecommunication device assignments."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

PHONE NUMBER clause errors occur when the telecommunication clause in the ENVIRONMENT DIVISION contains an invalid format or is unsupported by the target system.

## Common Causes

- PHONE NUMBER format incompatible with the runtime
- Using PHONE NUMBER on non-telecom systems
- Missing COMM-PORT or LINE SPEED clauses
- Incorrect ASSIGN-TO device name

## How to Fix

### 1. Check compiler support

```cobol
*> WRONG: PHONE NUMBER not supported
ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
SPECIAL-NAMES.
    PRINTER IS SYSOUT
    PHONE NUMBER IS '555-1234'.
```

### 2. Use ASSIGN-TO for file devices

```cobol
FILE-CONTROL.
    SELECT COM-FILE ASSIGN TO 'COM1'.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. PHONE-DEMO.

ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
SPECIAL-NAMES.
    PRINTER IS SYSOUT.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-MSG  PIC X(20) VALUE 'Phone demo done'.

PROCEDURE DIVISION.
    DISPLAY WS-MSG.
    STOP RUN.
```

## Related Errors

- [COBOL Environment Division Error](../cobol-environment-division)
- [COBOL Configuration Section Error](../cobol-configuration-section)
- [COBOL File Status Error](../cobol-file-status-error)
