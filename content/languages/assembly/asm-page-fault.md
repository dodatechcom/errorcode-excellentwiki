---
title: "Page fault in Assembly"
description: "A page fault in Assembly occurs when accessing a memory page that is not currently mapped in the process's address space."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A page fault is a hardware interrupt triggered when a program accesses a virtual memory page that isn't mapped or has incorrect permissions. The OS handles page faults for demand paging, but invalid accesses cause SIGSEGV.

## Common Causes

- Accessing freed/unmapped memory
- Writing to read-only pages
- Stack overflow into unmapped area
- Accessing NULL or near-NULL pointers
- Missing mmap for allocated memory

## How to Fix

```asm
; WRONG: Accessing unmapped memory
mov rax, 0
mov rbx, [rax]   ; Page fault - NULL pointer dereference

; CORRECT: Validate pointer before dereferencing
mov rax, buffer
test rax, rax
jz .error
mov rbx, [rax]
```

```asm
; WRONG: Accessing beyond mmap'd region
; (If only 4096 bytes were mapped)
mov rax, mmap_addr
mov rbx, [rax + 8192]   ; Page fault - beyond mapped region

; CORRECT: Stay within mapped bounds
mov rax, mmap_addr
cmp rsi, 4096
jae .out_of_bounds
mov rbx, [rax + rsi]
```

## Examples

```asm
section .text
    mov rax, 0xDEAD      ; Arbitrary unmapped address
    mov rbx, [rax]       ; Page fault here
```

## How to Debug

- Use `dmesg` to see page fault details
- Check `/proc/<pid>/maps` for valid memory regions
- Use `gdb` with `info proc mappings`

## Related Errors

- [Segmentation Fault](/languages/assembly/segmentation-fault) - general memory violations
- [General Protection Fault](/languages/assembly/asm-general-protection) - protection errors
