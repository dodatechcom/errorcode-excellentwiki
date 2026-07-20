---
title: "[Solution] COBOL INSPECT TALLYING — String Counting"
description: "Fix COBOL INSPECT TALLYING errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1106
---

INSPECT TALLYING counts occurrences of characters or phrases in a string. Errors involve wrong BEFORE/AFTER delimiters, or using TALLYING with an incompatible variable.

## Common Causes

- TALLYING variable is not numeric
- Missing BEFORE or AFTER delimiter clause
- TALLYING ALL vs TALLYING characters (syntax confusion)
- Counting a character that does not exist (returns 0, which is correct but confusing)

## How to Fix

### 1. Use correct TALLYING syntax

```cobol
01 WS-COUNT      PIC 9(3) VALUE 0.
01 WS-TEXT       PIC X(50) VALUE 'HELLO WORLD'.

INSPECT WS-TEXT TALLYING WS-COUNT FOR ALL 'L'.
```

### 2. Use BEFORE/AFTER for substring counting

```cobol
INSPECT WS-TEXT TALLYING WS-COUNT
    FOR ALL 'L' AFTER 'O'.
```

### 3. TALLYING for characters until a delimiter

```cobol
INSPECT WS-TEXT TALLYING WS-COUNT
    FOR CHARACTERS BEFORE ' '.
```

### 4. Use TALLYING with LEADING for leading zeros

```cobol
01 WS-NUMBER    PIC X(10) VALUE '00001234'.
01 WS-ZEROS     PIC 9(2).

INSPECT WS-NUMBER TALLYING WS-ZEROS
    FOR LEADING '0'.
```

### 5. Combine multiple TALLYING clauses

```cobol
INSPECT WS-TEXT TALLYING
    WS-COUNT-A FOR ALL 'A'
    WS-COUNT-B FOR ALL 'B'
    WS-COUNT-C FOR ALL 'C'.
```

## Examples

String analysis:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. TALLYING-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-SENTENCE   PIC X(80) VALUE 'THE QUICK BROWN FOX JUMPS'.
01 WS-SPACES     PIC 9(3) VALUE 0.
01 WS-CHARS      PIC 9(3) VALUE 0.

PROCEDURE DIVISION.
    INSPECT WS-SENTENCE TALLYING WS-SPACES FOR ALL ' '.
    DISPLAY 'Spaces: ' WS-SPACES.
    INSPECT WS-SENTENCE TALLYING WS-CHARS
        FOR CHARACTERS BEFORE ' '.
    DISPLAY 'First word length: ' WS-CHARS.
    STOP RUN.
```

## Related Errors

- [COBOL INSPECT REPLACING Error](../cobol-inspect-replacing)
- [COBOL STRING Error](../cobol-string)
- [COBOL UNSTRING Error](../cobol-unstring)
