---
title: "[Solution] COBOL FILE STATUS Non-Zero Code - How to Fix"
description: "Fix COBOL file status errors when OPEN, READ, WRITE, or CLOSE operations return non-zero FILE STATUS codes."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# FILE STATUS Non-Zero Code

This error is one of the most frequently encountered issues when developing with cobol. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- FILE STATUS is a two-character code returned after every file I/O operation. 00 means success. Any other value indicates an error condition.
- Common codes: 10 (end of file), 22 (duplicate key), 23 (record not found), 30 (permanent I/O error), 41 (file already open), 42 (file not open).
- The FILE STATUS is stored in the file's status field defined in the FD or with STATUS IS clause. It must be checked after every I/O operation.
- Some FILE STATUS codes require checking the second character. Status 9x indicates a vendor-specific error.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **FILE STATUS 10 - End of File Reached on READ**
2. **FILE STATUS 22 - Duplicate Key on WRITE or REWRITE**
3. **FILE STATUS 30 - Permanent I/O Error (disk failure, file locked)**
4. **FILE STATUS 41/42 - File Already Open / File Not Open**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```cobol
       OPEN INPUT CUST-FILE.
       READ CUST-FILE.
       *> What if status is not 00?
       MOVE CUST-ID TO WS-DISPLAY.

; CORRECT: Check STATUS after every I/O
       OPEN INPUT CUST-FILE.
       IF FS-STATUS NOT = '00'
           DISPLAY 'Open error: ' FS-STATUS
           GO TO MAIN-EXIT.
```

### Solution 2

```cobol
       MOVE WS-KEY TO CUST-KEY.
       WRITE CUST-REC.
       *> Status 22 if key already exists

; CORRECT: Check for duplicate key
       WRITE CUST-REC.
       EVALUATE FS-STATUS
           WHEN '00'
               CONTINUE
           WHEN '22'
               DISPLAY 'Duplicate key'
               REWRITE CUST-REC
           WHEN OTHER
               DISPLAY 'Write error: ' FS-STATUS.
```

### Solution 3

```cobol
       CLOSE CUST-FILE.
       *> May fail if file was not properly opened

; CORRECT: Check CLOSE status
       CLOSE CUST-FILE.
       IF FS-STATUS NOT = '00'
           DISPLAY 'Close error: ' FS-STATUS.
```

### Solution 4

```cobol
       OPEN I-O CUST-FILE.
       IF FS-STATUS NOT = '00'
           DISPLAY 'Cannot open: ' FS-STATUS
           GO TO MAIN-EXIT.
       PERFORM UNTIL FS-STATUS = '10'
           READ CUST-FILE
               AT END
                   MOVE '10' TO FS-STATUS
               NOT AT END
                   PERFORM PROCESS-RECORD
           END-READ
       END-PERFORM.
       CLOSE CUST-FILE.
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**OPEN INPUT fails with STATUS 30**

The file does not exist, the path is incorrect, or the file is locked by another process.

**WRITE returns STATUS 22 (duplicate key)**

The program attempts to write a record with a key that already exists in the file.

**READ after CLOSE returns STATUS 42**

The program attempts to read from a file that was closed or never successfully opened.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Always check FILE STATUS after every I/O operation.**
2. **Handle all common status codes (00, 10, 22, 23, 30, 41, 42) explicitly.**
3. **Log file status codes and record keys for debugging production issues.**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [RECORD Error](/languages/cobol/cobol-record-error) — record layout issues
- [VSAM Error](/languages/cobol/cobol-vsam-error) — VSAM file access
- [JCL Error](/languages/cobol/cobol-jcl-error) — job step errors

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
