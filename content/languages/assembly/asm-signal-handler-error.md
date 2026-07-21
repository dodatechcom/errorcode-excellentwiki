---
title: "[Solution] Assembly Signal Handler Error -- Incorrect Signal Handling"
description: "Fix assembly signal handler errors when handling Unix signals incorrectly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Signal Handler Error

This error occurs when signal handlers are set up incorrectly, causing crashes or undefined behavior.

## Common Causes

- Signal handler not preserving all registers
- Using async-signal-unsafe functions in handler
- Not restoring signal mask after handling
- SA_SIGINFO flag not set when accessing siginfo_t

## How to Fix

### Create minimal signal handler

```asm
; Signal handler must preserve all registers
signal_handler:
    ; rdi = signal number
    ; rsi = siginfo_t *
    ; rdx = ucontext_t *
    push rax
    push rcx
    push rdx
    push rsi
    push rdi
    
    ; Safe operations only (write is async-signal-safe)
    mov rax, 1      ; sys_write
    mov rdi, 2      ; stderr
    lea rsi, [sig_msg]
    mov rdx, sig_msg_len
    syscall
    
    pop rdi
    pop rsi
    pop rdx
    pop rcx
    pop rax
    ret
```

## Examples

```asm
; Install signal handler for SIGSEGV
section .data
sig_msg: db "Segmentation fault", 10
sig_msg_len equ $ - sig_msg

section .text
install_handler:
    ; sigaction(SIGSEGV, &sa, NULL)
    mov rax, 13     ; sys_rt_sigaction
    mov edi, 11     ; SIGSEGV
    lea rsi, [sa]
    xor edx, edx
    mov r10, 8      ; sizeof(sigset_t)
    syscall
    ret
```
