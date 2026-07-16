---
title: "[Solution] Kotlin General Protection Fault — JVM Crash Fix"
description: "Fix Kotlin General Protection Fault (JVM crash). This is a fatal JVM error, not a catchable exception. Check JVM version, memory settings, and native code."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["general-protection-fault", "jvm", "crash", "fatal", "native"]
weight: 5
---

# General Protection Fault — JVM Crash Fix

A General Protection Fault (GPF) is a fatal JVM error that causes the process to crash. It's not a catchable exception — the JVM terminates immediately. This typically indicates a JVM bug, corrupted memory, or issues with native code.

## Description

General Protection Fault is a CPU-level exception that occurs when a process performs an illegal operation at the hardware level. In the JVM context, it usually means corrupted internal state, a JIT compiler bug, or problematic native library code.

Common scenarios:

- **JVM bug** — bug in the JVM's JIT compiler or runtime.
- **Corrupted memory** — memory corruption from native libraries.
- **Stack overflow** — extreme recursion causing stack corruption.
- **Native library crash** — JNI library accessing invalid memory.
- **Corrupted class files** — damaged .class files loaded by the JVM.

## Common Causes

```kotlin
// Cause 1: JNI/native library crash
System.loadLibrary("problematic-native-lib")  // GPF if native code crashes

// Cause 2: Extreme recursion
tailrec fun infiniteRecursion(n: Int): Int = infiniteRecursion(n + 1)
// May cause JVM crash if not properly optimized

// Cause 3: Corrupted classpath
// Running with corrupted .class files
// java -cp "corrupted.jar" MainKt

// Cause 4: JVM bug with specific bytecode patterns
// Rare, but JIT compiler bugs can cause GPF
```

## Solutions

### Fix 1: Update JVM

```bash
# Wrong — using outdated JVM with known bugs
java -version  # Java 8u201

# Correct — use latest stable JVM
# Download latest JDK from https://adoptium.net/
java -version  # Java 21 or latest LTS
```

### Fix 2: Disable JIT compiler for debugging

```bash
# Temporarily disable JIT to see if it's a JIT bug
java -Xint MainKt

# Or use C2 compiler only
java -XX:+UnlockDiagnosticVMOptions -XX:TieredStopAtLevel=1 MainKt
```

### Fix 3: Increase stack size

```bash
# Wrong — default stack size may be too small
java MainKt

# Correct — increase stack size
java -Xss4m MainKt

# Or in Kotlin
fun main() {
    // Increase thread stack size for deep recursion
    val thread = Thread(null, {
        deepRecursion()
    }, "worker", 8 * 1024 * 1024)  // 8MB stack
    thread.start()
}
```

### Fix 4: Check native library compatibility

```kotlin
// Wrong — loading incompatible native library
System.loadLibrary("native-lib")  // May crash if wrong architecture

// Correct — verify library compatibility
try {
    System.loadLibrary("native-lib")
} catch (e: UnsatisfiedLinkError) {
    println("Native library not found or incompatible: ${e.message}")
}
```

## Examples

```kotlin
fun main() {
    println("If you see General Protection Fault:")
    println("1. Update your JVM to the latest version")
    println("2. Check for native library issues")
    println("3. Try disabling JIT: java -Xint MainKt")
    println("4. Increase stack size: java -Xss4m MainKt")
    println("5. Check for corrupted class files")
}
```

## Related Errors

- [StackOverflowError]({{< relref "/languages/kotlin/stack-overflow" >}}) — stack overflow from recursion.
- [OutOfMemoryError]({{< relref "/languages/kotlin/out-of-memory" >}}) — heap memory exhausted.
- [UnsatisfiedLinkError]({{< relref "/languages/kotlin/class-not-found" >}}) — native library not found.
