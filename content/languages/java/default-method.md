---
title: "[Solution] Java class X is not abstract and does not override abstract method Y — Fix Missing Implementation"
description: "Fix Java compiler error 'class is not abstract and does not override abstract method' by implementing the method, adding abstract modifier, or using default method in interface. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 458
---

# Java Compiler Error: class X is not abstract and does not override abstract method Y

This compile-time error occurs when a concrete (non-abstract) class does not implement all abstract methods inherited from its superclass or interfaces. Every concrete class must provide implementations for all abstract methods in its type hierarchy.

## Error Message

```
error: Dog is not abstract and does not override abstract method speak() in Animal
public class Dog extends Animal {
       ^
```

Other variants:

```
error: class X is not abstract and does not override abstract method Y in Z
error: X is not abstract and does not override abstract method Y
```

## Common Causes

### Cause 1: Missing Implementation of Abstract Method

```java
abstract class Animal {
    abstract void speak();
    abstract void eat();
}

class Dog extends Animal {
    void speak() { System.out.println("Woof"); }
    // ERROR: missing eat() implementation
}
```

### Cause 2: Interface Method Not Implemented

```java
interface Serializable {
    byte[] serialize();
}

class DataRecord implements Serializable {
    // ERROR: serialize() not implemented
}
```

### Cause 3: Inherited Abstract Method From Multi-Level Hierarchy

```java
abstract class Shape {
    abstract double area();
}

abstract class Polygon extends Shape {
    abstract int sides();
}

class Triangle extends Polygon {
    // ERROR: must implement both area() and sides()
    int sides() { return 3; }
}
```

### Cause 4: Adding Abstract Method to Existing Class

```java
abstract class Repository {
    // Previously concrete class, now has abstract method
    abstract void save(Object entity);

    // All existing subclasses now fail to compile
}

class UserRepository extends Repository {
    // ERROR: must implement save(Object entity)
}
```

### Cause 5: Forgetting One of Multiple Interface Methods

```java
interface Readable {
    char read();
}

interface Closeable {
    void close();
}

class MyReader implements Readable, Closeable {
    public char read() { return 'a'; }
    // ERROR: close() not implemented
}
```

## Solutions

### Fix 1: Implement All Missing Abstract Methods

```java
abstract class Animal {
    abstract void speak();
    abstract void eat();
}

class Dog extends Animal {
    @Override
    void speak() { System.out.println("Woof"); }

    @Override
    void eat() { System.out.println("Eating kibble"); }
}
```

### Fix 2: Make the Class Abstract

```java
abstract class Dog extends Animal {
    @Override
    void speak() { System.out.println("Woof"); }
    // eat() still abstract — class is abstract, so this is OK
}
```

### Fix 3: Add Default Method to the Interface (Java 8+)

```java
interface Repository {
    default void save(Object entity) {
        throw new UnsupportedOperationException("Not implemented yet");
    }
}

class UserRepository implements Repository {
    // save() has a default — no compilation error
}
```

### Fix 4: Implement Remaining Methods

```java
interface Readable {
    char read();
}

interface Closeable {
    void close();
}

class MyReader implements Readable, Closeable {
    @Override
    public char read() { return 'a'; }

    @Override
    public void close() { /* cleanup */ }
}
```

### Fix 5: Use Abstract Intermediate Class

```java
abstract class BaseRepository implements Repository {
    // Provide partial implementation
    @Override
    public void save(Object entity) {
        validate(entity);
        doSave(entity);
    }

    protected abstract void doSave(Object entity);
    protected abstract void validate(Object entity);
}
```

## Prevention Checklist

- Always implement all abstract methods from superclasses and interfaces
- Use `@Override` annotation to verify method signatures match
- Consider making classes `abstract` when not all methods can be implemented
- Add default methods to interfaces when you want backward-compatible changes
- Use IDE quick-fixes to auto-generate method stubs
- Test compilation after adding abstract methods to existing interfaces

## Related Errors

- [abstract method errors (abstract-method-in-abstract-class)](/languages/java/abstract-method-in-abstract-class)
- [X is abstract; cannot be instantiated (abstract-method)](/languages/java/abstract-method)
- [method does not override or implement a method from a supertype (override-methods)](/languages/java/override-methods)
