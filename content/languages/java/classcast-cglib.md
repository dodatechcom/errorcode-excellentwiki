---
title: "[Solution] Java ClassCastException — CGLIB proxy doesn't implement all interfaces of target"
description: "Fix Java ClassCastException when cglib proxy doesn't implement all interfaces of target with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassCastException — CGLIB proxy doesn't implement all interfaces of target

A `ClassCastException` occurs when Object obj = context.getBean(MyService.class);
Serializable s = (Serializable) obj;  // ClassCastException.

## Common Causes

```java
Object obj = context.getBean(MyService.class);
Serializable s = (Serializable) obj;  // ClassCastException
```

## Solutions

```java
// Fix: AopProxyUtils
Object target = AopProxyUtils.getSingletonTarget(bean);

// Fix: check proxy
if (AopUtils.isCglibProxy(bean)) {
    Object target = ((Advised) bean).getTargetSource().getTarget();
}
```

## Prevention Checklist

- Don't assume CGLIB proxies implement all interfaces.
- Use AopProxyUtils to unwrap.
- Test proxy behavior in AOP context.

## Related Errors

ClassCastException, BeanCreationException
