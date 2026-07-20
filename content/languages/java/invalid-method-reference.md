---
title: "[Solution] Java invalid method reference — Fix Method Reference Errors"
description: "Fix Java compiler error 'invalid method reference' or 'no applicable method found' by checking method signature, parameter types, and functional interface. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 411
---

# Java Compiler Error: invalid method reference

This compile-time error occurs when a method reference (`::`) doesn't match the target functional interface. The referenced method must have a compatible signature — same number of parameters, compatible parameter types, and a compatible return type.

## Error Message

```
error: invalid method reference
        list.stream().map(String::parseInt)
                                  ^
  method parseInt in class Integer cannot be applied to given types;
  required: String
  found: no arguments
  reason: actual and formal argument lists differ in length
```

Other variants:

```
error: no applicable method found for method reference
error: incompatible types: invalid method reference
```

## Common Causes

### Cause 1: Wrong Number of Parameters

The method reference has a different arity than the functional interface expects.

```java
// Comparator expects (T, T) -> int
List<String> sorted = list.stream()
    .sorted(String::compareTo) // OK — compareTo(String) takes 1 arg + this
    .collect(Collectors.toList());

// But this fails:
list.stream().map(String::format); // ERROR: format requires varargs
```

### Cause 2: Wrong Parameter Types

```java
@FunctionalInterface
interface Parser {
    int parse(String s);
}

// This works
Parser p = Integer::parseInt; // OK

// This doesn't
Parser p2 = Double::parseInt; // ERROR: parseInt doesn't exist on Double
```

### Cause 3: Method Reference on Wrong Type

```java
list.stream()
    .map(Objects::nonNull) // ERROR: nonNull is an instance method concept, not static
```

### Cause 4: Instance Method vs Static Method Confusion

```java
// Reference to instance method on parameter
list.stream().map(String::toUpperCase); // OK — instance method on String parameter

// Reference to static method (wrong)
list.stream().map(String::valueOf); // May fail if functional interface doesn't match
```

### Cause 5: Non-Existent Method

```java
list.stream()
    .map(String::toInt) // ERROR: String has no toInt() method
```

### Cause 6: Ambiguous Method Reference

```java
class MyClass {
    void process(int x) { }
    void process(String x) { }
}

// ERROR: ambiguous — which process() to reference?
Function<Integer, Boolean> fn = MyClass::process;
```

## Solutions

### Fix 1: Use Lambda Instead

Lambdas give you explicit control over parameter types.

```java
// Instead of method reference:
list.stream()
    .map(s -> Integer.parseInt(s)) // OK — lambda is more explicit
    .collect(Collectors.toList());
```

### Fix 2: Verify Method Signature

Ensure the referenced method matches the functional interface signature.

```java
@Functional interface
interface Transformer {
    String transform(String input);
}

// OK — matches (String) -> String
Transformer t1 = String::toUpperCase;

// OK — explicit lambda
Transformer t2 = s -> s.toUpperCase();
```

### Fix 3: Use Correct Static Method

```java
// Reference to static method
Function<String, Integer> parser = Integer::parseInt; // OK — (String) -> int

// Reference to static method on correct class
Function<String, Double> dbl = Double::valueOf; // OK
```

### Fix 4: Use Constructor Reference

```java
Supplier<List<String>> listFactory = ArrayList::new; // OK — () -> new ArrayList
Function<Integer, ArrayList> arrayListOfSize = ArrayList::new; // OK — (int) -> new ArrayList
```

### Fix 5: Add Explicit Lambda to Resolve Ambiguity

```java
class MyClass {
    void process(int x) { }
    void process(String x) { }
}

// Use lambda to resolve ambiguity
Function<MyClass, Consumer<?>> fn = obj -> obj::process; // explicit
```

## Prevention Checklist

- Verify the method reference matches the functional interface's parameter count and types
- Use your IDE's auto-complete to find valid method references
- When method references are ambiguous or complex, use lambda expressions instead
- Check the class you're referencing — static methods use `ClassName::methodName`, instance methods use `instance::methodName` or `ClassName::instanceMethod`
- Understand the functional interface you're targeting — read its `@FunctionalInterface` definition
- Ensure the referenced method exists and is accessible

## Related Errors

- [incompatible types: bad return type in lambda expression (lambda-body)](/languages/java/lambda-body)
- [cannot find symbol: method (method-not-found)](/languages/java/method-not-found)
- [incompatible types (incompatible-types)](/languages/java/incompatible-types)
- [X is abstract; cannot be instantiated (abstract-method)](/languages/java/abstract-method)
