---
title: "[Solution] Java ClassNotFoundException — Proxy.newProxyInstance cannot find proxy interface with wrong ClassLoader"
description: "Fix Java ClassNotFoundException when proxy.newproxyinstance cannot find proxy interface with wrong classloader with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassNotFoundException — Proxy.newProxyInstance cannot find proxy interface with wrong ClassLoader

A `ClassNotFoundException` occurs when Proxy.newProxyInstance(getClass().getClassLoader(), new Class[]{MyService.class}, handler);.

## Common Causes

```java
Proxy.newProxyInstance(getClass().getClassLoader(), new Class[]{MyService.class}, handler);
```

## Solutions

```java
// Fix: use interface's ClassLoader
Class<?> iface = MyService.class;
Proxy.newProxyInstance(iface.getClassLoader(), new Class[]{iface}, handler);

// Fix: Thread context ClassLoader
ClassLoader orig = Thread.currentThread().getContextClassLoader();
try {
    Thread.currentThread().setContextClassLoader(MyService.class.getClassLoader());
    Object p = Proxy.newProxyInstance(MyService.class.getClassLoader(), new Class[]{MyService.class}, handler);
} finally { Thread.currentThread().setContextClassLoader(orig); }
```

## Prevention Checklist

- Use interface's own ClassLoader.
- Test proxy creation in deployment environment.
- Use combined ClassLoaders for multi-module.

## Related Errors

ClassNotFoundException, ClassCastException
