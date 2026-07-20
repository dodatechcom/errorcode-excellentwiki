---
title: "[Solution] Java ';' expected — Add Missing Semicolon"
description: "Fix Java compiler error semicolon expected by adding semicolons at end of statements, checking for missing closing braces, and verifying statement structure. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 129
---

# Java Compiler Error: ';' expected

This compile-time error occurs when the Java compiler expects a semicolon at the end of a statement but does not find one. In Java, most statements must be terminated with a semicolon.

## Error Message

```
error: ';' expected
```

## Common Causes

### Cause 1: Missing Semicolon After Variable Declaration

```java
public class Example {
    public static void main(String[] args) {
        int x = 5
        System.out.println(x);
    }
}
```

### Cause 2: Missing Semicolon After Method Call

```java
public class Example {
    public static void main(String[] args) {
        System.out.println("Hello")
    }
}
```

### Cause 3: Missing Semicolon After Return

```java
public class Example {
    public static int getValue() {
        return 42
    }
}
```

### Cause 4: Missing Semicolon in For Loop

```java
public class Example {
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++)
        {
            System.out.println(i);
        }
    }
}
```

### Cause 5: Missing Semicolon After Import

```java
import java.util.List
import java.util.ArrayList

public class Example { }
```

## Solutions

### Fix 1: Add Semicolon After Declaration

```java
public class Example {
    public static void main(String[] args) {
        int x = 5; // Added semicolon
        System.out.println(x);
    }
}
```

### Fix 2: Add Semicolon After Method Call

```java
public class Example {
    public static void main(String[] args) {
        System.out.println("Hello"); // Added semicolon
    }
}
```

### Fix 3: Add Semicolon After Return

```java
public class Example {
    public static int getValue() {
        return 42; // Added semicolon
    }
}
```

### Fix 4: Add Semicolons in For Loop Header

```java
public class Example {
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) { // Semicolons separate for-loop parts
            System.out.println(i);
        }
    }
}
```

### Fix 5: Add Semicolon After Import

```java
import java.util.List;
import java.util.ArrayList;

public class Example { }
```

## Prevention Checklist

- End every statement (declarations, assignments, method calls, return) with a semicolon
- Use IDE auto-formatting to highlight missing semicolons
- Note that for-loop headers use semicolons to separate parts, not end the statement
- Import statements must end with semicolons
- Enable real-time syntax checking in your IDE
- Remember that brace-enclosed blocks (class, method, if, for) do not need semicolons after closing brace

## Related Errors

- [reached-eof-while-parsing](/languages/java/reached-eof-while-parsing/)
- [illegal-start-of-expression](/languages/java/illegal-start-of-expression/)
- [not-a-statement](/languages/java/not-a-statement/)
