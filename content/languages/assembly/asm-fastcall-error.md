---
title: "[Solution] Assembly Fastcall Convention Error — How to Fix"
description: "Fix fastcall calling convention errors in assembly when register-based argument passing violates ABI rules."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1027
---

# Fastcall Calling Convention Error

The fastcall convention passes the first two arguments in ECX and EDX (32-bit) or RCX, RDX, RDX, R8, R9 (64-bit Windows) to reduce stack traffic. Errors occur when arguments are passed on the stack instead of registers, or register clobbering is not handled.

## Common Causes

- Passing first two arguments on the stack instead of ECX/EDX
- Using ECX/EDX inside a fastcall function without saving them
- Mixing fastcall declarations between caller and callee
- Not accounting for the 4-byte stack alignment requirement (32-bit)

## How to Fix

### Solution 1 — Pass arguments in registers

```assembly
; 32-bit fastcall: first arg in ECX, second in EDX
fastcall_add:
    mov eax, ecx           ; first argument
    add eax, edx           ; second argument
    ret                    ; caller cleans stack (like cdecl)

; Caller:
    mov ecx, 22
    mov edx, 20
    call fastcall_add      ; EAX = 42
```

### Solution 2 — Save and restore scratch registers

```assembly
fastcall_safe:
    push ebx               ; save if using EBX
    mov ebx, ecx           ; save first arg
    ; ... do work using EDX ...
    mov eax, ebx           ; use saved first arg
    pop ebx
    ret
```

### Solution 3 — 64-bit Windows fastcall (4 register args)

```assembly
; RCX, RDX, R8, R9 for first 4 args, then stack
fastcall_64:
    mov rax, rcx           ; arg1
    add rax, rdx           ; arg2
    add rax, r8            ; arg3
    add rax, r9            ; arg4
    ret                    ; caller handles shadow space
```

### Solution 4 — Use GCC/MinGW fastcall (ECX, EDX)

```c
// In C: __attribute__((fastcall))
int __attribute__((fastcall)) add(int a, int b) {
    return a + b;
}
```

```assembly
; Assembly side: match the attribute
global _Z3addii@8
_Z3addii@8:
    mov eax, ecx
    add eax, edx
    ret
```

## Examples

A callback function is declared as fastcall but the caller pushes arguments onto the stack. The callee reads ECX/EDX which contain stale values from a previous call. Fixing the caller to pass in registers resolves the mismatch.

## Related Errors

- [cdecl Error](/languages/assembly/asm-cdecl-error) — stack-based convention
- [Stdcall Error](/languages/assembly/asm-stdcall-error) — callee cleanup
- [Calling Convention Error](/languages/assembly/asm-calling-convention-error) — general ABI
