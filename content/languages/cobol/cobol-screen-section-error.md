---
title: "[Solution] COBOL SCREEN SECTION Error"
description: "Fix COBOL SCREEN SECTION errors in terminal-based programs including invalid screen item attributes."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

SCREEN SECTION errors occur when screen items have invalid attributes, conflicting display properties, or are referenced before being defined.

## Common Causes

- Screen item attributes incompatible with terminal type
- Missing BLANK SCREEN before screen display
- OVERLAP between screen items on same position
- PIC clause unsupported in SCREEN SECTION

## How to Fix

### 1. Define complete screen items

```cobol
SCREEN SECTION.
01 TEST-SCREEN.
    05 LINE 1 COL 1 VALUE 'Name: '.
    05 S-NAME PIC X(20) LINE 1 COL 7 AUTO.
```

### 2. Use BLANK SCREEN to clear

```cobol
DISPLAY BLANK SCREEN.
DISPLAY TEST-SCREEN.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SCREEN-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-NAME  PIC X(20) VALUE 'Test User'.

PROCEDURE DIVISION.
    DISPLAY 'Name: ' WS-NAME.
    STOP RUN.
```

## Related Errors

- [COBOL Display Error](../cobol-display-error)
- [COBOL Runtime Error](../cobol-runtime-error)
- [COBOL PIC Clause Error](../cobol-pic-clause)
