---
title: "[Solution] COBOL: syntax error or invalid character"
description: "Fix COBOL syntax errors by correcting punctuation and following strict COBOL grammar rules."
languages: ["cobol"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A COBOL syntax error occurs when the compiler encounters code that violates the COBOL language grammar. This includes invalid characters, incorrect punctuation, words in wrong positions, and statements that do not follow COBOL syntax rules. COBOL is particularly strict about formatting: code must start in specific columns, punctuation must be exact, and reserved words must be used correctly. Syntax errors prevent compilation entirely and must be fixed before the program can be built.

## Why It Happens

COBOL syntax errors stem from the language's rigid formatting requirements. Characters outside the allowed set (uppercase A-Z, 0-9, and specific punctuation) trigger errors in strict compilers. Missing periods at the end of sentences, which in COBOL terminate statements, cause cascading syntax errors. Using commas where periods are required, or vice versa, confuses the compiler. Reserved words used as variable names produce errors. Incorrect column positioning, where code starts before column 8 in fixed-format source, is a frequent cause of cryptic syntax errors. Mismatched parentheses in expressions, missing keywords like END-IF or END-PERFORM, and improper use of figurative constants also trigger this error.

## How to Fix It

**Follow COBOL column rules for fixed format:**

```cobol
       IDENTIFICATION DIVISION.          *> Starts in Area A (cols 8-11)
       PROGRAM-ID. HELLO-WORLD.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-MESSAGE PIC X(13) VALUE 'Hello, World!'.

       PROCEDURE DIVISION.               *> Starts in Area A
       MAIN-PARAGRAPH.                   *> Paragraph name in Area A
           DISPLAY WS-MESSAGE.           *> Statements in Area B (cols 12-72)
           STOP RUN.
```

**Use proper punctuation:**

```cobol
       * WRONG: missing period at end of sentence
       * DISPLAY 'Hello'
       * DISPLAY 'World'

       * WRONG: comma where period needed
       * DISPLAY 'Hello',
       * DISPLAY 'World',

       * CORRECT: period terminates each sentence
       DISPLAY 'Hello'.
       DISPLAY 'World'.
```

**Avoid reserved words as identifiers:**

```cobol
       * WRONG: using COBOL reserved words
       * 01  MOVE PIC X(10).
       * 01  DISPLAY PIC X(10).
       * 01  IF PIC X(10).

       * CORRECT: use unique names
       01  WS-MOVE PIC X(10).
       01  WS-DISPLAY PIC X(10).
       01  WS-CONDITION PIC X(10).
```

**Fix mismatched delimiters:**

```cobol
       * WRONG: missing END-IF
       * IF WS-X > 0
       *     DISPLAY 'Positive'
       * END-PERFORM.

       * CORRECT: matching delimiters
       IF WS-X > 0
           DISPLAY 'Positive'
       END-IF.
```

**Remove invalid characters:**

```cobol
       * WRONG: special characters not allowed
       * 01  WS-NAME PIC A(20) VALUE 'John's'.

       * CORRECT: escape quotes properly
       01  WS-NAME PIC A(20) VALUE 'John' 's'.
       * Or use QUOTE special register
       MOVE QUOTE TO WS-NAME.
```

## Common Mistakes

- Forgetting that every COBOL sentence must end with a period
- Using free-format coding in a fixed-format compiler without the appropriate compiler flag
- Mixing up PIC X (alphanumeric) and PIC 9 (numeric) for data that does not match
- Not closing all opened IF, EVALUATE, PERFORM, and READ statements with matching terminators
- Copying code from word processors that replace standard quotes with smart quotes

## Related Pages

- [Undefined paragraph in COBOL](/languages/cobol/cobol-undefined-paragraph-new)
- [Copybook not found in COBOL](/languages/cobol/cobol-copy-error-new)
- [Linkage section error in COBOL](/languages/cobol/cobol-linkage-section-new)
- [Division by zero in COBOL](/languages/cobol/cobol-division-by-zero-v2)
