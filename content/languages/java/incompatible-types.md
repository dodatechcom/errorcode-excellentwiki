---
title: "[Solution] Java incompatible types — Fix Type Conversion Errors"
description: "Fix Java compiler error 'incompatible types: cannot convert from X to Y' by using correct types, adding casts, or using generics properly. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 401
---

# Java Compiler Error: incompatible types

This compile-time error occurs when the Java compiler detects that an expression of one type cannot be converted to the expected type. There is no implicit conversion between the two types, so the assignment or method call fails at compile time.

## Error Message

```
error: incompatible types: String cannot be converted to int
        int x = "hello";
              ^
```

Other variants:

```
error: incompatible types: int cannot be converted to String
error: incompatible types: ArrayList<String> cannot be converted to List<Integer>
error: incompatible types: Dog cannot be converted to Cat
error: incompatible types: Object cannot be converted to String
```

## Common Causes

### Cause 1: Assigning Wrong Primitive Type

Trying to assign one primitive type to another without a cast.

```java
public void example() {
    long big = 100L;
    int small = big; // ERROR: incompatible types: long cannot be converted to int

    double decimal = 3.14;
    int whole = decimal; // ERROR: incompatible types: double cannot be converted to int
}
```

### Cause 2: Passing Wrong Type to Method

Argument type doesn't match the parameter type.

```java
public void greet(String name) {
    System.out.println("Hello, " + name);
}

public void test() {
    greet(42); // ERROR: incompatible types: int cannot be converted to String
}
```

### Cause 3: Returning Wrong Type from Method

Return type doesn't match the declared return type.

```java
public String getName() {
    return 42; // ERROR: incompatible types: int cannot be converted to String
}
```

### Cause 4: Incompatible Generic Types

Assigning a `List<Integer>` to a `List<String>` is not allowed even though both are `List`.

```java
List<Integer> numbers = List.of(1, 2, 3);
List<String> strings = numbers; // ERROR: incompatible types
```

### Cause 5: Incompatible Reference Types (No Inheritance)

Trying to assign objects of unrelated class hierarchies.

```java
class Dog { }
class Cat { }

public void example() {
    Dog dog = new Dog();
    Cat cat = dog; // ERROR: incompatible types: Dog cannot be converted to Cat
}
```

### Cause 6: Autoboxing Mismatch

Assigning an incompatible wrapper type.

```java
Integer num = Boolean.TRUE; // ERROR: incompatible types
```

## Solutions

### Fix 1: Use an Explicit Cast

Cast the value to the target type when safe.

```java
long big = 100L;
int small = (int) big; // OK

double decimal = 3.14;
int whole = (int) decimal; // OK (truncates)
```

### Fix 2: Pass the Correct Type

Convert or provide the argument in the expected type.

```java
public void greet(String name) {
    System.out.println("Hello, " + name);
}

public void test() {
    greet(String.valueOf(42)); // OK
}
```

### Fix 3: Match the Return Type

Change the return value or the method signature.

```java
public int getCount() {
    return 42; // OK
}

// OR

public String getName() {
    return "Alice"; // OK
}
```

### Fix 4: Use Proper Generics

```java
List<Integer> numbers = List.of(1, 2, 3);
List<Integer> ints = numbers; // OK

// OR use wildcard
List<?> anyList = numbers; // OK
```

### Fix 5: Use Inheritance or Composition

Ensure the types have a relationship, or convert between them.

```java
class Animal { }
class Dog extends Animal { }

Dog dog = new Dog();
Animal animal = dog; // OK — Dog is a subclass of Animal
```

### Fix 6: Use Autoboxing Correctly

```java
Integer num = Integer.valueOf(42); // OK
Boolean flag = Boolean.TRUE; // OK — correct wrapper type
```

## Prevention Checklist

- Enable your IDE's type-checking inspections for compile-time warnings
- Use generics consistently to catch type mismatches early
- Prefer `var` (Java 10+) for local variables to reduce explicit type annotations when the type is clear
- Review method signatures before calling — check parameter and return types
- Use `instanceof` checks before downcasting reference types
- Avoid raw types; always parameterize generic collections

## Related Errors

- [incompatible types: possible lossy conversion (incompatible-types-assignment)](/languages/java/incompatible-types-assignment)
- [cannot find symbol: method (method-not-found)](/languages/java/method-not-found)
- [non-static method cannot be referenced from a static context (non-static-method)](/languages/java/non-static-method)
- [unchecked cast warning (unchecked-cast)](/languages/java/unchecked-cast)
