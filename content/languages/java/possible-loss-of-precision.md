---
title: "[Solution] Java possible loss of precision — Fix Narrowing Conversion"
description: "Fix Java compiler error possible loss of precision by adding explicit casts, using wider types, and avoiding narrowing conversions. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 123
---

# Java Compiler Error: possible loss of precision

This compile-time error occurs when you attempt a narrowing primitive conversion without an explicit cast. The compiler rejects the assignment because data could be lost when converting from a wider type to a narrower type.

## Error Message

```
error: possible loss of precision
  required: byte
  found:    int
```

## Common Causes

### Cause 1: Assigning int to byte

```java
public class Example {
    public static void main(String[] args) {
        byte b = 128; // 128 exceeds byte range (-128 to 127)
    }
}
```

### Cause 2: Assigning double to int

```java
public class Example {
    public static void main(String[] args) {
        int num = 3.14; // double cannot be assigned to int without cast
    }
}
```

### Cause 3: Assigning long to short

```java
public class Example {
    public static void main(String[] args) {
        short s = 100000; // 100000 exceeds short range
    }
}
```

### Cause 4: Arithmetic Result Too Large for Target

```java
public class Example {
    public static void main(String[] args) {
        int big = Integer.MAX_VALUE;
        short result = big + 1; // Arithmetic result exceeds short range
    }
}
```

### Cause 5: Float to Integer Conversion

```java
public class Example {
    public static void main(String[] args) {
        long value = 3.14f; // float cannot be assigned to long
    }
}
```

## Solutions

### Fix 1: Add an Explicit Cast

```java
public class Example {
    public static void main(String[] args) {
        byte b = (byte) 128; // Cast narrows; value wraps to -128
        System.out.println(b); // -128
    }
}
```

### Fix 2: Use a Wider Type

```java
public class Example {
    public static void main(String[] args) {
        int num = 3; // Use int instead of trying to store in byte
        System.out.println(num);
    }
}
```

### Fix 3: Use Math.round() for Floating-Point

```java
public class Example {
    public static void main(String[] args) {
        int num = (int) 3.14; // Explicit cast truncates
        long rounded = Math.round(3.14); // Rounds to 3
        System.out.println(num);     // 3
        System.out.println(rounded); // 3
    }
}
```

### Fix 4: Validate Before Narrowing

```java
public class Example {
    public static void main(String[] args) {
        int value = 127;
        if (value >= Byte.MIN_VALUE && value <= Byte.MAX_VALUE) {
            byte b = (byte) value; // Safe cast
            System.out.println(b);
        } else {
            System.out.println("Value out of byte range");
        }
    }
}
```

## Prevention Checklist

- Always check the range of the target type before narrowing
- Use explicit casts with a comment when narrowing is intentional
- Prefer `int` or `long` for intermediate calculations
- Use `Math.round()`, `Math.toIntExact()`, or `Math.addExact()` for safe conversions
- Enable IDE warnings for narrowing conversions
- Use `StrictMath` methods when precision is critical

## Related Errors

- [incompatible-types](/languages/java/incompatible-types/)
- [incompatible-types-assignment](/languages/java/incompatible-types-assignment/)
- [numberformatexception](/languages/java/numberformatexception/)
