---
title: "[Solution] Java OutOfMemoryError — JVM spends too much time in GC with too little memory freed"
description: "Fix Java OutOfMemoryError when jvm spends too much time in gc with too little memory freed with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# OutOfMemoryError — JVM spends too much time in GC with too little memory freed

A `OutOfMemoryError` occurs when // Tight loop allocating objects
while (true) { list.add(new Object()); }  // GC overhead OOM.

## Common Causes

```java
// Tight loop allocating objects
while (true) { list.add(new Object()); }  // GC overhead OOM
```

## Solutions

```java
// Fix: increase heap if needed
// -Xmx4g

// Fix: reduce allocations
// Use primitive arrays instead of wrapper collections
int[] arr = new int[size];  // compact

// Fix: use flyweight pattern
private static final Map<String,String> FLYWEIGHT = Map.of("k1","v1");
String v = FLYWEIGHT.computeIfAbsent(k, key -> expensive(key));

// Fix: profile and find leak
// jmap -histo:live <pid>
// VisualVM or YourKit for leak detection
```

## Prevention Checklist

- Monitor GC with -verbose:gc.
- Use -XX:+HeapDumpOnOutOfMemoryError.
- Profile memory usage regularly.
- Reduce unnecessary object allocation.

## Related Errors

OutOfMemoryError, OutOfMemoryError
