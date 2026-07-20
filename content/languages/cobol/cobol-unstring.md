---
title: "[Solution] COBOL UNSTRING — String Splitting"
description: "Fix COBOL UNSTRING statement errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1105
---

UNSTRING splits a string into multiple fields. Errors involve wrong delimiter, insufficient target fields, or missing TALLYING for count of fields produced.

## Common Causes

- Target fields too small for the split data
- Wrong DELIMITED BY value
- Missing TALLYING clause to count splits
- All delimited by ALL not working as expected

## How to Fix

### 1. Use correct delimiter

```cobol
UNSTRING WS-CSV-RECORD
    DELIMITED BY ','
    INTO WS-FIELD-1
         WS-FIELD-2
         WS-FIELD-3
```

### 2. Use DELIMITED BY ALL for consecutive delimiters

```cobol
UNSTRING WS-DATA
    DELIMITED BY ALL ','
    INTO WS-F1 WS-F2 WS-F3
```

### 3. TALLYING counts how many fields were filled

```cobol
UNSTRING WS-CSV
    DELIMITED BY ','
    INTO WS-A WS-B WS-C
    TALLYING WS-COUNT
```

### 4. Use POINTER for partial unstring

```cobol
MOVE 1 TO WS-PTR.
UNSTRING WS-DATA
    DELIMITED BY ','
    INTO WS-A
    WITH POINTER WS-PTR.
```

### 5. Ensure target sizes are adequate

```cobol
01 WS-SOURCE   PIC X(100) VALUE 'A,B,C,D'.
01 WS-F1       PIC X(10).
01 WS-F2       PIC X(10).
01 WS-F3       PIC X(10).
01 WS-F4       PIC X(10).
```

## Examples

CSV parsing with UNSTRING:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. UNSTRING-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-CSV-LINE   PIC X(100) VALUE 'JOHN,DOE,30,NEW YORK'.
01 WS-FIRST      PIC X(15).
01 WS-LAST       PIC X(15).
01 WS-AGE        PIC X(5).
01 WS-CITY       PIC X(20).
01 WS-COUNT      PIC 9(1).

PROCEDURE DIVISION.
    UNSTRING WS-CSV-LINE
        DELIMITED BY ','
        INTO WS-FIRST
             WS-LAST
             WS-AGE
             WS-CITY
        TALLYING WS-COUNT
    DISPLAY 'Name: ' WS-FIRST ' ' WS-LAST
    DISPLAY 'Age: ' WS-AGE
    DISPLAY 'City: ' WS-CITY
    STOP RUN.
```

## Related Errors

- [COBOL STRING Error](../cobol-string)
- [COBOL INSPECT TALLYING Error](../cobol-inspect-tallying)
- [COBOL Data Movement Error](../cobol-data-movement-error)
