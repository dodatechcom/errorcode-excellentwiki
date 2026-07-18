---
title: "[Solution] COBOL SUBSCRIPT Error - How to Fix"
description: "Fix COBOL subscript and INDEX errors when accessing OCCURS tables, including bounds violations and indexing mistakes."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# SUBSCRIPT or INDEX Error

This error is one of the most frequently encountered issues when developing with cobol. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- Subscripts must be within the OCCURS bounds. A subscript of 0 or exceeding the OCCURS count causes S0C4 (storage protection exception).
- INDEX is optimized for table access and uses binary search. SUBSCRIPT uses arithmetic. Mixed INDEX and SUBSCRIPT causes errors.
- INDEX BY creates a compressed binary index. Using a regular variable as a subscript works but is less efficient than INDEX.
- REVERSED subscripts (larger to smaller) are valid but can cause unexpected behavior with some compiler optimizations.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **S0C4 - Subscript out of bounds**
2. **INDEX used where SUBSCRIPT expected (or vice versa)**
3. **INDEX BY not declared for table**
4. **Mixed INDEX and SUBSCRIPT in same PERFORM**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```cobol
       01 WS-TABLE.
           05 WS-ENTRY PIC X(10) OCCURS 10.
       MOVE WS-ENTRY(15) TO WS-FIELD.
       *> S0C4: subscript 15 > max 10

; CORRECT: Check bounds
       IF WS-IDX >= 1 AND WS-IDX <= 10
           MOVE WS-ENTRY(WS-IDX) TO WS-FIELD.
```

### Solution 2

```cobol
       01 WS-TABLE.
           05 WS-ENTRY PIC X(10) OCCURS 10
              INDEXED BY WS-IDX.
       SET WS-IDX TO 5.
       MOVE WS-ENTRY(WS-IDX) TO WS-FIELD.
       *> Correct use of INDEX
```

### Solution 3

```cobol
       01 WS-TABLE.
           05 WS-ENTRY PIC X(10) OCCURS 10.
       PERFORM VARYING WS-SUB FROM 1 BY 1
           UNTIL WS-SUB > 10
           MOVE WS-ENTRY(WS-SUB) TO WS-FIELD
       END-PERFORM.
```

### Solution 4

```cobol
       01 WS-TABLE.
           05 WS-ENTRY PIC X(10) OCCURS 10
              INDEXED BY WS-IDX.
       SEARCH WS-ENTRY
           AT END DISPLAY 'Not found'
           WHEN WS-ENTRY(WS-IDX) = WS-TARGET
               DISPLAY 'Found at ' WS-IDX.
```

### Solution 5

```cobol
       01 WS-TABLE.
           05 WS-ROW OCCURS 10.
              10 WS-COL PIC 9(5) OCCURS 20.
       MOVE 99999 TO WS-COL(5)(10).
```

### Solution 6

```cobol
       PERFORM VARYING WS-IDX FROM 10 BY -1
           UNTIL WS-IDX < 1
           MOVE WS-ENTRY(WS-IDX) TO WS-FIELD
       END-PERFORM.
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**S0C4 abend from subscript exceeding OCCURS count**

The subscript variable contains a value greater than the maximum OCCURS count or less than 1 (if no LOWER BOUNDS).

**INDEX BY not declared**

The table is accessed with INDEX syntax but no INDEXED BY clause exists in the OCCURS definition.

**Mixed INDEX and SUBSCRIPT in SEARCH**

A SEARCH statement uses INDEX for the SET clause but SUBSCRIPT for the WHEN condition.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Always validate subscripts before table access, checking both lower and upper bounds.**
2. **Declare INDEXED BY on frequently searched tables and use SET/SEARCH for efficient lookups.**
3. **Use SEARCH ALL for binary search on sorted tables; ensure the key field is in ascending order.**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [MEMORY Error](/languages/cobol/cobol-memory-error) — storage issues
- [RECORD Error](/languages/cobol/cobol-record-error) — record layout
- [TABLE Error](/languages/cobol/cobol-table-error) — table operations

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
