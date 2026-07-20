---
title: "[Solution] Java InvocationHandler — Proxy Error"
description: "Fix Java InvocationHandler proxy errors by checking method.invoke, handling exceptions properly, and verifying proxy interfaces."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 23
---

# InvocationHandler — Proxy Error

Errors related to `InvocationHandler` occur when dynamic proxies fail to invoke the target method, throw unexpected exceptions, or violate the `Object` method contract.

## Description

`java.lang.reflect.InvocationHandler` is the core mechanism behind JDK dynamic proxies. Each method call on a proxy instance is routed to `invoke(Object proxy, Method method, Object[] args)`. Errors arise when the handler throws undeclared exceptions, calls `method.invoke()` incorrectly, or mismanages `Object` methods like `equals`, `hashCode`, and `toString`.

Common message variants:

- `UndeclaredThrowableException: exception not declared in interface`
- `IllegalArgumentException: object is not an instance of declaring class`
- `InvocationTargetException: target method threw exception`
- `NullPointerException in InvocationHandler.invoke — method or args null`
- `ClassCastException: proxy cannot be cast to expected interface`

## Common Causes

```java
// Cause 1: Throwing undeclared checked exception
InvocationHandler handler = (proxy, method, args) -> {
    throw new IOException("IO error");  // Not declared in interface
};
// Result: UndeclaredThrowableException

// Cause 2: Incorrect method.invoke call
InvocationHandler handler = (proxy, method, args) -> {
    return method.invoke(proxy, args);  // Infinite recursion for Object methods
};

// Cause 3: Passing wrong object to method.invoke
InvocationHandler handler = (proxy, method, args) -> {
    return method.invoke(someOtherObject, args);
    // IllegalArgumentException if someOtherObject doesn't declare the method
};

// Cause 4: Returning wrong type from invoke
InvocationHandler handler = (proxy, method, args) -> {
    if (method.getName().equals("toString")) {
        return 42;  // ClassCastException — must return String
    }
    return null;
};

// Cause 5: Null method or args without null checks
InvocationHandler handler = (proxy, method, args) -> {
    System.out.println(method.getName());
    // NPE if method is null
};
```

## Solutions

### Fix 1: Handle Object methods explicitly

```java
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

public class SafeInvocationHandler implements InvocationHandler {
    private final Object target;

    public SafeInvocationHandler(Object target) {
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        String name = method.getName();

        if ("equals".equals(name) && args != null && args.length == 1) {
            return proxy == args[0];
        }
        if ("hashCode".equals(name)) {
            return System.identityHashCode(proxy);
        }
        if ("toString".equals(name)) {
            return "Proxy[" + target.getClass().getSimpleName() + "]";
        }

        return method.invoke(target, args);
    }

    public static <T> T create(T target, Class<T> iface) {
        return (T) java.lang.reflect.Proxy.newProxyInstance(
            iface.getClassLoader(),
            new Class<?>[]{iface},
            new SafeInvocationHandler(target)
        );
    }
}
```

### Fix 2: Wrap target exceptions properly

```java
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class ExceptionWrappingHandler implements InvocationHandler {
    private final Object target;

    public ExceptionWrappingHandler(Object target) {
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        try {
            return method.invoke(target, args);
        } catch (InvocationTargetException e) {
            Throwable cause = e.getCause();
            if (cause instanceof RuntimeException) {
                throw (RuntimeException) cause;
            }
            if (cause instanceof Error) {
                throw (Error) cause;
            }
            throw e;
        }
    }
}
```

### Fix 3: Validate proxy type before casting

```java
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;

public class TypeSafeProxy {
    @SuppressWarnings("unchecked")
    public static <T> T create(Class<T> interfaceType, InvocationHandler handler) {
        if (!interfaceType.isInterface()) {
            throw new IllegalArgumentException(
                interfaceType.getName() + " is not an interface");
        }

        return (T) Proxy.newProxyInstance(
            interfaceType.getClassLoader(),
            new Class<?>[]{interfaceType},
            handler
        );
    }
}

// Usage
Runnable proxy = TypeSafeProxy.create(Runnable.class, (p, m, a) -> {
    if ("run".equals(m.getName())) {
        System.out.println("Running!");
        return null;
    }
    return null;
});
```

### Fix 4: Avoid infinite recursion on self-invocation

```java
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

public class NonRecursiveHandler implements InvocationHandler {
    private final Object target;
    private boolean inInvoke = false;

    public NonRecursiveHandler(Object target) {
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        if (inInvoke) {
            return method.invoke(target, args);  // Direct call, no proxy
        }
        inInvoke = true;
        try {
            System.out.println("Before: " + method.getName());
            Object result = method.invoke(target, args);
            System.out.println("After: " + method.getName());
            return result;
        } finally {
            inInvoke = false;
        }
    }
}
```

### Fix 5: Declare exceptions in the proxy interface

```java
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

public interface DataService {
    String fetchData() throws java.io.IOException;
    void saveData(String data) throws java.io.IOException;
}

public class DataServiceHandler implements InvocationHandler {
    private final DataService realService;

    public DataServiceHandler(DataService realService) {
        this.realService = realService;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        // Checked exceptions declared in DataService are allowed
        return method.invoke(realService, args);
    }
}
```

## Prevention Checklist

- Always handle `Object` methods (`equals`, `hashCode`, `toString`) in the handler.
- Catch `InvocationTargetException` and unwrap the cause from `method.invoke()`.
- Verify that `target` implements the same interface as the proxy.
- Declare checked exceptions in the proxy interface so they are not wrapped in `UndeclaredThrowableException`.
- Avoid calling methods on the proxy inside `invoke()` to prevent infinite recursion.
- Null-check `method` and `args` before use.

## Related Errors

- [UndeclaredThrowableException](../undeclaredthrownexception) — undeclared checked exception from proxy.
- [IllegalArgumentException](../illegalargumentexception) — wrong target in method.invoke.
- [InvocationTargetException](../invocationtargetexception) — target method threw exception.
- [ClassCastException](../classcastexception) — proxy cast to wrong interface.
