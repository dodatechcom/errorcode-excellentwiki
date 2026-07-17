---
title: "[Solution] Java BootstrapMethodError — InvokeDynamic Fix"
description: "Fix Java BootstrapMethodError by resolving method handle issues, ensuring compatible library versions, and verifying invokedynamic bytecode integrity."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# BootstrapMethodError — InvokeDynamic Fix

A `BootstrapMethodError` is thrown when the JVM cannot successfully link an `invokedynamic` instruction. This typically occurs when a bootstrap method (used by lambdas, method references, and string concatenation in Java 7+) fails during resolution. It is a subclass of `LinkageError`.

## Description

The `invokedynamic` bytecode instruction, introduced in Java 7, is the foundation for lambda expressions and string concatenation. When the bootstrap method referenced by `invokedynamic` cannot be found or fails, this error is thrown.

## Common Causes

```java
// Cause 1: Lambda in a class loaded by incompatible classloader
ClassLoader loader1 = new URLClassLoader(urls1);
ClassLoader loader2 = new URLClassLoader(urls2);
// Lambda in loader1's class referencing loader2's type

// Cause 2: Method handle lookup failure due to access restrictions
// Lambda referencing a private method in another class

// Cause 3: Corrupted class file with invalid invokedynamic
// Bytecode manipulation tool generating invalid bootstrap method ref

// Cause 4: Version mismatch between compiled and runtime classes
// Lambda compiled with JDK 11 but run on JDK 8
```

## Solutions

```java
// Fix 1: Ensure all classes are compiled with compatible JDK versions
// Use --release flag for cross-compilation
// javac --release 11 MyClass.java

// Fix 2: Avoid lambdas that reference private methods across classloaders
// Instead, use a factory method or protected access
public class SafeFactory {
    protected Runnable createTask() {
        return this::execute;  // safe reference to own method
    }
    private void execute() {
        System.out.println("Running task");
    }
}

// Fix 3: Replace lambdas with anonymous classes if classloader issues persist
Runnable task = new Runnable() {
    @Override
    public void run() {
        System.out.println("Running task");
    }
};

// Fix 4: Verify class file integrity
// javap -v MyClass.class | grep invokedynamic
```

## Examples

```java
// This can trigger BootstrapMethodError in complex classloader scenarios
public interface Processor {
    void process(String data);
}

public class App {
    public static void main(String[] args) {
        // Lambda relies on bootstrap method for invokedynamic
        Processor p = data -> System.out.println(data);
        p.process("hello");  // BootstrapMethodError if bootstrap fails
    }
}
```

## Related Exceptions

- [LinkageError](../linkageerror) — parent class for class linkage failures
- [ClassFormatError]({{< relref "/languages/java/classformaterror" >}}) — class file is malformed
- [AbstractMethodError]({{< relref "/languages/java/abstractmethodexception" >}}) — abstract method invocation failure
