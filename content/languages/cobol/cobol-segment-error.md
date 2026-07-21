---
title: "[Solution] COBOL Program Segment Error"
description: "Fix COBOL program segment errors when using overlapping segments or SHAREDCONTROL SECTION directives."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

Segment errors occur when COBOL program segments overlap in memory or when SHAREDCONTROL SECTION is misconfigured in partitioned programs.

## Common Causes

- Segments with overlapping priority numbers
- Missing SHAREDCONTROL SECTION
- Segments referencing uninitialized data from other segments
- Segment size exceeding memory allocation

## How to Fix

### 1. Define non-overlapping segments

```cobol
*> WRONG: Same segment number
SECTION-1 SECTION 50.
SECTION-2 SECTION 50.

*> CORRECT: Unique segment numbers
SECTION-1 SECTION 50.
SECTION-2 SECTION 60.
```

### 2. Initialize shared data

```cobol
SHAREDCONTROL SECTION.
01 WS-Shared PIC X(100) VALUE SPACES.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SEGMENT-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-VALUE  PIC 9(4) VALUE 0.

PROCEDURE DIVISION.
    MOVE 42 TO WS-VALUE.
    DISPLAY 'Segment demo: ' WS-VALUE.
    STOP RUN.
```

## Related Errors

- [COBOL Nested Programs Error](../cobol-nested-programs)
- [COBOL Memory Error](../cobol-memory-error)
- [COBOL Runtime Error](../cobol-runtime-error)
