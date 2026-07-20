---
title: "[Solution] Assembly IDT Error — How to Fix"
description: "Fix interrupt descriptor table errors in assembly when IDT entries are malformed or the table is not loaded correctly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1023
---

# IDT Error

The Interrupt Descriptor Table (IDT) maps interrupt/exception vectors to handler functions. Malformed entries, incorrect DPL, or missing entries cause double faults, triple faults, or unhandled exceptions.

## Common Causes

- IDT not aligned to an 8-byte boundary
- IDTR.limit set too small — vectors beyond limit cause #GP
- Gate type wrong (trap vs interrupt gate) causing interrupts not to be disabled
- Handler offset split across the 64-bit entry incorrectly
- Missing handlers for critical exceptions (DF, NMI, #PF)

## How to Fix

### Solution 1 — Create 64-bit IDT entries

```assembly
section .data
align 8
idt_start:
    ; Vector 0: Divide Error
    dw handler_div & 0xFFFF          ; offset low
    dw 0x08                          ; kernel code segment
    db 0x00                          ; reserved
    db 10001110b                     ; present, ring-0, interrupt gate
    dw (handler_div >> 16) & 0xFFFF  ; offset middle
    dd (handler_div >> 32) & 0xFFFFFFFF  ; offset high
    dd 0                             ; reserved

idt_end:

idtr:
    dw idt_end - idt_start - 1
    dq idt_start
```

### Solution 2 — Load IDT with LIDT

```assembly
load_idt:
    lidt [idtr]
    ret
```

### Solution 3 — Set up exception handlers for critical vectors

```assembly
handler_div:
    ; vector 0
    push rax
    mov rax, [rsp + 8]     ; error code (if any)
    ; log and halt
    pop rax
    iretq

handler_df:
    ; vector 8: double fault — always has error code 0
    cli
    hlt

handler_pf:
    ; vector 14: page fault — error code on stack
    push rax
    mov rax, cr2           ; faulting address
    ; log cr2 and error code
    pop rax
    add rsp, 8             ; pop error code
    iretq
```

### Solution 4 — Use IST (Interrupt Stack Table) for critical handlers

```assembly
; TSS IST entry for double fault handler
    mov qword [tss + 36], df_ist_top
    mov word [tss + 40], 0x10

df_handler:
    mov rsp, df_ist_top    ; guaranteed valid stack
    ; handle double fault
    iretq
```

## Examples

A kernel sets up IDT entries but uses a 16-bit offset field for a handler located above 64KB. The upper bits are zero, so the CPU jumps to address 0x0000:0x1234 instead of the full 64-bit address. Using the correct 64-bit gate format with split offset fields fixes the issue.

## Related Errors

- [GDT Error](/languages/assembly/asm-gdt-error) — segment descriptor setup
- [General Protection Fault](/languages/assembly/asm-general-protection-fault) — IDT DPL violations
- [Debug Exception](/languages/assembly/asm-debug-exception-error) — vector 1 handler
