---
title: "[Solution] COBOL REPLACE Error"
description: "Fix COBOL REPLACE statement errors in copybook replacement including delimiter and scope issues."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

REPLACE errors occur when the REPLACE statement uses incorrect delimiters, unmatched patterns, or applies to a wider scope than intended.

## Common Causes

- Mismatched == delimiters in REPLACE
- REPLACE pattern not found in copybook text
- REPLACE scope extending beyond intended COPY block
- Nested REPLACE statements conflicting

## How to Fix

### 1. Use consistent delimiters

```cobol
*> WRONG: Mixed delimiter styles
REPLACE ==OLD== BY 'NEW'.

*> CORRECT: Match delimiters
REPLACE ==OLD== BY ==NEW==.
```

### 2. Scope REPLACE properly

```cobol
COPY MY-COPYBOOK
    REPLACING ==OLD-NAME== BY ==NEW-NAME==.
*> REPLACE applies only to this COPY
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. REPLACE-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-VALUE  PIC 9(4) VALUE 100.

PROCEDURE DIVISION.
    DISPLAY 'Replace demo: ' WS-VALUE.
    STOP RUN.
```

## Related Errors

- [COBOL Replacing Error](../cobol-replacing-error)
- [COBOL Copy Error](../cobol-copy-error-new)
- [COBOL Compiler Directive Error](../cobol-compiler-directive)
