---
title: "[Solution] Java IllegalAccessError — Module Access Fix"
description: "Fix java.lang.IllegalAccessError by checking access modifiers, using setAccessible(true) cautiously, and opening packages in module-info.java."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IllegalAccessError — Module Access Fix

An `IllegalAccessError` is thrown when a program attempts to access or modify a field, call a method, or inherit a class that it does not have permission to access. Unlike `IllegalAccessException` (which is thrown by reflection), this `Error` is thrown by the JVM when bytecode directly violates access control rules.

## Description

IllegalAccessError extends `IncompatibleClassChangeError`. It is thrown when:

- Bytecode tries to access a `private`, `protected`, or package-private member from another class without proper access.
- The Java module system (JPMS) blocks access to a package that is not exported.
- Dynamic proxies or bytecode manipulation tools generate code that bypasses access checks incorrectly.

Common message variants include:

- `IllegalAccessError: class com.example.Caller cannot access a member of class com.example.Target`
- `IllegalAccessError: Attempt to access class com.example.Internal from class com.example.External`
- `IllegalAccessError: module java.base does not "opens java.lang" to unnamed module`

## Common Causes

```java
// Cause 1: Direct access to private field from another class
public class User {
    private String name; // Private field
}
public class Accessor {
    String n = new User().name; // IllegalAccessError at runtime
}

// Cause 2: Module system blocks reflective access
// Spring reflection tries to access java.lang internals
// JDK 17+ has strong encapsulation

// Cause 3: Bytecode manipulation (CGLIB, Javassist) accessing private members
// Proxy class tries to call private method on target
```

## Solutions

### Fix 1: Use proper access modifiers or getters/setters

```java
// Bad: Direct field access
public class User {
    private String name;
}
new User().name; // IllegalAccessError

// Good: Use getter/setter
public class User {
    private String name;

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}

User user = new User();
user.setName("John"); // Works
String name = user.getName(); // Works
```

### Fix 2: Use setAccessible for reflection (use cautiously)

```java
import java.lang.reflect.Field;

public class ReflectionAccessor {
    public static void setField(Object obj, String fieldName, Object value) {
        try {
            Field field = obj.getClass().getDeclaredField(fieldName);
            field.setAccessible(true); // Bypass access check
            field.set(obj, value);
        } catch (NoSuchFieldException | IllegalAccessException e) {
            throw new RuntimeException("Cannot access field: " + fieldName, e);
        }
    }
}
```

### Fix 3: Open packages in module-info.java

```java
// For your own module
module com.example.app {
    // Export public API
    exports com.example.api;

    // Open package for reflection (frameworks like Spring, Jackson)
    opens com.example.model;

    // Or open entire module for deep reflection
    opens com.example;
}

// For third-party modules — add JVM arguments
// --add-opens java.base/java.lang=ALL-UNNAMED
// --add-opens java.base/java.lang.reflect=ALL-UNNAMED
```

```xml
<!-- Maven: Add JVM args for test and runtime -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <argLine>
            --add-opens java.base/java.lang=ALL-UNNAMED
            --add-opens java.base/java.lang.reflect=ALL-UNNAMED
            --add-opens java.base/java.util=ALL-UNNAMED
        </argLine>
    </configuration>
</plugin>
```

### Fix 4: Configure framework module access

```bash
# Spring Boot: Add to application startup
java --add-opens java.base/java.lang=ALL-UNNAMED \
     --add-opens java.base/java.lang.reflect=ALL-UNNAMED \
     --add-opens java.base/java.util=ALL-UNNAMED \
     --add-opens java.base/java.math=ALL-UNNAMED \
     -jar myapp.jar

# Or in JAVA_TOOL_OPTIONS environment variable
export JAVA_TOOL_OPTIONS="--add-opens java.base/java.lang=ALL-UNNAMED"
```

## Prevention Checklist

- Use public/protected access modifiers and provide getters/setters.
- Avoid direct field access across class boundaries.
- Use `setAccessible(true)` only as a last resort.
- Add `--add-opens` JVM arguments for frameworks requiring reflection.
- Test with JDK 17+ strong encapsulation enabled.
- Document module opens in module-info.java.

## Related Errors

- [IllegalAccessException](../illegalaccessexception) — Reflective access violation.
- [LinkageError](../linkageerror) — Class linkage failure.
- [NoClassDefFoundError](../noclassdeffounderror) — Class not found at runtime.
