---
title: "[Solution] Assembly Calling Convention Error — How to Fix"
description: "Fix assembly ABI calling convention mismatches when interfacing with C libraries or using wrong register conventions."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# ABI Calling Convention Mismatch

This error is one of the most frequently encountered issues when developing with assembly. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- System V AMD64: args in RDI, RSI, RDX, RCX, R8, R9. Callee-saved: RBX, RBP, R12-R15. Return: RAX. Caller cleans.
- Windows x64: args in RCX, RDX, R8, R9. Callee-saved: RBX, RBP, RDI, RSI, R12-R15. Return: RAX. 32-byte shadow space required.
- Mixing conventions: a function using RCX for arg1 will read garbage on Linux where arg1 is in RDI.
- 32-bit cdecl passes all args on stack (caller clean); stdcall has callee clean. Wrong one corrupts the stack.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **Wrong Register for First Argument — Expected RDI, Got RCX**
2. **Callee-Saved Register RBX Corrupted — Return Value Destroyed**
3. **Stack Misalignment After Call — RSP Not 16-Byte Aligned**
4. **Shadow Space Not Allocated — Windows x64 ABI Violation**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```assembly
; WRONG: Windows convention on Linux
my_add:
    mov rax, rcx        ; Wrong! Linux arg1 is RDI
    add rax, rdx
    ret

    ; CORRECT: System V AMD64
my_add:
    mov rax, rdi        ; Arg1
    add rax, rsi        ; Arg2
    ret
```

### Solution 2

```assembly
; WRONG: Modify callee-saved without save
my_func:
    push rbp
    mov rbp, rsp
    mov rbx, rdi        ; RBX not saved!
    pop rbp
    ret                 ; Caller's RBX corrupted

    ; CORRECT: Save/restore
my_func:
    push rbp
    mov rbp, rsp
    push rbx            ; Save
    mov rbx, rdi
    pop rbx             ; Restore
    pop rbp
    ret
```

### Solution 3

```assembly
; WRONG: Stack misaligned at CALL
_start:
    push rax            ; RSP ends in 8
    push rbx            ; RSP ends in 0
    call my_func        ; Return push: RSP ends in 8

    ; CORRECT: Align before CALL
_start:
    push rbp
    mov rbp, rsp
    and rsp, -16
    call my_func        ; RSP aligned at entry
```

### Solution 4

```assembly
; CORRECT: Windows x64 with shadow space
my_func:
    push rbp
    mov rbp, rsp
    sub rsp, 32         ; Shadow space
    mov rax, rcx        ; Arg1
    add rax, rdx        ; Arg2
    add rsp, 32
    pop rbp
    ret
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**Calling Linux C library from Windows ASM**

Assembly uses RCX for arg1 (Windows), but the C library expects RDI (System V). C reads garbage; ASM ignores the actual argument.

**Forgot to save RBX called from C**

C compiler assumes RBX is preserved. ASM modifies it without saving. Subsequent C code uses corrupted RBX.

**Missing shadow space in Windows callee**

The callee doesn't allocate 32-byte shadow space. The called function writes register args beyond the caller's stack frame.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Learn the specific ABI for your target platform and document it in code.**
2. **Preserve callee-saved registers (RBX, RBP, R12-R15) in every function.**
3. **Verify RSP alignment at function entry: RSP % 16 == 8 (return address push).**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [Stack Error](/languages/assembly/asm-stack-error) — stack corruption
- [Relocation Error](/languages/assembly/asm-relocation-error) — linker errors
- [Symbol Resolution Error](/languages/assembly/asm-symbol-resolution-error) — undefined references

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
