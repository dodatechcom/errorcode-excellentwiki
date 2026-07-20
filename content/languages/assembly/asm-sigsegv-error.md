---
title: "[Solution] Assembly SIGSEGV Error — How to Fix"
description: "Fix SIGSEGV (segmentation fault) errors in assembly caused by invalid memory access or null pointer dereference."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1003
---

# SIGSEGV — Segmentation Fault

SIGSEGV (signal 11) fires when the CPU cannot translate a virtual address — the page table entry is missing, the page is not accessible at the requested ring, or segmentation protection is violated.

## Common Causes

- Dereferencing a null or uninitialized pointer
- Writing to read-only memory (e.g., .rodata or text segment)
- Stack overflow hitting the guard page
- Use-after-free accessing a munmap'd region

## How to Fix

### Solution 1 — Validate pointers before use

```assembly
safe_deref:
    test rdi, rdi
    jz .null_ptr
    cmp rdi, 0x7FFFFFFFF000  ; sanity: user-space max
    ja .invalid_ptr
    mov rax, [rdi]          ; safe dereference
    ret
.null_ptr:
.invalid_ptr:
    mov rax, -1
    ret
```

### Solution 2 — Mark read-only data correctly

```assembly
section .rodata
my_const: dq 42

section .text
    mov rax, [my_const]     ; OK
    ; mov [my_const], rbx   ; would SIGSEGV — .rodata is read-only
```

### Solution 3 — Set up stack guard page

```assembly
; Allocate stack with PROT_NONE guard page
    mov eax, 12             ; sys_mprotect
    mov rdi, guard_page
    mov rsi, 4096
    mov rdx, 0              ; PROT_NONE
    syscall
```

### Solution 4 — Use signal handler for diagnostics

```assembly
section .data
sa_flags:   dq 0x00000004    ; SA_SIGINFO
sa_handler: dq sigsegv_handler

section .text
sigsegv_handler:
    ; rdi = siginfo_t*, rsi = ucontext_t*
    mov rax, [rsi + 128]    ; get faulting RIP from ucontext
    ; log or dump register state
    mov rax, 60
    xor edi, edi
    syscall
```

## Examples

A linked list traversal follows a corrupted next pointer that is NULL. The `mov rax, [rdi]` dereferences address 0x0, triggering SIGSEGV. A null-check before dereferencing prevents the crash.

## Related Errors

- [Page Fault](/languages/assembly/asm-page-fault-error) — page-level memory fault
- [General Protection Fault](/languages/assembly/asm-general-protection-v2) — protection ring violations
- [Stack Overflow](/languages/assembly/asm-stack-error) — stack exhaustion
