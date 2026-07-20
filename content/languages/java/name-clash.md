---
title: "[Solution] Java name clash — Method Erasure Causes Duplicate JVM Signatures"
description: "Fix Java compiler error name clash by renaming methods, using different parameter types, and avoiding erasure conflicts. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 125
---

# Java Compiler Error: name clash

This compile-time error occurs when method erasure causes two overloaded methods to have the same JVM signature. After type erasure, generic type parameters are replaced with their bounds, which can make previously distinct methods identical at the bytecode level.

## Error Message

```
error: name clash: methodA(List<String>) and methodA(List<Integer>) have the same erasure
```

## Common Causes

### Cause 1: Overloading With Same Raw Type

```java
import java.util.List;

public class Example {
    public void process(List<String> items) { }
    public void process(List<Integer> items) { } // Same erasure after type removal
}
```

### Cause 2: Generic Method With Same Erasure

```java
public class Example {
    public <T> void show(T item) { }
    public void show(String item) { } // Same erasure: show(Object)
}
```

### Cause 3: Override With Incompatible Generic Parameters

```java
import java.util.List;

public class Base {
    public void add(List<String> items) { }
}

public class Child extends Base {
    public void add(List<Integer> items) { } // Name clash with parent
}
```

### Cause 4: Bridge Method Conflict

```java
import java.util.Comparator;

public class Example implements Comparator<String> {
    public int compare(String a, String b) { return 0; }
    public int compare(Object a, Object b) { return 0; } // Bridge method clash
}
```

## Solutions

### Fix 1: Rename the Methods

```java
import java.util.List;

public class Example {
    public void processStrings(List<String> items) { }
    public void processIntegers(List<Integer> items) { }
}
```

### Fix 2: Use Wrapper Types

```java
import java.util.List;

public class Example {
    public void process(List<StringWrapper> items) { }
    public void process(List<IntegerWrapper> items) { }
}

class StringWrapper { String value; }
class IntegerWrapper { Integer value; }
```

### Fix 3: Use a Common Parameter Type With Type Check

```java
import java.util.List;

public class Example {
    public void process(List<?> items) {
        if (items.isEmpty()) return;
        Object first = items.get(0);
        if (first instanceof String) {
            processStrings((List<String>) items);
        } else if (first instanceof Integer) {
            processIntegers((List<Integer>) items);
        }
    }

    private void processStrings(List<String> items) { }
    private void processIntegers(List<Integer> items) { }
}
```

### Fix 4: Use Varargs Instead of List

```java
public class Example {
    public void process(String... items) { }
    public void process(Integer... items) { }
}
```

## Prevention Checklist

- Avoid overloading methods that differ only by generic type parameters
- Check erasure implications when designing generic APIs
- Use distinct method names when generic erasure would cause conflicts
- Test with `javap -s` to verify generated JVM signatures
- Prefer composition over inheritance when generic overloading is needed
- UseIDE inspections to detect erasure conflicts before compilation

## Related Errors

- [incompatible-types](/languages/java/incompatible-types/)
- [cannot-be-applied](/languages/java/cannot-be-applied/)
- [override-methods](/languages/java/override-methods/)
