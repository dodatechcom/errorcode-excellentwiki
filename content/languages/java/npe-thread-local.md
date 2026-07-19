---
title: "[Solution] Java NullPointerException"
description: "ThreadLocal Null Value Access"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# accessing ThreadLocal values not set or removed for current thread

A `accessing` is thrown when private static final threadlocal<usercontext> currentuser = new threadlocal<>();.

## Common Causes

```java
private static final ThreadLocal<UserContext> currentUser = new ThreadLocal<>();
UserContext ctx = currentUser.get();  // null if not set
ctx.getUserId();  // NPE
```

## Solutions

```java
// Fix: use initialValue()
private static final ThreadLocal<UserContext> currentUser =
    ThreadLocal.withInitial(() -> new UserContext());

// Fix: remove in finally
try { currentUser.set(extractContext(req)); chain.doFilter(req, res); }
finally { currentUser.remove(); }
```

## Prevention Checklist

- Use ThreadLocal.withInitial().
- Null-check get() unless set() was called.
- Always remove() in finally blocks.

## Related Errors

[NullPointerException](nullpointerexception), [ConcurrentModificationException](concurrentmodificationexception)
