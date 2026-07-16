---
title: "[Solution] Java AbstractMethodError — Abstract Method Invocation Fix"
description: "Fix Java AbstractMethodError by ensuring concrete implementations exist, recompiling all classes, and resolving classpath conflicts."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["abstractmethoderror", "abstract", "interface", "linkage"]
weight: 5
---

# AbstractMethodError — Abstract Method Invocation Fix

An `AbstractMethodError` is thrown when your code attempts to call an abstract method at runtime. This is a subclass of `IncompatibleClassChangeError` and occurs when a class that was abstract at compile time is no longer abstract at runtime, or when a method was declared abstract but no implementation is provided.

## Description

The error occurs when the JVM tries to invoke a method that has no implementation. This typically happens when classes are recompiled independently or when classpath conflicts cause an outdated version of a class to be loaded.

## Common Causes

```java
// Cause 1: Interface method not implemented by concrete class
public interface Service {
    void execute();  // abstract method
}

public class MyService implements Service {
    // Missing implementation of execute()
}

// Cause 2: Abstract class without full implementation
public abstract class BaseHandler {
    public abstract void handle();
}

public class ConcreteHandler extends BaseHandler {
    // Forgot to implement handle()
}

// Cause 3: Classpath contains outdated compiled class
// Interface updated with new method but implementing class not recompiled

// Cause 4: Classloader conflict loading different versions
// Two JARs contain the same class at different compilation stages
```

## Solutions

```java
// Fix 1: Ensure all interface methods are implemented
public class MyService implements Service {
    @Override
    public void execute() {
        System.out.println("Executing service");
    }
}

// Fix 2: Clean and rebuild all modules
// mvn clean compile

// Fix 3: Verify all abstract methods are implemented
public abstract class BaseHandler {
    public abstract void handle();
}

public class ConcreteHandler extends BaseHandler {
    @Override
    public void handle() {
        System.out.println("Handling request");
    }
}

// Fix 4: Check classpath for duplicate classes
// Use -verbose:class to see which class file is loaded
// java -verbose:class -jar myapp.jar
```

## Examples

```java
// This triggers AbstractMethodError
public interface Logger {
    void log(String message);
}

public class ConsoleLogger implements Logger {
    // log() method missing
}

ConsoleLogger logger = new ConsoleLogger();
logger.log("hello");  // AbstractMethodError
```

## Related Exceptions

- [IncompatibleClassChangeError](../linkageerror) — parent class for class structure changes
- [ClassFormatError]({{< relref "/languages/java/classformaterror" >}}) — class file is malformed
- [NoSuchMethodError]({{< relref "/languages/java/nosuchmethoderror" >}}) — method not found in class hierarchy
