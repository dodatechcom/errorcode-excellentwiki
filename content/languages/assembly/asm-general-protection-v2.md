---
title: "[Solution] GPF: general protection fault in x86"
description: "Fix assembly general protection faults when accessing invalid segments, registers, or memory in x86/x86-64 mode."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A General Protection Fault (#GP) occurs in protected mode when the CPU detects an invalid memory access, segment violation, or privilege level violation. In 64-bit mode, most #GP errors are due to invalid memory addresses.

## Common Causes

- Accessing memory beyond segment limits
- Invalid segment selector
- Writing to code segment
- Ring level violations (user accessing kernel memory)
- Incorrect descriptor table usage

## How to Fix

```asm
; WRONG: Invalid segment access
section .text
    mov ax, 0x00    ; Null segment selector
    mov ds, ax      ; #GP: cannot load null selector
    mov [ds:bx], al

; CORRECT: Use valid segment selectors
section .text
    ; In 64-bit mode, segments are mostly flat
    ; Use proper registers
    lea rax, [rel data]
    mov [rax], 42
```

```asm
; WRONG: Writing to read-only descriptor
section .text
    ltr ax      ; Invalid task register
    ; #GP will occur

; CORRECT: Proper descriptor setup
section .gdt
    ; GDT should be set up by OS/loader
    ; User code shouldn't modify segment registers directly
```

```asm
; CORRECT: Safe memory access in 64-bit mode
section .text
    ; Use RIP-relative addressing
    lea rax, [rel my_variable]
    mov rbx, [rax]      ; Safe in 64-bit mode
    
    ; Use proper base addresses
    mov rax, 0x400000   ; Valid user-space address
    mov [rax], 42       ; May need mmap first
```

```asm
; CORRECT: Validate memory before access
section .text
    ; Check if address is in valid range
    cmp rdi, 0x1000     ; Below minimum
    jb .invalid
    cmp rdi, 0x7FFFFFFFFFFFFFFF  ; Above maximum
    ja .invalid
    
    mov rax, [rdi]      ; Safe access
    jmp .done
    
.invalid:
    mov rax, -1
.done:
```

## How to Debug

- Use `gdb` to inspect registers and memory
- Check `dmesg` for #GP reports
- Use `strace` to see signal delivery
- Check segment registers with `info registers`

## Related Errors

- [Segmentation Fault](asm-segmentation-fault-v2) - memory access
- [Page Fault](asm-page-fault-v2) - page errors
- [Stack Overflow](asm-stack-overflow-v2) - stack issues
