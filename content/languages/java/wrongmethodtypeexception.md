---
title: "[Solution] Java WrongMethodTypeException — MethodHandle Type Mismatch Fix"
description: "Fix Java WrongMethodTypeException by checking method type signatures, using asType() to adapt handles, and verifying parameter and return types."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 67
---

# WrongMethodTypeException — MethodHandle Type Mismatch Fix

A `WrongMethodTypeException` is thrown when a `MethodHandle` is invoked with a method type signature that does not match the handle's expected type. This is a runtime error in the `java.lang.invoke` package used with dynamic languages and MethodHandle-based programming.

## Description

`java.lang.invoke.WrongMethodTypeException` extends `WrongHandleTypeException` extends `LambdaException` extends `RuntimeException`. Common variants include:

- `wrong type: (int)java.lang.String cannot be used as (java.lang.Object)java.lang.Object`
- `expected (int,int)int but found (int)int`
- `MethodHandle.invokeExact failed for the wrong reason`

This exception is thrown by `MethodHandle.invoke()` or `MethodHandle.invokeExact()` when the supplied arguments do not match the handle's parameter types.

## Common Causes

```java
// Cause 1: Invoking a handle with wrong argument count
MethodHandle mh = MethodHandles.lookup()
    .findVirtual(String.class, "length", MethodType.methodType(int.class));
mh.invoke("hello", "extra");  // WrongMethodTypeException: too many arguments

// Cause 2: Invoking with wrong argument types
MethodHandle mh = MethodHandles.lookup()
    .findStatic(Math.class, "max", MethodType.methodType(int.class, int.class, int.class));
mh.invoke(1.0, 2.0);  // WrongMethodTypeException: expects int, got double

// Cause 3: Wrong return type expectation with invokeExact
MethodHandle mh = MethodHandles.lookup()
    .findStatic(Integer.class, "valueOf", MethodType.methodType(Integer.class, int.class));
Integer result = (int) mh.invokeExact(42);  // WrongMethodTypeException: int vs Integer

// Cause 4: Using asType incorrectly
MethodHandle mh = MethodHandles.Lookup.IMPL_LOOKUP.findVirtual(
    String.class, "substring", MethodType.methodType(String.class, int.class));
mh.asType(MethodType.methodType(String.class, int.class, int.class));  // WrongMethodTypeException

// Cause 5: Mixing up static and instance method handles
MethodHandle mh = MethodHandles.lookup()
    .findStatic(MyClass.class, "staticMethod", MethodType.methodType(void.class));
mh.invoke(new MyClass());  // WrongMethodTypeException: static handle got instance argument
```

## Solutions

### Fix 1: Check and match the exact method type signature

```java
MethodType expectedType = mh.type();
MethodType suppliedType = MethodType.methodType(returnType, paramTypes);

if (!expectedType.equals(suppliedType)) {
    throw new IllegalArgumentException(
        "Expected: " + expectedType + ", Supplied: " + suppliedType);
}

Object result = mh.invokeExact(args);
```

### Fix 2: Use asType() to adapt the handle before invocation

```java
MethodHandle mh = MethodHandles.lookup()
    .findStatic(Math.class, "max", MethodType.methodType(int.class, int.class, int.class));

// Adapt int arguments to double (widening conversion)
MethodHandle adapted = mh.asType(MethodType.methodType(double.class, double.class, double.class));
double result = adapted.invoke(3.5, 7.2);  // works via widening
```

### Fix 3: Use invoke() instead of invokeExact() for type flexibility

```java
MethodHandle mh = MethodHandles.lookup()
    .findStatic(Integer.class, "valueOf", MethodType.methodType(Integer.class, int.class));

// invoke() allows implicit widening/conversion
Object result = mh.invoke(42);  // works with autoboxing
```

### Fix 4: Verify parameter and return types before invocation

```java
public static Object safeInvoke(MethodHandle mh, Object... args) throws Throwable {
    MethodType type = mh.type();
    if (args.length != type.parameterCount()) {
        throw new WrongMethodTypeException("Expected " + type.parameterCount() +
            " args, got " + args.length);
    }
    return mh.invokeWithArguments(args);
}
```

## Prevention Checklist

- Always verify `MethodHandle.type()` before invoking
- Use `invokeWithArguments()` for flexibility, or `invokeExact()` when types are precisely known
- Use `asType()` to adapt method handles when argument types differ
- Double-check static vs instance method handles and their implicit receiver parameters
- Test method handle invocations with edge-case types (null, boxed primitives)

## Related Errors

- [ClassCastException](/languages/java/classcast-spring/) — Similar type mismatch at the object level
- [NoSuchMethodException](/languages/java/nosuchmethodexception/) — Method handle lookup failed
- [WrongThreadException](/languages/java/wrongthreadexception/) — Thread-safety violation in concurrency
