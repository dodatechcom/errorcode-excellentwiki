---
title: "[Solution] Java unchecked wildcard invocation warning — Fix Unchecked Generic Invocation"
description: "Fix Java compiler warning 'unchecked wildcard invocation' by using @SuppressWarnings, providing type bounds, or using capture helper. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["warning"]
error_types: ["compile"]
weight: 463
---

# Java Compiler Warning: unchecked wildcard invocation

This compile-time warning occurs when you invoke a method on a wildcard generic type and the compiler cannot guarantee type safety. The wildcard (`?`) represents an unknown type, and calling methods that modify the generic type through a wildcard is inherently unsafe.

## Error Message

```
warning: unchecked invocation of method sort(List) as a member of the raw type List
        Collections.sort(list);
                         ^
```

Other variants:

```
warning: unchecked or unsafe operations
warning: unchecked wildcard invocation
warning: unchecked method invocation
```

## Common Causes

### Cause 1: Calling Method on Raw Type

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Example {
    public void sort() {
        List<String> list = new ArrayList<>();
        Collections.sort(list); // warning: unchecked invocation
    }
}
```

### Cause 2: Wildcard Parameter in Method Call

```java
import java.util.List;

public class Example {
    public void process(List<?> items) {
        items.add(items.get(0)); // WARNING: unchecked wildcard invocation
    }
}
```

### Cause 3: Generic Method With Unbounded Wildcard

```java
import java.util.ArrayList;
import java.util.List;

public class Example {
    public <T> void copy(List<? super T> dest, List<? extends T> src) {
        for (T item : src) {
            dest.add(item); // unchecked if T is unknown
        }
    }
}
```

### Cause 4: Raw Type Usage

```java
import java.util.ArrayList;
import java.util.List;

public class Example {
    public void test() {
        List rawList = new ArrayList(); // raw type
        rawList.add("item"); // unchecked warning
    }
}
```

## Solutions

### Fix 1: Use @SuppressWarnings

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Example {
    @SuppressWarnings("unchecked")
    public void sort() {
        List<String> list = new ArrayList<>();
        Collections.sort(list); // suppressed — safe because list is List<String>
    }
}
```

### Fix 2: Use Type-Safe Methods

```java
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Example {
    public void sort() {
        List<String> list = new ArrayList<>();
        list.sort(Comparator.naturalOrder()); // type-safe — no warning
    }
}
```

### Fix 3: Provide Explicit Type Bounds

```java
import java.util.List;

public class Example {
    public <T> void copy(List<? super T> dest, List<? extends T> src) {
        for (T item : src) {
            dest.add(item); // T is bounded — safe
        }
    }

    public <T extends Comparable<T>> void sort(List<T> items) {
        items.sort(null); // sorted by natural order
    }
}
```

### Fix 4: Use Capture Helper Pattern

```java
import java.util.List;

public class Example {
    static <T> void unsafeAdd(List<? super T> list, T item) {
        list.add(item); // safe because T is captured
    }

    public void test(List<? super String> list) {
        unsafeAdd(list, "hello"); // type-safe
    }
}
```

### Fix 5: Replace Raw Types With Parameterized Types

```java
import java.util.ArrayList;
import java.util.List;

public class Example {
    public void test() {
        List<String> list = new ArrayList<>(); // parameterized type
        list.add("item"); // no warning
    }
}
```

## Prevention Checklist

- Avoid raw types — always use parameterized types (`List<String>` not `List`)
- Use `@SuppressWarnings("unchecked")` only when you've verified type safety
- Prefer bounded wildcards (`? extends T`, `? super T`) over unbounded `?`
- Use the capture helper pattern for complex wildcard operations
- Enable `-Xlint:unchecked` to catch all unchecked warnings
- Use streams and functional operations to avoid manual generic manipulation

## Related Errors

- [unchecked cast (unchecked-cast)](/languages/java/unchecked-cast)
- [incompatible types (incompatible-types)](/languages/java/incompatible-types)
- [type argument not within bounds of type-variable (generic-type-mismatch)](/languages/java/generic-type-mismatch)
