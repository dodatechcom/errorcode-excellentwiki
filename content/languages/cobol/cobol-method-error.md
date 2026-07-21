---
title: "[Solution] COBOL Method Invocation Error"
description: "Fix COBOL method call errors including invalid INVOKE syntax and missing method implementations in OO COBOL."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
---

Method invocation errors occur in Object-Oriented COBOL when INVOKE statements reference invalid methods or when the target object is NULL.

## Common Causes

- INVOKE on a NULL object reference
- Method name does not exist in the class hierarchy
- Wrong number or types of arguments
- Missing factory or object constructor

## How to Fix

### 1. Verify object is initialized

```cobol
*> WRONG: Object not instantiated
SET MY-OBJECT TO NULL.
INVOKE MY-OBJECT 'PROCESS'.

*> CORRECT: Create object first
SET MY-OBJECT TO NEW MY-CLASS.
INVOKE MY-OBJECT 'PROCESS'.
```

### 2. Match method signature

```cobol
INVOKE MY-OBJECT 'SET-VALUE' USING BY VALUE 100.
```

## Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. METHOD-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 MY-OBJECT  OBJECT REFERENCE.

PROCEDURE DIVISION.
    SET MY-OBJECT TO NEW 'MY-CLASS'.
    INVOKE MY-OBJECT 'DO-SOMETHING'.
    STOP RUN.
```

## Related Errors

- [COBOL Call Statement Error](../cobol-call-statement)
- [COBOL Nested Call Error](../cobol-nested-call-error)
- [COBOL Runtime Error](../cobol-runtime-error)
