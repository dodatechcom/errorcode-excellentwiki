---
title: "[Solution] Java CloneNotSupportedException — Object Clone Fix"
description: "Fix Java CloneNotSupportedException by implementing Cloneable, overriding clone(), or using copy constructors and factory methods instead of Object.clone()."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# CloneNotSupportedException — Object Clone Fix

A `CloneNotSupportedException` is thrown when your code calls `clone()` on an object whose class does not implement the `Cloneable` interface. This is a checked exception defined in `java.lang`.

## Description

The `Object.clone()` method checks whether the class implements `Cloneable` before performing the clone. If it does not, the method throws `CloneNotSupportedException`. This typically happens when:

- You call `clone()` on a class that does not implement `Cloneable`.
- You call `super.clone()` in a subclass whose parent does not implement `Cloneable`.
- You attempt to clone a final class that does not implement `Cloneable`.

## Common Causes

```java
// Cause 1: Class does not implement Cloneable
public class User {
    private String name;
    public User clone() throws CloneNotSupportedException {
        return (User) super.clone();  // CloneNotSupportedException
    }
}

// Cause 2: Parent class does not implement Cloneable
public class Base {
    // Does NOT implement Cloneable
}
public class Child extends Base implements Cloneable {
    public Child clone() throws CloneNotSupportedException {
        return (Child) super.clone();  // CloneNotSupportedException from Base
    }
}

// Cause 3: Calling clone() via reflection on non-Cloneable class
Object obj = new ArrayList<>();
Method cloneMethod = Object.class.getDeclaredMethod("clone");
cloneMethod.invoke(obj);  // CloneNotSupportedException
```

## Solutions

### Fix 1: Implement `Cloneable` and override `clone()`

```java
// Wrong
public class User {
    private String name;
    public User clone() throws CloneNotSupportedException {
        return (User) super.clone();
    }
}

// Correct
public class User implements Cloneable {
    private String name;
    @Override
    public User clone() {
        try {
            return (User) super.clone();
        } catch (CloneNotSupportedException e) {
            throw new AssertionError("Should not happen", e);  // We implement Cloneable
        }
    }
}
```

### Fix 2: Use copy constructors instead of `clone()`

```java
// Wrong — relies on clone()
User copy = original.clone();

// Correct — copy constructor is simpler and safer
public class User {
    private String name;
    public User(User other) {
        this.name = other.name;
    }
}

User copy = new User(original);
```

### Fix 3: Use factory methods for object copying

```java
public class User {
    private String name;

    public static User copyOf(User other) {
        return new User(other.name);
    }
}

User copy = User.copyOf(original);
```

### Fix 4: Use `SerializationUtils` for deep copies (Apache Commons)

```java
import org.apache.commons.lang3.SerializationUtils;

// Deep copy via serialization — requires Serializable
User copy = SerializationUtils.clone(original);
```

## Prevention Checklist

- Avoid `clone()` — prefer copy constructors or factory methods.
- If you must use `clone()`, always implement `Cloneable` and override `clone()` in the same class.
- Never call `clone()` via `Object.class` reflection on arbitrary objects.
- Consider using `record` types (Java 16+) which provide `copy()` patterns naturally.

## Related Errors

- [CloneNotSupportedException](../clonenotsupportedexception) — this exception itself.
- [UnsupportedOperationException](../unsupportedoperationexception) — thrown when an operation is not supported.
- [IllegalAccessException](../illegalaccessexception) — reflection access denied.
