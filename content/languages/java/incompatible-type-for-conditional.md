---
title: "[Solution] Java incompatible types for ?: operator — Fix Ternary Type Mismatch"
description: "Fix Java compiler error incompatible types for ?: operator by ensuring compatible types, adding explicit casts, and handling null cases. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 132
---

# Java Compiler Error: incompatible types for ?: operator

This compile-time error occurs when the two value expressions in a ternary (`?:`) operator return incompatible types. Both the second and third operands must be assignable to a common type.

## Error Message

```
error: incompatible types: int cannot be converted to String
```

## Common Causes

### Cause 1: Different Primitive Types

```java
public class Example {
    public static void main(String[] args) {
        boolean flag = true;
        String result = flag ? "yes" : 1; // String vs int
    }
}
```

### Cause 2: Incompatible Class Types

```java
import java.util.ArrayList;
import java.util.List;

public class Example {
    public static void main(String[] args) {
        boolean flag = true;
        List<String> result = flag ? new ArrayList<>() : "not a list"; // List vs String
    }
}
```

### Cause 3: Null vs Incompatible Type

```java
public class Example {
    public static void main(String[] args) {
        boolean flag = true;
        String result = flag ? null : 42; // null vs Integer
    }
}
```

### Cause 4: Primitive and Wrapper Mismatch

```java
public class Example {
    public static void main(String[] args) {
        boolean flag = true;
        Object result = flag ? 1 : "hello"; // Integer vs String
        // This actually works with Object, but explicit type causes issues
    }
}
```

### Cause 5: Incompatible Interface Types

```java
import java.io.Serializable;
import java.lang.Comparable;

public class Example {
    public static void main(String[] args) {
        boolean flag = true;
        Comparable<String> result = flag ? Serializable::toString : "hello";
    }
}
```

## Solutions

### Fix 1: Use Compatible Types

```java
public class Example {
    public static void main(String[] args) {
        boolean flag = true;
        String result = flag ? "yes" : "no"; // Both String
        System.out.println(result);
    }
}
```

### Fix 2: Cast to Common Type

```java
public class Example {
    public static void main(String[] args) {
        boolean flag = true;
        Object result = flag ? "yes" : 1; // Both assign to Object
        System.out.println(result);
    }
}
```

### Fix 3: Wrap Primitive in Wrapper

```java
public class Example {
    public static void main(String[] args) {
        boolean flag = true;
        Number result = flag ? Integer.valueOf(1) : Double.valueOf(2.0); // Both Number
        System.out.println(result);
    }
}
```

### Fix 4: Handle Null Properly

```java
public class Example {
    public static void main(String[] args) {
        boolean flag = true;
        String result = flag ? null : "default"; // null is assignable to String
        System.out.println(result);
    }
}
```

### Fix 5: Use Method That Returns Consistent Type

```java
public class Example {
    public static String getValue(boolean flag) {
        return flag ? "yes" : "no"; // Both are String
    }

    public static void main(String[] args) {
        System.out.println(getValue(true));
    }
}
```

## Prevention Checklist

- Both ternary operands should be the same type or have a common supertype
- Use `Object` as the result type when operands are truly different types
- `null` is compatible with any reference type, but the other operand must also be a reference type
- For primitives, ensure both operands are the same type or use wrapper classes
- Enable IDE type checking for real-time ternary type validation
- Consider using `if-else` when ternary expressions become complex

## Related Errors

- [incompatible-types](/languages/java/incompatible-types/)
- [incompatible-types-assignment](/languages/java/incompatible-types-assignment/)
- [possible-loss-of-precision](/languages/java/possible-loss-of-precision/)
