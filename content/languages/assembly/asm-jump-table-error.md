---
title: "[Solution] Assembly Jump Table Error -- Incorrect Indirect Jump"
description: "Fix assembly jump table errors when using indexed jump tables for switch statements."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Jump Table Error

This error occurs when jump table entries are incorrect or the index calculation causes an out-of-bounds jump.

## Common Causes

- Index not bounds-checked before table lookup
- Jump table entries not aligned to pointer size
- Missing entries in the table
- Table base address incorrect

## How to Fix

### Bounds-check the index

```asm
; WRONG: no bounds check
mov eax, [case_index]
jmp [jump_table + rax*8]

; CORRECT: bounds check first
mov eax, [case_index]
cmp eax, MAX_CASE
ja .default_case
jmp [jump_table + rax*8]
```

### Align jump table entries

```asm
section .data
align 8  ; align to pointer size
jump_table:
    dq case_0
    dq case_1
    dq case_2
```

## Examples

```asm
section .text
switch:
    cmp edi, 3
    ja .default
    lea rax, [switch_table]
    movsxd rcx, edi
    jmp qword [rax + rcx*8]

switch_table:
    dq .case0
    dq .case1
    dq .case2
    dq .case3
```
