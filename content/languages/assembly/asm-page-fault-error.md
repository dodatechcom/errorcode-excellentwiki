---
title: "[Solution] Assembly Page Fault Error — How to Fix"
description: "Fix assembly page fault exceptions when accessing unmapped memory, invalid page table entries, or permission violations."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Page Fault or Access Violation

This error is one of the most frequently encountered issues when developing with assembly. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- A page fault (#PF, exception 14) occurs when the CPU accesses a virtual address with no valid physical page mapping or when page table permissions conflict with the access type.
- CR2 contains the faulting virtual address. The error code indicates: page not present (P=0), write to read-only page (W=1, R/W=0), user access to supervisor page (U=1, U/S=0), or instruction fetch from NX page.
- In user space, unmapped pages produce SIGSEGV. In kernel mode, they can cause a kernel panic if the address is outside recognized kernel ranges.
- Common causes include accessing freed memory, writing to .rodata, executing shellcode in NX memory, and dereferencing uninitialized pointers.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **#PF (Page Fault, Vector 14) — Page Not Present (P=0 in PTE)**
2. **#PF — Write to Read-Only Page (Write bit set, R/W=0 in PTE)**
3. **#PF — User-Mode Access to Supervisor Page (U/S=0 in PTE)**
4. **SIGSEGV — Segmentation Fault at Invalid Address**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```assembly
; WRONG: Access unmapped memory
    mov rax, 0xDEADBEEF
    mov eax, [rax]          ; #PF: not mapped

    ; CORRECT: Map memory first (Linux mmap)
    mov rax, 9              ; sys_mmap
    mov rdi, 0              ; addr = NULL
    mov rsi, 4096           ; size = one page
    mov rdx, 3              ; PROT_READ | PROT_WRITE
    mov r10, 0x22           ; MAP_PRIVATE | MAP_ANONYMOUS
    mov r8, -1
    mov r9, 0
    syscall
    cmp rax, -1
    je .mmap_error
    ; RAX = valid pointer
```

### Solution 2

```assembly
; WRONG: Write to read-only section
section .rodata
    msg db 'Hello', 0
section .text
    mov rax, msg
    mov byte [rax], 'X'    ; #PF: .rodata is read-only

    ; CORRECT: Use writable .data section
section .data
    buf db 'Hello', 0
section .text
    mov rax, buf
    mov byte [rax], 'X'    ; OK: .data is writable
```

### Solution 3

```assembly
; WRONG: Call through null pointer
    xor rax, rax
    call rax               ; #PF: executing at address 0

    ; CORRECT: Validate before calling
    mov rax, [func_ptr]
    test rax, rax
    jz .null_func
    call rax               ; Safe
```

### Solution 4

```assembly
; CORRECT: Kernel page fault handler
page_fault_handler:
    push rax
    mov rax, cr2           ; Faulting address
    shr rax, 12
    shl rax, 12            ; Page-align
    cmp rax, KERNEL_START
    jb .invalid
    cmp rax, KERNEL_END
    ja .invalid
    call handle_page_fault
    pop rax
    add rsp, 8
    iretq
.invalid:
    pop rax
    add rsp, 8
    hlt
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**Accessing mmap'd region after munmap**

The program maps a file, reads it, then munmaps. A subsequent access to the same address triggers #PF because the page tables no longer map that region.

**Writing to copy-on-write page after fork**

After fork(), both processes share CoW pages. If the kernel cannot allocate a new page on write, the process is OOM-killed.

**NX bit violation executing shellcode**

Attempting to execute code in heap or stack marked non-executable by the NX bit triggers #PF with the instruction-fetch bit set.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Always check mmap return against MAP_FAILED (0xFFFFFFFFFFFFFFFF).**
2. **Install SIGSEGV handlers for graceful fault recovery in user-space.**
3. **Use madvise(MADV_DONTNEED) to test your fault handling code.**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [Alignment Error](/languages/assembly/asm-alignment-error) — unaligned memory access
- [Stack Error](/languages/assembly/asm-stack-error) — stack overflow/underflow
- [Memory Mapping Error](/languages/assembly/asm-memory-mapping-error) — mmap failures

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
