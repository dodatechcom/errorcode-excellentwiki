---
title: "[Solution] Java ArrayStoreException — Wrong Type in Array Fix"
description: "Fix Java ArrayStoreException when storing wrong type in array by checking array component type, verifying object type before assignment, and using generics."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 8
---

# ArrayStoreException — Wrong Type in Array Fix

An `ArrayStoreException` is thrown when you attempt to store an object of an incompatible type into an array. The array's component type does not match the type of the object being stored, and the JVM detects this at runtime.

## Description

Java arrays are covariant — `String[]` is a subtype of `Object[]`. This means you can assign a `String[]` to an `Object[]` variable, but the runtime still enforces the actual component type. If you try to store a non-String into that array, you get `ArrayStoreException`.

Message variants:

- `java.lang.ArrayStoreException: java.lang.Integer`
- `java.lang.ArrayStoreException: com.example.MyClass`
- `java.lang.ArrayStoreException` (no message in some JVM implementations)

## Common Causes

```java
// Cause 1: Covariant array — assign wrong type
Object[] arr = new String[3];  // String[] assigned to Object[]
arr[0] = "hello";   // OK
arr[1] = 42;        // ArrayStoreException — cannot store Integer in String[]

// Cause 2: Generic type erased — raw array stores wrong element
List<String> list = Arrays.asList("a", "b", "c");
Object[] raw = list.toArray();  // Object[] at runtime
raw[0] = 123;  // No compile error, but breaks list contract

// Cause 3: Casting array to wrong component type
Integer[] ints = {1, 2, 3};
Object[] objs = ints;
objs[0] = "string";  // ArrayStoreException — Integer[] cannot hold String

// Cause 4: System.arraycopy with incompatible types
String[] src = {"a", "b"};
Integer[] dst = new Integer[2];
System.arraycopy(src, 0, dst, 0, 2);  // ArrayStoreException

// Cause 5: Stream toArray with wrong type
Stream<Integer> stream = Stream.of(1, 2, 3);
Object[] arr = stream.toArray();
String[] strArr = (String[]) arr[0];  // ClassCastException / ArrayStoreException
```

## Solutions

### Fix 1: Check array component type before assignment

```java
public static void safeStore(Object[] array, Object value) {
    Class<?> componentType = array.getClass().getComponentType();
    if (value != null && !componentType.isInstance(value)) {
        throw new ArrayStoreException(
            "Cannot store " + value.getClass().getName()
            + " into " + componentType.getName() + "[]"
        );
    }
    array[0] = value;
}
```

### Fix 2: Use generics to prevent type confusion

```java
// Wrong — raw types allow mismatched storage
Object[] arr = new String[3];
arr[0] = 42;  // ArrayStoreException at runtime

// Right — generic method constrains the type
public static <T> T[] createArray(Class<T> componentType, int size) {
    @SuppressWarnings("unchecked")
    T[] arr = (T[]) Array.newInstance(componentType, size);
    return arr;
}

String[] arr = createArray(String.class, 3);  // type-safe
// arr[0] = 42;  // compile error — prevented at compile time
```

### Fix 3: Verify object type before putting in collection-backed array

```java
// Wrong — toArray returns Object[] even if list is typed
List<String> strings = new ArrayList<>();
strings.add("hello");
Object[] arr = strings.toArray();
arr[0] = Integer.valueOf(42);  // ArrayStoreException

// Right — use typed toArray
String[] arr = strings.toArray(new String[0]);  // type-safe
// arr[0] = 42;  // compile error

// Right — collect into correct array type
String[] arr = stream.collect(Collectors.toList()).toArray(new String[0]);
```

### Fix 4: Use List instead of arrays for safer collections

```java
// Arrays are covariant and error-prone
Object[] array = new String[10];
array[0] = 123;  // ArrayStoreException

// Lists are invariant and safe
List<String> list = new ArrayList<>();
list.add("hello");
// list.add(123);  // compile error — type safety enforced
```

## Prevention Checklist

- Prefer `List<T>` over `T[]` to avoid covariance pitfalls.
- Use `toArray(IntFunction<T[]>)` instead of `toArray()` for typed arrays.
- Check `array.getClass().getComponentType().isInstance(value)` before storing.
- Avoid casting `Object[]` to a specific component type after assignment.
- Use `Collectors.toList().toArray(new T[0])` for stream-to-array conversion.

## Related Errors

- [ClassCastException](../classcastexception) — type mismatch in general casting
- [ArrayIndexOutOfBoundsException](../arrayindexoutofboundsexception) — index out of range
- [ArrayStoreException](../arraystore-generic) — generic type confusion in arrays
