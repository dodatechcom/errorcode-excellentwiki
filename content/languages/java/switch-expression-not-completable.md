---
title: "[Solution] Java switch expression does not cover all values — Fix Exhaustive Switch"
description: "Fix Java compiler error switch expression does not cover all possible input values by adding default case, using exhaustive pattern matching, and handling all enum values. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 139
---

# Java Compiler Error: switch expression does not cover all possible input values

This compile-time error occurs in Java 14+ when a switch expression does not handle all possible input values. Unlike switch statements, switch expressions must be exhaustive—every possible value of the switch type must be covered.

## Error Message

```
error: the switch expression does not cover all possible input values
```

## Common Causes

### Cause 1: Missing Enum Value

```java
enum Day { MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY }

public class Example {
    public static String getDayType(Day day) {
        return switch (day) {
            case MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY -> "Weekday";
            case SATURDAY -> "Weekend";
            // Missing: SUNDAY
        };
    }
}
```

### Cause 2: Missing Default in Switch Expression

```java
public class Example {
    public static String classify(int value) {
        return switch (value) {
            case 1 -> "one";
            case 2 -> "two";
            case 3 -> "three";
            // Missing default case
        };
    }
}
```

### Cause 3: Switch on Sealed Class Without All Subclasses

```java
sealed interface Shape permits Circle, Rectangle, Triangle {}

record Circle(double radius) implements Shape {}
record Rectangle(double w, double h) implements Shape {}
record Triangle(double base, double height) implements Shape {}

public class Example {
    public static double area(Shape shape) {
        return switch (shape) {
            case Circle c -> Math.PI * c.radius() * c.radius();
            case Rectangle r -> r.w() * r.h();
            // Missing: Triangle case
        };
    }
}
```

### Cause 4: Missing Pattern Match Cases

```java
public class Example {
    public static String describe(Object obj) {
        return switch (obj) {
            case Integer i -> "Integer: " + i;
            case String s -> "String: " + s;
            // Missing: default case for other types
        };
    }
}
```

### Cause 5: Incomplete Boolean Switch

```java
public class Example {
    public static String check(boolean flag) {
        return switch (flag) {
            case true -> "yes";
            // Missing: false case
        };
    }
}
```

## Solutions

### Fix 1: Handle All Enum Values

```java
enum Day { MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY }

public class Example {
    public static String getDayType(Day day) {
        return switch (day) {
            case MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY -> "Weekday";
            case SATURDAY, SUNDAY -> "Weekend"; // Both weekend days covered
        };
    }
}
```

### Fix 2: Add Default Case

```java
public class Example {
    public static String classify(int value) {
        return switch (value) {
            case 1 -> "one";
            case 2 -> "two";
            case 3 -> "three";
            default -> "other"; // Default covers remaining values
        };
    }
}
```

### Fix 3: Cover All Sealed Class Permits

```java
sealed interface Shape permits Circle, Rectangle, Triangle {}

record Circle(double radius) implements Shape {}
record Rectangle(double w, double h) implements Shape {}
record Triangle(double base, double height) implements Shape {}

public class Example {
    public static double area(Shape shape) {
        return switch (shape) {
            case Circle c -> Math.PI * c.radius() * c.radius();
            case Rectangle r -> r.w() * r.h();
            case Triangle t -> 0.5 * t.base() * t.height();
        };
    }
}
```

### Fix 4: Add Default for Object Switch

```java
public class Example {
    public static String describe(Object obj) {
        return switch (obj) {
            case Integer i -> "Integer: " + i;
            case String s -> "String: " + s;
            default -> "Unknown: " + obj.getClass().getSimpleName();
        };
    }
}
```

### Fix 5: Handle Both Boolean Values

```java
public class Example {
    public static String check(boolean flag) {
        return switch (flag) {
            case true -> "yes";
            case false -> "no";
        };
    }
}
```

## Prevention Checklist

- Switch expressions must be exhaustive; every possible value must be handled
- Enum switches should cover all constants or include a default case
- Sealed class switches should cover all permitted subclasses
- Use default cases for integer and Object switches
- Enable IDE inspections for non-exhaustive switch expressions
- When adding new enum values, update all switch expressions immediately

## Related Errors

- [constant-expression-required](/languages/java/constant-expression-required/)
- [missing-return-statement](/languages/java/missing-return-statement/)
- [unreachable-statement](/languages/java/unreachable-statement/)
