---
title: "[Solution] Assembly Stack Alignment Error -- ABI Violation"
description: "Fix assembly stack alignment errors when violating the System V or Windows ABI stack requirements."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Stack Alignment Error

This error occurs when the stack pointer is not properly aligned before calling functions, violating ABI requirements.

## Common Causes

- Stack not 16-byte aligned before CALL instruction
- PUSH/POP mismatch causing misalignment
- Incorrect function prologue/epilogue
- Calling conventions with different alignment requirements

## How to Fix

### Ensure 16-byte alignment before call

```asm
; WRONG: stack not aligned before call
push rax
push rbx
call printf  ; may crash if stack misaligned

; CORRECT: ensure alignment
push rbp
mov rbp, rsp
and rsp, -16  ; align to 16 bytes
call printf
mov rsp, rbp
pop rbp
```

### Use proper prologue/epilogue

```asm
; System V AMD64 ABI: RSP must be 16-byte aligned before CALL
my_function:
    push rbp
    mov rbp, rsp
    sub rsp, 32  ; allocate shadow space + alignment
    ; ... body ...
    leave
    ret
```

## Examples

```asm
section .text
global call_with_alignment

call_with_alignment:
    push rbp
    mov rbp, rsp
    push rbx           ; odd number of pushes
    and rsp, -16       ; align to 16 bytes
    call external_func
    lea rsp, [rbp-8]
    pop rbx
    pop rbp
    ret
```
