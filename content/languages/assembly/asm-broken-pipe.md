---
title: "[Solution] SIGPIPE: broken pipe in assembly"
description: "Fix assembly SIGPIPE errors when writing to a pipe or socket whose read end has been closed."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["sigpipe", "broken-pipe", "pipe", "socket", "signal", "assembly"]
weight: 5
---

## What This Error Means

SIGPIPE occurs when a process writes to a pipe or socket that has no reading process (the read end was closed). The kernel sends SIGPIPE to the writing process, which typically terminates it.

## Common Causes

- Writing to pipe after reader closed
- Socket connection reset by peer
- Shell pipeline broken
- File descriptor closed prematurely
- Network connection dropped

## How to Fix

```asm
; WRONG: No SIGPIPE handling
section .text
    ; Write to pipe - may get SIGPIPE
    mov rax, 1       ; sys_write
    mov rdi, [pipe_fd]
    lea rsi, [rel data]
    mov rdx, 10
    syscall           ; May generate SIGPIPE

; CORRECT: Ignore SIGPIPE
section .text
    ; Set SIG_IGN for SIGPIPE (signal 13)
    mov rax, 13      ; SIGPIPE
    mov rdi, 1       ; SIG_IGN
    mov rsi, 0
    mov rdx, 0
    mov rax, 13      ; sys_rt_sigaction
    mov rdi, 13      ; sig
    lea rsi, [rel act]
    xor rdx, rdx
    mov r10, 8       ; sizeof(sigset_t)
    syscall
```

```asm
; CORRECT: Check write return value
section .text
    mov rax, 1       ; sys_write
    mov rdi, fd
    lea rsi, [rel data]
    mov rdx, 10
    syscall
    
    ; Check for error
    cmp rax, 0
    jl .write_error
    ; rax = bytes written
    
    jmp .done
.write_error:
    ; Handle error (errno = -rax)
    neg rax
    cmp rax, 32      ; EPIPE
    jne .other_error
    ; Handle broken pipe specifically
.other_error:
.done:
```

```asm
; CORRECT: Use MSG_NOSIGNAL for sockets
section .text
    ; send() with MSG_NOSIGNAL flag
    mov rax, 44      ; sys_sendto
    mov rdi, sock_fd
    lea rsi, [rel data]
    mov rdx, 10
    mov r10, 0x4000  ; MSG_NOSIGNAL
    xor r8, r8
    xor r9, r9
    syscall
```

```asm
; CORRECT: Handle SIGPIPE with signal handler
section .data
    sigaction_struct:
        dq sigpipe_handler  ; sa_handler
        dq 0                ; sa_flags
        dq 0                ; sa_mask

section .text
sigpipe_handler:
    ; Handle SIGPIPE - just return
    mov rax, 0
    ret

section .text
    ; Install handler
    mov rax, 13       ; sys_rt_sigaction
    mov rdi, 13       ; SIGPIPE
    lea rsi, [rel sigaction_struct]
    xor rdx, rdx
    mov r10, 8
    syscall
```

## Related Errors

- [Invalid Syscall](asm-invalid-syscall) - syscall errors
- [Segmentation Fault](asm-segmentation-fault-v2) - memory access
- [General Protection](asm-general-protection-v2) - protection faults
