---
title: "[Solution] COBOL JSON PARSE Error"
description: "Fix COBOL JSON parsing errors including invalid JSON syntax and malformed GENERATE/PARSE statements."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

JSON errors occur when COBOL JSON PARSE or JSON GENERATE statements encounter malformed data or invalid target item declarations.

## Common Causes

- JSON source string has syntax errors
- Target items not properly declared for JSON mapping
- Missing SUPPRESS clause on unwanted fields
- JSON PARSE with non-JSON string data

## How to Fix

### 1. Validate JSON before parsing

```cobol
*> WRONG: Invalid JSON
MOVE '{bad json}' TO WS-JSON-SOURCE.
JSON PARSE WS-JSON-SOURCE INTO WS-TARGET.

*> CORRECT: Valid JSON
MOVE '{"id":1,"name":"test"}' TO WS-JSON-SOURCE.
JSON PARSE WS-JSON-SOURCE INTO WS-TARGET.
```

### 2. Map fields correctly

```cobol
01 WS-TARGET.
    05 WS-ID     PIC 9(4).
    05 WS-NAME   PIC X(20).
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. JSON-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-JSON-SOURCE  PIC X(100) VALUE
    '{"error_code":404,"message":"Not found"}'.
01 WS-TARGET.
    05 WS-ERR-CODE PIC 9(4).
    05 WS-ERR-MSG  PIC X(50).

PROCEDURE DIVISION.
    JSON PARSE WS-JSON-SOURCE
        INTO WS-TARGET
        WITH COPIES.
    DISPLAY 'Error: ' WS-ERR-CODE ' - ' WS-ERR-MSG.
    STOP RUN.
```

## Related Errors

- [COBOL String Error](../cobol-string-error)
- [COBOL Record Error](../cobol-record-error)
- [COBOL Runtime Error](../cobol-runtime-error)
