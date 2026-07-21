---
title: "[Solution] Assembly Data Size Error -- Operand Size Mismatch"
description: "Fix assembly data size errors when using wrong-sized registers for data operations."
languages: ["assembly"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Assembly Data Size Error

This error occurs when operand sizes do not match, such as loading a byte into a 32-bit register.

## Common Causes

- Using MOV with mismatched source/destination sizes
- Accessing array elements with wrong stride
- Not using zero/sign extension for byte/word operations
- Mixed 8-bit and 32-bit operations

## How to Fix

### Match operand sizes

```asm
; WRONG: size mismatch
mov eax, [byte_ptr]  ; loads 4 bytes, not 1

; CORRECT: use proper size
movzx eax, byte [byte_ptr]  ; zero-extend byte to dword
```

### Use correct extension

```asm
; Zero extension (unsigned)
movzx eax, byte [data]   ; byte to dword, zero-extend
movzx rax, word [data]   ; word to qword, zero-extend

; Sign extension (signed)
movsx eax, byte [data]   ; byte to dword, sign-extend
```

## Examples

```asm
; Process byte array
    movzx eax, byte [rsi + rcx]  ; load byte
    add edx, eax                  ; add to accumulator
```
