---
title: "Syntax error"
description: "A syntax error occurs when the COBOL compiler encounters code that violates the language's syntax rules."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["syntax", "compiler", "compilation", "cobol"]
weight: 5
---

## What This Error Means

A syntax error in COBOL occurs when the compiler encounters code that doesn't conform to the language's syntax rules. This is a compile-time error that prevents the program from being built.

## Common Causes

- Missing period at end of sentence
- Incorrect division order
- Missing keywords
- Invalid character usage

## How to Fix

```cobol
      * WRONG: Missing period
       IDENTIFICATION DIVISION
       PROGRAM-ID. MY-PROGRAM

      * CORRECT: Add periods
       IDENTIFICATION DIVISION.
       PROGRAM-ID. MY-PROGRAM.
```

```cobol
      * WRONG: Wrong division order
       DATA DIVISION.
       IDENTIFICATION DIVISION.
       PROGRAM-ID. MY-PROGRAM.

      * CORRECT: Proper division order
       IDENTIFICATION DIVISION.
       PROGRAM-ID. MY-PROGRAM.
       DATA DIVISION.
```

## Examples

```cobol
      * Example 1: Missing period
       PROCEDURE DIVISION
           DISPLAY "Hello"
      * syntax error

      * Example 2: Wrong keyword
       MOVV "hello" TO WS-VAR
      * syntax error: MOVV not valid

      * Example 3: Missing section header
       WORKING-STORAGE.
       01 WS-VAR PIC X(10).
      * syntax error: missing SECTION
```

## Related Errors

- [End of file](/languages/cobol/end-of-file)
- [Decimal precision error](/languages/cobol/decimal-error)
