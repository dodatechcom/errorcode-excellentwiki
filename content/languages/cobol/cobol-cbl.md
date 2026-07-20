---
title: "[Solution] COBOL CBL — Compiler Directive"
description: "Fix COBOL CBL compiler directive errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1121
---

The CBL (or CALL-INTERFACE) directive provides compiler-specific options. Errors involve unsupported directives, wrong syntax, or using CBL where standard COBOL should be used.

## Common Causes

- CBL directive not supported by the target compiler
- Wrong syntax for the specific compiler (IBM, Micro Focus, GnuCOBOL)
- Using CBL for options that have standard COBOL equivalents
- Missing end-of-directive marker

## How to Fix

### 1. Check compiler documentation

```cobol
*> IBM COBOL
CBL NOLIB,NOXREF

*> Micro Focus
CBL DELAY,NOFORMATTED

*> GnuCOBOL
*> Usually uses compiler flags, not CBL
```

### 2. Use standard alternatives when possible

```cobol
*> Instead of CBL, use compiler flags:
*> cobc -std=cobol85 -free myprog.cbl
```

### 3. Check for duplicate directives

```cobol
CBL NOLIB
CBL NOLIB  *> duplicate, may cause warning
```

### 4. Use appropriate compiler options

```cobol
*> Debug options
CBL LIST,MAP,XREF
```

### 5. Use CONTROL DIVISION for portable options

```cobol
CONTROL DIVISION.
OPTIONS.
    OPTION 'COBOL85'.
```

## Examples

Common CBL directives:

```cobol
*> Suppress listing
CBL NOLIST

*> Enable debugging
CBL TEST,LIST

*> Control alignment
CBL ALIGN,NOALIGN

*> Map generation
CBL MAP,XREF
```

## Related Errors

- [COBOL IDENTIFICATION DIVISION Error](../cobol-identification-division)
- [COBOL ENVIRONMENT DIVISION Error](../cobol-environment-division)
- [COBOL DATA DIVISION Error](../cobol-data-division)
