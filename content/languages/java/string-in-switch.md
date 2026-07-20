---
title: "[Solution] Java string cannot be converted to int in switch — Fix String Switch"
description: "Fix Java compiler error 'string cannot be converted to int' when using String in switch. Use .equals() instead or ensure Java 7+. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 410
---

# Java Compiler Error: string cannot be converted to int in switch

This compile-time error occurs when you try to use a `String` value in a `switch` statement that expects an `int` (or other primitive type), or when mixing `String` and `int` case labels. Starting from Java 7, `String` is supported in switch statements, but the selector expression and case labels must be consistent.

## Error Message

```
error: incompatible types: String cannot be converted to int
        switch (strValue) {
                 ^
```

Other variants:

```
error: string cannot be converted to int
error: incompatible types: int cannot be converted to String
error: case expressions must have the same type
```

## Common Causes

### Cause 1: Switching on String with Int Cases

```java
public void process(String input) {
    switch (input) { // input is String
        case 1: // ERROR: String cannot be converted to int
            System.out.println("one");
            break;
    }
}
```

### Cause 2: Mixed String and Int Case Labels

```java
public void check(String type) {
    switch (type) {
        case "admin": // OK — String
            break;
        case 0: // ERROR: incompatible types — mixing int with String
            break;
    }
}
```

### Cause 3: Using int Variable with String Cases

```java
public void example(int code) {
    switch (code) {
        case "OK": // ERROR: String cannot be converted to int
            break;
    }
}
```

### Cause 4: Old Java Version (Pre-Java 7)

```java
// Java 6 or earlier
String status = "active";
switch (status) { // ERROR: String cannot be used in switch (Java < 7)
    case "active":
        break;
}
```

### Cause 5: Enum Mixed with String

```java
enum Color { RED, BLUE }

public void example(String input) {
    switch (input) {
        case RED: // ERROR: comparing String with enum
            break;
    }
}
```

## Solutions

### Fix 1: Match Case Types to Selector Type

Ensure case labels match the type of the switch expression.

```java
public void process(String input) {
    switch (input) {
        case "admin": // OK — String case for String selector
            System.out.println("Admin user");
            break;
        case "user":
            System.out.println("Regular user");
            break;
    }
}
```

### Fix 2: Use int Selector with int Cases

```java
public void check(int code) {
    switch (code) {
        case 0: // OK — int case for int selector
            System.out.println("Zero");
            break;
        case 1:
            System.out.println("One");
            break;
    }
}
```

### Fix 3: Use .equals() Instead of Switch

For simple comparisons, use if-else with `.equals()`.

```java
public void process(String input) {
    if ("admin".equals(input)) {
        System.out.println("Admin user");
    } else if ("user".equals(input)) {
        System.out.println("Regular user");
    }
}
```

### Fix 4: Upgrade to Java 7+

String switch is supported from Java 7 onward. Upgrade your Java version.

```java
// Java 7+
String status = "active";
switch (status) { // OK in Java 7+
    case "active":
        System.out.println("Active");
        break;
}
```

### Fix 5: Use Enum Switch

For fixed sets of values, use enums instead of strings.

```java
enum Status { ACTIVE, INACTIVE, PENDING }

public void check(Status status) {
    switch (status) {
        case ACTIVE:
            System.out.println("Active");
            break;
    }
}
```

### Fix 6: Use Map Lookup for String Dispatch

```java
Map<String, Runnable> actions = new HashMap<>();
actions.put("admin", () -> handleAdmin());
actions.put("user", () -> handleUser());

Runnable action = actions.get(input);
if (action != null) {
    action.run();
}
```

## Prevention Checklist

- Ensure switch case labels match the type of the selector expression
- Verify your Java version supports String switch (Java 7+)
- Use `switch` on enums for fixed sets of values — more type-safe than strings
- When using String switch, put the most common cases first for readability
- Consider if-else chains or Map lookups when switch doesn't fit the use case
- Avoid mixing types in case labels (e.g., String and int)

## Related Errors

- [constant expression required (constant-expression-required)](/languages/java/constant-expression-required)
- [incompatible types (incompatible-types)](/languages/java/incompatible-types)
- [unreachable statement (unreachable-statement)](/languages/java/unreachable-statement)
