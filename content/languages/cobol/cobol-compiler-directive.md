---
title: "[Solution] COBOL Compiler Directive Error"
description: "Fix COBOL compiler directive errors caused by incorrect COPY, REPLACE, or conditional compilation usage."
languages: ["cobol"]
error-types: ["compiler-error"]
severities: ["error"]
---

Compiler directive errors occur when COPY, REPLACE, or conditional compilation directives contain syntax errors or reference missing copybooks.

## Common Causes

- COPY statement referencing a nonexistent copybook
- Incorrect COPYREPLACING syntax
- Mismatched REPLACE delimiters
- Nested COPY statements causing naming conflicts

## How to Fix

### 1. Verify copybook exists in the copy path

```cobol
*> WRONG: Copybook not found
COPY NONEXISTENT-COPYBOOK.

*> CORRECT: Verify path and spelling
COPY CUSTOMER-RECORD.
```

### 2. Fix REPLACE syntax

```cobol
*> WRONG: Mismatched delimiters
REPLACE ==OLD-TEXT== BY NEW-TEXT.

*> CORRECT: Match delimiters on both sides
REPLACE ==OLD-TEXT== BY ==NEW-TEXT==.
```

### 3. Use COPYREPLACING properly

```cobol
COPY CUSTOMER-REPLACING
    == cust-name == BY == customer-name ==
    == cust-id   == BY == customer-id ==.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. COMPILER-DIRECTIVE-DEMO.

COPY ERROR-DEFS.

PROCEDURE DIVISION.
    DISPLAY 'Compiler directive demo complete'.
    STOP RUN.
```

## Related Errors

- [COBOL Copy Error](../cobol-copy-error-new)
- [COBOL Copybook Error](../cobol-copybook-error)
- [COBOL Replacing Error](../cobol-replacing-error)
