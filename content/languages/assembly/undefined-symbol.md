---
title: "Undefined symbol"
description: "An undefined symbol error occurs when the linker cannot find the definition of a referenced function or variable."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["linker", "symbol", "undefined", "link-time"]
weight: 5
---

## What This Error Means

An undefined symbol error occurs when the assembler or linker encounters a reference to a label, function, or variable that has not been defined anywhere in the source files or linked libraries. This is a link-time error that prevents the executable from being produced.

## Common Causes

- Missing `global` or `extern` declaration for a symbol
- Typo in a function or variable name
- Forgetting to link against the library that provides the symbol
- Referencing a label that was removed or renamed

## How to Fix

```asm
; WRONG: Using a symbol without declaring it
section .text
    call my_function      ; where is my_function defined?

; CORRECT: Declare external symbols or define them
extern my_function       ; declared in another object file

section .text
    call my_function      ; linker will resolve this
```

```asm
; WRONG: Forgetting to export a symbol for other files
section .text
helper_func:
    mov rax, 42
    ret

; CORRECT: Mark the symbol as global so other files can use it
section .text
    global helper_func
helper_func:
    mov rax, 42
    ret
```

## Examples

```asm
section .text
    global _start

_start:
    call calculate        ; undefined - never defined anywhere
    mov rdi, rax
    mov rax, 60
    syscall

; Symbol is missing entirely - linker will fail:
; ld: undefined symbol: calculate
```

## Related Errors

- [Linker error: undefined reference](/languages/assembly/linker-error)
- [Invalid instruction](/languages/assembly/invalid-instruction)
