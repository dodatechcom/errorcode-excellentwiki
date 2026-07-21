---
title: "[Solution] Assembly Section Error -- Invalid Section Declarations"
description: "Fix assembly section errors when sections are declared incorrectly."
languages: ["assembly"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Assembly Section Error

This error occurs when assembly sections are declared incorrectly or have conflicting attributes.

## Common Causes

- Mixing read-only and read-write in same section
- Missing section declarations before code
- Using wrong section flags for the target format
- Section names not matching linker script expectations

## How to Fix

### Use correct section declarations

```asm
; WRONG: mixing attributes
section .data
    immutable: db "constant"
    mutable: dd 0  ; writable in .data

; CORRECT: separate sections
section .rodata
    immutable: db "constant"
section .data
    mutable: dd 0
```

### Match section to content type

```asm
section .text     ; executable code
section .data     ; initialized read-write data
section .rodata   ; read-only data (constants)
section .bss      ; uninitialized data
```

## Examples

```asm
section .rodata
    pi: dq 3.14159265358979

section .data
    counter: dd 0

section .bss
    buffer: resb 1024
```
