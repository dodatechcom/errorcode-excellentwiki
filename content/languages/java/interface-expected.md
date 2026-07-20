---
title: "[Solution] Java interface expected here — Fix Missing Interface Type"
description: "Fix Java compiler error interface expected here by implementing interface, checking type hierarchy, and verifying implements clause. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 137
---

# Java Compiler Error: interface expected here

This compile-time error occurs when a type is used where the Java compiler expects an interface. This happens when using `implements`, passing to generic bounds requiring interfaces, or in other contexts where only interfaces are valid.

## Error Message

```
error: interface expected here
```

## Common Causes

### Cause 1: Using Class Instead of Interface in implements

```java
class BaseEntity { }

public class Example implements BaseEntity { }
// Error: BaseEntity is a class, not an interface
```

### Cause 2: Generic Bound Requires Interface

```java
import java.util.Comparator;

public class Example<T extends Comparable> {
    // Comparable is an interface, but raw type usage may cause issues
}
```

### Cause 3: Annotation Processing With Class

```java
import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@interface MyAnnotation { }

class NotAnInterface { }

@MyAnnotation
public class Example implements NotAnInterface { }
// Error if annotation requires interface
```

### Cause 4: Extending a Class With implements Keyword

```java
class Animal { }

public class Dog extends Animal implements Animal { }
// Error: Animal is a class, cannot be in implements clause
```

### Cause 5: Wrong Type in Functional Interface Context

```java
import java.util.function.Function;

class MyConverter { String convert(Object o) { return o.toString(); } }

public class Example {
    Function<Object, String> fn = new MyConverter()::convert;
    // May cause issues if MyConverter is not a functional interface
}
```

## Solutions

### Fix 1: Use extends for Classes

```java
class BaseEntity { }

public class Example extends BaseEntity { }
// Use 'extends' for class inheritance
```

### Fix 2: Implement an Actual Interface

```java
interface Loggable {
    void log();
}

public class Example implements Loggable {
    @Override
    public void log() {
        System.out.println("Logging");
    }
}
```

### Fix 3: Create Interface From Class

```java
interface Printable {
    void print();
}

class Document implements Printable {
    @Override
    public void print() {
        System.out.println("Printing document");
    }
}
```

### Fix 4: Use Correct Generic Bounds

```java
import java.util.Comparator;

public class Example<T extends Comparable<T>> {
    public int compare(T a, T b) {
        return a.compareTo(b);
    }
}
```

### Fix 5: Implement Functional Interface Properly

```java
import java.util.function.Function;

@FunctionalInterface
interface MyConverter {
    String convert(Object o);
}

public class Example {
    Function<Object, String> fn = Object::toString;
}
```

## Prevention Checklist

- Use `extends` for class inheritance and `implements` for interfaces
- Verify that the type you are implementing is actually an interface
- Use IDE quick-fixes to distinguish classes from interfaces
- Check generic type bounds to ensure they reference interfaces when required
- Create interfaces when you need to decouple implementation from contract
- Use `javap` to inspect whether a type is a class or interface

## Related Errors

- [abstract-method-in-abstract-class](/languages/java/abstract-method-in-abstract-class/)
- [anonymous-class-cannot-extend](/languages/java/anonymous-class-cannot-extend/)
- [override-methods](/languages/java/override-methods/)
