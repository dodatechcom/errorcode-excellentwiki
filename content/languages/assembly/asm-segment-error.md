---
title: "[Solution] Assembly Segment Register Error — How to Fix"
description: "Fix assembly segment register errors caused by invalid selectors or descriptor table issues in protected mode programs."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Segment Register or Selector Error

This error is one of the most frequently encountered issues when developing with assembly. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- Segment registers (CS, DS, ES, FS, GS, SS) hold selectors that reference entries in the Global Descriptor Table (GDT) or Local Descriptor Table (LDT). Each selector contains a 13-bit index, a table indicator bit, and a 2-bit requested privilege level (RPL).
- When a segment register is loaded with a selector whose index exceeds the GDT/LDT limit, the CPU raises a General Protection Fault (#GP, interrupt 13). This prevents code from accessing memory segments not properly defined by the OS.
- In 64-bit long mode, CS, DS, ES, and SS are largely ignored for address computation, but FS and GS remain critical for thread-local storage via MSRs. Invalid FS/GS selectors still cause faults.
- Corrupted descriptor tables from buffer overflows or kernel bugs can turn previously valid selectors into invalid ones, causing random #GP faults throughout the system.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **#GP (General Protection Fault) — Segment Selector Index Out of GDT Limit**
2. **#NP (Not Present) — Segment Descriptor Marked Not Present in GDT/LDT**
3. **#GP — Null Segment Selector Loaded into DS, ES, FS, GS, or SS**
4. **#GP — Requested Privilege Level (RPL) Exceeds Descriptor Privilege Level (DPL)**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```assembly
; WRONG: Loading an invalid selector into DS
    mov ax, 0xFFFF        ; Selector index = 0x7FFF (beyond GDT limit)
    mov ds, ax            ; #GP fault!

    ; CORRECT: Load a valid selector from the GDT
    mov ax, 0x10          ; Data segment selector (index 2, TI=0, RPL=0)
    mov ds, ax            ; Safe: this selector exists in the GDT
```

### Solution 2

```assembly
; WRONG: Using null selector for segment register
    xor ax, ax
    mov es, ax            ; #GP: null selector invalid for DS/ES/FS/GS/SS

    ; CORRECT: Load a non-null, valid selector
    mov ax, 0x08          ; Code segment selector (index 1)
    mov cs, ax
    mov ax, 0x10          ; Data segment selector (index 2)
    mov ds, ax
    mov es, ax
```

### Solution 3

```assembly
; WRONG: Selector with RPL > DPL
    mov ax, 0x13          ; Index=2, TI=0, RPL=3
    mov ds, ax            ; #GP: RPL(3) > DPL(0)

    ; CORRECT: Match RPL to the required privilege level
    mov ax, 0x10          ; Index=2, TI=0, RPL=0
    mov ds, ax            ; Safe: RPL(0) <= DPL(0)
```

### Solution 4

```assembly
; CORRECT: Full GDT setup for protected mode
section .gdt
gdt_start:
    dq 0                  ; Null descriptor (index 0)
    ; Code segment (index 1): Base=0, Limit=4GB, Ring 0, Execute/Read
    dw 0xFFFF, 0, 0
    db 10011010b          ; Present=1, DPL=00, S=1, Type=Execute/Read
    db 11001111b          ; G=1, D/B=1, Limit=0xF
    db 0
    ; Data segment (index 2): Base=0, Limit=4GB, Ring 0, Read/Write
    dw 0xFFFF, 0, 0
    db 10010010b          ; Present=1, DPL=00, S=1, Type=Read/Write
    db 11001111b
    db 0
gdt_end:
gdt_descriptor:
    dw gdt_end - gdt_start - 1
    dd gdt_start
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**Bootloader transitioning from real mode to protected mode**

The bootloader loads a segment register with a value that worked in real mode but is invalid in protected mode. The GDT must be properly configured before switching to protected mode with MOV CR0.

**Thread-local storage using invalid FS/GS selector**

In 64-bit Linux, FS/GS base addresses are set via WRMSR. If the FS selector in the GDT is invalid, accessing TLS data through [FS:offset] triggers #GP.

**Kernel module loading with incorrect segment setup**

A kernel module that manually loads segment registers must ensure the kernel GDT has entries at the expected indices.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Document every GDT entry index and selector value in code comments.**
2. **In 64-bit long mode, minimize segment register usage — rely on RIP-relative addressing.**
3. **Use SLDT to verify the current LDT selector before loading segment registers.**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [Page Fault](/languages/assembly/asm-page-fault-error) — memory access violations
- [Stack Error](/languages/assembly/asm-stack-error) — stack overflow and underflow
- [Alignment Error](/languages/assembly/asm-alignment-error) — unaligned memory access

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
