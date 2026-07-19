---
title: "[Solution] Java OutOfMemoryError — too many classes from classloader leaks or dynamic proxies"
description: "Fix Java OutOfMemoryError when too many classes from classloader leaks or dynamic proxies with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# OutOfMemoryError — too many classes from classloader leaks or dynamic proxies

A `OutOfMemoryError` occurs when // ClassLoader leak in web app
// Deploying/undeploying WAR without cleanup.

## Common Causes

```java
// ClassLoader leak in web app
// Deploying/undeploying WAR without cleanup
```

## Solutions

```java
// Fix: set limit
// -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m

// Fix: fix classloader leaks
Thread.currentThread().setContextClassLoader(null);

// Fix: cache proxies
private static final Map<Class<?>,Object> CACHE = new ConcurrentHashMap<>();

// Fix: monitor
MemoryMXBean m = ManagementFactory.getMemoryMXBean();
System.out.println("Metaspace: "+m.getNonHeapMemoryUsage().getUsed());
```

## Prevention Checklist

- Set -XX:MaxMetaspaceSize.
- Fix classloader leaks.
- Cache dynamically generated classes.
- Monitor with JMX.

## Related Errors

OutOfMemoryError, ClassNotFoundException
