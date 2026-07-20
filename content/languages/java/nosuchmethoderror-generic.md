---
title: "[Solution] Java NoSuchMethodError — Generic Method Type Erasure Fix"
description: "Fix Java NoSuchMethodError with generic methods by checking method signature at runtime, verifying generic type parameters, and handling erasure."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# NoSuchMethodError — Generic Method Type Erasure Fix

A `NoSuchMethodError` involving generic methods occurs when the runtime method signature does not match what was expected at compile time, due to type erasure removing generic type information from method signatures. The JVM resolves the erased signature, which may differ from the generic version.

## Description

Java generics are a compile-time construct — generic type parameters are erased at runtime. If a generic method like `List<String> getItems()` is compiled expecting a return type of `List` (erased), but the runtime class has changed the method signature or the generics were resolved differently, `NoSuchMethodError` occurs. This is especially common with bridge methods, covariant return types, and framework-generated proxies.

Message variants:

- `java.lang.NoSuchMethodError: com.example.Repository.getItems()Ljava/util/List;`
- `java.lang.NoSuchMethodError: 'java.util.List com.example.Service.process(java.lang.Object)'`
- `java.lang.NoSuchMethodError: com.example.GenericClass.getData()Ljava/lang/Object;`

## Common Causes

```java
// Cause 1: Generic method return type changed
public interface Repository<T> {
    List<T> findAll();  // returns List<T> (erased to List at runtime)
}
// After refactoring to:
public interface Repository<T> {
    ArrayList<T> findAll();  // signature changes to ArrayList — NoSuchMethodError

// Cause 2: Bridge method mismatch after compilation
public class StringList implements List<String> {
    // Compiler generates bridge: public Object get(int) → String get(int)
    // If bridge method is missing due to stale .class files, NoSuchMethodError
}

// Cause 3: Generic type parameter causes different erasure
public class Service<T extends Comparable<T>> {
    public int compare(T a, T b) {  // erased to compare(Comparable, Comparable)
        return a.compareTo(b);
    }
}
// Caller compiled with Service<String> expects compare(String, String)
// Runtime has compare(Comparable, Comparable) — NoSuchMethodError

// Cause 4: Framework proxy missing generic method
// Spring AOP creates proxies that may not include generic bridge methods
// if compiled incorrectly

// Cause 5: Mixing raw types and parameterized types
Map rawMap = new HashMap();
rawMap.put("key", "value");
String value = (String) rawMap.get("key");  // OK, but:
// If refactored to Map<String, String>, the erased get() signature is the same
// but bridge methods may differ
```

## Solutions

### Fix 1: Check method signature at runtime before calling

```java
import java.lang.reflect.Method;
import java.lang.reflect.Type;

public class GenericMethodInspector {
    public static void printMethods(Class<?> clazz) {
        for (Method method : clazz.getDeclaredMethods()) {
            System.out.printf("Method: %s%n", method.getName());
            System.out.printf("  Generic return: %s%n", method.getGenericReturnType());
            System.out.printf("  Erased return: %s%n", method.getReturnType());
            System.out.printf("  Parameter count: %d%n", method.getParameterCount());
        }
    }

    public static boolean methodExists(Class<?> clazz, String name, Class<?>... paramTypes) {
        try {
            Method m = clazz.getMethod(name, paramTypes);
            return m != null;
        } catch (NoSuchMethodException e) {
            return false;
        }
    }
}

// Usage
GenericMethodInspector.printMethods(MyGenericClass.class);
```

### Fix 2: Use reflection for safe generic method invocation

```java
import java.lang.reflect.Method;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;

public class GenericInvoker {
    public static Object invokeGenericMethod(Object obj, String methodName, Object... args) {
        Class<?> targetClass = obj.getClass();

        // Search for method by name (ignoring exact parameter types)
        for (Method method : targetClass.getMethods()) {
            if (method.getName().equals(methodName)
                && method.getParameterCount() == args.length) {
                try {
                    // Check generic return type
                    Type returnType = method.getGenericReturnType();
                    System.out.println("Return type: " + returnType);

                    return method.invoke(obj, args);
                } catch (Exception e) {
                    throw new RuntimeException("Invoke failed", e);
                }
            }
        }

        throw new NoSuchMethodError(
            "Method " + methodName + " not found in " + targetClass.getName());
    }
}
```

### Fix 3: Clean build to regenerate bridge methods

```bash
# Stale .class files can have missing bridge methods
# Always do a clean build when changing generic signatures

# Maven
mvn clean compile

# Gradle
gradle clean build

# Manual — delete all .class files
find . -name "*.class" -delete
javac -d out $(find src -name "*.java")
```

### Fix 4: Verify generic type parameters match at compile time

```java
// Wrong — raw type hides mismatch
List list = new ArrayList<String>();
list.add("hello");
// Compiles, but if List's internal methods change signature, runtime error

// Right — use parameterized types consistently
List<String> list = new ArrayList<>();
list.add("hello");

// Right — check generic type at runtime
public static Class<?> getGenericTypeParam(Field field) {
    Type type = field.getGenericType();
    if (type instanceof ParameterizedType pt) {
        Type[] typeArgs = pt.getActualTypeArguments();
        if (typeArgs.length > 0 && typeArgs[0] instanceof Class<?> clazz) {
            return clazz;
        }
    }
    return Object.class;
}
```

### Fix 5: Handle erasure in framework-generated code

```java
// When generating proxy or wrapper classes, preserve generic signatures
public class SafeProxy<T> implements InvocationHandler {
    private final T target;

    public SafeProxy(T target) {
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        // Look up the actual method on the target class
        // (not the proxy's erased interface method)
        Class<?> targetClass = target.getClass();
        for (Method m : targetClass.getMethods()) {
            if (m.getName().equals(method.getName())
                && m.getParameterCount() == method.getParameterCount()) {
                return m.invoke(target, args);
            }
        }
        throw new NoSuchMethodError(method.getName());
    }
}
```

## Prevention Checklist

- Always do `mvn clean` or `gradle clean` when changing generic method signatures.
- Use parameterized types consistently — avoid raw types.
- Verify bridge methods exist using `javap -v` after compilation.
- Test generic methods with different type parameters in unit tests.
- Avoid changing generic method return types in library APIs.
- Use `method.getGenericReturnType()` to inspect actual generic types at runtime.

## Related Errors

- [NoSuchMethodError](../nosuchmethoderror) — general binary incompatibility
- [NoSuchMethodException](../nosuchmethodexception) — method not found via reflection
- [ClassCastException](../classcastexception) — type mismatch after erasure
- [BridgeMethodError](../incompatibleclasschangeerror) — missing bridge methods
