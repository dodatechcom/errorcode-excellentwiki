---
title: "[Solution] Assembly Prologue/Epilogue Error — How to Fix"
description: "Fix function prologue and epilogue errors in assembly when registers are not properly saved and restored."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1029
---

# Prologue/Epilogue Error

The function prologue saves the caller's frame and sets up the callee's. The epilogue tears it down. Mismatched push/pop sequences or missing register saves corrupt the caller's state.

## Common Causes

- Saving RBX in prologue but not restoring it in epilogue
- Epilogue not returning RSP to its value before CALL
- Using `RET` without popping the saved RBP first
- Leaving a non-zero RSP adjustment in the middle of the function

## How to Fix

### Solution 1 — Symmetric prologue/epilogue

```assembly
my_func:
    push rbp                ; save caller's frame pointer
    mov rbp, rsp            ; establish new frame
    push rbx                ; save callee-saved register
    sub rsp, 24             ; locals (keep 16-byte aligned)

    ; ... function body ...

    add rsp, 24             ; deallocate locals
    pop rbx                 ; restore callee-saved
    pop rbp                 ; restore caller's frame pointer
    ret
```

### Solution 2 — Use LEAVE for epilogue (x86 shortcut)

```assembly
my_func:
    push rbp
    mov rbp, rsp
    sub rsp, 64
    ; ... body ...
    leave                   ; equivalent to: mov rsp,rbp / pop rbp
    ret
```

### Solution 3 — Handle callee-saved registers properly

```assembly
multi_save:
    push rbp
    mov rbp, rsp
    push rbx
    push r12
    push r13
    push r14
    push r15
    sub rsp, 8              ; alignment

    ; ... body ...

    add rsp, 8
    pop r15
    pop r14
    pop r13
    pop r12
    pop rbx
    pop rbp
    ret
```

### Solution 4 — Leaf function (no frame needed)

```assembly
leaf_add:
    ; No stack frame — RSP is already 16-byte aligned at entry
    lea rax, [rdi + rsi]
    ret                    ; no push/pop needed
```

## Examples

A function pushes RBX to save it but the epilogue pops into RAX instead. RBX is never restored, and the caller's RBX value is lost. The caller then uses a corrupted RBX, causing a segfault. Fixing the pop order resolves the issue.

## Related Errors

- [Stack Frame Error](/languages/assembly/asm-stack-frame-error) — frame pointer setup
- [Stack Overflow](/languages/assembly/asm-stack-error) — stack exhaustion
- [Calling Convention Error](/languages/assembly/asm-calling-convention-error) — ABI rules
