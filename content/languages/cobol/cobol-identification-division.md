---
title: "[Solution] COBOL IDENTIFICATION DIVISION — Program Header"
description: "Fix COBOL IDENTIFICATION DIVISION errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1122
---

IDENTIFICATION DIVISION is the first division of every COBOL program. Errors involve missing PROGRAM-ID, wrong period placement, or unsupported clauses.

## Common Causes

- Missing PROGRAM-ID paragraph
- Period missing after PROGRAM-ID
- Using AUTHOR, DATE-WRITTEN without proper syntax
- Wrong division name (misspelling)

## How to Fix

### 1. Always include PROGRAM-ID

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. MY-PROGRAM.
```

### 2. Period after PROGRAM-ID is required

```cobol
PROGRAM-ID. MY-PROG.  *> period is mandatory
```

### 3. Add optional paragraphs

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. MY-PROG.
AUTHOR. JOHN DOE.
DATE-WRITTEN. 01 JAN 2026.
SECURITY. CONFIDENTIAL.
```

### 4. Use PROGRAM-ID RECURSIVE for recursive programs

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. RECURSIVE-PROG RECURSIVE.
```

### 5. Check division spelling

```cobol
IDENTIFICATION DIVISION.  *> correct
PROGRAM-ID. MY-PROG.
```

## Examples

A complete IDENTIFICATION DIVISION:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. COMPLETE-PROG.
AUTHOR. DEVELOPER.
DATE-WRITTEN. 2026-07-20.
SECURITY. INTERNAL USE ONLY.

PROCEDURE DIVISION.
    DISPLAY 'Hello from COMPLETE-PROG'.
    STOP RUN.
```

## Related Errors

- [COBOL ENVIRONMENT DIVISION Error](../cobol-environment-division)
- [COBOL DATA DIVISION Error](../cobol-data-division)
- [COBOL Nested Programs Error](../cobol-nested-programs)
