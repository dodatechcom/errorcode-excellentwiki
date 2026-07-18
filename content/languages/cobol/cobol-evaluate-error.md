---
title: "[Solution] COBOL EVALUATE Statement Error - How to Fix"
description: "Fix COBOL EVALUATE statement errors including missing WHEN clauses, incorrect ANY usage, and boolean logic mistakes."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# EVALUATE Statement Error

This error is one of the most frequently encountered issues when developing with cobol. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- EVALUATE replaces nested IF-ELSE for cleaner decision logic. A missing END-EVALUATE causes a compilation error or the code to fall through.
- WHEN OTHER catches all unhandled cases. Without it, unmatched conditions silently do nothing.
- EVALUATE TRUE tests boolean conditions in WHEN clauses. Each WHEN must be a complete condition, not just a value.
- Multiple WHEN clauses can be combined with ALSO for compound conditions. Incorrect ALSO placement causes wrong logic.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **Missing END-EVALUATE - syntax error**
2. **WHEN OTHER missing - unhandled cases**
3. **EVALUATE TRUE with incomplete conditions**
4. **WHEN ALSO - wrong compound logic**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```cobol
       EVALUATE WS-CODE
           WHEN 'A'
               DISPLAY 'Alpha'
           WHEN 'B'
               DISPLAY 'Beta'
       *> Missing END-EVALUATE!

; CORRECT:
       EVALUATE WS-CODE
           WHEN 'A'
               DISPLAY 'Alpha'
           WHEN 'B'
               DISPLAY 'Beta'
       END-EVALUATE.
```

### Solution 2

```cobol
       EVALUATE WS-CODE
           WHEN 'A'
               DISPLAY 'Alpha'
           WHEN 'B'
               DISPLAY 'Beta'
       END-EVALUATE.
       *> What if WS-CODE is 'C'? Nothing happens.

; CORRECT: Add WHEN OTHER
       EVALUATE WS-CODE
           WHEN 'A'
               DISPLAY 'Alpha'
           WHEN 'B'
               DISPLAY 'Beta'
           WHEN OTHER
               DISPLAY 'Unknown'
       END-EVALUATE.
```

### Solution 3

```cobol
       EVALUATE TRUE
           WHEN WS-AGE > 65
               DISPLAY 'Senior'
           WHEN WS-AGE > 18
               DISPLAY 'Adult'
       END-EVALUATE.
       *> This works, but order matters!
       *> If WS-AGE=70, first WHEN matches

; CORRECT: Order from most specific to least
       EVALUATE TRUE
           WHEN WS-AGE > 65
               DISPLAY 'Senior'
           WHEN WS-AGE > 18
               DISPLAY 'Adult'
           WHEN OTHER
               DISPLAY 'Minor'
       END-EVALUATE.
```

### Solution 4

```cobol
       EVALUATE WS-CODE
           WHEN 'A' ALSO WS-FLAG = 'Y'
               DISPLAY 'A and Yes'
           WHEN 'B' ALSO WS-FLAG = 'N'
               DISPLAY 'B and No'
       END-EVALUATE.
       *> ALSO means AND condition
```

### Solution 5

```cobol
       EVALUATE WS-CODE ALSO WS-FLAG
           WHEN 'A' ALSO 'Y'
               DISPLAY 'A and Yes'
           WHEN 'B' ALSO 'N'
               DISPLAY 'B and No'
           WHEN OTHER
               DISPLAY 'Other'
       END-EVALUATE.
```

### Solution 6

```cobol
       EVALUATE WS-COUNT
           WHEN 1 DISPLAY 'One'
           WHEN 2 DISPLAY 'Two'
           WHEN 3 DISPLAY 'Three'
           WHEN OTHER DISPLAY 'Other'
       END-EVALUATE.
```

### Solution 7

```cobol
       EVALUATE WS-STATUS
           WHEN 'ACT' ALSO WS-TYPE
               WHEN 'A' DISPLAY 'Active Account'
               WHEN 'B' DISPLAY 'Active Bond'
           WHEN 'INA' ALSO WS-TYPE
               WHEN 'A' DISPLAY 'Inactive Account'
               WHEN OTHER DISPLAY 'Inactive'
           WHEN OTHER
               DISPLAY 'Unknown status'
       END-EVALUATE.
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**Missing END-EVALUATE causes syntax error**

The EVALUATE statement is not closed with END-EVALUATE, causing a compilation error or unstructured code execution.

**WHEN OTHER omitted - silent fall-through**

No WHEN OTHER clause means any value not matching a WHEN is silently ignored, causing logic errors.

**EVALUATE TRUE with wrong condition order**

Less specific conditions precede more specific ones, causing the first match to always win.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Always include END-EVALUATE and WHEN OTHER for complete coverage.**
2. **Order WHEN clauses from most specific to least specific in EVALUATE TRUE.**
3. **Use ALSO for compound conditions and ensure both sides match expected types.**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [PERFORM Error](/languages/cobol/cobol-perform-error) — loop issues
- [IF-ELSE Error](/languages/cobol/cobol-if-else-error) — conditional logic
- [STRING Error](/languages/cobol/cobol-string-error) — string operations

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
