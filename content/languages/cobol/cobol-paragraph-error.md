---
title: "[Solution] COBOL Paragraph Error"
description: "Fix COBOL paragraph errors including missing periods, unreachable paragraphs, and duplicate paragraph names."
languages: ["cobol"]
error-types: ["syntax-error"]
severities: ["error"]
---

Paragraph errors occur when COBOL paragraphs are missing their terminating periods, have duplicate names, or are unreachable due to flow control issues.

## Common Causes

- Missing period at end of paragraph
- Two paragraphs with the same name
- Paragraph defined but never referenced
- Period placed in wrong position in compound IF

## How to Fix

### 1. End each paragraph with a period

```cobol
*> WRONG: Missing period
PROCEDURE DIVISION.
    DISPLAY 'Hello'
    DISPLAY 'World'.

*> CORRECT
PROCEDURE DIVISION.
    DISPLAY 'Hello'.
    DISPLAY 'World'.
```

### 2. Use unique paragraph names

```cobol
*> WRONG: Duplicate
PROCESS-DATA.
    ADD 1 TO WS-COUNT.
PROCESS-DATA.
    DISPLAY 'Done'.

*> CORRECT
PROCESS-DATA-COUNT.
    ADD 1 TO WS-COUNT.
PROCESS-DATA-DISPLAY.
    DISPLAY 'Done'.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. PARAGRAPH-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-COUNT  PIC 9(4) VALUE 0.

PROCEDURE DIVISION.
    INITIALIZE-SECTION.
    MOVE 0 TO WS-COUNT.
    PROCESS-DATA.
    ADD 1 TO WS-COUNT.
    DISPLAY 'Count: ' WS-COUNT.
    STOP RUN.
```

## Related Errors

- [COBOL Syntax Error](../cobol-syntax-error-new)
- [COBOL Perform Error](../cobol-perform-error)
- [COBOL Undefined Paragraph](../cobol-undefined-paragraph-new)
