---
title: "[Solution] Java NullPointerException"
description: "HashMap Operations"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# calling methods on null values from map.get() or using null in ConcurrentHashMap

A `calling` is thrown when map<string,string> config = loadconfig();.

## Common Causes

```java
Map<String,String> config = loadConfig();
String host = config.get("host");
host.length();  // NPE if key missing
```

## Solutions

```java
// Fix: null check
String host = config.get("host");
if (host != null) { host.length(); }

// Fix: getOrDefault
String host = config.getOrDefault("host", "localhost");

// Fix: Optional
String host = Optional.ofNullable(config.get("host")).orElse("localhost");
```

## Prevention Checklist

- Never store null in ConcurrentHashMap.
- Prefer getOrDefault/computeIfAbsent.
- Use Optional.ofNullable for safe access.

## Related Errors

[NullPointerException](nullpointerexception), [ConcurrentModificationException](concurrentmodificationexception)
