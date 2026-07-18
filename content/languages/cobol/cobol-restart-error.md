---
title: "[Solution] COBOL RESTART Error - How to Fix"
description: "Fix COBOL checkpoint/restart errors when implementing restartable batch procedures, including missing checkpoints and file position issues."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# RESTART or CHECKPOINT Error

This error is one of the most frequently encountered issues when developing with cobol. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- RESTART allows a batch job to resume from a checkpoint after failure. The checkpoint number must match the RESTART parameter in the JCL EXEC statement.
- CHECKPOINT saves program state including file positions and working storage. Missing CHECKPOINT on critical files causes them to be re-processed from the beginning.
- RESTART PROCEDURE must be coded in the COBOL program to handle resumption. Without it, the program always starts from the beginning.
- After a restart, files opened before the checkpoint must be repositioned. Sequential files need to skip records already processed.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **RESTART parameter mismatch between JCL and program**
2. **CHECKPOINT not called before critical file operations**
3. **RESTART PROCEDURE missing - restart ignored**
4. **Sequential file position not restored after restart**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```cobol
//STEP1 EXEC PGM=MYPROG,RESTART=STEP1
       *> RESTART=STEP1 restarts at STEP1
       *> Program must have RESTART PROCEDURE

; CORRECT: Code RESTART PROCEDURE
       PROCEDURE DIVISION RESTART-PROC.
       IF RESTART-SW = 'Y'
           PERFORM REPOSITION-FILES
       ELSE
           PERFORM INITIAL-OPEN.
```

### Solution 2

```cobol
       OPEN INPUT IN-FILE.
       *> No CHECKPOINT between records
       *> After restart, file reads from beginning

; CORRECT: CHECKPOINT after processing
       READ IN-FILE.
       PERFORM PROCESS-RECORD.
       COMMIT.
```

### Solution 3

```cobol
       PROCEDURE DIVISION.
       *> No RESTART PROCEDURE
       DISPLAY 'Processing'.
       *> RESTART parameter in JCL ignored

; CORRECT: Add RESTART PROCEDURE
       PROCEDURE DIVISION RESTART-RTN.
       IF RESTART-FLAG = 'Y'
           PERFORM REPOSITION
       ELSE
           PERFORM INITIAL-OPEN.
```

### Solution 4

```cobol
       READ IN-FILE.
       *> After restart, already-processed
       *> records are read again

; CORRECT: Save position and skip
       MOVE LAST-PROCESSED-KEY TO WS-KEY.
       START IN-FILE KEY >= WS-KEY.
```

### Solution 5

```cobol
       MOVE 'N' TO RESTART-FLAG.
       IF RESTART-PARM = 'Y'
           MOVE 'Y' TO RESTART-FLAG
       END-IF.
```

### Solution 6

```cobol
       CHECKPOINT.
       *> Saves current state
       *> Must be called at logical boundaries
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**RESTART parameter not matching**

The JCL RESTART=STEP1 parameter specifies a step that does not exist in the job, or the program does not have a matching RESTART PROCEDURE.

**CHECKPOINT too infrequent**

CHECKPOINT is called only once per 100,000 records. After restart, 99,999 records must be reprocessed.

**File position lost after restart**

Sequential files are reopened but not repositioned. All records are re-read from the beginning.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Code RESTART PROCEDURE in every batch program that uses checkpoint/restart.**
2. **Call CHECKPOINT after each logical unit of work (e.g., after processing each record or batch).**
3. **Save the last processed key in working storage and use START to reposition files after restart.**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [JCL Error](/languages/cobol/cobol-jcl-error) — job control issues
- [FILE STATUS Error](/languages/cobol/cobol-file-status-error) — file I/O errors
- [SORT Error](/languages/cobol/cobol-sort-error) — sort operations

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
