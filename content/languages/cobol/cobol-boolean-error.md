---
title: "[Solution] COBOL Boolean Type Error - How to Fix"
description: "Fix COBOL boolean TYPE and condition name errors when using 88-level conditions and conditional expressions."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Boolean TYPE or Condition Name Error

This error is one of the most frequently encountered issues when developing with cobol. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- 88-level condition names define boolean-like conditions based on the parent field value. Incorrect values cause the condition to never evaluate to TRUE.
- 88-level values can be single values, ranges (THRU), or multiple values separated by spaces. Syntax errors in VALUE clauses cause compilation failures.
- BOOLEAN TYPE requires specific syntax. Not all COBOL compilers support native boolean types.
- Condition names with 88 level can be used in IF, EVALUATE, and SEARCH WHEN clauses.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **88-level condition never TRUE - value mismatch**
2. **88-level VALUE syntax error - THRU not working**
3. **BOOLEAN TYPE not supported by compiler**
4. **Condition name used in wrong context**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```cobol
       01 WS-CODE PIC X(1).
           88 VALID-CODE VALUES 'A' 'B' 'C'.
       IF VALID-CODE
           DISPLAY 'Valid'.
       *> If WS-CODE = 'D', VALID-CODE is FALSE
```

### Solution 2

```cobol
       01 WS-AGE PIC 9(3).
           88 ADULT VALUES THRU 18 THRU 65.
       *> Wrong syntax!

; CORRECT: Use proper THRU syntax
       01 WS-AGE PIC 9(3).
           88 ADULT VALUE 18 THRU 65.
```

### Solution 3

```cobol
       01 WS-FLAG PIC 1.
           88 YES VALUE 1.
           88 NO VALUE 0.
       IF WS-FLAG = 1
           DISPLAY 'Yes'
       ELSE
           DISPLAY 'No'.
```

### Solution 4

```cobol
       01 WS-CODE PIC X(1).
           88 VALID-CODE VALUES 'A' THRU 'Z'.
       *> Range A to Z
       IF VALID-CODE
           DISPLAY 'Alpha'.
```

### Solution 5

```cobol
       01 WS-FLAG PIC 1 VALUE 0.
           88 IS-ON VALUE 1.
           88 IS-OFF VALUE 0.
       IF IS-ON
           DISPLAY 'On'
       ELSE
           DISPLAY 'Off'.
```

### Solution 6

```cobol
       01 WS-CODE PIC X(2).
           88 ERROR-CODE VALUES 'ER' 'EF' 'EX'.
       EVALUATE TRUE
           WHEN ERROR-CODE
               DISPLAY 'Error'
           WHEN OTHER
               DISPLAY 'OK'
       END-EVALUATE.
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**88-level value never matches**

The 88-level VALUE clause defines values that never occur in the parent field. The condition is always FALSE.

**88-level VALUE syntax wrong**

The VALUE clause syntax is incorrect. Ranges need THRU, and multiple values need spaces between them.

**Condition name in COMPUTE**

Using an 88-level condition name in a COMPUTE statement is invalid. 88-levels are boolean conditions, not data items.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Verify 88-level VALUE clauses match actual data values in the parent field.**
2. **Use THRU for ranges and space-separated values for discrete lists.**
3. **Test condition names with known data values to ensure correct boolean evaluation.**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [IF-ELSE Error](/languages/cobol/cobol-if-else-error) — conditional logic
- [EVALUATE Error](/languages/cobol/cobol-evaluate-error) — decision statements
- [TABLE Error](/languages/cobol/cobol-table-error) — table operations

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
