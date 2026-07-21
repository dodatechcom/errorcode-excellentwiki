---
title: "[Solution] COBOL CALL BY CONTENT Error"
description: "Fix COBOL CALL BY CONTENT errors when passing values instead of references to subprograms."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

CALL BY CONTENT errors occur when passing values to a subprogram when references are expected, or when the receiving parameter modifies the passed content.

## Common Causes

- BY CONTENT prevents modification but callee expects BY REFERENCE
- Wrong parameter size passed with BY CONTENT
- Using BY CONTENT when BY REFERENCE is needed for performance
- Parameter type mismatch with BY CONTENT

## How to Fix

### 1. Match passing mode to intent

```cobol
*> WRONG: Modifying a BY CONTENT parameter
CALL 'SUB-PROG' USING BY CONTENT WS-DATA.

*> CORRECT: Use BY REFERENCE for output parameters
CALL 'SUB-PROG' USING BY REFERENCE WS-DATA.
```

### 2. Use BY VALUE for primitives

```cobol
CALL 'C-FUNC' USING BY VALUE WS-INTEGER.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. BY-CONTENT-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-INPUT   PIC 9(4) VALUE 42.
01 WS-OUTPUT  PIC 9(4) VALUE 0.

PROCEDURE DIVISION.
    CALL 'SUB-PROCESS' USING BY CONTENT WS-INPUT
                             BY REFERENCE WS-OUTPUT.
    DISPLAY 'Output: ' WS-OUTPUT.
    STOP RUN.
```

## Related Errors

- [COBOL Call Statement Error](../cobol-call-statement)
- [COBOL Linkage Section Error](../cobol-linkage-section)
- [COBOL Subprogram Error](../cobol-subprogram-error)
