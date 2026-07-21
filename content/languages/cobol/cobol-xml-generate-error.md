---
title: "[Solution] COBOL XML GENERATE Error"
description: "Fix COBOL XML GENERATE errors when converting COBOL data items to XML format output."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

XML GENERATE errors occur when trying to generate XML from COBOL data items that have invalid structures or when the target variable is too small.

## Common Causes

- Target variable too short for generated XML
- Data items with PIC types unsupported by XML GENERATE
- GROUP items with FILLER causing unnamed elements
- SUPPRESS clause misconfiguration

## How to Fix

### 1. Ensure target is large enough

```cobol
*> WRONG: Target too short
01 WS-XML-OUT  PIC X(10).
XML GENERATE WS-XML-OUT FROM WS-DATA.

*> CORRECT: Adequate size
01 WS-XML-OUT  PIC X(1000).
XML GENERATE WS-XML-OUT FROM WS-DATA.
```

### 2. Name all group items

```cobol
*> WRONG: FILLER in group
01 WS-RECORD.
    05 FILLER       PIC X(5).
    05 WS-ID        PIC 9(6).

*> CORRECT: Named items
01 WS-RECORD.
    05 WS-PREFIX    PIC X(5).
    05 WS-ID        PIC 9(6).
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. XML-GEN-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ERROR-REC.
    05 WS-ERR-CODE  PIC 9(4) VALUE 500.
    05 WS-ERR-MSG   PIC X(50) VALUE 'Internal Server Error'.
01 WS-XML-OUTPUT  PIC X(500).

PROCEDURE DIVISION.
    XML GENERATE WS-XML-OUTPUT FROM WS-ERROR-REC.
    DISPLAY 'Generated XML: ' WS-XML-OUTPUT.
    STOP RUN.
```

## Related Errors

- [COBOL XML Error](../cobol-xml-error)
- [COBOL JSON Error](../cobol-json-error)
- [COBOL Record Error](../cobol-record-error)
