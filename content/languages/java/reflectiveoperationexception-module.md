---
title: "[Solution] Java InaccessibleObjectException — Module System Fix"
description: "Fix Java InaccessibleObjectException in module system by using --add-opens, modifying module-info.java, and using privileged actions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# InaccessibleObjectException — Module System Fix

An `InaccessibleObjectException` is thrown when reflective access to a field, method, or constructor is blocked by the Java module system (Java 9+). This occurs when code in one module tries to reflectively access members of another module that has not been explicitly opened for reflection.

## Description

Java 9+ introduced the module system (`JPMS`) which enforces strong encapsulation. Modules must explicitly declare which packages they `open` for reflective access. Without an `opens` directive, reflective calls to `setAccessible(true)` on members of that module will fail with `InaccessibleObjectException`.

Message variants:

- `java.lang.reflect.InaccessibleObjectException: Unable to make field private java.lang.String value accessible: module java.base does not "opens java.lang" to unnamed module @1a2b3c4d`
- `java.lang.reflect.InaccessibleObjectException: Unable to make method public void process() accessible: module my.module does not "opens com.example.service" to all unnamed modules`
- `java.lang.reflect.InaccessibleObjectException: Cannot access final field`

## Common Causes

```java
// Cause 1: Reflective access to JDK internal classes
Field field = String.class.getDeclaredField("value");
field.setAccessible(true);  // InaccessibleObjectException — java.base not opened

// Cause 2: Accessing private members of another module
// In module A:
public class SecretService {
    private void internalProcess() { }
}
// In module B (unnamed):
Method method = SecretService.class.getDeclaredMethod("internalProcess");
method.setAccessible(true);  // InaccessibleObjectException

// Cause 3: Framework accessing module members without opens directive
// Hibernate/Jackson trying to access private fields of model classes
// in a module that doesn't open its packages

// Cause 4: Testing framework needing access to private constructors
Constructor<?> ctor = SomeClass.class.getDeclaredConstructor();
ctor.setAccessible(true);  // blocked by module system

// Cause 5: Serialization framework accessing private fields
Field field = MyClass.class.getDeclaredField("transientData");
field.setAccessible(true);  // InaccessibleObjectException
```

## Solutions

### Fix 1: Use --add-opens JVM argument

```bash
# Open a specific package to all unnamed modules
java --add-opens java.base/java.lang=ALL-UNNAMED \
     --add-opens java.base/java.util=ALL-UNNAMED \
     -jar myapp.jar

# Open your own module's packages for reflection
java --add-opens my.module/com.example.model=ALL-UNNAMED \
     --add-opens my.module/com.example.service=ALL-UNNAMED \
     -jar myapp.jar

# Open for specific module only
java --add-opens my.module/com.example.model=other.module \
     -jar myapp.jar

# For Maven/Gradle tests
# pom.xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <argLine>
            --add-opens my.module/com.example.model=ALL-UNNAMED
        </argLine>
    </configuration>
</plugin>
```

### Fix 2: Modify module-info.java to open packages

```java
// module-info.java
module my.module {
    // Open packages for reflective access
    opens com.example.model;                // opens to all modules
    opens com.example.service to spring.core;  // opens to specific module only

    // Export for compile-time access (does NOT allow reflection to private members)
    exports com.example.api;

    // Open everything for testing
    opens com.example;
}
```

### Fix 3: Use privileged actions for controlled reflection

```java
import java.security.AccessController;
import java.security.PrivilegedAction;
import java.security.PrivilegedExceptionAction;

public class ReflectionHelper {
    public static <T> T privilegedGetField(Object obj, String fieldName) throws Exception {
        Field field = obj.getClass().getDeclaredField(fieldName);

        PrivilegedAction<Void> setAccessible = () -> {
            field.setAccessible(true);
            return null;
        };

        AccessController.doPrivileged(setAccessible);
        return (T) field.get(obj);
    }

    public static <T> T privilegedNewInstance(Class<T> clazz) throws Exception {
        Constructor<T> ctor = clazz.getDeclaredConstructor();

        PrivilegedExceptionAction<T> newInstance = ctor::newInstance;
        return AccessController.doPrivileged(newInstance);
    }
}
```

### Fix 4: Configure build tools for module-aware reflection

```xml
<!-- Maven Surefire with module opens -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.0.0</version>
    <configuration>
        <argLine>
            --add-opens java.base/java.lang=ALL-UNNAMED
            --add-opens java.base/java.lang.reflect=ALL-UNNAMED
            --add-opens java.base/java.util=ALL-UNNAMED
        </argLine>
    </configuration>
</plugin>
```

```groovy
// Gradle
test {
    jvmArgs = [
        '--add-opens', 'java.base/java.lang=ALL-UNNAMED',
        '--add-opens', 'java.base/java.util=ALL-UNNAMED'
    ]
}
```

## Prevention Checklist

- Declare `opens` directives in `module-info.java` for packages needing reflection.
- Use `--add-opens` JVM arguments for frameworks that require reflective access.
- Avoid reflective access to JDK internal classes when possible.
- Test reflective access in module-aware environments (Java 9+).
- Document module opens requirements in project README.
- Use `AccessController.doPrivileged()` for security-sensitive reflection.

## Related Errors

- [IllegalAccessException](../illegalaccessexception) — general reflection access denial
- [InaccessibleObjectException](../inaccessibleobjectexception) — module system block
- [SecurityException](../securityexception) — security manager rejection
