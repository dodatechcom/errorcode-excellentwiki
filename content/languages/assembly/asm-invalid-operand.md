---
title: "Invalid operand in Assembly"
description: "Invalid operand errors in Assembly occur when instruction operands have wrong types, sizes, or combinations."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Invalid operand errors happen when an instruction receives operands that are incompatible with its encoding. For example, `mov` cannot have both operands be memory references, or a size mismatch between operands.

## Common Causes

- Two memory operands in one instruction
- Size mismatch between operands
- Immediate value too large for operand size
- Wrong addressing mode

## How to Fix

```asm
; WRONG: Both operands are memory
mov [rax], [rbx]   ; Error: two memory operands

; CORRECT: Use register as intermediate
mov rcx, [rbx]
mov [rax], rcx
```

```asm
; WRONG: Size mismatch
mov al, [rbx+1000000]  ; Offset too large for 8-bit displacement

; CORRECT: Use proper addressing
lea rcx, [rbx+1000000]
mov al, [rcx]
```

## Examples

```asm
; Invalid operand examples
mov [rax], 0x100000000   ; Value too large for 32-bit store
push byte 0xFF           ; Cannot push byte on x86-64
```

## How to Debug

- Check NASM documentation for instruction forms
- Verify operand sizes match
- Use `-w+error` for warnings as errors

## Related Errors

- [Invalid Register](/languages/assembly/asm-invalid-register) - register errors
- [Invalid Instruction](/languages/assembly/asm-invalid-instruction) - opcode errors
