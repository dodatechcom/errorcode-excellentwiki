---
title: "[Solution] Java NullPointerException"
description: "Autoboxing Null Values"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# unboxing a null Integer, Long, or Boolean wrapper to a primitive

A `unboxing` is thrown when // unboxing null integer.

## Common Causes

```java
// Unboxing null Integer
Integer count = getCountFromDb();
int total = count + 1;  // NPE

// For-each with null element
List<Integer> nums = Arrays.asList(1, null, 3);
for (int n : nums) { sum += n; }  // NPE on null
```

## Solutions

```java
// Fix: null check
Integer count = getCountFromDb();
if (count != null) { int total = count + 1; }

// Fix: use Optional
int total = Optional.ofNullable(getCountFromDb()).orElse(0) + 1;

// Fix: filter nulls in stream
int sum = nums.stream().filter(Objects::nonNull).mapToInt(Integer::intValue).sum();
```

## Prevention Checklist

- Null-check wrapper types before unboxing.
- Use Optional to provide defaults.
- Enable null analysis in your IDE.

## Related Errors

[NullPointerException](nullpointerexception), [NumberFormatException](numberformatexception)
