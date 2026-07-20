---
title: "[Solution] COBOL PERFORM THRU — Paragraph Execution"
description: "Fix COBOL PERFORM THRU errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1098
---

PERFORM THRU executes a range of paragraphs. Errors involve executing paragraphs out of order, falling through the end paragraph, or THRU to a paragraph that does not exist.

## Common Causes

- The end paragraph of THRU does not exist
- Code after the THRU target executes unexpectedly (fall-through)
- Circular THRU references
- Using THRU when a simple PERFORM would suffice

## How to Fix

### 1. Always have a clear exit paragraph

```cobol
PROCEDURE DIVISION.
    PERFORM PROCESS-DATA THRU PROCESS-EXIT
    STOP RUN.

PROCESS-DATA.
    DISPLAY 'Processing'.
    *> ... work ...
    GO TO PROCESS-EXIT.

PROCESS-EXIT.
    EXIT.
```

### 2. Use EXIT PARAGRAPH to stop execution

```cobol
PROCESS-DATA.
    IF WS-ERROR
        DISPLAY 'Error'
        EXIT PARAGRAPH
    END-IF
    DISPLAY 'OK'.
```

### 3. Use PERFORM VARYING for loops

```cobol
PERFORM VARYING WS-I FROM 1 BY 1
        UNTIL WS-I > 10
    DISPLAY WS-I
END-PERFORM
```

### 4. Check that THRU target is reachable

```cobol
PERFORM PARA-A THRU PARA-C.
*> All three paragraphs (A, B, C) execute in order
```

### 5. Use EXIT SECTION to leave an entire section

```cobol
PROCESS-SECTION.
    PARA-1.
        DISPLAY 'Step 1'.
    PARA-2.
        DISPLAY 'Step 2'.
    EXIT SECTION.
```

## Examples

PERFORM THRU with proper exit handling:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. PERFORM-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-COUNTER      PIC 9(3) VALUE 0.
01  WS-MAX          PIC 9(3) VALUE 5.

PROCEDURE DIVISION.
    PERFORM COUNT-UP THRU COUNT-EXIT
    DISPLAY 'Final: ' WS-COUNTER
    STOP RUN.

COUNT-UP.
    ADD 1 TO WS-COUNTER
    IF WS-COUNTER < WS-MAX
        GO TO COUNT-UP
    END-IF.

COUNT-EXIT.
    EXIT.
```

## Related Errors

- [COBOL PERFORM VARYING Error](../cobol-perform-varying)
- [COBOL PERFORM UNTIL Error](../cobol-perform-until)
- [COBOL PERFORM Error](../cobol-perform-error)
