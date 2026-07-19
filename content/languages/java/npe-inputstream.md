---
title: "[Solution] Java NullPointerException"
description: "InputStream Null Operations"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# calling read/write on null InputStream or OutputStream references

A `calling` is thrown when inputstream is = getclass().getresourceasstream("/config.properties");.

## Common Causes

```java
InputStream is = getClass().getResourceAsStream("/config.properties");
byte[] data = is.readAllBytes();  // NPE if resource not found
```

## Solutions

```java
// Fix: check resource
InputStream is = getClass().getResourceAsStream("/config.properties");
if (is == null) throw new IOException("Resource not found");

// Fix: null-safe wrapper
InputStream safeStream(InputStream is) {
    return is == null ? InputStream.nullInputStream() : is;
}
```

## Prevention Checklist

- Always check getResourceAsStream() return.
- Use InputStream.nullInputStream() as safe no-op.
- Validate resource existence before creating streams.

## Related Errors

[NullPointerException](nullpointerexception), [IOException](ioexception)
