---
title: "[Solution] COBOL RECORD Layout Error - How to Fix"
description: "Fix COBOL record layout and size mismatch errors when data descriptions do not match the actual file structure."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# RECORD Layout or Size Mismatch

This error is one of the most frequently encountered issues when developing with cobol. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- A RECORD clause specifies the expected record length. If the actual data record is longer or shorter, I/O operations fail or corrupt adjacent memory.
- REDEFINES allows the same memory to be interpreted as different record types. Incorrect REDEFINES causes data to be read with the wrong field layout.
- When a record contains variable-length fields (OCCURS DEPENDING ON), the maximum and minimum RECORD sizes must accommodate all valid data.
- COMP-3 (packed decimal) fields within records must be on odd-byte boundaries for correct nibble alignment in the record layout.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **RECORD SIZE mismatch - expected X but got Y bytes**
2. **REDEFINES overlap error - overlapping field definitions**
3. **Variable record - OCCURS DEPENDING ON value exceeds RECORD VARYING clause**
4. **Packed decimal alignment - COMP-3 field not on byte boundary**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```cobol
       FD  CUST-FILE
           RECORD CONTAINS 80 CHARACTERS.
       01  CUST-REC.
           05 CUST-ID      PIC X(10).
           05 CUST-NAME    PIC X(30).
           05 CUST-ADDR    PIC X(50).  *> Total 90, not 80!

; CORRECT: Match RECORD to actual data
       FD  CUST-FILE
           RECORD CONTAINS 90 CHARACTERS.
```

### Solution 2

```cobol
       01  RECORD-A.
           05 FIELD-A      PIC X(20).
       01  RECORD-B REDEFINES RECORD-A.
           05 FIELD-B      PIC X(30). *> Longer than RECORD-A!

; CORRECT: Redefines must be same size
       01  RECORD-A.
           05 FIELD-A      PIC X(30).
       01  RECORD-B REDEFINES RECORD-A.
           05 FIELD-B      PIC X(30).
```

### Solution 3

```cobol
       FD  TABLE-FILE
           RECORD CONTAINS 3 TO 2003
           DEPENDING ON ENTRY-COUNT.
           RECORD VARYING FROM 3 TO 2003.
```

### Solution 4

```cobol
       01  PAYMENT-REC.
           05 PAY-ID        PIC X(8).
           05 PAY-AMOUNT    PIC 9(7)V99 COMP-3.
           05 PAY-DATE      PIC 9(8).
       *> Total: 8 + 5 + 8 = 21 bytes
       *> RECORD CONTAINS 21 CHARACTERS.
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**File opened with different RECORD CONTAINS than the data**

A COBOL program defines RECORD CONTAINS 80 but actual records are 90 bytes. READ operations read 10 bytes of the next record.

**REDEFINES field longer than original**

A REDEFINES clause defines a redefining record longer than the original, causing overlap with adjacent records.

**Variable-length record with wrong max size**

The RECORD VARYING clause specifies a maximum of 100 bytes but actual data can be up to 2003 bytes.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Always verify RECORD CONTAINS matches the actual data file layout.**
2. **Ensure REDEFINES records are exactly the same size as the original.**
3. **Test variable-length records with both minimum and maximum entry counts.**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [COPYBOOK Error](/languages/cobol/cobol-copybook-error) — copybook issues
- [FILE STATUS Error](/languages/cobol/cobol-file-status-error) — file I/O problems
- [NUMERICAL Error](/languages/cobol/cobol-numerical-error) — data item overflow

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
