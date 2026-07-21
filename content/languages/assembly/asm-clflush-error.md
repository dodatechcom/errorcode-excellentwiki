---
title: "[Solution] Assembly CLFLUSH Error -- Cache Line Flush Issues"
description: "Fix assembly CLFLUSH errors when using cache line flush instructions incorrectly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["warning"]
---

# Assembly CLFLUSH Error

This error occurs when CLFLUSH is used incorrectly, causing performance issues or incorrect cache behavior.

## Common Causes

- Flushing non-existent cache line
- Using CLFLUSH where MFENCE is needed
- Not checking CLFLUSH support via CPUID
- Flushing too frequently causing performance degradation

## How to Fix

### Use CLFLUSH correctly

```asm
; WRONG: flushing constantly in loop
.loop:
    clflush [rdi]  ; slow!
    ; ...
    jmp .loop

; CORRECT: flush only when needed
    clflush [rdi]
    mfence         ; ensure flush completes
```

### Check CLFLUSH support

```asm
has_clflush:
    mov eax, 1
    cpuid
    test edx, 1 << 19  ; CLFLUSH bit
    setnz al
    movzx eax, al
    ret
```

## Examples

```asm
; Flush cache line and ensure ordering
flush_cache:
    clflush [rdi]
    mfence
    ret
```
