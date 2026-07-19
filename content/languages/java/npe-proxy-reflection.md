---
title: "[Solution] Java NullPointerException"
description: "Proxy and Reflection Null"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# invoking methods via reflection where target or args are null

A `invoking` is thrown when method m = clazz.getmethod("process", string.class);.

## Common Causes

```java
Method m = clazz.getMethod("process", String.class);
m.invoke(null, "hello");  // NPE if not static
```

## Solutions

```java
// Fix: null-check target
Object target = getTarget();
if (target != null) m.invoke(target, "hello");

// Fix: null-safe reflection
public static Object invoke(Object o, Method m, Object... args) {
    if (o == null) throw new IAE("target null");
    return m.invoke(o, args);
}
```

## Prevention Checklist

- Validate target before reflective invocation.
- Use null-safe reflection utilities.
- Null-check AOP arguments before use.

## Related Errors

[NullPointerException](nullpointerexception), [InvocationTargetException](invocationtargetexception)
