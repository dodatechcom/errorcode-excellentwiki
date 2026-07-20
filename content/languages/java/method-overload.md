---
title: "[Solution] Java method is already defined in class — Fix Duplicate Method Signature"
description: "Fix Java compiler error 'method is already defined in class' by renaming methods, using different parameter types, or using varargs. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 448
---

# Java Compiler Error: method is already defined in class

This compile-time error occurs when you declare two methods with the exact same name and parameter types in the same class. Java resolves methods by their signature (name + parameter list), so two methods with identical signatures are considered duplicates.

## Error Message

```
error: method add(int,int) is already defined in class Calculator
    public int add(int a, int b) {
               ^
```

Other variants:

```
error: method process(String) is already defined in class Handler
error: name clash: methodName(ParamType) and methodName(ParamType) have the same erasure
```

## Common Causes

### Cause 1: Identical Method Signature

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public int add(int x, int y) { // ERROR: method add(int,int) is already defined
        return x + y;
    }
}
```

### Cause 2: Overloading With Same Parameter Types After Erasure

```java
import java.util.List;

public class Processor {
    public void handle(List<String> items) { }

    public void handle(List<Integer> items) { } // ERROR: same erasure after type removal
}
```

### Cause 3: Copied Method Without Renaming

```java
public class Service {
    public void processData(String data) {
        System.out.println("Processing: " + data);
    }

    // Accidentally copied and forgot to rename
    public void processData(String data) { // ERROR: method is already defined
        System.out.println("Handling: " + data);
    }
}
```

### Cause 4: Overloading That Differs Only by Return Type

```java
public class Converter {
    public String convert(int value) {
        return String.valueOf(value);
    }

    public int convert(int value) { // ERROR: method is already defined (return type doesn't matter)
        return value;
    }
}
```

## Solutions

### Fix 1: Rename the Method

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public int addAndDouble(int a, int b) { // renamed
        return (a + b) * 2;
    }
}
```

### Fix 2: Use Different Parameter Types

```java
public class Service {
    public void process(String data) { }

    public void process(String data, String encoding) { // different parameters — OK
    }

    public void process(int code) { // different type — OK
    }
}
```

### Fix 3: Use Varargs

```java
public class Logger {
    public void log(String message) { }

    public void log(String... messages) { // varargs version — OK
    }
}
```

### Fix 4: Use Generics With Different Bounds

```java
import java.util.List;

public class Processor {
    public void handle(List<String> items) { }

    public void handleNumbers(List<Integer> items) { } // renamed to avoid erasure conflict
}
```

### Fix 5: Fix Copied Methods

```java
public class Service {
    public void processData(String data) {
        System.out.println("Processing: " + data);
    }

    public void validateData(String data) { // correct name for the copy
        System.out.println("Validating: " + data);
    }
}
```

## Prevention Checklist

- Always check existing method signatures before adding new methods
- Use IDE auto-complete and refactoring tools to avoid accidental duplication
- Remember that return type alone is not enough to distinguish overloaded methods
- Watch for generic erasure — `List<String>` and `List<Integer>` have the same erasure
- Use descriptive, distinct method names rather than relying on overloading when logic differs
- Run `javap -s` on compiled classes to verify generated JVM signatures

## Related Errors

- [name clash — erasure causes duplicate JVM signatures (name-clash)](/languages/java/name-clash)
- [cannot be applied (cannot-be-applied)](/languages/java/cannot-be-applied)
- [method does not override or implement a method from a supertype (override-methods)](/languages/java/override-methods)
