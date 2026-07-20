---
title: "[Solution] Java case expressions must be constant expressions — Fix String Switch"
description: "Fix Java compiler error 'case expressions must be constant expressions' in String switch by using if-else with .equals(), ensuring case values are compile-time constants. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 451
---

# Java Compiler Error: case expressions must be constant expressions

This compile-time error occurs when a `case` label in a `switch` statement is not a compile-time constant. For String switches (Java 7+), case values must be String literals or compile-time constant expressions — they cannot be method calls, variables, or computed values.

## Error Message

```
error: case expressions must be constant expressions
        case getStatus():
            ^
```

Other variants:

```
error: constant expression required
error: case expressions must be constant expressions
error: incompatible types: String cannot be converted to int
```

## Common Causes

### Cause 1: Using a Variable as Case Value

```java
private static final String ACTIVE = "active";

public void process(String status) {
    switch (status) {
        case ACTIVE: // OK — static final constant
            break;
    }
}

public void process(String input) {
    String key = "admin";
    switch (input) {
        case key: // ERROR: key is not a compile-time constant
            break;
    }
}
```

### Cause 2: Using a Method Return as Case Value

```java
public void process(String input) {
    switch (input) {
        case getDefault(): // ERROR: method call is not a constant expression
            break;
    }
}

public String getDefault() { return "default"; }
```

### Cause 3: Using a Runtime Computed String

```java
private static final String PREFIX = "user_";

public void process(String input) {
    String role = PREFIX + "admin"; // computed at runtime, not a constant
    switch (input) {
        case role: // ERROR: role is not a compile-time constant
            break;
    }
}
```

### Cause 4: Using a Non-Constant Static Field

```java
public class Config {
    static String MODE = "production"; // not final — not a constant

    public void check(String input) {
        switch (input) {
            case MODE: // ERROR: MODE is not a compile-time constant
                break;
        }
    }
}
```

## Solutions

### Fix 1: Use if-else With .equals()

```java
public void process(String input) {
    if ("admin".equals(input)) {
        handleAdmin();
    } else if ("user".equals(input)) {
        handleUser();
    }
}
```

### Fix 2: Use Static Final Constants

```java
private static final String STATUS_ACTIVE = "active";
private static final String STATUS_INACTIVE = "inactive";

public void process(String input) {
    switch (input) {
        case STATUS_ACTIVE: // OK — compile-time constant
            activate();
            break;
        case STATUS_INACTIVE:
            deactivate();
            break;
    }
}
```

### Fix 3: Use Enums Instead of Strings

```java
enum Status { ACTIVE, INACTIVE, PENDING }

public void process(Status status) {
    switch (status) { // enum values are always compile-time constants
        case ACTIVE:
            activate();
            break;
    }
}
```

### Fix 4: Use a Map Lookup

```java
import java.util.HashMap;
import java.util.Map;

public class Dispatcher {
    private static final Map<String, Runnable> actions = new HashMap<>();

    static {
        actions.put("admin", () -> handleAdmin());
        actions.put("user", () -> handleUser());
    }

    public void process(String input) {
        Runnable action = actions.get(input);
        if (action != null) {
            action.run();
        }
    }
}
```

### Fix 5: Use String Concatenation Correctly

```java
private static final String PREFIX = "ROLE_";
private static final String ADMIN = PREFIX + "ADMIN"; // OK — constant expression

public void check(String input) {
    switch (input) {
        case ADMIN: // OK — compiler evaluates at compile time
            break;
    }
}
```

## Prevention Checklist

- Ensure all `case` values are compile-time constants (static final fields or literals)
- Use if-else with `.equals()` when case values are not constants
- Prefer enums over String constants for type-safe switch dispatch
- Make static fields `final` when used as switch case values
- Use Map-based dispatch for dynamic case values
- Check that static final concatenations are purely compile-time evaluable

## Related Errors

- [constant expression required (constant-expression-required)](/languages/java/constant-expression-required)
- [string cannot be converted to int in switch (string-in-switch)](/languages/java/string-in-switch)
- [enum constant must be followed by ',' or '}' (enum-constant)](/languages/java/enum-constant)
