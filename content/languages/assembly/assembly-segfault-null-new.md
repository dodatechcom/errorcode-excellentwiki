---
title: "[Solution] Assembly: segmentation fault null pointer dereference"
description: "Fix Assembly segfaults from null pointer dereference by validating pointers and checking returns."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A segmentation fault from null pointer dereference in Assembly occurs when the program attempts to read from or write to memory address 0x0 (NULL). On Linux, this produces a SIGSEGV signal. The kernel detects that the page at address 0 is not mapped into the process address space and terminates the program. This error typically produces the message `Segmentation fault (core dumped)` or in gdb shows `Program received signal SIGSEGV, Segmentation fault`.

## Why It Happens

Null pointer dereferences occur when a pointer variable contains the value zero and is used to access memory. This commonly happens when a function returns NULL (0) as an error indicator and the caller does not check for this condition before dereferencing the result. In Assembly, register values may be zero if not properly initialized. System calls that return error codes in RAX may leave the register at zero, and subsequent use of RAX as a pointer triggers the fault. Linked list or tree traversal code that does not check for NULL child pointers crashes when reaching a leaf node. Memory allocation functions that fail return NULL, and using the returned pointer without checking causes the fault.

## How to Fix It

**Check pointers before dereferencing:**

```asm
; WRONG: dereference without null check
my_function:
    mov rdi, [rsi]      ; RSI might be NULL
    ; Crash if RSI = 0

; CORRECT: check for null first
my_function:
    test rsi, rsi       ; Check if pointer is NULL
    jz .null_error      ; Jump if NULL
    mov rdi, [rsi]      ; Safe to dereference
    ret

.null_error:
    mov rax, -1         ; Return error code
    ret
```

**Validate malloc return values:**

```asm
section .text
extern malloc
extern free

allocate_buffer:
    push rbp
    mov rbp, rsp
    sub rsp, 16

    mov rdi, 1024       ; Request 1024 bytes
    call malloc
    test rax, rax       ; Check for NULL
    jz .alloc_failed

    ; RAX contains valid pointer
    mov [rbp-8], rax    ; Store pointer safely

    ; Use the buffer...
    mov byte [rax], 0   ; Safe dereference

    mov rax, [rbp-8]
    leave
    ret

.alloc_failed:
    xor rax, rax        ; Return NULL
    leave
    ret
```

**Initialize pointers explicitly:**

```asm
section .data
    null_ptr dq 0       ; Explicit NULL

section .bss
    buffer resq 1       ; Uninitialized pointer

section .text
init_example:
    ; WRONG: using uninitialized pointer
    ; mov rax, [buffer]  ; Contains garbage

    ; CORRECT: initialize first
    mov qword [buffer], 0  ; Set to NULL
    ; Now safe to check
    mov rax, [buffer]
    test rax, rax
    jz .handle_null
```

**Check return values from system calls:**

```asm
; Linux read syscall
; RAX=0, RDI=fd, RSI=buffer, RDX=count
safe_read:
    push rbp
    mov rbp, rsp
    sub rsp, 32

    mov rax, 0          ; SYS_read
    mov rdi, [fd]       ; File descriptor
    lea rsi, [rbp-32]   ; Buffer on stack
    mov rdx, 32         ; Count
    syscall

    ; Check for error (negative return)
    test rax, rax
    js .read_error
    ; RAX contains bytes read
    leave
    ret

.read_error:
    mov rax, -1
    leave
    ret
```

## Common Mistakes

- Not checking function return values before using them as pointers
- Forgetting that `malloc`, `calloc`, and `mmap` can return NULL on failure
- Using a pointer after freeing the memory it points to
- Not initializing pointer variables before first use
- Assuming the OS will always provide memory when requested

## Related Pages

- [Stack smashing in Assembly](/languages/assembly/assembly-stack-smashing-new)
- [Page fault in Assembly](/languages/assembly/assembly-page-fault-new)
- [Invalid opcode in Assembly](/languages/assembly/assembly-invalid-opcode-new)
- [mmap failed in Assembly](/languages/assembly/assembly-mmap-error-new)
