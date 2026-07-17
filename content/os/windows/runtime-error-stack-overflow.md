---
title: "[Solution] Stack Overflow Runtime Error — Fix Stack Exhaustion"
description: "Fix stack overflow runtime errors on Windows. Resolve infinite recursion, deep call stacks, and thread stack size issues."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["stack-overflow", "recursion", "thread", "stack-size", "memory"]
weight: 5
---

# Stack Overflow Runtime Error — Stack Exhaustion

A stack overflow runtime error occurs when a program uses more stack space than is allocated for its thread. The crash dialog shows:

> "Runtime Error! Program: C:\...\program.exe
> R6025 - pure virtual function call"

Or an access violation at a stack address:

> "Exception code: 0xC00000FD — stack overflow"

## What This Error Means

Each thread in a Windows process has a fixed-size stack (default 1 MB for the main thread, 1 MB for worker threads). When a function calls itself recursively or the call chain is very deep, the stack grows until it hits the allocated limit. The program then crashes because it cannot allocate more stack space for local variables and return addresses.

## Common Causes

- Infinite recursion (function calling itself without a base case)
- Very deep recursion (thousands of nested calls)
- Large local arrays or structures on the stack
- Very small thread stack size allocated by the application
- Recursive data structures processed without tail-call optimization

## How to Fix

### Increase Thread Stack Size

For applications you control, increase the stack size:

```cmd
# Link with a larger stack (in Visual Studio / link.exe)
link /STACK:4194304 /SUBSYSTEM:CONSOLE app.obj
```

Or in Visual Studio project settings:
1. **Project Properties** > **Linker** > **System** > **Stack Reserve Size**
2. Set to `4194304` (4 MB) or higher.

### Rewrite Recursive Code as Iterative

Convert recursive algorithms to iterative ones with an explicit stack (heap-allocated):

```c
// Recursive (causes stack overflow)
void traverse(Node* node) {
    if (node == NULL) return;
    process(node);
    traverse(node->left);
    traverse(node->right);
}

// Iterative (safe)
void traverse(Node* root) {
    Stack* stack = createStack();
    push(stack, root);
    while (!isEmpty(stack)) {
        Node* node = pop(stack);
        process(node);
        if (node->right) push(stack, node->right);
        if (node->left) push(stack, node->left);
    }
    destroyStack(stack);
}
```

### Use `/GS` and `/SafeSEH` Protections

```cmd
# Enable in Visual Studio
cl /GS /SafeSEH app.c
```

### Analyze with Debug Diagnostics Tool

Download [Debug Diagnostic Tool](https://www.microsoft.com/en-us/download/details.aspx?id=58210) and configure it to capture stack overflow exceptions:

```powershell
# Set a breakpoint on 0xC00000FD exception
# Or use: DebugDiag to create a memory dump rule
```

### Check for Recursion with Process Explorer

1. Download [Process Explorer](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer).
2. Right-click the process > **Threads** tab.
3. Sort by **Stack Base** — a thread with a very small remaining stack indicates the problem.

## Related Errors

- [Buffer Overrun]({{< relref "/os/windows/runtime-error-buffer-overrun" >}}) — Stack buffer overflow from writing past boundaries
- [Access Violation 0xC0000005]({{< relref "/os/windows/runtime-error-c0000005" >}}) — General memory access violations
- [FastFail Error]({{< relref "/os/windows/runtime-error-fast-fail" >}}) — Fast-fail from security mitigations
