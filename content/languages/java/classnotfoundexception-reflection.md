---
title: "[Solution] Java ClassNotFoundException — Reflection Loading Fix"
description: "Fix Java ClassNotFoundException when loading class via Class.forName() by verifying fully qualified name, checking classpath, and using correct classloader."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 12
---

# ClassNotFoundException — Reflection Loading Fix

A `ClassNotFoundException` occurs when `Class.forName()` or a classloader attempts to load a class by its fully qualified name but cannot locate the corresponding `.class` file at runtime.

## Description

This variant focuses on reflection-based class loading failures. Unlike static imports (which fail at compile time), `Class.forName()` resolves class names dynamically, so errors only surface at runtime.

Message variants:

- `java.lang.ClassNotFoundException: com.example.MyClass`
- `java.lang.ClassNotFoundException: org.xml.sax.SAXParser`
- `Exception in thread "main" java.lang.ClassNotFoundException: com.mysql.cj.jdbc.Driver`

## Common Causes

```java
// Cause 1: Typo in fully qualified class name
Class.forName("com.example.Myclass");  // wrong capitalization — should be MyClass

// Cause 2: Class not on classpath at runtime
Class.forName("org.apache.commons.lang3.StringUtils");  // JAR not in runtime classpath

// Cause 3: Wrong classloader used
ClassLoader loader = Thread.currentThread().getContextClassLoader();
Class.forName("com.example.Plugin", true, loader);  // loader cannot see the class

// Cause 4: Class only exists at compile time (test scope)
Class.forName("com.example.TestHelper");  // compiled with test scope, not on runtime classpath

// Cause 5: Dynamic class name constructed incorrectly
String className = "com.example." + moduleName + "Service";  // moduleName is wrong
Class.forName(className);
```

## Solutions

### Fix 1: Verify the fully qualified class name

```java
// Use the canonical name from the class itself
String name = MyClass.class.getName();  // guaranteed correct
Class<?> clazz = Class.forName(name);

// Avoid constructing names with string concatenation
// Wrong
Class.forName("com.example." + "my" + "Service");
// Right — use constants
private static final String SERVICE_CLASS = "com.example.MyService";
Class.forName(SERVICE_CLASS);
```

### Fix 2: Check the runtime classpath

```bash
# Print the classpath your JVM sees
java -verbose:class -cp "libs/*:." Main 2>&1 | grep MyClass

# For Maven projects, use dependency:tree to inspect
mvn dependency:tree -Dincludes=com.example

# Ensure the dependency is compile scope, not just test
# pom.xml
<dependency>
    <groupId>com.example</groupId>
    <artifactId>my-lib</artifactId>
    <version>1.0</version>
    <scope>compile</scope>  <!-- NOT test -->
</dependency>
```

### Fix 3: Use the correct classloader

```java
// Wrong — uses bootstrap classloader which cannot see application classes
Class.forName("com.example.MyClass", false, null);

// Right — use the classloader that loaded your own code
Class<?> clazz = Class.forName(
    "com.example.MyClass",
    true,
    MyClass.class.getClassLoader()
);

// Right — use thread context classloader in application servers
ClassLoader loader = Thread.currentThread().getContextClassLoader();
Class<?> clazz = Class.forName("com.example.MyClass", true, loader);
```

### Fix 4: Handle ClassNotFoundException gracefully in reflection

```java
public static Optional<Class<?>> safeLoadClass(String className) {
    try {
        return Optional.of(Class.forName(className));
    } catch (ClassNotFoundException e) {
        System.err.println("Class not found: " + className
            + " — classpath: " + System.getProperty("java.class.path"));
        return Optional.empty();
    }
}

// Usage
Optional<Class<?>> clazz = safeLoadClass("com.example.MyService");
clazz.ifPresent(c -> {
    try {
        Object instance = c.getDeclaredConstructor().newInstance();
        // use instance
    } catch (Exception e) {
        e.printStackTrace();
    }
});
```

## Prevention Checklist

- Always use `ClassName.class.getName()` instead of hand-typed strings when possible.
- Catch and handle `ClassNotFoundException` in reflection-heavy code.
- Verify dependencies are `compile` scope, not `test` or `provided`.
- Print or log the classpath when diagnosing class loading failures.
- Use the same classloader to load and invoke reflective classes.

## Related Errors

- [ClassNotFoundException](../classnotfoundexception) — general class not found
- [NoClassDefFoundError](../noclassdeffounderror) — class was present at compile time but missing at runtime
- [ClassCastException](../classcastexception) — wrong class loaded from classpath
