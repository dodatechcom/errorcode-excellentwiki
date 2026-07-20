---
title: "[Solution] Java cannot find symbol — Check Spelling, Imports, and Classpath"
description: "Fix Java compiler error cannot find symbol by checking spelling, verifying imports, ensuring classpath is correct, and reviewing class hierarchy. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 120
---

# Java Compiler Error: cannot find symbol

This compile-time error occurs when the Java compiler cannot locate a variable, method, class, or package reference in the current scope. It is one of the most common javac errors and usually stems from typos, missing imports, or incorrect classpath configuration.

## Error Message

```
error: cannot find symbol
  symbol:   variable myVariable
  location: class MyClass
```

## Common Causes

### Cause 1: Typo in Variable or Method Name

```java
public class Example {
    public static void main(String[] args) {
        String message = "Hello";
        System.out.println(messge); // Typo: messge instead of message
    }
}
```

### Cause 2: Missing Import Statement

```java
public class Example {
    public static void main(String[] args) {
        List<String> items = new ArrayList<>(); // List and ArrayList not imported
    }
}
```

### Cause 3: Method Does Not Exist in the Class

```java
public class Example {
    public static void main(String[] args) {
        String text = "Hello";
        text.toUpper(); // Method does not exist; should be toUpperCase()
    }
}
```

### Cause 4: Class Not on Classpath

```java
import com.example.MyLibrary; // MyLibrary.jar not in classpath

public class Example {
    public static void main(String[] args) {
        MyLibrary.process(); // Compiler cannot find the class
    }
}
```

### Cause 5: Accessing Member of Wrong Type

```java
public class Example {
    public static void main(String[] args) {
        Integer num = 42;
        num.length(); // Integer has no length() method
    }
}
```

## Solutions

### Fix 1: Correct the Spelling

```java
public class Example {
    public static void main(String[] args) {
        String message = "Hello";
        System.out.println(message); // Correct spelling
    }
}
```

### Fix 2: Add the Required Import

```java
import java.util.List;
import java.util.ArrayList;

public class Example {
    public static void main(String[] args) {
        List<String> items = new ArrayList<>();
    }
}
```

### Fix 3: Use the Correct Method Name

```java
public class Example {
    public static void main(String[] args) {
        String text = "Hello";
        System.out.println(text.toUpperCase()); // Correct method name
    }
}
```

### Fix 4: Verify Classpath Configuration

```bash
# Compile with classpath specified
javac -cp /path/to/library.jar Example.java

# Or add all jars in a directory
javac -cp "/path/to/libs/*" Example.java
```

### Fix 5: Check Class Hierarchy

```java
public class Animal {
    public void speak() { }
}

public class Dog extends Animal {
    public void bark() { }
}

public class Example {
    public static void main(String[] args) {
        Animal a = new Dog();
        a.bark(); // Error: bark() is not in Animal
        // Fix: cast or use Dog type
        ((Dog) a).bark();
    }
}
```

## Prevention Checklist

- Always check for typos in identifiers before assuming a classpath issue
- Use IDE auto-import features to add missing import statements
- Verify that all required libraries are on the compilation classpath
- Use fully qualified names when auto-import is ambiguous
- Check the class hierarchy to ensure the member exists on the declared type
- Use `javac -verbose` to see which classes the compiler loads

## Related Errors

- [method-not-found](/languages/java/method-not-found/)
- [non-static-method](/languages/java/non-static-method/)
- [classnotfoundexception](/languages/java/classnotfoundexception/)
- [incompatible-types](/languages/java/incompatible-types/)
