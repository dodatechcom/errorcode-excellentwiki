---
title: "[Solution] Null Key for Map — Jackson NullPointerException Fix"
description: "Fix Jackson NullPointerException when serializing maps with null keys. Configure serialization settings."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jackson", "json", "null-key", "map", "serialization"]
weight: 5
---

# Null Key for Map — Jackson NullPointerException Fix

This error occurs when Jackson attempts to serialize a `Map` that contains a `null` key. JSON does not allow null keys, so Jackson throws a `NullPointerException`.

## What This Error Means

Common message:

- `Null key for a Map (out of bound entries) not allowed in JSON`

## Common Causes

```java
// Cause 1: Map with null key
Map<String, String> map = new HashMap<>();
map.put(null, "value");  // Null key
objectMapper.writeValueAsString(map);  // NullPointerException

// Cause 2: Null key from database query
Map<String, Object> results = queryResults;  // May contain null keys
```

## How to Fix

### Fix 1: Filter null keys before serialization

```java
Map<String, String> filtered = map.entrySet().stream()
    .filter(entry -> entry.getKey() != null)
    .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));

objectMapper.writeValueAsString(filtered);
```

### Fix 2: Replace null keys with empty string

```java
Map<String, String> safeMap = new HashMap<>();
map.forEach((k, v) -> safeMap.put(k != null ? k : "", v));
```

## Related Errors

- {{< relref "jackson-deserialization" >}} — MismatchedInputException
- {{< relref "jackson-unknown" >}} — UnrecognizedPropertyException
- {{< relref "nullpointerexception" >}} — General NullPointerException
