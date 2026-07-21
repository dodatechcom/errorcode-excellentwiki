---
title: "[Solution] Assembly LEA vs MOV Error -- Address Calculation Mistakes"
description: "Fix assembly LEA vs MOV errors when confusing address calculation with memory load."
languages: ["assembly"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Assembly LEA vs MOV Error

This error occurs when LEA (Load Effective Address) is confused with MOV, causing incorrect address calculation.

## Common Causes

- Using MOV where LEA is needed for address calculation
- Using LEA where MOV is needed for memory load
- LEA with wrong address size
- Incorrect addressing mode syntax

## How to Fix

### Use LEA for address calculation

```asm
; WRONG: loads value at address, not address itself
mov rax, [rbx + rcx*4]  ; loads value

; CORRECT: LEA computes address without dereferencing
lea rax, [rbx + rcx*4]  ; rax = rbx + rcx*4
```

### Use MOV for value loading

```asm
; WRONG: LEA loads address
lea rax, [value]  ; rax = address of value

; CORRECT: MOV loads value
mov rax, [value]  ; rax = value at address
```

## Examples

```asm
; Calculate array element address
lea rax, [array + rcx*8]  ; rax = &array[rcx]

; Load array element
mov rax, [array + rcx*8]  ; rax = array[rcx]
```
