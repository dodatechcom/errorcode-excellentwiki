---
title: "[Solution] Assembly Struct Padding Error -- Incorrect Structure Layout"
description: "Fix assembly struct padding errors when structures have unexpected padding between fields."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Struct Padding Error

This error occurs when structure fields are accessed at incorrect offsets due to compiler-inserted padding.

## Common Causes

- Misunderstanding alignment requirements for fields
- Accessing fields at wrong offsets
- Different compilers adding different amounts of padding
- Mixing C struct layout assumptions in assembly

## How to Fix

### Account for padding

```asm
; WRONG: assuming no padding
; struct { char a; int b; } -- actually 8 bytes, not 5
section .data
struc MyStruct
    .a resb 1
    .b resd 1  ; offset 4, not 1!
endstruc

; CORRECT: use proper alignment
section .data
align 4
struc MyStruct
    .a resb 1
    align 4
    .b resd 1
endstruc
```

### Match C structure layout

```c
// C: struct { char a; int b; char c; };
// Assembly offsets: a=0, b=4, c=8, size=12
```

## Examples

```asm
section .data
; Match C struct { int x; char y; int z; }
struc Point3D
    .x resd 1   ; offset 0
    .y resb 1   ; offset 4
    align 4
    .z resd 1   ; offset 8
endstruc
```
