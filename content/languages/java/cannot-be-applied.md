---
title: "[Solution] Java cannot be applied to given types — Fix Method Argument Mismatch"
description: "Fix Java compiler error cannot be applied to given types by checking method signature, verifying argument types, and adding type conversion. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 134
---

# Java Compiler Error: cannot be applied to given types

This compile-time error occurs when a method is called with arguments that do not match any available method signature. The compiler finds the method name but the provided argument types do not match the declared parameter types.

## Error Message

```
error: method calculate in class Math cannot be applied to given types;
  required: int, int
  found:    int, int, int
  reason: actual and formal argument lists differ in length
```

## Common Causes

### Cause 1: Wrong Number of Arguments

```java
public class Calculator {
    public static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        add(1, 2, 3); // add() only takes 2 arguments
    }
}
```

### Cause 2: Wrong Argument Types

```java
public class Example {
    public static void greet(String name) {
        System.out.println("Hello, " + name);
    }

    public static void main(String[] args) {
        greet(42); // greet() expects String, not int
    }
}
```

### Cause 3: Incompatible Reference Types

```java
import java.util.ArrayList;
import java.util.List;

public class Example {
    public static void process(List<String> items) { }

    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        process(numbers); // process() expects List<String>, not List<Integer>
    }
}
```

### Cause 4: Varargs Mismatch

```java
public class Example {
    public static void printAll(String... items) { }

    public static void main(String[] args) {
        printAll(1, 2, 3); // printAll() expects String, not int
    }
}
```

### Cause 5: Method Overload Resolution Failure

```java
public class Example {
    public static void log(int value) { }
    public static void log(String message) { }

    public static void main(String[] args) {
        log(3.14); // No log(double) overload exists
    }
}
```

## Solutions

### Fix 1: Provide Correct Number of Arguments

```java
public class Calculator {
    public static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        add(1, 2); // Correct: 2 arguments
    }
}
```

### Fix 2: Convert Argument Types

```java
public class Example {
    public static void greet(String name) {
        System.out.println("Hello, " + name);
    }

    public static void main(String[] args) {
        greet(String.valueOf(42)); // Convert int to String
    }
}
```

### Fix 3: Use Correct Generic Type

```java
import java.util.ArrayList;
import java.util.List;

public class Example {
    public static void process(List<String> items) { }

    public static void main(String[] args) {
        List<String> strings = new ArrayList<>(); // Correct generic type
        process(strings);
    }
}
```

### Fix 4: Pass Correct Varargs Type

```java
public class Example {
    public static void printAll(String... items) { }

    public static void main(String[] args) {
        printAll("a", "b", "c"); // Correct: String arguments
    }
}
```

### Fix 5: Add Missing Overload

```java
public class Example {
    public static void log(int value) { }
    public static void log(String message) { }
    public static void log(double value) { } // Added overload

    public static void main(String[] args) {
        log(3.14); // Now works with new overload
    }
}
```

## Prevention Checklist

- Always verify method parameter types before calling
- Use IDE auto-complete to see available method signatures
- Check generic type parameters when passing collections
- Ensure argument count matches parameter count (accounting for varargs)
- Add overloads when a method needs to accept additional types
- Use `javap -p` to inspect compiled class method signatures

## Related Errors

- [method-not-found](/languages/java/method-not-found/)
- [name-clash](/languages/java/name-clash/)
- [incompatible-types](/languages/java/incompatible-types/)
