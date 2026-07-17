---
title: "General Protection Fault in Assembly"
description: "A General Protection Fault (#GP) in Assembly occurs when a protected operation violates x86 protection mechanisms."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["general-protection", "gpf", "segmentation", "protection", "ring"]
weight: 5
---

## What This Error Means

A General Protection Fault (#GP) is a hardware exception triggered when a program violates x86 protection rules. This includes accessing restricted memory segments, using privileged instructions in user mode, or invalid descriptor table access.

## Common Causes

- Accessing memory outside segment limits
- Using ring-0 instructions in ring-3 (user mode)
- Invalid segment selector in memory reference
- Writing to code segment
- Invalid TSS (Task State Segment) access

## How to Fix

```asm
; WRONG: Trying to execute privileged instruction in user mode
section .text
    cli             ; #GP: clear interrupts requires ring 0
    hlt             ; #GP: halt requires ring 0
    lgdt [gdt_ptr]  ; #GP: load GDT requires ring 0

; CORRECT: Only use privileged instructions in kernel mode
; In kernel code (ring 0):
    cli             ; Valid in kernel mode
```

```asm
; WRONG: Invalid segment register
mov ax, 0xFFFF
mov ds, ax         ; #GP: invalid segment selector

; CORRECT: Use valid segment selectors
xor ax, ax
mov ds, ax         ; Use NULL or valid GDT selector
```

## Examples

```asm
; In user-mode program:
section .text
    ; These will cause #GP:
    mov cr0, rax    ; Control register access - #GP
    in al, 0x92     ; I/O port access - may #GP
    lidt [idt_ptr]  ; IDT access - #GP in ring 3
```

## How to Debug

- Check `dmesg` for general protection fault logs
- Use `gdb` to inspect segment registers
- Verify code runs in correct privilege level

## Related Errors

- [Segmentation Fault](/languages/assembly/segmentation-fault) - memory access violations
- [Invalid Instruction](/languages/assembly/asm-invalid-instruction) - opcode errors
