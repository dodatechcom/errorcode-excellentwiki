---
title: "[Solution] COBOL STRING Statement Error - How to Fix"
description: "Fix COBOL STRING and UNSTRING statement errors including delimiter handling, overflow, and pointer manipulation issues."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# STRING Statement Error

This error is one of the most frequently encountered issues when developing with cobol. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- STRING concatenates delimited data into a receiving field. If the result exceeds the receiving field length, an overflow occurs and the field is partially filled.
- UNSTRING splits a delimited string into individual fields. Incorrect DELIMITER specification causes fields to be parsed with wrong boundaries.
- The POINTER clause tracks position in the receiving field. Starting at position 0 or exceeding the field length causes an error.
- DELIMITED BY SIZE means use as much of the sending field as fits. DELIMITED BY space stops at the first space character.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **STRING overflow - receiving field too small**
2. **UNSTRING delimiter mismatch - wrong field boundaries**
3. **STRING POINTER out of range**
4. **DELIMITED BY space vs SIZE confusion**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```cobol
       STRING WS-FIRST WS-LAST
           DELIMITED BY SIZE
           INTO WS-FULL-NAME.
       *> If WS-FIRST + WS-LAST > WS-FULL-NAME length

; CORRECT: Ensure receiving field is large enough
       01 WS-FULL-NAME PIC X(60).
       STRING WS-FIRST ' ' WS-LAST
           DELIMITED BY SIZE
           INTO WS-FULL-NAME.
```

### Solution 2

```cobol
       UNSTRING WS-CSV
           DELIMITED BY ','
           INTO WS-FIELD1 WS-FIELD2 WS-FIELD3.
       *> If data has 'A,B,C' but WS-FIELD1 is PIC 9(5)
       *> alpha data in numeric field causes S0C7

; CORRECT: Match field types
       01 WS-CSV PIC X(20).
       01 WS-FIELD1 PIC X(5).
       01 WS-FIELD2 PIC X(5).
       01 WS-FIELD3 PIC X(5).
```

### Solution 3

```cobol
       STRING WS-A INTO WS-B
           WITH POINTER WS-POS.
       *> WS-POS starts at 0

; CORRECT: Initialize POINTER
       MOVE 1 TO WS-POS.
       STRING WS-A INTO WS-B
           WITH POINTER WS-POS.
```

### Solution 4

```cobol
       STRING WS-A DELIMITED BY SPACE
           INTO WS-B.
       *> If WS-A = 'Hello  World' (two spaces)
       *> Only 'Hello' is captured

; CORRECT: Use DELIMITED BY SIZE if needed
       STRING WS-A DELIMITED BY SIZE
           INTO WS-B.
```

### Solution 5

```cobol
       UNSTRING WS-CSV
           DELIMITED BY ','
           INTO WS-FIELD1 WS-FIELD2
           WITH POINTER WS-POS
           TALLYING IN WS-COUNT.
       *> TALLYING counts fields actually parsed

; CORRECT: Check TALLYING result
       IF WS-COUNT NOT = 2
           DISPLAY 'Wrong number of fields'.
```

### Solution 6

```cobol
       MOVE 1 TO WS-POS.
       STRING 'Hello' ' ' 'World'
           DELIMITED BY SIZE
           INTO WS-RESULT
           WITH POINTER WS-POS.
       DISPLAY WS-RESULT. *> 'Hello World'
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**STRING overflow truncates data**

The receiving field is too short to hold all concatenated data. Data beyond the field length is silently lost.

**UNSTRING with multiple delimiters**

The data contains delimiters that are not accounted for, causing fields to be merged incorrectly.

**STRING POINTER initialized to 0**

COBOL STRING POINTER must start at 1. Starting at 0 causes an out-of-range error.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Size receiving fields to accommodate maximum expected STRING output.**
2. **Use TALLYING to verify UNSTRING parsed the expected number of fields.**
3. **Always initialize STRING POINTER to 1 before the first STRING/UNSTRING operation.**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [REPLACING Error](/languages/cobol/cobol-replacing-error) — text substitution
- [COPYBOOK Error](/languages/cobol/cobol-copybook-error) — copybook issues
- [FILE STATUS Error](/languages/cobol/cobol-file-status-error) — I/O errors

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
