---
title: "[Solution] Java CannotCatchError — InternalError Fix"
description: "Fix Java CannotCatchError (InternalError) by avoiding catching Error subclasses, fixing JVM-level issues, and handling unrecoverable failures gracefully."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# CannotCatchError — InternalError Fix

A `CannotCatchError` (typically an `InternalError`) is thrown when the JVM encounters an internal error that it cannot recover from. This is a subclass of `VirtualMachineError` and indicates a serious problem with the JVM itself or with the bytecode being executed.

## Description

`InternalError` indicates that the JVM has encountered an unexpected internal condition. This is different from application-level errors and typically signals a JVM bug, corrupted internal state, or bytecode that violates JVM invariants.

## Common Causes

```java
// Cause 1: JVM bug or internal corruption
// Rare, but can happen with specific bytecode patterns

// Cause 2: Stack corruption from native code via JNI
public native void corruptStack();

// Cause 3: Infinite recursion that exhausts native stack
// Different from StackOverflowError — occurs in native frames

// Cause 4: JVM resource exhaustion (internal tables, code cache)
// When JIT compiler runs out of code cache space
```

## Solutions

```java
// Fix 1: Report the issue to JVM maintainers with full stack trace
try {
    // problematic code
} catch (InternalError e) {
    e.printStackTrace();  // capture full details
    // Report to JVM vendor
}

// Fix 2: Increase JVM code cache for JIT compilation issues
// java -XX:ReservedCodeCacheSize=256m -jar myapp.jar

// Fix 3: Avoid problematic JNI native code
// Review and fix native method implementations

// Fix 4: Restart the JVM if internal state is corrupted
// Use a process manager (systemd, supervisord) to auto-restart
```

## Examples

```java
// InternalError can occur in various scenarios
public class Example {
    public void triggerError() {
        // This might trigger InternalError in certain JVM implementations
        int[] arr = new int[Integer.MAX_VALUE];
    }
}
```

## Related Exceptions

- [VirtualMachineError](../stackoverflowerror) — parent class for JVM errors
- [OutOfMemoryError]({{< relref "/languages/java/outofmemoryerror" >}}) — JVM memory exhausted
- [StackOverflowError]({{< relref "/languages/java/stackoverflowerror" >}}) — call stack exhausted
