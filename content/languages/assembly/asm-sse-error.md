---
title: "[Solution] Assembly SSE/AVX Alignment Error — How to Fix"
description: "Fix assembly SSE and AVX alignment errors when using MOVAPS, MOVAPD, or VMOVDQA on unaligned memory addresses."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# SSE/AVX Alignment Error

This error is one of the most frequently encountered issues when developing with assembly. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- SSE instructions MOVAPS/MOVAPD/MOVDQA require 16-byte alignment. AVX VMOVDQA requires 32-byte alignment. Misaligned access causes #GP.
- The alignment requirement exists because SSE/AVX load/store accesses memory in 16/32/64-byte chunks. The base address must be aligned to the chunk size.
- RSP must be 16-byte aligned before every CALL. PUSH and CALL each decrement RSP by 8, so an odd number of pushes leaves RSP misaligned for SSE spills.
- MXCSR contains an Alignment Check mask bit. When unmasked, misaligned access generates #AC (vector 17) instead of #GP.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **#GP — MOVAPS on Non-16-Byte-Aligned Address**
2. **#GP — VMOVDQA on Non-32-Byte-Aligned Address**
3. **#AC (Alignment Check, Vector 17) — Unaligned Access with AC Enabled**
4. **Segmentation Fault — SSE Load from Invalid Misaligned Address**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```assembly
; WRONG: MOVAPS on misaligned address
    lea rdi, [buffer + 4]
    movaps xmm0, [rdi]    ; #GP!

    ; CORRECT: Use aligned data or unaligned instruction
    movaps xmm0, [buffer]           ; Aligned
    lea rdi, [buffer + 4]
    movups xmm0, [rdi]              ; Unaligned variant
```

### Solution 2

```assembly
; WRONG: VMOVDQA with 32-byte requirement
    lea rdi, [vec_a + 8]
    vmovdqa ymm0, [rdi]    ; #GP: not 32-byte aligned

    ; CORRECT: Use vmovdqu or ensure alignment
    vmovdqu ymm0, [vec_a]  ; Unaligned: safe
    vmovdqa ymm0, [vec_a]  ; Aligned: faster
```

### Solution 3

```assembly
; WRONG: Stack misaligned for SSE
    push rax               ; RSP ends in 8
    push rbx               ; RSP ends in 0
    sub rsp, 8             ; RSP ends in 8
    movaps [rsp], xmm0     ; #GP!

    ; CORRECT: Maintain alignment
    push rax
    push rbx               ; Aligned
    sub rsp, 16            ; Still aligned
    movaps [rsp], xmm0     ; OK
```

### Solution 4

```assembly
; CORRECT: Aligned function prologue
sse_func:
    push rbp
    mov rbp, rsp
    and rsp, -16           ; Force alignment
    sub rsp, 32
    movaps [rsp], xmm0     ; Safe
    ; ... SSE code ...
    mov rsp, rbp
    pop rbp
    ret
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**SSE-optimized memory copy with unaligned pointers**

A programmer replaces byte-copy with 16-byte MOVAPS copy. If source or dest is not 16-byte aligned, every MOVAPS instruction faults.

**Stack-allocated SSE locals with wrong SUB RSP**

SUB RSP, 12 instead of SUB RSP, 16 leaves RSP misaligned. MOVAPS to [RSP+8] triggers #GP.

**AVX-512 requiring 64-byte alignment**

VMOVDQA64 needs 64-byte alignment. The allocator only provides 32-byte alignment, causing #GP.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Use align directives (align 16/32/64) for guaranteed data alignment.**
2. **Prefer MOVUPS/VMOVDQU — the speed penalty is minimal on modern CPUs.**
3. **Ensure RSP is 16-byte aligned at every CALL by counting pushes.**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [Page Fault](/languages/assembly/asm-page-fault-error) — memory access violations
- [Alignment Error](/languages/assembly/asm-alignment-error) — unaligned access
- [FPU Error](/languages/assembly/asm-fpu-error) — floating-point exceptions

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
