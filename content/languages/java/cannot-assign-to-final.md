---
title: "[Solution] Java cannot assign a value to final variable — Fix Final Variable Reassignment"
description: "Fix Java compiler error cannot assign a value to final variable by removing the final modifier, creating new variables, or avoiding reassignment. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 131
---

# Java Compiler Error: cannot assign a value to final variable

This compile-time error occurs when you attempt to reassign a value to a variable declared as `final`. Final variables can only be assigned once—either at declaration or in the constructor for instance fields.

## Error Message

```
error: cannot assign a value to final variable x
```

## Common Causes

### Cause 1: Reassigning a Final Local Variable

```java
public class Example {
    public static void main(String[] args) {
        final int x = 10;
        x = 20; // Cannot reassign final variable
    }
}
```

### Cause 2: Reassigning a Final Parameter

```java
public class Example {
    public static void modify(final int value) {
        value = 100; // Cannot reassign final parameter
    }
}
```

### Cause 3: Reassigning a Final Instance Field Outside Constructor

```java
public class Example {
    final String name;

    public Example(String name) {
        this.name = name; // Valid: first assignment in constructor
    }

    public void setName(String name) {
        this.name = name; // Error: final field already assigned
    }
}
```

### Cause 4: Reassigning Final in Lambda

```java
public class Example {
    public static void main(String[] args) {
        final int count = 0;
        Runnable r = () -> {
            count++; // Error: cannot modify final variable in lambda
        };
    }
}
```

### Cause 5: Reassigning Final in Loop

```java
public class Example {
    public static void main(String[] args) {
        final int max = 10;
        for (int i = 0; i < max; i++) {
            max++; // Cannot modify final variable
        }
    }
}
```

## Solutions

### Fix 1: Remove the Final Modifier

```java
public class Example {
    public static void main(String[] args) {
        int x = 10;
        x = 20; // Allowed when not final
        System.out.println(x);
    }
}
```

### Fix 2: Create a New Variable

```java
public class Example {
    public static void main(String[] args) {
        final int x = 10;
        int y = x + 10; // New variable instead of reassigning
        System.out.println(y);
    }
}
```

### Fix 3: Use a Non-Final Field With Setter

```java
public class Example {
    private String name;

    public Example(String name) {
        this.name = name;
    }

    public void setName(String name) {
        this.name = name; // Allowed: field is not final
    }
}
```

### Fix 4: Use AtomicInteger for Lambda Modification

```java
import java.util.concurrent.atomic.AtomicInteger;

public class Example {
    public static void main(String[] args) {
        AtomicInteger count = new AtomicInteger(0);
        Runnable r = () -> {
            count.incrementAndGet(); // Allowed: object reference is effectively final
        };
        r.run();
        System.out.println(count.get());
    }
}
```

### Fix 5: Use a Non-Final Loop Variable

```java
public class Example {
    public static void main(String[] args) {
        int max = 10; // Not final
        for (int i = 0; i < max; i++) {
            System.out.println(i);
        }
    }
}
```

## Prevention Checklist

- Only declare variables as `final` when you are certain they will not be reassigned
- Use final for constants, callback parameters, and lambda-captured variables
- For mutable fields, omit the `final` modifier and use setter methods
- Use `AtomicInteger`, `AtomicReference`, etc. for thread-safe mutable state in lambdas
- Review final fields before adding setter methods

## Related Errors

- [variable-not-init](/languages/java/variable-not-init/)
- [incompatible-types-assignment](/languages/java/incompatible-types-assignment/)
- [illegalaccesserror](/languages/java/illegalaccesserror/)
