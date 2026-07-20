---
title: "[Solution] Assembly General Protection Fault — How to Fix"
description: "Fix general protection fault (#GP) errors in assembly caused by privilege violations or invalid segment selectors."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1004
---

# General Protection Fault (#GP)

The general protection fault (interrupt 13) triggers when the CPU detects a protection violation that is not a page fault — invalid segment selector, privilege escalation attempt, or writing to a read-only page in protected mode.

## Common Causes

- Loading a null or invalid segment selector into DS/ES/FS/GS
- Attempting ring-3 access to ring-0 data segments
- Writing to code segments or system descriptor tables
- Accessing I/O ports without IOPL permission

## How to Fix

### Solution 1 — Load valid segment selectors in protected mode

```assembly
; WRONG: null selector
    xor ax, ax
    mov ds, ax           ; #GP — null selector in data segment

; CORRECT: load a valid GDT selector
    mov ax, 0x10         ; ring-0 data segment selector
    mov ds, ax
    mov es, ax
```

### Solution 2 — Use iretq to return to ring 3

```assembly
; Transitioning back to user mode
return_to_user:
    push 0x23            ; user data selector (ring 3)
    push user_rsp
    push 0x202           ; RFLAGS with IF=1
    push 0x2B            ; user code selector (ring 3)
    push user_rip
    iretq
```

### Solution 3 — Validate I/O port access

```assembly
; Check IOPL before IN/OUT
check_iopl:
    pushfq
    pop rax
    test ax, 0x3000      ; check IOPL bits (bits 12-13)
    jnz .has_privilege
    ; No privilege — use syscall instead of direct I/O
    ret
.has_privilege:
    in al, 0x60          ; safe to read keyboard port
    ret
```

## Examples

A boot loader loads a null selector into DS before setting up the GDT. The first memory access via DS triggers #GP. The fix is to set up the GDT and load proper selectors before any segment register usage.

## Related Errors

- [Page Fault](/languages/assembly/asm-page-fault-error) — virtual memory faults
- [Invalid Instruction](/languages/assembly/asm-invalid-instruction) — opcode decoding
- [Segmentation Fault](/languages/assembly/asm-segmentation-fault-v2) — user-mode memory fault
