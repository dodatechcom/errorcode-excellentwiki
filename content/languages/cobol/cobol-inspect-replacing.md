---
title: "[Solution] COBOL INSPECT REPLACING — String Substitution"
description: "Fix COBOL INSPECT REPLACING errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1107
---

INSPECT REPLACING replaces characters or phrases in a string. Errors involve wrong FIRST/LAST/ALL usage, or replacing with a different-length string.

## Common Causes

- Replacing with a string of different length (changes field length)
- Wrong usage of ALL vs FIRST vs LEADING
- Missing BEFORE/AFTER delimiters
- REPLACING a phrase that does not exist (no-op, not error)

## How to Fix

### 1. Use ALL for replacing all occurrences

```cobol
01 WS-TEXT    PIC X(50) VALUE 'HELLO WORLD'.
INSPECT WS-TEXT REPLACING ALL 'L' BY 'R'.
*> 'HERRO WORLD'
```

### 2. Use FIRST for only the first occurrence

```cobol
INSPECT WS-TEXT REPLACING FIRST 'L' BY 'R'.
*> 'HELRO WORLD'
```

### 3. Use LEADING for leading characters

```cobol
01 WS-NUM     PIC X(10) VALUE '00001234'.
INSPECT WS-NUM REPLACING LEADING '0' BY ' '.
*> '    1234  '
```

### 4. Use CHARACTERS to replace entire substrings

```cobol
INSPECT WS-TEXT REPLACING CHARACTERS
    BEFORE ' ' BY '***'.
```

### 5. Combine with BEFORE/AFTER

```cobol
INSPECT WS-TEXT REPLACING ALL 'X' BY 'Y'
    AFTER 'START'.
```

## Examples

Text replacement:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. REPLACE-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ORIG    PIC X(40) VALUE 'aaa bbb aaa ccc aaa'.
01 WS-RESULT  PIC X(40).

PROCEDURE DIVISION.
    MOVE WS-ORIG TO WS-RESULT.
    INSPECT WS-RESULT REPLACING ALL 'aaa' BY 'XXX'.
    DISPLAY 'Original: ' WS-ORIG.
    DISPLAY 'Replaced: ' WS-RESULT.
    STOP RUN.
```

## Related Errors

- [COBOL INSPECT TALLYING Error](../cobol-inspect-tallying)
- [COBOL STRING Error](../cobol-string)
- [COBOL Data Movement Error](../cobol-data-movement-error)
