---
title: "[Solution] Java InstantiationError — Object Creation Fix"
description: "Fix java.lang.InstantiationError by using factory methods instead of new for abstract classes, verifying class hierarchy, and checking for interface instantiation."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# InstantiationError — Object Creation Fix

An `InstantiationError` is thrown when a program attempts to use the Java `new` keyword to instantiate an abstract class or interface. This is an `Error` (not an `Exception`) and indicates a fundamental type violation that should have been caught at compile time but appeared due to dynamic class loading or bytecode manipulation.

## Description

InstantiationError extends `IncompatibleClassChangeError`. Unlike `InstantiationException` (which is thrown by reflection), this error is thrown by the JVM when the bytecode directly tries to `new` an abstract class or interface. It typically occurs when:

- A class was abstract at compile time but concrete at runtime, or vice versa.
- Dynamic proxies or bytecode generation tools create incorrect subclasses.
- Classpath conflicts load an incompatible version of a class.

Common message variants include:

- `InstantiationError: com.example.AbstractService`
- `InstantiationError: com.example.Drawable (interface)`
- `InstantiationError: Cannot instantiate abstract class`

## Common Causes

```java
// Cause 1: Direct instantiation of an abstract class
public abstract class Shape {
    abstract void draw();
}
Shape s = new Shape(); // InstantiationError

// Cause 2: Direct instantiation of an interface
public interface Runnable {
    void run();
}
Runnable r = new Runnable(); // InstantiationError

// Cause 3: Bytecode manipulation creating invalid subclass
// CGLIB or Javassist generates a subclass that doesn't extend properly
```

## Solutions

### Fix 1: Use factory methods instead of direct instantiation

```java
public abstract class Shape {
    abstract void draw();

    public static Shape create(String type) {
        switch (type) {
            case "circle": return new Circle();
            case "rectangle": return new Rectangle();
            default: throw new IllegalArgumentException("Unknown shape: " + type);
        }
    }
}

// Usage
Shape s = Shape.create("circle"); // Works — concrete class
```

### Fix 2: Use reflection or DI for abstract class creation

```java
// Spring: Use @ComponentScan to inject concrete implementations
@Service
public class Circle extends Shape {
    @Override
    void draw() { /* draw circle */ }
}

@Component
public class ShapeRenderer {
    @Autowired
    private Shape shape; // Spring injects Circle (the concrete implementation)

    public void render() {
        shape.draw(); // Works — Circle is a concrete class
    }
}
```

### Fix 3: Fix bytecode generation issues

```java
// Ensure CGLIB generates proper subclasses
// CGLIB requires a no-arg constructor (can be protected)
public abstract class BaseService {
    protected BaseService() {} // Required for CGLIB proxying
}

// For Hibernate proxies, ensure entity classes are not final
@Entity
public class User { // NOT final — allows proxy subclassing
    @Id
    private Long id;
}
```

### Fix 4: Validate class hierarchy at runtime

```java
public class ClassValidator {
    public static <T> T instantiateSafe(Class<T> clazz) {
        if (clazz.isInterface()) {
            throw new IllegalArgumentException("Cannot instantiate interface: " + clazz.getName());
        }
        if (Modifier.isAbstract(clazz.getModifiers())) {
            throw new IllegalArgumentException("Cannot instantiate abstract class: " + clazz.getName());
        }
        try {
            Constructor<T> constructor = clazz.getDeclaredConstructor();
            constructor.setAccessible(true);
            return constructor.newInstance();
        } catch (ReflectiveOperationException e) {
            throw new RuntimeException("Failed to instantiate: " + clazz.getName(), e);
        }
    }
}
```

## Prevention Checklist

- Never use `new` on abstract classes or interfaces — use factories or DI.
- Ensure bytecode-generated classes (CGLIB, Javassist) extend correctly.
- Use `Modifier.isAbstract()` checks when dynamically loading classes.
- Keep entity classes non-final to allow proxy subclassing.
- Test class hierarchy assumptions in unit tests.

## Related Errors

- [InstantiationException](../instantiationexception) — Reflective instantiation of abstract class.
- [IllegalAccessException](../illegalaccessexception) — Access control violation.
- [LinkageError](../linkageerror) — Class linkage failure.
