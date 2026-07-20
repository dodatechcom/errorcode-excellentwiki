---
title: "[Solution] Assembly EFLAGS Register Error — How to Fix"
description: "Fix EFLAGS register errors in assembly when flag bits are incorrectly set, cleared, or saved across operations."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1019
---

# EFLAGS Register Error

EFLAGS holds the processor status flags (CF, PF, AF, ZF, SF, OF, IF, DF, TF, etc.). Incorrectly saving, restoring, or modifying EFLAGS leads to unpredictable branching, interrupt behavior, and direction errors.

## Common Causes

- Pushing EFLAGS with PUSHF and modifying bits accidentally
- Not clearing DF before string operations (STD sets DF=1, causing backward iteration)
- Enabling interrupts (IF=1) in critical sections
- Restoring EFLAGS from a wrong stack offset after a function call

## How to Fix

### Solution 1 — Save/restore EFLAGS around critical sections

```assembly
critical_section:
    pushfq
    pop rax
    push rax
    and eax, ~0x200        ; clear IF (disable interrupts)
    push rax
    popfq
    ; ... critical code ...
    popfq                  ; restore original flags including IF
```

### Solution 2 — Always clear DF before string operations

```assembly
string_copy:
    cld                    ; clear DF — string ops go forward
    rep movsb              ; copy RCX bytes from RSI to RDI
    ret
```

### Solution 3 — Use PUSHF/POPF for signal handler safety

```assembly
signal_handler:
    pushfq
    pop rax
    mov [saved_flags], rax
    ; ... handle signal ...
    mov rax, [saved_flags]
    push rax
    popfq
    iretq

section .data
saved_flags: dq 0
```

### Solution 4 — Manipulate specific flag bits without side effects

```assembly
set_direction_forward:
    cld                    ; preferred over: pushfq; and ...; popfq
    ret

set_direction_backward:
    std                    ; set DF for reverse string ops
    ret
```

## Examples

An OS task switch saves EFLAGS with PUSHF but the stack pointer is off by 8 bytes. The restored flags are garbage, causing ZF and CF to have wrong values. The next conditional branch goes to the wrong label. Fixing the stack offset resolves the issue.

## Related Errors

- [Overflow Flag](/languages/assembly/asm-overflow-flag-error) — OF bit
- [Carry Flag](/languages/assembly/asm-carry-flag-error) — CF bit
- [Zero Flag](/languages/assembly/asm-zero-flag-error) — ZF bit
