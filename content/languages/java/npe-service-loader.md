---
title: "[Solution] Java NullPointerException"
description: "ServiceLoader Null Provider"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ServiceLoader findFirst returns no provider used without null checks

A `ServiceLoader` is thrown when serviceloader<serializer> loader = serviceloader.load(serializer.class);.

## Common Causes

```java
ServiceLoader<Serializer> loader = ServiceLoader.load(Serializer.class);
Serializer s = loader.findFirst().get();  // NoSuchElementException
```

## Solutions

```java
// Fix: Optional
loader.findFirst().ifPresent(s -> process(s));

// Fix: orElseThrow
Serializer s = loader.findFirst()
    .orElseThrow(() -> new ISE("No provider found"));

// Fix: check iterator
Iterator<Plugin> it = loader.iterator();
if (it.hasNext()) { process(it.next()); }
```

## Prevention Checklist

- Check if ServiceLoader found a provider.
- Use Optional.orElseThrow() with descriptive message.
- Ensure META-INF/services files are correct.

## Related Errors

[NullPointerException](nullpointerexception), [ServiceConfigurationError](classnotfoundexception)
