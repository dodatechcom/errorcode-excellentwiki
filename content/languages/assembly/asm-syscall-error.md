---
title: "[Solution] Assembly SYSCALL Error -- Incorrect System Call Usage"
description: "Fix assembly syscall errors when using the syscall instruction incorrectly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly SYSCALL Error

This error occurs when the `syscall` instruction is used with incorrect register setup or wrong syscall number.

## Common Causes

- Wrong syscall number in RAX
- Clobbering RCX and R11 (saved by kernel)
- Incorrect argument registers (RDI, RSI, RDX, R10, R8, R9)
- Not checking return value in RAX for errors

## How to Fix

### Use correct registers

```asm
; WRONG: using wrong registers
mov rax, 1      ; write syscall
mov rbx, 1      ; fd should be in RDI
syscall

; CORRECT: System V syscall ABI
mov rax, 1      ; sys_write
mov rdi, 1      ; stdout
lea rsi, [msg]  ; buffer
mov rdx, 13     ; length
syscall
```

### Check for errors

```asm
syscall
cmp rax, 0
jl .error       ; negative return = error
```

## Examples

```asm
; Hello world using syscall
section .data
    msg db "Hello, World!", 10
    len equ $ - msg

section .text
    global _start
_start:
    mov rax, 1      ; sys_write
    mov rdi, 1      ; stdout
    lea rsi, [msg]
    mov rdx, len
    syscall

    mov rax, 60     ; sys_exit
    xor edi, edi
    syscall
```
