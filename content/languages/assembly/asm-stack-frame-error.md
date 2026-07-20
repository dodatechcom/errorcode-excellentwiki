---
title: "[Solution] Assembly Stack Frame Error — How to Fix"
description: "Fix stack frame errors in assembly when the frame pointer (RBP) setup and teardown are incorrect."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1028
---

# Stack Frame Error

A stack frame (activated via PUSH RBP / MOV RBP,RSP) provides a stable reference for accessing local variables and function arguments. Incorrect setup or teardown corrupts the frame chain and breaks debugging/backtraces.

## Common Causes

- Missing PUSH RBP / MOV RBP,RSP in function prologue
- Not restoring RSP to RBP before POP RBP in epilogue
- Modifying RSP without updating RBP (dynamic stack allocation)
- Forgetting to preserve RBP in leaf functions that don't use a frame

## How to Fix

### Solution 1 — Standard function prologue/epilogue

```assembly
my_function:
    push rbp
    mov rbp, rsp
    sub rsp, 32            ; allocate local variables

    ; ... function body ...
    ; access args: [rbp+16], [rbp+24], ...
    ; access locals: [rbp-8], [rbp-16], ...

    mov rsp, rbp           ; deallocate locals
    pop rbp
    ret
```

### Solution 2 — Frame pointer omission (FPO) with debug info

```assembly
; When using -fomit-frame-pointer, RSP-based access is used
my_leaf:
    sub rsp, 16            ; allocate without RBP
    mov [rsp + 8], rdi     ; save arg
    ; ... work ...
    add rsp, 16
    ret
```

### Solution 3 — Handle variable-size locals

```assembly
var_func:
    push rbp
    mov rbp, rsp
    ; RAX = number of local bytes needed
    sub rsp, rax
    and rsp, -16           ; keep 16-byte aligned
    ; ... use [rsp + offset] for locals ...
    mov rsp, rbp
    pop rbp
    ret
```

### Solution 4 — Verify frame chain for debugging

```assembly
dump_frames:
    push rbp
    mov rbp, rsp
    mov rcx, rbp           ; start of current frame
.dump_loop:
    test rcx, rcx
    jz .done
    ; print [rcx] (saved RBP) and [rcx+8] (return address)
    mov rcx, [rcx]         ; follow chain
    jmp .dump_loop
.done:
    pop rbp
    ret
```

## Examples

A function allocates local variables on the stack but forgets `SUB RSP, n`. The function body writes to negative RSP offsets, overwriting the caller's saved registers. Adding the SUB and corresponding ADD fixes the corruption.

## Related Errors

- [Stack Overflow](/languages/assembly/asm-stack-overflow) — stack exhaustion
- [Stack Fault](/languages/assembly/asm-stack-fault-error) — segment limit
- [Calling Convention Error](/languages/assembly/asm-calling-convention-error) — ABI mismatch
