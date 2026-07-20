---
title: "[Solution] Assembly GDT/LDT Error — How to Fix"
description: "Fix GDT and LDT descriptor table errors in assembly when segment selectors are misconfigured."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1022
---

# GDT/LDT Error

The Global Descriptor Table (GDT) and Local Descriptor Table (LDT) define memory segments in protected mode. Incorrect GDT entries, missing null selectors, or malformed LDT causes #GP or triple faults.

## Common Causes

- Missing null descriptor at GDT entry 0
- GDT limit set too small — accessing descriptors beyond limit
- DPL (Descriptor Privilege Level) bits preventing ring-3 access
- LDT not loaded via LLDT with a valid GDT selector
- Using 16-bit code segment descriptors for 32-bit code

## How to Fix

### Solution 1 — Set up a minimal GDT

```assembly
section .data
gdt_start:
    dq 0                    ; GDT[0]: null descriptor

gdt_code: equ $ - gdt_start
    dw 0xFFFF               ; limit low
    dw 0x0000               ; base low
    db 0x00                 ; base middle
    db 10011010b            ; access: present, ring-0, code, readable
    db 11001111b            ; flags: 4KB gran, 32-bit, limit high=0xF
    db 0x00                 ; base high

gdt_data: equ $ - gdt_start
    dw 0xFFFF
    dw 0x0000
    db 0x00
    db 10010010b            ; access: present, ring-0, data, writable
    db 11001111b
    db 0x00

gdt_end:

gdt_ptr:
    dw gdt_end - gdt_start - 1
    dq gdt_start
```

### Solution 2 — Load GDT and reload segment registers

```assembly
load_gdt:
    lgdt [gdt_ptr]
    ; reload segment registers
    mov ax, gdt_data
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax
    mov ss, ax
    ; far jump to reload CS
    jmp gdt_code:reload_cs
reload_cs:
    ret
```

### Solution 3 — Create a ring-3 code segment

```assembly
user_code: equ $ - gdt_start
    dw 0xFFFF
    dw 0x0000
    db 0x00
    db 11111010b            ; present, ring-3, code, readable
    db 11001111b
    db 0x00

user_data: equ $ - gdt_start
    dw 0xFFFF
    dw 0x0000
    db 0x00
    db 11110010b            ; present, ring-3, data, writable
    db 11001111b
    db 0x00
```

### Solution 4 — Set TSS for ring-0 stack in GDT

```assembly
gdt_tss: equ $ - gdt_start
    dw tss_size - 1         ; limit
    dw tss_addr & 0xFFFF    ; base low
    db (tss_addr >> 16) & 0xFF
    db 10001001b            ; present, ring-0, 32-bit TSS (busy=0)
    db 00000000
    db (tss_addr >> 24) & 0xFF

section .data
tss_addr: dd tss_start
tss_size: equ 104
```

## Examples

A kernel boots with a GDT that is missing the null descriptor at offset 0. The CPU loads DS=0 and on the first memory access, generates #GP because offset 0 does not point to a valid descriptor. Adding the null descriptor fixes the boot.

## Related Errors

- [General Protection Fault](/languages/assembly/asm-general-protection-fault) — selector validation
- [IDT Error](/languages/assembly/asm-idt-error) — interrupt descriptor setup
- [Long Mode Switch](/languages/assembly/asm-long-mode-switch-error) — mode transition
