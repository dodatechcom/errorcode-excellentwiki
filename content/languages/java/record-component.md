---
title: "[Solution] Java record component errors — Fix Record Definitions"
description: "Fix Java compiler errors related to record components such as 'record component is not public' or 'cannot override record component'. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 419
---

# Java Compiler Error: record component errors

This compile-time error occurs when there are issues with record components (Java 16+). Records are a special kind of class that automatically generates canonical constructors, getters, `equals()`, `hashCode()`, and `toString()`. Errors arise when components conflict with generated methods, have accessibility issues, or violate record constraints.

## Error Message

```
error: record component must have a name
        record Point(int, int)
                      ^
```

Other variants:

```
error: record component x is not public
error: cannot override record component accessor method
error: variable x is already defined in record Point
error: record components cannot have the same name
error: record component must be followed by , or )
```

## Common Causes

### Cause 1: Duplicate Record Component Names

```java
record Point(int x, int x) { } // ERROR: duplicate record component name 'x'
```

### Cause 2: Conflicting Method with Generated Accessor

```java
record Person(String name) {
    public String name() { // ERROR: cannot override record component accessor
        return "custom";
    }
}
```

### Cause 3: Instance Field in Record

```java
record Point(int x, int y) {
    private String label; // ERROR: records cannot have instance fields (use components)
}
```

### Cause 4: Extending a Record

```java
record Point(int x, int y) { }

record ColoredPoint(int x, int y, Color color) extends Point { // ERROR: records cannot extend classes
}
```

### Cause 5: Record Component Name Conflicts with This

```java
record Example(int this) { } // ERROR: 'this' is a reserved name
```

### Cause 6: Non-Static Field Declaration

```java
record Point(int x, int y) {
    static int count; // OK — static fields are allowed
    int invalid; // ERROR: records cannot have instance fields outside components
}
```

### Cause 7: Constructor Parameter Name Conflict

```java
record Point(int x, int y) {
    Point(int x, int y) { // canonical constructor — must use same names
        this.x = x;
        this.y = y;
    }

    Point(int a, int b) { // compact constructor — different parameter names OK
        // this.x and this.y are auto-assigned
    }
}
```

## Solutions

### Fix 1: Use Unique Component Names

```java
record Point(int x, int y) { } // OK — unique names
```

### Fix 2: Don't Override Generated Accessors

```java
record Person(String name) {
    // If you need custom logic, use a separate method
    public String displayName() {
        return name.toUpperCase();
    }
}
```

### Fix 3: Use Components, Not Fields

```java
record Point(int x, int y) { } // components ARE the data
// No instance fields needed — components provide the data
```

### Fix 4: Use Composition Instead of Inheritance

```java
record Point(int x, int y) { }

record ColoredPoint(Point point, Color color) { } // composition instead of extends
```

### Fix 5: Rename Conflicting Components

```java
record Example(int id) { } // renamed from 'this' to 'id'
```

### Fix 6: Use Static Fields for Shared State

```java
record Point(int x, int y) {
    static int count = 0; // static field is OK

    Point {
        count++; // compact constructor can modify static state
    }
}
```

### Fix 7: Validate in Compact Constructor

```java
record PositiveInt(int value) {
    PositiveInt { // compact constructor — validation before assignment
        if (value < 0) {
            throw new IllegalArgumentException("value must be positive");
        }
        // this.value = value; — auto-assigned after compact constructor
    }
}
```

## Prevention Checklist

- Records are Java 16+ (preview in 14, 15) — verify your Java version
- Record component names must be unique within the record
- Don't override auto-generated accessor methods (use different method names)
- Records are implicitly `final` — they cannot be extended
- Records can only extend `java.lang.Record` — no other inheritance
- Use static fields for shared state, not instance fields
- Use compact constructors for validation — the assignment happens automatically after the body
- Component names must be valid Java identifiers (no reserved words)

## Related Errors

- [variable X is already defined in method (already-defined)](/languages/java/already-defined)
- [non-static method cannot be referenced from a static context (non-static-method)](/languages/java/non-static-method)
- [method does not override or implement a method from a supertype (override-methods)](/languages/java/override-methods)
