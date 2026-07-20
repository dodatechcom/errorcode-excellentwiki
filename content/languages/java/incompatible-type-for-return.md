---
title: "[Solution] Java incompatible types: possible lossy conversion from X to Y — Fix Return Type"
description: "Fix Java compiler error 'incompatible types: possible lossy conversion' in return statements by adding explicit casts, using wider return types, or matching method signatures. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 450
---

# Java Compiler Error: incompatible types: possible lossy conversion from X to Y

This compile-time error occurs when a return statement tries to return a value that requires a narrowing conversion, which could result in data loss. Unlike assignment conversions, return statements do not allow implicit narrowing of primitive types (e.g., `long` to `int`, `double` to `float`).

## Error Message

```
error: incompatible types: possible lossy conversion from long to int
        return System.currentTimeMillis();
               ^
```

Other variants:

```
error: incompatible types: possible lossy conversion from double to float
error: incompatible types: possible lossy conversion from int to byte
error: incompatible types: possible lossy conversion from double to int
```

## Common Causes

### Cause 1: Returning long as int

```java
public class Timer {
    public int getTime() {
        return System.currentTimeMillis(); // ERROR: long cannot be converted to int
    }
}
```

### Cause 2: Returning double as float

```java
public class Calculator {
    public float getArea(double radius) {
        return Math.PI * radius * radius; // ERROR: double cannot be converted to float
    }
}
```

### Cause 3: Returning int as byte

```java
public class Parser {
    public byte getStatusCode() {
        return 200; // ERROR: possible lossy conversion from int to byte
    }
}
```

### Cause 4: Returning Incompatible Object Type

```java
public class Factory {
    public Number getResult() {
        return "42"; // ERROR: String cannot be converted to Number
    }
}
```

### Cause 5: Returning Subtype From Wrong Generic

```java
import java.util.ArrayList;
import java.util.List;

public class Provider {
    public List<Number> getNumbers() {
        List<Integer> ints = new ArrayList<>(); // List<Integer> is not a subtype of List<Number>
        return ints; // ERROR: incompatible types
    }
}
```

## Solutions

### Fix 1: Add Explicit Cast

```java
public class Timer {
    public int getTime() {
        return (int) System.currentTimeMillis(); // explicit cast — may lose data
    }
}
```

### Fix 2: Use the Wider Return Type

```java
public class Timer {
    public long getTime() { // changed return type to long
        return System.currentTimeMillis();
    }
}
```

### Fix 3: Match Return Type to Actual Value

```java
public class Calculator {
    public double getArea(double radius) { // return type matches the computation
        return Math.PI * radius * radius;
    }
}
```

### Fix 4: Use Safe Conversion Methods

```java
public class Parser {
    public byte getStatusCode() {
        int code = 200;
        return Integer.valueOf(code).byteValue(); // explicit safe conversion
    }
}
```

### Fix 5: Fix Generic Return Types

```java
import java.util.ArrayList;
import java.util.List;

public class Provider {
    public List<Integer> getNumbers() { // match generic types
        List<Integer> ints = new ArrayList<>();
        return ints;
    }
}
```

## Prevention Checklist

- Ensure return types match the actual expression type — avoid implicit narrowing
- Use `long` for timestamps, file sizes, and other large numeric values
- Use `double` for floating-point computations instead of `float` unless memory is critical
- Check generic type parameters when returning collection types
- Use explicit casts only when you're certain the value fits in the target type
- Use IDE inspections to detect lossy conversions before compilation

## Related Errors

- [incompatible types (incompatible-types)](/languages/java/incompatible-types)
- [incompatible types for assignment (incompatible-types-assignment)](/languages/java/incompatible-types-assignment)
- [possible loss of precision (possible-loss-of-precision)](/languages/java/possible-loss-of-precision)
