---
title: "[Solution] Assembly cdecl Calling Convention Error — How to Fix"
description: "Fix cdecl calling convention errors in assembly when caller and callee disagree on stack cleanup and argument passing."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1025
---

# cdecl Calling Convention Error

In the cdecl convention, the caller pushes arguments right-to-left and cleans the stack after the call. The return value is in EAX. Violating these rules causes stack corruption and wrong return values.

## Common Causes

- Callee cleaning the stack (stdcall behavior) when caller expects cdecl
- Not aligning RSP to 16 bytes before CALL in 64-bit code
- Wrong argument order (left-to-right instead of right-to-left)
- Forgetting to preserve callee-saved registers (EBX, ESI, EDI, EBP)

## How to Fix

### Solution 1 — Proper 32-bit cdecl function

```assembly
; cdecl: caller cleans stack
cdecl_func:
    push ebp
    mov ebp, esp
    mov eax, [ebp + 8]     ; first argument
    add eax, [ebp + 12]    ; second argument
    pop ebp
    ret                    ; caller does: add esp, 8

; Caller:
    push dword 20
    push dword 22
    call cdecl_func
    add esp, 8             ; clean up 2 arguments
```

### Solution 2 — 64-bit System V AMD64 ABI

```assembly
; Arguments in RDI, RSI, RDX, RCX, R8, R9 (integer/pointer)
; RSP must be 16-byte aligned before CALL
sysv_func:
    push rbp
    mov rbp, rsp
    mov rax, rdi            ; first argument
    add rax, rsi            ; second argument
    pop rbp
    ret

; Caller:
    mov rdi, 22
    mov rsi, 20
    call sysv_func
    ; no stack cleanup needed
```

### Solution 3 — Preserve callee-saved registers

```assembly
my_callee:
    push rbx                ; must preserve
    push rsi                ; must preserve
    push rdi                ; must preserve
    ; ... use RBX, RSI, RDI freely ...
    pop rdi
    pop rsi
    pop rbx
    ret
```

### Solution 4 — 32-bit Windows cdecl (with underscore prefix)

```assembly
; Windows 32-bit cdecl adds underscore to function names
global _my_function
_my_function:
    push ebp
    mov ebp, esp
    mov eax, [ebp + 8]
    pop ebp
    ret
```

## Examples

A library function uses stdcall (callee cleans stack) but the caller compiles with cdecl (expects to clean). After the call, ESP is off by the argument size, corrupting the stack frame. Ensuring both sides agree on the convention fixes the corruption.

## Related Errors

- [Stdcall Error](/languages/assembly/asm-stdcall-error) — Windows convention
- [Fastcall Error](/languages/assembly/asm-fastcall-error) — register-based convention
- [Stack Frame Error](/languages/assembly/asm-stack-frame-error) — frame pointer setup
