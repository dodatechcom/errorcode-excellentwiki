---
title: "[Solution] Assembly Stack Canary Error -- Buffer Overflow Protection"
description: "Fix assembly stack canary errors when stack protection is not properly implemented."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Stack Canary Error

This error occurs when stack buffer overflow protection (canaries) is not properly implemented or checked.

## Common Causes

- Not placing canary between local variables and saved RBP/return address
- Canary value not initialized from random source
- Missing canary check before RET
- Canary not placed in all functions with buffers

## How to Fix

### Implement stack canary

```asm
; WRONG: no stack protection
vulnerable_func:
    push rbp
    mov rbp, rsp
    sub rsp, 64
    ; buffer overflow can overwrite return address
    leave
    ret

; CORRECT: add canary
vulnerable_func:
    push rbp
    mov rbp, rsp
    sub rsp, 72
    mov rax, [fs:0x28]    ; load canary from TLS
    mov [rbp-8], rax       ; place canary
    ; ... body ...
    mov rax, [rbp-8]
    xor rax, [fs:0x28]    ; verify canary
    jne .stack_smash
    leave
    ret
.stack_smash:
    call __stack_chk_fail
```

## Examples

```asm
; Function with stack canary
safe_func:
    push rbp
    mov rbp, rsp
    sub rsp, 32
    mov rax, [fs:0x28]
    mov [rbp-8], rax
    ; ... body ...
    mov rax, [rbp-8]
    xor rax, [fs:0x28]
    jne .fail
    leave
    ret
.fail:
    call __stack_chk_fail
```
