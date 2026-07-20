---
title: "[Solution] Java incompatible types: bad return type in lambda — Fix Lambda Return Type"
description: "Fix Java compiler error 'incompatible types: bad return type in lambda expression' by matching return type, checking functional interface, or using explicit cast. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 416
---

# Java Compiler Error: incompatible types: bad return type in lambda expression

This compile-time error occurs when a lambda expression's return type doesn't match the expected return type of the target functional interface. The lambda body must produce a value compatible with the functional interface's abstract method return type.

## Error Message

```
error: incompatible types: bad return type in lambda expression
        String is not assignable to int
        () -> "hello"
               ^
```

Other variants:

```
error: incompatible types: bad return type in lambda expression
        int cannot be converted to String
error: incompatible types: no instance(s) of type variable(s) T exist so that lambda is compatible
```

## Common Causes

### Cause 1: Return Type Mismatch

```java
Function<Integer, String> intToString = (Integer i) -> i; // ERROR: int not assignable to String
```

### Cause 2: Returning Null from Primitive Return Type

```java
ToIntFunction<String> lengthFn = (String s) -> null; // ERROR: null not assignable to int
```

### Cause 3: Incompatible Return in Different Branches

```java
Function<Integer, Object> fn = (Integer i) -> {
    if (i > 0) {
        return "positive"; // String
    } else {
        return -1; // int — ERROR: inconsistent return types
    }
};
```

### Cause 4: Void Method Expected, Value Returned

```java
Consumer<String> printer = (String s) -> {
    return s.toUpperCase(); // ERROR: Consumer expects void, not String
};
```

### Cause 5: Method Reference Returns Wrong Type

```java
Function<String, Integer> parser = Integer::parseInt; // OK
Function<String, Integer> broken = Double::intValue; // ERROR: Double::intValue doesn't take String
```

### Cause 6: Recursive Lambda with Wrong Return Type

```java
Function<Integer, Integer> factorial = (Integer n) -> {
    if (n <= 1) return 1;
    return n * factorial.apply(n - 1); // OK if consistent
};

Function<Integer, String> broken = (Integer n) -> {
    return factorial.apply(n); // ERROR: Integer not assignable to String
};
```

## Solutions

### Fix 1: Match the Return Type

Ensure the lambda returns the type specified by the functional interface.

```java
// Expected: Function<Integer, String>
Function<Integer, String> fn = (Integer i) -> String.valueOf(i); // OK

// NOT:
Function<Integer, String> broken = (Integer i) -> i; // ERROR
```

### Fix 2: Return the Correct Primitive or Wrapper

```java
// For primitive return types:
ToIntFunction<String> lengthFn = (String s) -> s.length(); // OK — returns int

// For wrapper return types:
Function<String, Integer> fn = (String s) -> s.length(); // OK — returns Integer
```

### Fix 3: Use Consistent Return Types in All Branches

```java
Function<Integer, String> fn = (Integer i) -> {
    if (i > 0) {
        return "positive"; // String
    } else {
        return "non-positive"; // String — consistent
    }
};
```

### Fix 4: Don't Return Values from Consumer

```java
Consumer<String> printer = (String s) -> {
    System.out.println(s); // OK — no return value
};
```

### Fix 5: Use Explicit Type in Lambda

Sometimes adding explicit parameter types resolves inference issues.

```java
Function<String, Integer> fn = (String s) -> Integer.parseInt(s); // OK
```

### Fix 6: Use a Method Reference That Matches

```java
Function<String, Integer> parser = Integer::parseInt; // OK

// For custom methods:
class Converter {
    public String toString(int value) { return String.valueOf(value); }
}

Converter conv = new Converter();
Function<Integer, String> fn = conv::toString; // OK
```

## Prevention Checklist

- Verify the functional interface's abstract method return type before writing the lambda
- Ensure all branches of a multi-line lambda return the same type
- Don't return values from `Consumer` lambdas (they return `void`)
- Use explicit parameter types when type inference fails
- Use method references when the lambda is a simple delegation to an existing method
- Check that method references have compatible parameter and return types

## Related Errors

- [invalid method reference (invalid-method-reference)](/languages/java/invalid-method-reference)
- [incompatible types (incompatible-types)](/languages/java/incompatible-types)
- [X is abstract; cannot be instantiated (abstract-method)](/languages/java/abstract-method)
