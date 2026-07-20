---
title: "[Solution] Java type argument X is not within bounds of type-variable Y — Fix Generic Bounds"
description: "Fix Java compiler error 'type argument X is not within bounds of type-variable Y' by verifying type bounds, using wildcard ?, or checking generic constraints. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 452
---

# Java Compiler Error: type argument X is not within bounds of type-variable Y

This compile-time error occurs when you provide a type argument that does not satisfy the declared bounds of a type parameter. Generic type parameters can have upper bounds (using `extends`) that restrict which types can be used as arguments.

## Error Message

```
error: type argument String is not within bounds of type-variable T
        Container<String> c = new Container<>();
                         ^
```

Other variants:

```
error: type argument not within bounds of type-variable
error: incompatible types: inference variable T has incompatible bounds
```

## Common Causes

### Cause 1: Using Wrong Type With Bounded Generic

```java
public class NumberHolder<T extends Number> {
    private T value;
    public NumberHolder(T value) { this.value = value; }
}

// ERROR: String is not a subtype of Number
NumberHolder<String> holder = new NumberHolder<>("hello");
```

### Cause 2: Multiple Bounds Violated

```java
import java.io.Serializable;
import java.util.Comparator;

public class Processor<T extends Comparable<T> & Serializable> {
    // ...
}

// ERROR: StringBuilder is Serializable but not Comparable<StringBuilder>
Processor<StringBuilder> p = new Processor<>();
```

### Cause 3: Wildcard Bound Violation

```java
import java.util.ArrayList;
import java.util.List;

public class Example {
    public void addNumber(List<? extends Number> list) {
        // ...
    }

    public void test() {
        List<String> strings = new ArrayList<>();
        addNumber(strings); // ERROR: String is not within bounds of ? extends Number
    }
}
```

### Cause 4: Extending the Wrong Base Type

```java
public class Repository<T extends Entity> {
    // ...
}

class Entity { }

class Product { } // Product does NOT extend Entity

Repository<Product> repo = new Repository<>(); // ERROR: Product is not within bounds of T
```

## Solutions

### Fix 1: Use a Type That Satisfies the Bounds

```java
public class NumberHolder<T extends Number> {
    private T value;
    public NumberHolder(T value) { this.value = value; }
}

NumberHolder<Integer> holder = new NumberHolder<>(42); // OK — Integer extends Number
NumberHolder<Double> holder2 = new NumberHolder<>(3.14); // OK — Double extends Number
```

### Fix 2: Use Wildcard for Flexibility

```java
import java.util.List;

public class Example {
    public void process(List<? extends Number> list) {
        for (Number n : list) {
            System.out.println(n);
        }
    }

    public void test() {
        List<Integer> ints = List.of(1, 2, 3);
        process(ints); // OK — Integer extends Number

        List<Double> doubles = List.of(1.0, 2.0);
        process(doubles); // OK — Double extends Number
    }
}
```

### Fix 3: Remove or Relax the Bounds

```java
public class Container<T> { // no bounds restriction
    private T value;
    public Container(T value) { this.value = value; }
}

Container<String> c = new Container<>("hello"); // OK
```

### Fix 4: Add the Required Bound to Your Type

```java
import java.io.Serializable;

class Product implements Serializable {
    // ...
}

// Now Product satisfies Comparable<T> & Serializable if also Comparable
Repository<Product> repo = new Repository<>(); // OK if Product extends Entity
```

### Fix 5: Use a Capture Helper for Wildcards

```java
import java.util.List;

public class Example {
    static <T extends Number> void processHelper(List<T> list) {
        for (T item : list) {
            System.out.println(item.doubleValue());
        }
    }

    public void test(List<? extends Number> list) {
        processHelper(list); // OK — captures the wildcard type
    }
}
```

## Prevention Checklist

- Verify that type arguments satisfy all declared bounds (`extends` clauses)
- Use wildcards (`? extends X`) when you only need to read, not write
- Check the full set of bounds when using multiple bounds (`T extends A & B`)
- Use `? super T` for write-only operations (PECS principle)
- Review generic class declarations before instantiating with specific types
- Use IDE type inference to catch bound violations early

## Related Errors

- [incompatible types (incompatible-types)](/languages/java/incompatible-types)
- [unchecked cast (unchecked-cast)](/languages/java/unchecked-cast)
- [cannot infer type arguments (type-witness)](/languages/java/type-witness)
