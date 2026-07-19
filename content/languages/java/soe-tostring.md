---
title: "[Solution] Java StackOverflowError — toString() methods with circular references"
description: "Fix Java StackOverflowError when tostring() methods with circular references with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# StackOverflowError — toString() methods with circular references

A `StackOverflowError` occurs when public class Person {
    private List<Pet> pets;
    public String toString() { return "Person{"+pets+"}"; }
}
public class Pet {
    private Person owner;
    public String toString() { return "Pet{"+owner+"}"; }
}.

## Common Causes

```java
public class Person {
    private List<Pet> pets;
    public String toString() { return "Person{"+pets+"}"; }
}
public class Pet {
    private Person owner;
    public String toString() { return "Pet{"+owner+"}"; }
}
```

## Solutions

```java
// Fix: break circular refs
@Data
public class Order {
    @ToString.Exclude private Customer customer;
}

// Fix: visited set
public String toString(Set<Object> visited) {
    if (visited.contains(this)) return "[circular]";
    visited.add(this);
    return "Person{name="+name+"}";
}

// Fix: Jackson for debug
String json = new ObjectMapper().writeValueAsString(obj);
```

## Prevention Checklist

- Avoid bidirectional toString() calls.
- Use @ToString.Exclude on back-references.
- Use Jackson for safe debug serialization.

## Related Errors

OutOfMemoryError, NullPointerException
