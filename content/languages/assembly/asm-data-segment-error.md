---
title: "[Solution] Assembly Data Segment Error -- Read-Only Data Modification"
description: "Fix assembly data segment errors when attempting to write to read-only data sections."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Data Segment Error

This error occurs when attempting to write to memory in the `.rodata` or `.text` sections, causing a segmentation fault.

## Common Causes

- Modifying string constants in `.rodata`
- Writing to `.text` section for self-modifying code
- Incorrect section attributes for writable data
- Using `db` in `.text` instead of `.data`

## How to Fix

### Use correct section for writable data

```asm
; WRONG: writing to .rodata
section .rodata
    msg db "hello", 0

section .text
    mov byte [msg], 'H'  ; segfault!

; CORRECT: use .data for writable data
section .data
    msg db "hello", 0

section .text
    mov byte [msg], 'H'  ; OK
```

### Use correct section directives

```asm
section .data        ; read-write data
section .rodata      ; read-only data
section .bss         ; uninitialized data
section .text        ; code (execute-only on modern OS)
```

## Examples

```asm
section .data
    mutable_str db "changeable", 0

section .text
    global _start
_start:
    mov byte [mutable_str], 'C'  ; valid
```
