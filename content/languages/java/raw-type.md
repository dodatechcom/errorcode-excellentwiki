---
title: "[Solution] Java X is a raw type — Fix Raw Type Usage"
description: "Fix Java compiler warning 'X is a raw type' by adding type parameters, using diamond operator, or replacing raw collections. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["warning"]
error_types: ["compile"]
weight: 413
---

# Java Compiler Warning: X is a raw type

This compile-time warning occurs when you use a generic class or interface without specifying its type parameter. Raw types bypass the compiler's generic type checking and can lead to `ClassCastException` at runtime. Java introduced generics in version 5 to provide compile-time type safety.

## Error Message

```
warning: [rawtypes] found raw type: List
        List list = new ArrayList();
        ^
```

Other variants:

```
warning: [rawtypes] found raw type: Map
warning: [rawtypes] found raw type: Comparable
warning: [unchecked] unchecked call to List.add(E) as a member of raw type List
```

## Common Causes

### Cause 1: Declaring Raw Type Variables

```java
// Raw type — no type parameter
List list = new ArrayList();
Map map = new HashMap();
Set set = new HashSet();
```

### Cause 2: Using Raw Type in Method Signatures

```java
public void process(List items) { // raw List
    for (Object item : items) { // must use Object
        System.out.println(item);
    }
}
```

### Cause 3: Instantiating with Raw Type

```java
ArrayList<String> list = new ArrayList(); // WARNING: raw type on right side
```

### Cause 4: Raw Type in Generic Containers

```java
List<List> nested = new ArrayList<>(); // WARNING: raw List inside List
```

### Cause 5: Raw Type in Extends/Implements

```java
class MyList extends ArrayList { // WARNING: raw ArrayList
    // ...
}
```

### Cause 6: Raw Type in Annotations or Annotations Processing

```java
Class rawClass = String.class; // WARNING: raw Class
```

## Solutions

### Fix 1: Add Type Parameters

Specify the type parameter on the left side.

```java
// Instead of:
List list = new ArrayList();

// Use:
List<String> list = new ArrayList<>(); // diamond operator infers type
```

### Fix 2: Use Diamond Operator

Java 7+ supports diamond operator (`<>`) for type inference.

```java
// Java 7+
List<String> names = new ArrayList<>();
Map<String, Integer> scores = new HashMap<>();
Set<Integer> numbers = new HashSet<>();
```

### Fix 3: Parameterize Method Signatures

```java
// Instead of:
public void process(List items) {
    for (Object item : items) { }
}

// Use:
public void process(List<String> items) {
    for (String item : items) { }
}
```

### Fix 4: Use Wildcards When Type is Unknown

```java
// Accept any List
public void printAll(List<?> items) {
    for (Object item : items) {
        System.out.println(item);
    }
}

// Accept Lists of any Number subtype
public void sum(List<? extends Number> numbers) {
    double total = 0;
    for (Number n : numbers) {
        total += n.doubleValue();
    }
}
```

### Fix 5: Parameterize Subclass

```java
class MyList extends ArrayList<String> { // parameterized
    // ...
}
```

### Fix 6: Use Class<T> Instead of Raw Class

```java
Class<String> clazz = String.class; // parameterized
```

## Prevention Checklist

- Always specify type parameters when using generic classes
- Use diamond operator (`<>`) on the right side of assignments (Java 7+)
- Replace `List` with `List<String>` (or appropriate type) in method signatures
- Use `List<?>` when you don't care about the element type
- Use IDE inspections to find and fix raw type warnings
- Avoid using legacy pre-generics APIs when modern alternatives exist
- Set your IDE to flag raw type usage as a warning

## Related Errors

- [unchecked cast warning (unchecked-cast)](/languages/java/unchecked-cast)
- [incompatible types (incompatible-types)](/languages/java/incompatible-types)
- [incompatible types: bad return type in lambda expression (lambda-body)](/languages/java/lambda-body)
