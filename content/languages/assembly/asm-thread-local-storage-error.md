---
title: "[Solution] Assembly Thread Local Storage Error -- TLS Access Issues"
description: "Fix assembly thread local storage errors when accessing TLS variables incorrectly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Thread Local Storage Error

This error occurs when thread-local storage (TLS) is accessed with incorrect segment registers or addressing modes.

## Common Causes

- Not using GS/FS segment override for TLS access
- Wrong TLS model (local-exec, initial-exec, general-dynamic)
- TLS variable not declared with __thread/_Thread_local
- Incorrect offset in TLS block

## How to Fix

### Use correct TLS access

```asm
; WRONG: accessing TLS as regular variable
mov rax, [my_tls_var]  ; wrong, not thread-local

; CORRECT: use FS segment for TLS (x86-64 Linux)
mov rax, [fs:my_tls_var@tpoff]

; Or use %fs: prefix
mov rax, fs:[0]  ; get TLS base
```

### Use proper TLS model

```asm
; Local execution (within same module)
mov rax, [fs:my_var@tpoff]

; Initial execution (dynamically linked)
; Use __tls_get_addr for general-dynamic model
```

## Examples

```asm
section .tls
my_thread_var: dq 0

section .text
get_thread_var:
    mov rax, [fs:my_thread_var@tpoff]
    ret
```
