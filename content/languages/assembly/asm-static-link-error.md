---
title: "[Solution] Assembly Static Link Error -- Missing Main Entry Point"
description: "Fix assembly static link errors when the linker cannot find the entry point."
languages: ["assembly"]
error-types: ["link-time"]
severities: ["error"]
---

# Assembly Static Link Error

This error occurs when creating statically linked executables and the entry point is not properly defined.

## Common Causes

- Missing _start symbol for static linking
- Using main instead of _start for direct syscall
- Not linking libc when using C library functions
- Entry point address not matching linker expectations

## How to Fix

### Define _start for static linking

```asm
; WRONG: using main without libc
global main
main:
    ; this won't work without C runtime

; CORRECT: use _start for static linking
global _start
_start:
    ; use direct syscalls
    mov rax, 60
    xor edi, edi
    syscall
```

### Link statically

```bash
nasm -f elf64 myfile.asm -o myfile.o
ld -static myfile.o -o myfile
```

## Examples

```asm
; Minimal static executable
section .text
global _start
_start:
    mov rax, 1      ; sys_write
    mov rdi, 1      ; stdout
    lea rsi, [msg]
    mov rdx, 14
    syscall

    mov rax, 60     ; sys_exit
    xor edi, edi
    syscall

section .data
msg: db "Hello, World!", 10
```
