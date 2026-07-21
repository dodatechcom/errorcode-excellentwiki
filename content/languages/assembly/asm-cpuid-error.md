---
title: "[Solution] Assembly CPUID Error -- Incorrect Feature Detection"
description: "Fix assembly CPUID errors when detecting CPU features incorrectly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly CPUID Error

This error occurs when CPUID is used incorrectly to detect CPU features or when the wrong leaf is queried.

## Common Causes

- Not setting EAX before CPUID call
- Checking wrong bit position for feature
- Not preserving EBX/EDX which CPUID clobbers
- Using CPUID leaf that CPU does not support

## How to Fix

### Use CPUID correctly

```asm
; WRONG: not setting EAX
cpuid  ; EAX may contain anything

; CORRECT: set EAX to desired leaf
mov eax, 1     ; processor info
cpuid
test edx, 1 << 25  ; check SSE
jz .no_sse
```

### Preserve registers

```asm
; CPUID clobbers EAX, EBX, ECX, EDX
push rbx
mov eax, 7     ; extended features
xor ecx, ecx   ; sub-leaf 0
cpuid
test ebx, 1 << 16  ; check AVX-512F
pop rbx
```

## Examples

```asm
; Check for SSE2 support
has_sse2:
    push rbx
    mov eax, 1
    cpuid
    pop rbx
    test edx, 1 << 26  ; SSE2 bit
    setnz al
    movzx eax, al
    ret
```
