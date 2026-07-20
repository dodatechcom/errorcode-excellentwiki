---
title: "[Solution] Java InaccessibleObjectException — Module Access Reflection Fix"
description: "Fix Java InaccessibleObjectException by using --add-opens, opening packages in module-info.java, and using setAccessible(true) with proper module configuration."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 66
---

# InaccessibleObjectException — Module Access Reflection Fix

An `InaccessibleObjectException` is thrown when reflective access to a field, method, or constructor is blocked by the Java module system. Introduced in Java 9, this exception replaced many of the older `IllegalAccessException` and `SecurityException` cases for module-internal elements.

## Description

`java.lang.reflect.InaccessibleObjectException` extends `IllegalAccessException`. Common variants include:

- `java.lang.reflect.InaccessibleObjectException: Unable to make field private java.lang.String java.lang.String.value accessible: module java.base does not "opens java.lang" to unnamed module`
- `java.lang.reflect.InaccessibleObjectException: Unable to make method final void java.lang.Object.finalize() accessible: module java.base does not "opens java.lang" to unnamed module @...`
- `Strong encapsulation` errors when frameworks try to access JDK internals

Since Java 9, strong encapsulation prevents frameworks from deeply reflecting into JDK internals unless explicitly permitted.

## Common Causes

```java
// Cause 1: Accessing private field in java.lang classes
Field valueField = String.class.getDeclaredField("value");
valueField.setAccessible(true);  // InaccessibleObjectException (module java.base not open)

// Cause 2: Accessing internal Sun/Oracle classes
Field unsafeField = Unsafe.class.getDeclaredField("theUnsafe");
unsafeField.setAccessible(true);  // InaccessibleObjectException

// Cause 3: Framework accessing JDK internals (e.g., Spring, Mockito)
Constructor<MethodHandles.Lookup> lookup = MethodHandles.Lookup.class
    .getDeclaredConstructor(Class.class);
lookup.setAccessible(true);  // InaccessibleObjectException

// Cause 4: Using reflection on classes in a named module that does not open packages
// Your own module:
// module my.module { does not open com.my.module.internal; }

// Cause 5: Testing libraries accessing private constructors
Constructor<MyService> c = MyService.class.getDeclaredConstructor();
c.setAccessible(true);  // InaccessibleObjectException if MyService is in a module
```

## Solutions

### Fix 1: Add --add-opens JVM argument

```bash
java --add-opens java.base/java.lang=ALL-UNNAMED \
     --add-opens java.base/java.util=ALL-UNNAMED \
     --add-opens java.base/java.lang.reflect=ALL-UNNAMED \
     -jar app.jar

# Or for test execution:
mvn test --add-opens java.base/java.lang=ALL-UNNAMED
```

### Fix 2: Open packages in your module's module-info.java

```java
module my.library {
    // Open internal packages for reflection
    opens com.my.library.internal;
    // Or open everything in the module
    opens com.my.library;
}
```

### Fix 3: Use setAccessible(true) with module permission

```java
import java.lang.reflect.Field;
import java.lang.reflect.Modifier;

public static <T> void setFieldValue(Object obj, String fieldName, T value)
        throws ReflectiveOperationException {
    Field field = obj.getClass().getDeclaredField(fieldName);
    field.setAccessible(true);  // May throw InaccessibleObjectException
    field.set(obj, value);
}

// Run with: java --add-opens java.base/java.lang=ALL-UNNAMED
```

### Fix 4: Use the Unsafe API as a last resort

```java
import sun.misc.Unsafe;

Field f = Unsafe.class.getDeclaredField("theUnsafe");
f.setAccessible(true);
Unsafe unsafe = (Unsafe) f.get(null);

// Direct memory access bypasses module restrictions
long offset = unsafe.objectFieldOffset(MyClass.class.getDeclaredField("value"));
unsafe.putObject(myInstance, offset, newValue);
```

## Prevention Checklist

- Always add `--add-opens` flags when frameworks need reflective access to JDK internals
- Document required `--add-opens` flags in your project README
- Prefer public APIs over reflective access to internal classes
- Test with `--illegal-access=deny` (Java 9-16) or the module system restrictions (Java 17+)
- Use `module-info.java` to explicitly `open` packages your library needs to expose

## Related Errors

- [IllegalAccessException](/languages/java/illegalaccessexception/) — Similar but older; pre-module-system
- [SecurityException](/languages/java/securityexception/) — SecurityManager-based restrictions
- [NoSuchFieldException](/languages/java/nosuchfieldexception/) — Field does not exist (different root cause)
