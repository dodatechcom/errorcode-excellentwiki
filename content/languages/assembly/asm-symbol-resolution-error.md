---
title: "[Solution] Assembly Undefined Symbol Linker Error — How to Fix"
description: "Fix assembly undefined symbol errors when the linker cannot resolve references to functions or variables across object files."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Undefined Symbol in Linking

This error is one of the most frequently encountered issues when developing with assembly. It affects programs of all sizes, from small utility scripts to large-scale production systems. Recognizing this error early and understanding its root cause can save hours of debugging and prevent data corruption or security vulnerabilities.

The error typically manifests at runtime when the program encounters an unexpected condition during execution. Depending on the severity and the runtime environment, it may produce a visible error message, silently produce incorrect results, or cause an immediate crash with a core dump or stack trace.

Effective diagnosis requires examining the error message, the code path leading to the error, and the state of the program at the moment of failure. Many instances of this error are non-deterministic — they depend on specific input values, timing conditions, or environmental factors that are difficult to reproduce in a development environment.

Before diving into solutions, it is important to understand that this error often has multiple possible root causes. The error message itself may not always point directly to the true source of the problem. Systematic debugging, logging, and testing are essential to identify the specific cause in your codebase.

## Why It Happens

- The linker matches undefined references with global definitions across object files. If a symbol is used but never defined, undefined reference is reported.
- Common causes: forgetting GLOBAL directive, misspelling (assembly is case-sensitive), not linking the defining object file.
- Link order matters: the defining file must appear AFTER files that reference it on the command line.
- Multiple definitions occur when the same symbol is defined in multiple files without WEAK or COMMON.

Understanding these root causes enables you to apply the correct fix rather than merely treating symptoms. Each cause requires a different approach, and misidentifying the root cause can lead to patches that mask the problem without actually resolving it.

In many cases, the root cause is a combination of factors — for example, an uninitialized variable combined with a missing bounds check, or a race condition combined with an incorrect memory barrier. Addressing all contributing factors is essential for a complete fix.

## Common Error Messages

1. **undefined reference to `function_name'**
2. **multiple definition of `symbol_name'**
3. **symbol undefined but referenced from file.o**
4. **ld: link terminated with unresolved symbols**

Pay close attention to the exact wording of the error message. Different messages often indicate different root causes, even when the underlying error appears similar. Capture the complete error message including any stack trace, line numbers, or additional context provided by the runtime.

When debugging, always record the full error output along with the input data, environment variables, and configuration settings that were in effect at the time of the error. This information is invaluable for reproducing and fixing the issue.

## How to Fix It

The following solutions address the most common causes of this error. Work through them in order, starting with the simplest fix that matches your situation. Each solution includes complete, tested code that you can adapt to your specific use case.


### Solution 1

```assembly
; WRONG: Call without extern declaration
section .text
    global _start
_start:
    call external_func   ; Undefined reference

    ; CORRECT: Declare extern
section .text
    extern external_func
    global _start
_start:
    call external_func
```

### Solution 2

```assembly
; WRONG: Same symbol in two files
; file1.asm:
section .data
    myvar dd 42
; file2.asm:
section .data
    myvar dd 100    ; Multiple definition

    ; CORRECT: extern/global
; file1.asm:
section .data
    global myvar
    myvar dd 42
; file2.asm:
section .text
    extern myvar
```

### Solution 3

```assembly
; WRONG: Missing global
section .text
_start:             ; Not visible
    ret

    ; CORRECT:
section .text
    global _start
_start:
    ret
```

### Solution 4

```assembly
; CORRECT: Multi-file example
; main.asm:
    extern calculate
    global _start
_start:
    mov rdi, 10
    mov rsi, 20
    call calculate
    mov rdi, rax
    mov rax, 60
    syscall

; calc.asm:
    global calculate
calculate:
    mov rax, rdi
    add rax, rsi
    ret
```

After applying a fix, verify it by running your test suite under the same conditions that previously triggered the error. Pay special attention to edge cases, boundary conditions, and concurrent execution scenarios that may not trigger the error consistently.

It is recommended to add regression tests that specifically target the conditions that caused this error. This ensures that the fix remains effective as the codebase evolves and prevents the same error from being reintroduced in the future.

## Common Scenarios

These real-world scenarios illustrate how this error manifests in practice. If your situation matches one of these patterns, apply the corresponding solution directly.


**Calling function from another file without extern**

file_a.asm calls file_b.asm's function without extern. Assembler creates undefined reference; linker fails.

**Forgot to export with global**

_start is defined but global _start is missing. Symbol is invisible to the linker.

**Wrong link order**

ld calc.o main.o — linker processes calc.o first, finds no references to resolve, then main.o's references are unresolved.

Recognizing these patterns in your own code accelerates the debugging process. Many experienced developers learn to identify the characteristic symptoms of each scenario through practice and code review.

## Debugging Tips

When this error occurs, start by collecting as much diagnostic information as possible. Enable verbose logging, use debugging tools, and create minimal reproduction cases that isolate the failing behavior from the rest of the application.

Use breakpoints, watchpoints, and step-through debugging to trace the exact execution path that leads to the error. Pay special attention to the values of variables at each step, particularly those that are used in conditional checks or arithmetic operations.

Consider adding assertions or runtime checks at key points in your code to catch the error earlier and with more context. Assertions are especially valuable in development and testing environments where they can catch bugs before they reach production.

## Prevent It

Prevention is more efficient than debugging. Incorporate these practices into your development workflow to avoid encountering this error in the first place.

1. **Always use extern for symbols defined in other files.**
2. **Use global to export symbols other modules need.**
3. **Put defining files AFTER referencing files on the linker command line.**

These prevention strategies should be part of your standard development practices. Code review checklists should include verification of the patterns described above, and automated tests should cover the edge cases that commonly trigger this error.

## When to Seek Help

If you have tried the solutions above and the error persists, consider seeking help from the community. Provide the full error message, the code that triggers it, the steps to reproduce it, and what you have already tried. This information helps others diagnose the problem efficiently.

Online forums, issue trackers, and professional support channels are all valuable resources. When posting questions, include your language version, compiler version, operating system, and any relevant configuration details.

## Related Errors

- [Relocation Error](/languages/assembly/asm-relocation-error) — address range overflow
- [ELF Error](/languages/assembly/asm-elf-error) — binary format issues
- [Calling Convention Error](/languages/assembly/asm-calling-convention-error) — ABI mismatches

Understanding the relationships between these errors helps you diagnose cascading failures where one error leads to another. When you encounter this error, check whether related errors are also present in the same code path or in dependent modules.

Fixing related errors often resolves the primary error as well, since they may share a common root cause. Always look for patterns across multiple error reports to identify systemic issues in the codebase.
