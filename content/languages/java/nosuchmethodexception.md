---
title: "[Solution] Java NoSuchMethodException — Reflection Method Not Found Fix"
description: "Fix Java NoSuchMethodException by checking method name and parameter types, using getDeclaredMethods() to list all methods, and verifying generics."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 56
---

# NoSuchMethodException — Reflection Method Not Found Fix

A `NoSuchMethodException` is thrown when code tries to look up a method via `Class.getMethod()`, `Class.getDeclaredMethod()`, `Class.getConstructor()`, or `Class.getDeclaredConstructor()` but no matching method or constructor exists.

## Description

`java.lang.NoSuchMethodException` extends `ReflectiveOperationException`. Common variants include:

- `java.lang.NoSuchMethodException: com.example.User.setName(java.lang.String)`
- `java.lang.NoSuchMethodException: com.example.User.<init>()`
- `java.lang.NoSuchMethodException: no method: getId() in class com.example.User`

This is one of the most common reflection errors and usually results from a mismatched method name, wrong parameter types, or forgetting that generics are erased at runtime.

## Common Causes

```java
// Cause 1: Wrong method name
Method m = User.class.getMethod("get_username");  // NoSuchMethodException: method is getUsername()

// Cause 2: Wrong parameter types
Method m = User.class.getMethod("setId", int.class);  // NoSuchMethodException: expects Integer

// Cause 3: Using getMethod() for a private method
Method m = User.class.getMethod("validate");  // NoSuchMethodException: validate is private

// Cause 4: Constructor with wrong signature
Constructor<User> c = User.class.getDeclaredConstructor(String.class);  // NoSuchMethodException

// Cause 5: Bridge methods from generics not accessible
Method m = GenericService.class.getMethod("process", Object.class);  // NoSuchMethodException
```

## Solutions

### Fix 1: List all declared methods to find the correct signature

```java
Method[] methods = User.class.getDeclaredMethods();
for (Method method : methods) {
    System.out.println(Modifier.toString(method.getModifiers()) + " " +
        method.getReturnType().getSimpleName() + " " +
        method.getName() + "(" +
        Arrays.stream(method.getParameterTypes())
              .map(Class::getSimpleName)
              .collect(Collectors.joining(", ")) + ")");
}
```

### Fix 2: Walk the class hierarchy to find inherited methods

```java
public static Method findMethod(Class<?> clazz, String name, Class<?>... paramTypes)
        throws NoSuchMethodException {
    Class<?> current = clazz;
    while (current != null) {
        try {
            return current.getDeclaredMethod(name, paramTypes);
        } catch (NoSuchMethodException e) {
            current = current.getSuperclass();
        }
    }
    throw new NoSuchMethodException("Method " + name + " not found in " + clazz.getName());
}
```

### Fix 3: Match exact parameter types including wrapper classes

```java
// These are different and will not match each other:
Method m1 = MyClass.class.getMethod("process", int.class);      // matches int
Method m2 = MyClass.class.getMethod("process", Integer.class);  // matches Integer

// For varargs, the type is the array component type:
Method m3 = MyClass.class.getMethod("process", String[].class);
```

### Fix 4: Use getDeclaredMethod for any visibility level

```java
Method m = User.class.getDeclaredMethod("validate");
m.setAccessible(true);  // enables access to private methods
m.invoke(userInstance);
```

## Prevention Checklist

- Always list methods using `getDeclaredMethods()` when unsure of the exact signature
- Double-check parameter types — `int.class` and `Integer.class` are different
- Use `getDeclaredMethod()` + `setAccessible(true)` instead of `getMethod()` for non-public methods
- Walk the superclass hierarchy when the method may be inherited
- Use IDE auto-complete or documentation to verify method signatures before reflection

## Related Errors

- [NoSuchFieldException](/languages/java/nosuchfieldexception/) — Same issue but for fields
- [IllegalAccessException](/languages/java/illegalaccessexception/) — Method found but access denied
- [InvocationTargetException](/languages/java/reflectiveoperationexception/) — Method found but threw an exception internally
