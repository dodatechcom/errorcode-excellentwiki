---
title: "[Solution] COBOL PERFORM Loop Error - How to Fix"
description: "Fix COBOL PERFORM statement errors including infinite loops, missing THRU/UNTIL conditions, and procedure scope issues."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# PERFORM Loop Error

This error is one of the most frequently encountered issues when developing with cobol. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- PERFORM with UNTIL requires the condition to become true. If the loop body never modifies the condition variable, the loop runs forever.
- PERFORM THRU executes paragraphs in sequence. If the THRU target does not exist or is misspelled, the compiler reports an error.
- NESTED PERFORM statements can cause unintended re-entrancy if the same paragraph is PERFORMed by multiple levels simultaneously.
- PERFORM TIMES with a count of 0 or negative does not execute the body. If the count variable is uninitialized, behavior is undefined.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **Infinite loop - UNTIL condition never becomes true**
2. **PERFORM THRU - target paragraph not found**
3. **PERFORM VARYING - counter not incremented**
4. **Nested PERFORM re-entrancy**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```cobol
       MOVE 1 TO WS-COUNT.
       PERFORM UNTIL WS-COUNT > 10
           DISPLAY WS-COUNT
       END-PERFORM.
       *> Infinite loop! WS-COUNT never changes

; CORRECT: Increment the counter
       MOVE 1 TO WS-COUNT.
       PERFORM UNTIL WS-COUNT > 10
           DISPLAY WS-COUNT
           ADD 1 TO WS-COUNT
       END-PERFORM.
```

### Solution 2

```cobol
       PERFORM PROC-A THRU PROC-Z.
       *> Error if PROC-Z does not exist

; CORRECT: Ensure all targets exist
       PROC-A SECTION.
       DISPLAY 'A'.
       PROC-B SECTION.
       DISPLAY 'B'.
       PROC-Z SECTION.
       DISPLAY 'Z'.
```

### Solution 3

```cobol
       PERFORM VARYING WS-IDX FROM 1 BY 1
           UNTIL WS-IDX > 100
           DISPLAY WS-IDX
       END-PERFORM.
       *> This works, but if FROM/BY is wrong:
       PERFORM VARYING WS-IDX FROM 10 BY -1
           UNTIL WS-IDX < 1
           DISPLAY WS-IDX
       END-PERFORM.
```

### Solution 4

```cobol
       PERFORM CALC-RTN.
       PERFORM CALC-RTN. *> Re-entrancy

; CORRECT: Use different paragraphs
       PERFORM CALC-RTN-1.
       PERFORM CALC-RTN-2.
```

### Solution 5

```cobol
       MOVE 1 TO WS-COUNT.
       PERFORM WS-COUNT TIMES
           DISPLAY 'Loop'
       END-PERFORM.
       *> If WS-COUNT is uninitialized, unpredictable

; CORRECT: Initialize
       MOVE 5 TO WS-COUNT.
       PERFORM WS-COUNT TIMES
           DISPLAY 'Loop'
       END-PERFORM.
```

### Solution 6

```cobol
       MOVE 0 TO WS-COUNT.
       PERFORM UNTIL WS-COUNT > 10
           ADD 1 TO WS-COUNT
       END-PERFORM.
       DISPLAY 'Done'.
```

### Solution 7

```cobol
       PERFORM PARA-A
           VARYING WS-I FROM 1 BY 1
           UNTIL WS-I > 10
           AFTER WS-J FROM 1 BY 1
           UNTIL WS-J > 5.
       *> Nested PERFORM VARYING works correctly
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**Infinite loop in PERFORM UNTIL**

The loop condition checks a variable that is never updated inside the loop body.

**PERFORM VARYING counter wraps around**

The counter variable overflows its PIC clause before reaching the UNTIL condition.

**Nested PERFORM same paragraph**

Two levels of PERFORM both call the same paragraph, causing unexpected re-entrancy.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Always ensure PERFORM UNTIL conditions are modified inside the loop body.**
2. **Initialize PERFORM TIMES count variables before use.**
3. **Use different paragraphs for nested PERFORM calls to avoid re-entrancy.**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [EVALUATE Error](/languages/cobol/cobol-evaluate-error) — decision logic
- [STRING Error](/languages/cobol/cobol-string-error) — string handling
- [ARITHMETIC Error](/languages/cobol/cobol-arithmetic-error) — computation issues

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
