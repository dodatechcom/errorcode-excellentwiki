---
title: "[Solution] Assembly Macro Error -- Incorrect Macro Definitions"
description: "Fix assembly macro errors when using %macro directives incorrectly."
languages: ["assembly"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Assembly Macro Error

This error occurs when assembly macros are defined or invoked incorrectly.

## Common Causes

- Wrong parameter count in macro invocation
- Missing %endmacro directive
- Macro parameters not properly referenced with %1, %2
- Nested macros causing expansion issues

## How to Fix

### Define macros correctly

```asm
; WRONG: missing endmacro
%macro push_all 0
    push rax
    push rbx
    ; ...

; CORRECT: complete macro definition
%macro push_all 0
    push rax
    push rbx
    push rcx
    push rdx
%endmacro
```

### Reference parameters correctly

```asm
%macro mov_imm 2
    mov %1, %2
%endmacro

mov_imm rax, 42    ; expands to: mov rax, 42
mov_imm rbx, 100   ; expands to: mov rbx, 100
```

## Examples

```asm
%macro function_prologue 1
    push rbp
    mov rbp, rsp
    sub rsp, %1
%endmacro

%macro function_epilogue 0
    leave
    ret
%endmacro

my_func:
    function_prologue 32
    ; ... body ...
    function_epilogue
```
