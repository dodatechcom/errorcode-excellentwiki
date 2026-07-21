---
title: "[Solution] COBOL INSPECT TALLYING Error"
description: "Fix COBOL INSPECT TALLYING errors when counting characters or substrings in alphanumeric fields."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

INSPECT TALLYING errors occur when the INSPECT statement is used with invalid TALLYING clauses or mismatched BEFORE/AFTER phrases.

## Common Causes

- TALLYING target not numeric
- Missing BEFORE or AFTER delimiter
- BEFORE/AFTER delimiter not found in subject
- TALLYING and REPLACING used together incorrectly

## How to Fix

### 1. Use correct TALLYING syntax

```cobol
*> WRONG: Non-numeric tally counter
01 WS-COUNT  PIC X(4).
INSPECT WS-TEXT TALLYING WS-COUNT FOR ALL 'A'.

*> CORRECT: Numeric tally counter
01 WS-COUNT  PIC 9(4) VALUE 0.
INSPECT WS-TEXT TALLYING WS-COUNT FOR ALL 'A'.
```

### 2. Validate BEFORE/AFTER clauses

```cobol
INSPECT WS-TEXT TALLYING WS-COUNT
    FOR ALL 'A'
    BEFORE 'Z'
    AFTER FIRST 'B'.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. TALLYING-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-TEXT     PIC X(30) VALUE 'HELLO WORLD'.
01 WS-COUNT    PIC 9(4) VALUE 0.

PROCEDURE DIVISION.
    INSPECT WS-TEXT TALLYING WS-COUNT FOR ALL 'L'.
    DISPLAY 'Count of L: ' WS-COUNT.
    STOP RUN.
```

## Related Errors

- [COBOL Inspect Replacing Error](../cobol-inspect-replacing)
- [COBOL Inspect Tallying Error](../cobol-inspect-tallying)
- [COBOL String Error](../cobol-string-error)
