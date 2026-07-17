---
title: "[Solution] Java IllegalAccessException — Access Permission Fix"
description: "Fix Java IllegalAccessException by using setAccessible, opening modules, or providing proper access modifiers for reflective access to fields and methods."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IllegalAccessException — Access Permission Fix

An `IllegalAccessException` is thrown when your code attempts to access a field, method, or constructor reflectively and the Java access control system denies the operation — typically because the member is `private`, `protected`, or in a different package without proper access.

## Description

This is a checked exception (extends `ReflectiveOperationException`). It occurs when reflective access violates Java's visibility rules:

- `IllegalAccessException: Cannot access a member of class com.example.Target`
- `IllegalAccessException: class com.example.Caller cannot access a member of class com.example.Target`

## Common Causes

```java
// Cause 1: Accessing a private field without setAccessible
Field field = clazz.getDeclaredField("secret");
field.get(instance);  // IllegalAccessException — field is private

// Cause 2: Accessing a method in a different package without access
// Class in package a trying to call protected method in package b
Method method = otherClass.getDeclaredMethod("protectedMethod");
method.invoke(otherInstance);  // IllegalAccessException

// Cause 3: Accessing a constructor without proper permissions
Constructor<?> ctor = privateClass.getDeclaredConstructor();
ctor.newInstance();  // IllegalAccessException

// Cause 4: Module system blocks access (Java 9+)
Class<?> clazz = Class.forName("java.lang.String");
Field field = clazz.getDeclaredField("value");
field.setAccessible(true);  // InaccessibleObjectException (subclass of IllegalAccessException)
```

## Solutions

### Fix 1: Use `setAccessible(true)` for private members

```java
Field field = clazz.getDeclaredField("privateField");
field.setAccessible(true);  // Bypass access check
Object value = field.get(instance);
```

### Fix 2: Open the module/package for reflection (Java 9+)

```java
// In module-info.java
opens com.example.model to com.fasterxml.jackson.core, java.base;
```

```bash
# Or via JVM flags
java --add-opens com.example.model/com.example.model=ALL-UNNAMED -jar app.jar
java --add-opens java.base/java.lang=ALL-UNNAMED -jar app.jar
```

### Fix 3: Change access modifiers to allow reflective access

```java
// Wrong — field is private, blocks reflective access
public class User {
    private String name;
}

// Correct — make accessible or add getter
public class User {
    public String name;  // Or use a getter
    public String getName() { return name; }
}
```

### Fix 4: Use `MethodHandles.Lookup` for controlled access (Java 9+)

```java
// Requires module to open the package to your module
MethodHandles.Lookup lookup = MethodHandles.privateLookupIn(clazz, MethodHandles.lookup());
VarHandle handle = lookup.findVarHandle(clazz, "field", String.class);
```

## Prevention Checklist

- Use `setAccessible(true)` only when truly necessary and log a warning.
- For Java 9+ modular applications, declare `opens` directives for packages that need reflective access.
- Prefer public APIs and getters/setters over direct field access via reflection.
- Use `MethodHandles` for modern, module-friendly reflection.

## Related Errors

- [InstantiationException](../instantiationexception) — cannot instantiate the target class.
- [InvocationTargetException](../invocationtargetexception) — target method threw an exception.
- [ReflectiveOperationException](../reflectiveoperationexception) — parent class for all reflection failures.
