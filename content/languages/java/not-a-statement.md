---
title: "[Solution] Java not a statement — Fix Statement That Does Nothing"
description: "Fix Java compiler error not a statement by adding method calls, verifying expressions are valid statements, and checking for typos. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 128
---

# Java Compiler Error: not a statement

This compile-time error occurs when the compiler encounters a line that does not constitute a valid statement. The expression on the line does not perform any action and has no side effects, so it cannot stand alone as a statement.

## Error Message

```
error: not a statement
```

## Common Causes

### Cause 1: Assignment Without Variable

```java
public class Example {
    public static void main(String[] args) {
        5 + 3; // Expression result is discarded; not a statement
    }
}
```

### Cause 2: String Literal as Statement

```java
public class Example {
    public static void main(String[] args) {
        "Hello World"; // String literal does nothing
    }
}
```

### Cause 3: Method Call Without Assigning Result

```java
public class Example {
    public static int compute() {
        return 42;
    }

    public static void main(String[] args) {
        compute(); // Return value is discarded; may be intentional
        // but often indicates a forgotten assignment
    }
}
```

### Cause 4: Type Name Used as Statement

```java
public class Example {
    public static void main(String[] args) {
        int; // Type name alone is not a statement
    }
}
```

### Cause 5: Comparison Used as Statement

```java
public class Example {
    public static void main(String[] args) {
        int a = 5, b = 10;
        a == b; // Comparison result is discarded
    }
}
```

## Solutions

### Fix 1: Assign the Result to a Variable

```java
public class Example {
    public static void main(String[] args) {
        int result = 5 + 3; // Assign result
        System.out.println(result);
    }
}
```

### Fix 2: Use the String in a Method Call

```java
public class Example {
    public static void main(String[] args) {
        System.out.println("Hello World"); // Print the string
    }
}
```

### Fix 3: Use the Method Return Value

```java
public class Example {
    public static int compute() {
        return 42;
    }

    public static void main(String[] args) {
        int value = compute(); // Assign return value
        System.out.println(value);
    }
}
```

### Fix 4: Remove the Invalid Statement

```java
public class Example {
    public static void main(String[] args) {
        // Removed: int;
        System.out.println("Valid statement");
    }
}
```

### Fix 5: Use the Comparison in a Condition

```java
public class Example {
    public static void main(String[] args) {
        int a = 5, b = 10;
        if (a == b) { // Use comparison in condition
            System.out.println("Equal");
        } else {
            System.out.println("Not equal");
        }
    }
}
```

## Prevention Checklist

- Every statement must perform an action: assignment, method call, declaration, or control flow
- Discarded return values often indicate missing assignments
- Use `System.out.println()` to verify intermediate values during debugging
- Enable IDE warnings for expressions with no side effects
- Check that comparison operators are used inside conditions, not as standalone lines
- Remove or fix lines that are only type names or literals

## Related Errors

- [illegal-start-of-expression](/languages/java/illegal-start-of-expression/)
- [illegal-start-of-statement](/languages/java/illegal-start-of-statement/)
- [unreachable-statement](/languages/java/unreachable-statement/)
