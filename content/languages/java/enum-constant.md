---
title: "[Solution] Java enum constant must be followed by ',' or '}' — Fix Enum Syntax"
description: "Fix Java compiler error 'enum constant must be followed by comma or closing brace' by checking enum syntax, adding commas, and verifying semicolon placement. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 456
---

# Java Compiler Error: enum constant must be followed by ',' or '}'

This compile-time error occurs when enum constants are not properly separated by commas, or when there is a syntax error in the enum body. Enum constants must be separated by commas, and a semicolon is required after the last constant only if there are members (methods, fields, or constructors) following them.

## Error Message

```
error: enum constant must be followed by a comma or '}' 
        INACTIVE
           ^
```

Other variants:

```
error: ',' expected
error: ';' expected
error: enum constant must be followed by a comma, ';', or '}'
```

## Common Causes

### Cause 1: Missing Comma Between Constants

```java
public enum Status {
    ACTIVE
    INACTIVE  // ERROR: missing comma after ACTIVE
    PENDING
}
```

### Cause 2: Trailing Comma Before Semicolon

```java
public enum Color {
    RED,
    GREEN,
    BLUE,;  // ERROR: trailing comma before semicolon (not allowed in older Java)
}
```

Note: Trailing commas are allowed in Java 11+ enum constants but not before a semicolon.

### Cause 3: Semicolon Required But Missing

```java
public enum Operation {
    ADD, SUBTRACT, MULTIPLY
    public double apply(double a, double b) { } // ERROR: semicolon required after constants when methods follow
}
```

### Cause 4: Extra Semicolon After Constants

```java
public enum Direction {
    NORTH, SOUTH, EAST, WEST;; // ERROR: double semicolon
}
```

### Cause 5: Syntax Error in Enum Body

```java
public enum Season {
    SPRING, SUMMER
    ; // OK

    FALL, WINTER // ERROR: constants must come first, before any members
}
```

## Solutions

### Fix 1: Add Missing Commas

```java
public enum Status {
    ACTIVE,   // comma added
    INACTIVE, // comma added
    PENDING
}
```

### Fix 2: Remove Trailing Comma Before Semicolon

```java
public enum Color {
    RED,
    GREEN,
    BLUE  // no trailing comma before semicolon
}
```

### Fix 3: Add Semicolon When Methods Follow

```java
public enum Operation {
    ADD, SUBTRACT, MULTIPLY; // semicolon required

    public double apply(double a, double b) {
        return switch (this) {
            case ADD -> a + b;
            case SUBTRACT -> a - b;
            case MULTIPLY -> a * b;
        };
    }
}
```

### Fix 4: Remove Extra Semicolons

```java
public enum Direction {
    NORTH, SOUTH, EAST, WEST; // single semicolon
}
```

### Fix 5: Put All Constants First

```java
public enum Season {
    SPRING, SUMMER, FALL, WINTER; // all constants together

    public String getDisplayName() {
        return name().charAt(0) + name().substring(1).toLowerCase();
    }
}
```

## Prevention Checklist

- Separate all enum constants with commas
- Add a semicolon after the last constant only if methods, fields, or constructors follow
- Place all enum constants before any member declarations
- Avoid trailing commas before semicolons (for Java < 11 compatibility)
- Use IDE auto-formatting to catch enum syntax issues
- Use enhanced switch expressions (Java 14+) for cleaner enum logic

## Related Errors

- [constant expression required (constant-expression-required)](/languages/java/constant-expression-required)
- [case expressions must be constant expressions (string-switch-constant)](/languages/java/string-switch-constant)
- [enum constant not present in enum (enumconstantnotpresentexception)](/languages/java/enumconstantnotpresentexception)
