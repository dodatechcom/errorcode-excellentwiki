---
title: "[Solution] Assembly System Call Error — How to Fix"
description: "Fix assembly system call errors when using INT 0x80, SYSCALL, or software interrupts with incorrect parameters or registers."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# System Call or Interrupt Error

This error is one of the most frequently encountered issues when developing with assembly. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- On x86_64 Linux, SYSCALL replaces INT 0x80. RAX holds the syscall number; args go in RDI, RSI, RDX, R10, R8, R9. SYSCALL clobbers RCX and R11.
- INT 0x80 in 64-bit mode truncates all arguments to 32 bits, causing failures when pointers are above 4GB.
- The return value in RAX is negative on error — the absolute value is errno. Failing to check for negative returns means errors go undetected.
- macOS uses different syscall numbers (0x2000000 + Linux number) and requires underscore-prefixed symbols.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **System Call Returns -EINVAL (22) — Invalid Parameter**
2. **System Call Returns -EFAULT (14) — Bad Memory Address**
3. **ENOSYS (38) — Invalid Syscall Number**
4. **SIGSEGV — Kernel Fault on Unmapped Syscall Argument Pointer**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```assembly
; WRONG: Wrong syscall number
    mov rax, 999           ; Non-existent
    syscall                ; Returns -ENOSYS

    ; CORRECT: Use proper numbers
    mov rax, 1             ; sys_write
    mov rdi, 1             ; stdout
    lea rsi, [msg]
    mov rdx, 14
    syscall
    test rax, rax
    js .error
```

### Solution 2

```assembly
; WRONG: INT 0x80 in 64-bit mode
    mov eax, 4             ; 32-bit sys_write
    mov ebx, 1
    mov ecx, msg           ; Truncated to 32 bits!
    int 0x80

    ; CORRECT: Use SYSCALL
    mov rax, 1             ; 64-bit sys_write
    mov rdi, 1
    lea rsi, [msg]         ; Full 64-bit address
    mov rdx, 14
    syscall
```

### Solution 3

```assembly
; WRONG: Using RCX across syscall
    mov rcx, 42
    mov rax, 1
    syscall                ; RCX destroyed!

    ; CORRECT: Use R12-R15 (preserved across SYSCALL)
    mov r12, 42
    mov rax, 1
    syscall
    mov rax, r12           ; R12 still valid
```

### Solution 4

```assembly
; CORRECT: Error-checked syscall wrapper
linux_write:
    push rbx
    mov rax, 1
    syscall
    test rax, rax
    jns .success
    neg rax                ; Convert to positive errno
    pop rbx
    ret
.success:
    pop rbx
    ret
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**Stack address above 4GB with INT 0x80**

A 64-bit program's stack is above 4GB. INT 0x80 truncates the buffer pointer, causing -EFAULT from the kernel.

**Linux syscall numbers used on macOS**

Code ported from Linux uses syscall 1 (write on Linux, but exit on macOS). The program exits instead of writing.

**Missing EINTR retry after signal interruption**

A read() syscall is interrupted by a signal, returning -EINTR. The program treats it as EOF instead of retrying.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Use SYSCALL (not INT 0x80) in 64-bit programs to avoid pointer truncation.**
2. **Check RAX after every syscall — negative values indicate errno.**
3. **Use R12-R15 for values that must survive across SYSCALL invocations.**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [Protected Mode Error](/languages/assembly/asm-protected-mode-error) — privilege violations
- [Timer Interrupt Error](/languages/assembly/asm-timer-interrupt-error) — interrupt handling
- [Page Fault](/languages/assembly/asm-page-fault-error) — memory access violations

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
