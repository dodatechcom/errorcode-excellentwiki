---
title: "[Solution] Java NullPointerException"
description: "Constructor Delegation Chains"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# constructor delegation via this() leaving fields uninitialized

A `constructor` is thrown when public service(string name) { this(name, null); }.

## Common Causes

```java
public Service(String name) { this(name, null); }
public Service(String name, Database db) {
    this.name = name; this.db = db;
    db.connect();  // NPE from first constructor
}
```

## Solutions

```java
// Fix: provide non-null defaults
public Service(String name) { this(name, createDefaultDb()); }

// Fix: use factory methods
public static Service create(String name) {
    return new Service(name, new DefaultDatabase());
}
```

## Prevention Checklist

- Validate all constructors initialize all fields.
- Use Objects.requireNonNull() for parameters.
- Prefer factory methods over delegation.

## Related Errors

[NullPointerException](nullpointerexception), [IllegalStateException](illegalstateexception)
