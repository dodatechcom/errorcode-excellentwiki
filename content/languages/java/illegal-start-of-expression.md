---
title: "[Solution] Java illegal start of expression — Fix Statement in Expression Context"
description: "Fix Java compiler error illegal start of expression by checking syntax, adding missing operators, and verifying statement structure. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 126
---

# Java Compiler Error: illegal start of expression

This compile-time error occurs when a statement appears where the compiler expects an expression. It typically indicates a syntax problem such as missing operators, misplaced keywords, or incorrect method call syntax.

## Error Message

```
error: illegal start of expression
```

## Common Causes

### Cause 1: Missing Operator Between Expressions

```java
public class Example {
    public static void main(String[] args) {
        int a = 5;
        int b = 10;
        int result = a +; // Incomplete expression
    }
}
```

### Cause 2: Statement Used as Expression

```java
public class Example {
    public static void main(String[] args) {
        int x = if (true) 1 else 2; // if-statement cannot be an expression
    }
}
```

### Cause 3: Incorrect Method Call Syntax

```java
public class Example {
    public static void main(String[] args) {
        System.out.println("Hello"; // Missing closing parenthesis
    }
}
```

### Cause 4: Return Without Value in Non-Void Method

```java
public class Example {
    public static int getValue() {
        return; // Missing return value
    }
}
```

### Cause 5: Access Modifier in Wrong Context

```java
public class Example {
    public static void main(String[] args) {
        public int x = 5; // Local variables cannot have access modifiers
    }
}
```

## Solutions

### Fix 1: Complete the Expression

```java
public class Example {
    public static void main(String[] args) {
        int a = 5;
        int b = 10;
        int result = a + b; // Complete expression
    }
}
```

### Fix 2: Use Ternary Operator for Inline Conditional

```java
public class Example {
    public static void main(String[] args) {
        int x = true ? 1 : 2; // Ternary works as expression
    }
}
```

### Fix 3: Close the Parenthesis

```java
public class Example {
    public static void main(String[] args) {
        System.out.println("Hello"); // Added closing parenthesis
    }
}
```

### Fix 4: Provide Return Value

```java
public class Example {
    public static int getValue() {
        return 42; // Added return value
    }
}
```

### Fix 5: Remove Access Modifier From Local Variable

```java
public class Example {
    public static void main(String[] args) {
        int x = 5; // No access modifier on local variable
    }
}
```

## Prevention Checklist

- Ensure every expression has a complete operator and operands
- Use IDE auto-complete for method calls to avoid missing parentheses
- Remember that `if`/`for`/`while` are statements, not expressions, in Java
- Local variables cannot have access modifiers (`public`, `private`, `protected`)
- Always provide a value when returning from a non-void method
- Enable syntax checking in your IDE for real-time feedback

## Related Errors

- [illegal-start-of-statement](/languages/java/illegal-start-of-statement/)
- [semicolon-expected](/languages/java/semicolon-expected/)
- [reached-eof-while-parsing](/languages/java/reached-eof-while-parsing/)
