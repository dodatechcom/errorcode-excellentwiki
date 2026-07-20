---
title: "[Solution] Assembly Stdcall Convention Error — How to Fix"
description: "Fix stdcall calling convention errors in assembly when callee-stack cleanup is implemented incorrectly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1026
---

# Stdcall Calling Convention Error

In the Windows stdcall convention, arguments are pushed right-to-left and the callee cleans the stack via `RET n`. If the callee uses plain `RET` or the caller cleans up, the stack becomes misaligned.

## Common Causes

- Callee uses `RET` instead of `RET 8` (for 2 dword arguments)
- Caller does `ADD ESP, n` after a stdcall call (double cleanup)
- Mixing cdecl and stdcall functions in the same call chain
- Forgetting `_FunctionName` name decoration for stdcall

## How to Fix

### Solution 1 — Callee cleans stack with RET n

```assembly
; stdcall: callee cleans 8 bytes (2 dword args)
global _add_numbers@8
_add_numbers@8:
    push ebp
    mov ebp, esp
    mov eax, [ebp + 8]
    add eax, [ebp + 12]
    pop ebp
    ret 8                   ; clean 8 bytes from stack
```

### Solution 2 — Caller does NOT clean stack

```assembly
; WRONG: caller cleans after stdcall (double cleanup)
    push 20
    push 22
    call _add_numbers@8
    add esp, 8              ; WRONG — callee already cleaned!

; CORRECT: caller does nothing after stdcall
    push 20
    push 22
    call _add_numbers@8     ; callee does: ret 8
    ; EAX = result, stack already clean
```

### Solution 3 — Use STDCALL macro for consistency

```assembly
%macro stdcall_func 1
    push ebp
    mov ebp, esp
    ; arguments at [ebp+8], [ebp+12], ...
    %endmacro

%macro stdcall_ret 1
    pop ebp
    ret %1                  ; n = number of argument bytes
    %endmacro
```

### Solution 4 — Declare stdcall in linker/NASM

```bash
# NASM: export with correct decoration
nasm -f win32 file.asm

# Linker: ensure @N suffix matches argument size
link /subsystem:console file.obj
```

## Examples

A Windows API call to `CreateFileA` expects stdcall. The assembly routine pushes 7 arguments (28 bytes) and calls the function. If the function returns with `RET` instead of `RET 28`, ESP is off by 28 bytes when the next instruction executes, causing a stack fault.

## Related Errors

- [cdecl Error](/languages/assembly/asm-cdecl-error) — caller cleanup convention
- [Fastcall Error](/languages/assembly/asm-fastcall-error) — register convention
- [Stack Frame Error](/languages/assembly/asm-stack-frame-error) — frame setup
