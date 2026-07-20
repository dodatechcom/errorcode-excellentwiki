---
title: "[Solution] Java ClassCircularityError — Circular Class Hierarchy Fix"
description: "Fix Java ClassCircularityError when class hierarchy has circular dependency by restructuring class hierarchy, breaking circular dependency, and recompiling all classes."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 8
---

# ClassCircularityError — Circular Class Hierarchy Fix

A `ClassCircularityError` is thrown when the JVM detects a circular reference during class linking — the class hierarchy contains a loop that prevents safe initialization. This is a `LinkageError` subclass that occurs during class loading, not during normal execution.

## Description

The JVM links classes in phases: loading, verification, preparation, and resolution. If class A requires class B to be loaded, and class B requires class A, the JVM cannot determine the correct initialization order and throws this error. Unlike `ClassCircularReferenceError` (which relates to circular references), `ClassCircularityError` specifically indicates a circular class hierarchy.

Message variants:

- `java.lang.ClassCircularityError: com/example/ClassA`
- `java.lang.ClassCircularityError: com/example/InterfaceA`
- `Exception in thread "main" java.lang.ClassCircularityError: com/example/Base`

## Common Causes

```java
// Cause 1: Circular class inheritance
public class Parent extends Child { }  // Parent extends Child
public class Child extends Parent { }  // Child extends Parent — cycle

// Cause 2: Circular interface implementation
public interface A extends B { }
public interface B extends A { }

// Cause 3: Interface that extends a class (not allowed, but can cause confusion)
public class MyClass implements Runnable {
    // If Runnable somehow referenced MyClass — circular

// Cause 4: Circular dependency through superclass and subclass
public class BaseService {
    static {
        SubService.init();  // triggers SubService loading
    }
}
public class SubService extends BaseService {
    static {
        BaseService.init();  // triggers BaseService loading — circular
    }
}

// Cause 5: Circular generic type bounds
public class Node<T extends Node<T>> {
    T child;
}
// If the bound resolution creates a loop, ClassCircularityError can occur
```

## Solutions

### Fix 1: Restructure the class hierarchy to remove cycles

```java
// Wrong — circular inheritance
public class Manager extends Employee {
    List<Employee> team;
}
public class Employee extends Manager {  // circular!
    Manager supervisor;
}

// Right — use composition
public class Manager {
    private final Employee delegate;  // composition, not inheritance
    private final List<Employee> team;

    public Manager(Employee delegate, List<Employee> team) {
        this.delegate = delegate;
        this.team = team;
    }
}

public class Employee {
    private Manager supervisor;
}
```

### Fix 2: Break circular static initializer dependencies

```java
// Wrong — circular static initialization
public class ServiceA {
    static ServiceB b;
    static { b = new ServiceB(); }
}
public class ServiceB {
    static ServiceA a;
    static { a = new ServiceA(); }
}

// Right — lazy initialization breaks the cycle
public class ServiceA {
    private static ServiceB b;
    public static synchronized ServiceB getB() {
        if (b == null) b = new ServiceB();
        return b;
    }
}

public class ServiceB {
    private static ServiceA a;
    public static synchronized ServiceA getA() {
        if (a == null) a = new ServiceA();
        return a;
    }
}
```

### Fix 3: Break circular interface inheritance

```java
// Wrong — circular interface
public interface Readable extends Writable { }
public interface Writable extends Readable { }

// Right — separate interfaces with a shared base
public interface IOBase { }
public interface Readable extends IOBase { }
public interface Writable extends IOBase { }

public class MyIO implements Readable, Writable { }
```

### Fix 4: Recompile all classes when changing inheritance

```bash
# Clean and rebuild everything when you change class hierarchies
# Maven
mvn clean compile

# Gradle
gradle clean build

# Manual javac — compile all files together
javac -d out $(find src -name "*.java")

# Never mix old .class files with new ones — delete target/classes first
rm -rf target/classes && mvn compile
```

## Prevention Checklist

- Never create circular inheritance relationships between classes.
- Break circular static initializer dependencies with lazy initialization.
- Avoid circular interface extends chains.
- Recompile all dependent classes when restructuring class hierarchies.
- Use composition over inheritance to avoid hierarchy-related circular dependencies.
- Delete old `.class` files before recompiling.

## Related Errors

- [ClassCircularReferenceError](../classcircularreference) — circular reference during class loading
- [IncompatibleClassChangeError](../incompatibleclasschangeerror) — class structure changed between compilations
- [NoClassDefFoundError](../noclassdeffounderror) — class file missing at runtime
- [ExceptionInInitializerError](../exceptionininitializererror) — static initializer failed
