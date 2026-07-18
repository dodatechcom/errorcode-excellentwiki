---
title: "[Solution] COBOL: undefined paragraph name error"
description: "Fix COBOL undefined paragraph errors by verifying definitions and checking PERFORM target names."
languages: ["cobol"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A COBOL undefined paragraph error occurs when a PERFORM statement, GO TO statement, or SECTION reference targets a paragraph or section name that does not exist in the program. The compiler cannot locate the named paragraph in any visible scope. This error indicates that the program is trying to transfer control to a location that was either never defined, has a misspelled name, or is defined in a scope that is not accessible from the current context.

## Why It Happens

Undefined paragraph errors result from several situations. The most common is a typo in the paragraph name referenced by a PERFORM or GO TO statement. Paragraph names in COBOL are case-insensitive but must match exactly otherwise. A paragraph that was defined in one section but referenced from another section may not be visible depending on the PERFORM syntax used. GO TO statements that reference paragraphs defined after the current paragraph in the same section may not be found by some compilers. Paragraphs defined inside copybooks that were not properly copied into the source will appear undefined. Conditional compilation or copy-replacing directives that modify paragraph names can also cause mismatches. Using a section name where a paragraph name was intended, or vice versa, triggers this error.

## How to Fix It

**Verify paragraph names match exactly:**

```cobol
       PROCEDURE DIVISION.
       MAIN-LOGIC.
           PERFORM INITIALIZE-PROGRAM.    *> Must match paragraph name
           PERFORM PROCESS-RECORDS.
           PERFORM CLEANUP-PROGRAM.
           STOP RUN.

       INITIALIZE-PROGRAM.                *> Exact name required
           MOVE SPACES TO WS-RECORD.
           MOVE ZERO TO WS-COUNTER.

       PROCESS-RECORDS.
           READ INPUT-FILE
               AT END
                   MOVE 'Y' TO WS-EOF
               NOT AT END
                   PERFORM WRITE-OUTPUT
           END-READ.

       WRITE-OUTPUT.
           WRITE OUTPUT-RECORD FROM WS-RECORD.

       CLEANUP-PROGRAM.
           CLOSE INPUT-FILE OUTPUT-FILE.
```

**Check PERFORM with inline target:**

```cobol
       PROCEDURE DIVISION.
       MAIN.
           PERFORM VARYING WS-I FROM 1 BY 1
               UNTIL WS-I > 10
               DISPLAY WS-I
           END-PERFORM.

           *> PERFORM a paragraph
           PERFORM CALCULATE-TOTAL.

           *> PERFORM a section
           PERFORM SUMMARIZE SECTION.

       CALCULATE-TOTAL.
           COMPUTE WS-TOTAL = WS-A + WS-B.

       SUMMARIZE SECTION.
       SUMMARIZE-PARAGRAPH.
           DISPLAY 'Total: ' WS-TOTAL.
```

**Use correct scope for cross-section references:**

```cobol
       PROCEDURE DIVISION.
       SECTION-A.
       PARA-A1.
           PERFORM SECTION-B-PARA-B1.  *> Can reference any paragraph
           GO TO PARA-A2.

       PARA-A2.
           DISPLAY 'Back in Section A'.

       SECTION-B.
       SECTION-B-PARA-B1.              *> Paragraph in Section B
           DISPLAY 'In Section B'.
```

**Ensure copybooks are properly included:**

```cobol
       COPY PARAGRAPHS.  *> Must contain valid paragraph definitions

       *> If PARAGRAPHS copybook contains:
       *> HELLO-PARA.
       *>     DISPLAY 'Hello'.
       *> Then this works:
       PERFORM HELLO-PARA.
```

## Common Mistakes

- Misspelling paragraph names in PERFORM or GO TO statements
- Referencing a paragraph that exists only inside a copybook that was not copied
- Confusing section names with paragraph names in PERFORM statements
- Using GO TO to jump into the middle of a paragraph (undefined behavior)
- Not realizing that paragraph names are unique within a section but not globally

## Related Pages

- [Syntax error in COBOL](/languages/cobol/cobol-syntax-error-new)
- [Copybook not found in COBOL](/languages/cobol/cobol-copy-error-new)
- [Linkage section error in COBOL](/languages/cobol/cobol-linkage-section-new)
- [Runtime error in COBOL](/languages/cobol/cobol-runtime-error-v2)
