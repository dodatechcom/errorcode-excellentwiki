---
title: "[Solution] Java NullPointerException"
description: "Try-with-Resources Null Resource"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# resource initialization returns null before the try block

A `resource` is thrown when inputstream is = getinputstream();  // null.

## Common Causes

```java
InputStream is = getInputStream();  // null
try (InputStream auto = is) { auto.read(); }  // NPE
```

## Solutions

```java
// Fix: null-check before try
InputStream is = getInputStream();
if (is == null) throw new IOException("null stream");
try (InputStream auto = is) { auto.read(); }

// Fix: validate inside try
try (Connection c = dataSource.getConnection()) {
    Objects.requireNonNull(c);
    process(c);
}
```

## Prevention Checklist

- Null-check or validate resource creation.
- Use Optional.ofNullable() for nullable creation.
- Verify connection pool configs.

## Related Errors

[NullPointerException](nullpointerexception), [IOException](ioexception)
