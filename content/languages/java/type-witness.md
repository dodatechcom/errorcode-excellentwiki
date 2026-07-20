---
title: "[Solution] Java cannot infer type arguments for X — Fix Type Inference"
description: "Fix Java compiler error 'cannot infer type arguments for X' by providing explicit type witness, simplifying expression, or checking generic parameters. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 460
---

# Java Compiler Error: cannot infer type arguments for X

This compile-time error occurs when the Java compiler cannot automatically infer the generic type arguments for a method call, constructor, or diamond expression. The compiler doesn't have enough information to determine the concrete type(s) to use.

## Error Message

```
error: cannot infer type arguments for ArrayList<>
        List<String> list = new ArrayList<>();
                                 ^
```

Other variants:

```
error: cannot infer type arguments for method X
error: cannot infer type-variable T
error: incompatible types: inference variable T has incompatible bounds
```

## Common Causes

### Cause 1: Diamond Expression With Ambiguous Types

```java
import java.util.ArrayList;
import java.util.List;

public class Example {
    public static <T> List<T> createList(T... items) {
        return new ArrayList<>();
    }

    public void test() {
        List list = createList(); // ERROR: cannot infer type arguments
    }
}
```

### Cause 2: Method Return Type Too Ambiguous

```java
import java.util.Optional;

public class Example {
    public <T> Optional<T> find(Class<T> type) {
        return Optional.empty(); // compiler can't infer T
    }

    public void test() {
        var result = find(null); // ERROR: cannot infer type arguments
    }
}
```

### Cause 3: Lambda With Inferred Type Conflict

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Example {
    public void test() {
        List<String> list = Arrays.asList("1", "2", "3");
        var numbers = list.stream()
            .map(s -> Integer.parseInt(s)) // ERROR: cannot infer type for map
            .collect(Collectors.toList());
    }
}
```

### Cause 4: Constructor Inference Failure

```java
public class Pair<A, B> {
    private A first;
    private B second;

    public Pair(A first, B second) {
        this.first = first;
        this.second = second;
    }
}

public class Example {
    public void test() {
        Pair p = new Pair("hello", 42); // ERROR: cannot infer type arguments
    }
}
```

### Cause 5: Generic Method With Insufficient Context

```java
public class Example {
    public static <T> T identity(T value) {
        return value;
    }

    public void test() {
        var result = identity(); // ERROR: no argument — can't infer T
    }
}
```

## Solutions

### Fix 1: Provide Explicit Type Witness

```java
import java.util.ArrayList;
import java.util.List;

public class Example {
    public void test() {
        List<String> list = Example.<String>createList(); // explicit type witness
    }

    public static <T> List<T> createList(T... items) {
        return new ArrayList<>();
    }
}
```

### Fix 2: Provide Arguments for Inference

```java
import java.util.Optional;

public class Example {
    public <T> Optional<T> find(Class<T> type) {
        return Optional.empty();
    }

    public void test() {
        var result = find(String.class); // compiler can infer T = String
    }
}
```

### Fix 3: Explicit Type for Diamond

```java
import java.util.ArrayList;
import java.util.List;

public class Example {
    public void test() {
        List<String> list = new ArrayList<String>(); // explicit type instead of diamond
    }
}
```

### Fix 4: Add Type Annotation to Lambda

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Example {
    public void test() {
        List<String> list = Arrays.asList("1", "2", "3");
        var numbers = list.stream()
            .map((String s) -> Integer.parseInt(s)) // explicit parameter type
            .collect(Collectors.toList());
    }
}
```

### Fix 5: Simplify Complex Expressions

```java
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Example {
    public void test() {
        // Complex — may fail inference
        // var result = Stream.of(1, 2, 3).map(x -> x.toString()).collect(Collectors.toList());

        // Simpler — explicit
        List<String> result = Stream.of(1, 2, 3)
            .map(x -> x.toString())
            .collect(Collectors.toList());
    }
}
```

## Prevention Checklist

- Provide explicit type witnesses when diamond inference fails
- Supply method arguments that give the compiler enough information to infer types
- Use explicit type parameters for constructors when diamond (`<>`) inference is ambiguous
- Add explicit lambda parameter types when inference is unclear
- Simplify complex generic chains — break them into steps
- Use IDE type inference hints to understand what the compiler expects

## Related Errors

- [type argument not within bounds of type-variable (generic-type-mismatch)](/languages/java/generic-type-mismatch)
- [incompatible types (incompatible-types)](/languages/java/incompatible-types)
- [unchecked cast (unchecked-cast)](/languages/java/unchecked-cast)
