---
title: "[Solution] Java ClassCastException — incorrect casting of Method.invoke return value"
description: "Fix Java ClassCastException when incorrect casting of method.invoke return value with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassCastException — incorrect casting of Method.invoke return value

A `ClassCastException` occurs when Method m = clazz.getMethod("getValue");
Object r = m.invoke(instance);
String v = (String) r;  // ClassCastException if returns Integer.

## Common Causes

```java
Method m = clazz.getMethod("getValue");
Object r = m.invoke(instance);
String v = (String) r;  // ClassCastException if returns Integer
```

## Solutions

```java
// Fix: check return type
Object r = m.invoke(instance);
if (r instanceof String s) { process(s); }

// Fix: cast utility
public static <T> T invokeAndCast(Method m, Object o, Class<T> t) {
    return t.cast(m.invoke(o));
}
```

## Prevention Checklist

- Verify return type before casting reflection results.
- Use instanceof or Class.cast().
- Document expected return types.

## Related Errors

ClassCastException, InvocationTargetException
