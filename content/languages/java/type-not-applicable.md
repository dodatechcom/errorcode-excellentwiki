---
title: "[Solution] Java type not applicable here — Fix Incorrect Type Usage"
description: "Fix Java compiler error type not applicable here by checking type usage, verifying generic parameters, and ensuring type is appropriate for context. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 135
---

# Java Compiler Error: type not applicable here

This compile-time error occurs when a type is used in a context where it is not valid. The type itself may be correct, but its usage in the particular location violates Java's type system rules.

## Error Message

```
error: type not applicable here
```

## Common Causes

### Cause 1: Primitive Type in Generic Context

```java
import java.util.List;

public class Example {
    public static void main(String[] args) {
        List<int> numbers = new ArrayList<>(); // Cannot use primitive in generic
    }
}
```

### Cause 2: Using Non-Static Type in Static Context

```java
public class Example {
    class Inner { }

    public static void main(String[] args) {
        Inner obj = new Inner(); // Cannot use non-static inner class in static context
    }
}
```

### Cause 3: Void Type in Expression

```java
public class Example {
    public static void main(String[] args) {
        int x = System.out.println("Hello"); // println returns void, not assignable
    }
}
```

### Cause 4: Interface Type Where Class Is Expected

```java
import java.io.Serializable;

public class Example {
    public static void main(String[] args) {
        Serializable s = new Serializable() {}; // Anonymous class works
        // But: Serializable obj = new Serializable(); // Cannot instantiate interface
    }
}
```

### Cause 5: Using Annotation as Type

```java
import java.lang.Override;

public class Example {
    public static void main(String[] args) {
        Override o = new Override(); // Annotation cannot be used as a type
    }
}
```

## Solutions

### Fix 1: Use Wrapper Class for Generics

```java
import java.util.ArrayList;
import java.util.List;

public class Example {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>(); // Use Integer, not int
        numbers.add(42); // Autoboxing handles conversion
    }
}
```

### Fix 2: Create Instance of Outer Class First

```java
public class Example {
    class Inner { }

    public static void main(String[] args) {
        Example outer = new Example();
        Inner obj = outer.new Inner(); // Use outer class instance
    }
}
```

### Fix 3: Don't Assign Void Return

```java
public class Example {
    public static void main(String[] args) {
        System.out.println("Hello"); // Call void method as statement
        // int x = System.out.println("Hello"); // Wrong
    }
}
```

### Fix 4: Create Concrete Implementation

```java
import java.io.Serializable;

public class Example implements Serializable {
    public static void main(String[] args) {
        Example obj = new Example(); // Instantiate class, not interface
    }
}
```

### Fix 5: Use Annotation in Correct Context

```java
import java.lang.Override;

public class Example {
    @Override // Annotation used as annotation, not as type
    public String toString() {
        return "Example";
    }
}
```

## Prevention Checklist

- Use wrapper classes (`Integer`, `Double`, etc.) with generics, never primitives
- Non-static inner classes require an instance of the enclosing class
- Void methods cannot be used as expressions or assigned to variables
- Interfaces cannot be instantiated directly; use implementing classes
- Annotations are metadata, not types; use them in annotation context only
- Check IDE type warnings for incorrect type usage

## Related Errors

- [incompatible-types](/languages/java/incompatible-types/)
- [non-static-method](/languages/java/non-static-method/)
- [cannot-be-applied](/languages/java/cannot-be-applied/)
