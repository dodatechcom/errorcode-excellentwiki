---
title: "[Solution] COBOL XML PARSE Error"
description: "Fix COBOL XML parsing errors including malformed XML input and incorrect XML GENERATE/PARSE targets."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

XML parsing errors occur when COBOL XML PARSE or XML GENERATE statements encounter malformed XML or invalid target item declarations.

## Common Causes

- Malformed XML source string
- Missing XML PARSE EVENT procedures
- Target items not matching XML structure
- XML GENERATE with non-XML-able data items

## How to Fix

### 1. Validate XML before parsing

```cobol
*> WRONG: Malformed XML
MOVE '<root><unclosed>' TO WS-XML-SOURCE.
XML PARSE WS-XML-SOURCE
    PROCESSING PROCEDURE XML-HANDLER.

*> CORRECT: Well-formed XML
MOVE '<root><item>value</item></root>' TO WS-XML-SOURCE.
```

### 2. Define proper event handler

```cobol
XML PARSE WS-XML-SOURCE
    PROCESSING PROCEDURE XML-HANDLER.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. XML-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-XML-SOURCE  PIC X(100) VALUE
    '<error><code>404</code><msg>Not found</msg></error>'.
01 WS-ERROR-CODE  PIC 9(4).
01 WS-ERROR-MSG   PIC X(50).

PROCEDURE DIVISION.
    DISPLAY 'XML source: ' WS-XML-SOURCE.
    STOP RUN.
```

## Related Errors

- [COBOL JSON Error](../cobol-json-error)
- [COBOL Runtime Error](../cobol-runtime-error)
- [COBOL String Error](../cobol-string-error)
