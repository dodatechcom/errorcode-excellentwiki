---
title: "[Solution] Assembly AT&T Syntax Error — How to Fix"
description: "Fix AT&T syntax errors in assembly when using GNU assembler (GAS) with incorrect operand notation."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1035
---

# AT&T Syntax Error

AT&T syntax (used by GAS) reverses operand order, prefixes registers with `%`, immediates with `$`, and uses parentheses for memory. These conventions differ from Intel/NASM and cause frequent errors.

## Common Causes

- Using Intel operand order (`mov eax, 42`) in AT&T syntax
- Forgetting `%` prefix on register names
- Using `[]` for memory instead of `()`
- Not using `$` for immediate values

## How to Fix

### Solution 1 — Follow AT&T operand order (src, dst)

```assembly
; AT&T: instruction src, dst
    movl $42, %eax         ; eax = 42
    movl %eax, (%ebx)      ; [ebx] = eax
    addl $8, %esp          ; esp += 8
```

### Solution 2 — Use correct memory syntax

```assembly
; AT&T memory: displacement(base, index, scale)
    movl 8(%ebp), %eax     ; eax = [ebp + 8]
    movl (%ebx,%ecx,4), %eax  ; eax = [ebx + ecx*4]
    movl -4(%rsp), %eax    ; eax = [rsp - 4]
```

### Solution 3 — Use size suffixes

```assembly
; AT&T requires size suffixes on some instructions
    movb $65, %al          ; byte
    movw $1000, %ax        ; word
    movl $100000, %eax     ; dword
    movq $0x1000000, %rax  ; qword
```

### Solution 4 — Switch to Intel syntax

```assembly
.intel_syntax noprefix
; Now use Intel syntax: dst, src
mov eax, 42
mov [ebx], eax
```

## Examples

A developer writes `movl %eax, 42(%ebx)` but means `[ebx+42] = eax`. In AT&T, this is actually `eax = [ebx+42]`. The operand order confusion swaps load and store, corrupting memory. Understanding the src,dst order fixes the bug.

## Related Errors

- [NASM vs GAS](/languages/assembly/asm-nasm-gas-error) — syntax comparison
- [MODRM Error](/languages/assembly/asm-modrm-error) — encoding issues
- [AT&T Syntax](/languages/assembly/asm-att-syntax-error) — general syntax
