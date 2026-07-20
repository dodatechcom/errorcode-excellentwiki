---
title: "[Solution] Assembly Debug Exception — How to Fix"
description: "Fix debug exception errors in assembly caused by hardware breakpoint or watchpoint triggers during execution."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1013
---

# Debug Exception (#DB, INT 1)

The debug exception fires when a hardware breakpoint or watchpoint is hit, when single-stepping with TF (Trap Flag, EFLAGS bit 8), or when a branch is taken with BTF enabled. It is the primary mechanism for debugger single-stepping.

## Common Causes

- EFLAGS.TF = 1: every instruction triggers #DB after execution
- DR0-DR3 hardware breakpoint on execution/data access
- DR7 debug condition met (local/global enable bits)
- Branch trace fault with EFLAGS.BTF and IA32_DEBUGCTL.BTF

## How to Fix

### Solution 1 — Clear Trap Flag in exception handler

```assembly
db_handler:
    push rbp
    mov rbp, rsp
    pushfq
    pop rax
    and ax, 0xFEFF          ; clear TF (bit 8)
    push rax
    popfq
    ; resume execution without single-stepping
    pop rbp
    iretq
```

### Solution 2 — Configure hardware watchpoint

```assembly
set_watchpoint:
    mov dr0, rdi            ; address to watch
    xor eax, eax
    mov dr7, eax            ; clear all
    mov dr7, 0x00000001     ; enable local watchpoint 0, write
    ret
```

### Solution 3 — Disable debug exceptions in release builds

```assembly
disable_debug:
    xor eax, eax
    mov dr7, eax            ; disable all breakpoints/watchpoints
    pushfq
    pop rax
    and ax, 0xFEFF          ; clear TF
    push rax
    popfq
    ret
```

### Solution 4 — Read debug status register

```assembly
check_debug_state:
    mov rax, dr6            ; read debug status
    test eax, 0x0F          ; check B0-B3 ( breakpoint hit bits)
    jnz .bp_hit
    ret
.bp_hit:
    ; determine which breakpoint was hit
    and eax, 0x0F
    ; handle accordingly
    ret
```

## Examples

A debugger sets TF to single-step through a function. Each instruction fires #DB. The handler saves the register state, advances RIP past the current instruction, and resumes. Without clearing TF in the handler, an infinite loop of #DB exceptions occurs.

## Related Errors

- [Breakpoint](/languages/assembly/asm-breakpoint-exception) — INT 3 software breakpoint
- [Single Step](/languages/assembly/asm-single-step-error) — trap flag details
- [General Protection Fault](/languages/assembly/asm-general-protection-fault) — DR7 access from ring 3
