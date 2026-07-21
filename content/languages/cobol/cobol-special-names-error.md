---
title: "[Solution] COBOL SPECIAL-NAMES Error"
description: "Fix COBOL SPECIAL-NAMES errors including invalid mnemonic names and unsupported device assignments."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

SPECIAL-NAMES errors occur when the SPECIAL-NAMES paragraph in the ENVIRONMENT DIVISION contains invalid mnemonic names or unsupported device assignments.

## Common Causes

- Mnemonic name conflicts with reserved words
- ASSIGN TO clause referencing undefined device
- Missing SPECIAL-NAMES when SYSPRINT is used
- Duplicate mnemonic definitions

## How to Fix

### 1. Define mnemonics before use

```cobol
*> WRONG: Mnemonic not defined
DISPLAY 'Hello' UPON MY-PRINTER.

*> CORRECT
SPECIAL-NAMES.
    PRINTER IS MY-PRINTER.
DISPLAY 'Hello' UPON MY-PRINTER.
```

### 2. Avoid reserved word conflicts

```cobol
*> WRONG: 'CONSOLE' may be reserved
SPECIAL-NAMES.
    CONSOLE IS MY-CONSOLE.

*> CORRECT: Use unique name
SPECIAL-NAMES.
    CONSOLE IS CRT-DEVICE.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SPECIAL-NAMES-DEMO.

ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
SPECIAL-NAMES.
    PRINTER IS SYSOUT.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-MSG  PIC X(20) VALUE 'Special names demo'.

PROCEDURE DIVISION.
    DISPLAY WS-MSG UPON SYSOUT.
    STOP RUN.
```

## Related Errors

- [COBOL Environment Division Error](../cobol-environment-division)
- [COBOL Configuration Section Error](../cobol-configuration-section)
- [COBOL Display Upon Error](../cobol-display-upon)
