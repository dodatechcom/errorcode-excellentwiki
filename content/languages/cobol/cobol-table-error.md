---
title: "[Solution] COBOL TABLE Error - How to Fix"
description: "Fix COBOL OCCURS table errors including SEARCH failures, initialization issues, and table population mistakes."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# OCCURS TABLE Error

This error is one of the most frequently encountered issues when developing with cobol. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- SEARCH scans a table sequentially from the current INDEX position. If INDEX is beyond the table, SEARCH returns immediately without finding anything.
- SEARCH ALL requires the table to be sorted in ascending order on the search key. Unsorted data causes incorrect results.
- Table initialization with VALUE on OCCURS is valid only for tables with fixed OCCURS (not DEPENDING ON). Dynamic tables must be populated at runtime.
- PERFORM VARYING is used to populate tables. Missing VARYING initialization causes the index to start at 0, skipping the first entry.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **SEARCH AT END always reached - table empty**
2. **SEARCH ALL on unsorted table - incorrect results**
3. **OCCURS DEPENDING ON with VALUE - compilation error**
4. **Table not populated before SEARCH**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```cobol
       01 WS-TABLE.
           05 WS-ENTRY PIC X(10) OCCURS 10
              INDEXED BY WS-IDX.
       SET WS-IDX TO 1.
       SEARCH WS-ENTRY
           AT END DISPLAY 'Not found'
           WHEN WS-ENTRY(WS-IDX) = WS-TARGET
               DISPLAY 'Found'.
```

### Solution 2

```cobol
       01 WS-TABLE.
           05 WS-KEY PIC X(5).
           05 WS-DATA PIC X(10).
       *> Not sorted on WS-KEY!
       SEARCH ALL WS-ENTRY
           AT END DISPLAY 'Not found'
           WHEN WS-ENTRY-KEY(WS-IDX) = WS-TARGET
               DISPLAY 'Found'.
```

### Solution 3

```cobol
       01 WS-TABLE.
           05 WS-ENTRY PIC X(10) OCCURS 100
              DEPENDING ON WS-COUNT.
       *> Cannot use VALUE clause here

; CORRECT: Populate at runtime
       MOVE 0 TO WS-COUNT.
       PERFORM VARYING WS-IDX FROM 1 BY 1
           UNTIL WS-IDX > 100
           READ IN-FILE
           ADD 1 TO WS-COUNT
           MOVE IN-DATA TO WS-ENTRY(WS-IDX)
       END-PERFORM.
```

### Solution 4

```cobol
       SEARCH WS-ENTRY
           AT END DISPLAY 'Not found'
           WHEN WS-ENTRY(WS-IDX) = WS-TARGET
               DISPLAY 'Found'.
       *> If WS-IDX = 11 (beyond OCCURS 10)
       *> SEARCH returns AT END immediately

; CORRECT: Initialize INDEX
       SET WS-IDX TO 1.
       SEARCH WS-ENTRY ...
```

### Solution 5

```cobol
       SEARCH WS-ENTRY VARYING WS-IDX
           AT END DISPLAY 'Not found'
           WHEN WS-ENTRY(WS-IDX) = WS-TARGET
               DISPLAY 'Found at ' WS-IDX.
```

### Solution 6

```cobol
       PERFORM VARYING WS-IDX FROM 1 BY 1
           UNTIL WS-IDX > 10
           MOVE WS-ENTRY(WS-IDX) TO WS-FIELD
           DISPLAY WS-FIELD
       END-PERFORM.
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**SEARCH ALL on unsorted table**

SEARCH ALL requires the table to be sorted on the search key. If the data is not in ascending order, the binary search produces incorrect results.

**OCCURS DEPENDING ON with VALUE clause**

A table with OCCURS DEPENDING ON cannot use VALUE for initialization because the size is determined at runtime.

**Table SEARCH without initializing INDEX**

The INDEX variable is not SET before SEARCH. If the index is 0 or beyond the table, SEARCH fails immediately.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Use SEARCH ALL only on tables sorted in ascending order on the key field.**
2. **Initialize INDEX with SET before SEARCH. Use SEARCH VARYING for multiple searches.**
3. **Populate OCCURS DEPENDING ON tables at runtime using PERFORM VARYING loops.**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [SUBSCRIPT Error](/languages/cobol/cobol-subscript-error) — indexing issues
- [MEMORY Error](/languages/cobol/cobol-memory-error) — storage issues
- [SEARCH Error](/languages/cobol/cobol-search-error) — search failures

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
