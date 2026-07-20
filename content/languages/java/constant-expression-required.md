---
title: "[Solution] Java constant expression required — Fix Switch Case Value"
description: "Fix Java compiler error 'constant expression required' by using compile-time constants in switch cases or converting to if-else chains. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 406
---

# Java Compiler Error: constant expression required

This compile-time error occurs when a `case` label in a `switch` statement is not a compile-time constant. Java requires switch case values to be determined at compile time — they must be `static final` constants, enum values, or `String` literals (Java 7+).

## Error Message

```
error: constant expression required
        case getConfig():
               ^
```

Other variants:

```
error: case expression must be constant
error: constant expression required for case label
```

## Common Causes

### Cause 1: Using a Non-Constant Variable

A `static final` field initialized in a constructor is not a compile-time constant.

```java
public class Example {
    private static final int MAX = Integer.parseInt("100"); // not compile-time constant

    public void check(int value) {
        switch (value) {
            case MAX: // ERROR: constant expression required
                break;
        }
    }
}
```

### Cause 2: Using a Method Call

```java
public void check(int value) {
    switch (value) {
        case getDefaultValue(): // ERROR: constant expression required
            break;
    }
}

private int getDefaultValue() {
    return 42;
}
```

### Cause 3: Using a Runtime-Computed String

```java
String key = "STATUS_" + "ACTIVE"; // This IS a constant (concatenated literals)

// But this is NOT:
String dynamicKey = System.getProperty("key");
switch (input) {
    case dynamicKey: // ERROR: constant expression required
        break;
}
```

### Cause 4: Using a Non-Constant Static Final Field

```java
public class Config {
    public static final String MODE; // initialized in static block

    static {
        MODE = "production";
    }
}

public void check(String mode) {
    switch (mode) {
        case Config.MODE: // ERROR: not a compile-time constant
            break;
    }
}
```

### Cause 5: Using a Variable as Switch Selector (Not Label)

Sometimes confused — the expression *being switched on* doesn't need to be constant, but the `case` labels do.

```java
int selector = getRuntimeValue(); // OK — runtime value
switch (selector) {
    case 1: // OK — compile-time constant
        break;
    case getOtherValue(): // ERROR — not a compile-time constant
        break;
}
```

## Solutions

### Fix 1: Make the Field a Compile-Time Constant

```java
public class Example {
    private static final int MAX = 100; // compile-time constant

    public void check(int value) {
        switch (value) {
            case MAX: // OK
                break;
        }
    }
}
```

### Fix 2: Use an Enum

Enums are always valid case labels.

```java
enum Status { ACTIVE, INACTIVE, PENDING }

public void check(Status status) {
    switch (status) {
        case ACTIVE: // OK — enum constant
            break;
    }
}
```

### Fix 3: Convert to if-else Chain

When the value can't be a constant, use if-else.

```java
public void check(int value) {
    if (value == getDefaultValue()) { // OK — runtime comparison
        // handle
    } else if (value == anotherValue()) {
        // handle
    }
}
```

### Fix 4: Use a Map Instead of Switch

For complex key lookups.

```java
Map<String, Integer> actions = new HashMap<>();
actions.put("CREATE", 1);
actions.put("UPDATE", 2);

Integer actionId = actions.get(input); // No switch needed
```

### Fix 5: Use Text Blocks or String Concatenation for Constants

```java
public class Constants {
    public static final String PREFIX = "app"; // compile-time constant
    public static final String FULL = PREFIX + ".config"; // also compile-time constant
}

public void check(String value) {
    switch (value) {
        case Constants.FULL: // OK
            break;
    }
}
```

## Prevention Checklist

- Use `static final` with literal values for constants used in switch cases
- Initialize `static final` fields directly (not in static blocks or constructors) to ensure they are compile-time constants
- Use enums instead of integer or string constants for switch labels
- For runtime-determined values, use if-else chains instead of switch
- String concatenation of literal values produces compile-time constants

## Related Errors

- [unreachable statement (unreachable-statement)](/languages/java/unreachable-statement)
- [non-static method cannot be referenced from a static context (non-static-method)](/languages/java/non-static-method)
- [variable X might not have been initialized (variable-not-init)](/languages/java/variable-not-init)
