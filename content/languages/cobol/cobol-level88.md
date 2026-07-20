---
title: "[Solution] COBOL 88 Level — Condition Names"
description: "Fix COBOL 88 level condition name errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1086
---

Level 88 defines condition names (boolean-like flags) for a parent field. Errors involve wrong values, missing 88 entries, or using condition names in inappropriate contexts.

## Common Causes

- 88 level values do not match the parent PIC format
- Missing VALUE clause on 88 level items
- Using 88 level where a regular field comparison is needed
- 88 level values that overlap unintentionally

## How to Fix

### 1. Define 88 levels with correct values

```cobol
01 WS-STATUS      PIC X(1).
    88 WS-ACTIVE      VALUE 'A'.
    88 WS-INACTIVE    VALUE 'I'.
    88 WS-DELETED     VALUE 'D'.
```

### 2. Use 88 in conditionals

```cobol
IF WS-ACTIVE
    DISPLAY 'Record is active'
ELSE-IF WS-DELETED
    DISPLAY 'Record is deleted'
END-IF.
```

### 3. Use 88 with VALUE ALL for ranges

```cobol
01 WS-CODE        PIC 9(2).
    88 WS-VALID     VALUE 1 THRU 50.
    88 WS-INVALID   VALUE 51 THRU 99.
```

### 4. Set 88 conditions with SET

```cobol
SET WS-ACTIVE TO TRUE.
SET WS-VALID TO TRUE.
```

### 5. Use 88 for table searches

```cobol
01 WS-TYPE        PIC X(1).
    88 WS-TYPE-A    VALUE 'A'.
    88 WS-TYPE-B    VALUE 'B'.
    88 WS-TYPE-C    VALUE 'C'.
```

## Examples

Complete 88 level usage:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. LEVEL88-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ORDER-STATUS    PIC 9(1).
    88 WS-PENDING     VALUE 1.
    88 WS-PROCESSING  VALUE 2.
    88 WS-SHIPPED     VALUE 3.
    88 WS-DELIVERED   VALUE 4.
    88 WS-CANCELLED   VALUE 5.

01 WS-VALID-FLAG      PIC X(1).
    88 WS-IS-VALID    VALUE 'Y'.
    88 WS-IS-INVALID  VALUE 'N'.

PROCEDURE DIVISION.
    MOVE 2 TO WS-ORDER-STATUS.
    IF WS-PROCESSING
        DISPLAY 'Order is being processed'
    END-IF.
    SET WS-IS-VALID TO TRUE.
    IF WS-IS-VALID
        DISPLAY 'Order is valid'
    END-IF.
    STOP RUN.
```

## Related Errors

- [COBOL PIC Clause Error](../cobol-pic-clause)
- [COBOL EVALUATE Error](../cobol-evaluate-error)
- [COBOL SEARCH ALL Error](../cobol-search-all)
