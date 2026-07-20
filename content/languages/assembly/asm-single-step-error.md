---
title: "[Solution] Assembly Single Step Error — How to Fix"
description: "Fix single-step trap errors in assembly caused by the Trap Flag (TF) in EFLAGS during instruction execution."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1015
---

# Single Step Error (Trap Flag)

When EFLAGS.TF (bit 8) is set, the CPU generates a debug exception (#DB) after every instruction. This is the foundation of single-step debugging. Incorrect handling creates infinite traps or corrupted single-step state.

## Common Causes

- Debugger sets TF but handler does not advance RIP past the current instruction
- Nested single-step: handler execution with TF still set traps again
- TF set in an interrupt handler without being cleared before iret
- Context switch not saving/restoring TF per-task

## How to Fix

### Solution 1 — Clear TF in the #DB handler

```assembly
single_step_handler:
    pushfq
    pop rax
    and eax, ~0x100         ; clear TF
    push rax
    popfq
    ; now handler code runs without re-triggering
    ; ... handle step ...
    iretq
```

### Solution 2 — Single-step a function call manually

```assembly
single_step_call:
    pushfq
    pop rax
    or rax, 0x100           ; set TF
    push rax
    popfq
    call target_function    ; after first instruction, #DB fires
    ; handler clears TF, logs registers, sets TF again for next step
    ret
```

### Solution 3 — Save/restore TF in context switch

```assembly
context_switch:
    pushfq
    pop rax
    and eax, ~0x100         ; clear TF in old task
    mov [old_task_tf], eax
    mov eax, [new_task_tf]
    push rax
    popfq                   ; set TF for new task if needed
    ret

section .data
old_task_tf: dd 0
new_task_tf: dd 0
```

### Solution 4 — Use TF for code coverage tracing

```assembly
; Enable TF, set up handler to record instruction addresses
enable_trace:
    pushfq
    pop rax
    or rax, 0x100
    push rax
    popfq
    ; next instruction triggers #DB → handler logs RIP → clears TF → iretq
```

## Examples

A debugger sets TF before stepping. The first instruction executes, triggering #DB. The handler saves RIP, clears TF, logs the state, and re-enables TF before iretq. If TF is not cleared in the handler, the handler itself is single-stepped, causing infinite recursion.

## Related Errors

- [Debug Exception](/languages/assembly/asm-debug-exception-error) — DR7 breakpoints
- [Breakpoint](/languages/assembly/asm-breakpoint-exception-error) — INT 3
- [General Protection Fault](/languages/assembly/asm-general-protection-fault) — EFLAGS modification
