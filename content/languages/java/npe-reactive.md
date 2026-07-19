---
title: "[Solution] Java NullPointerException"
description: "Reactive Streams Null Values"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# returning null from Reactor/RxJava map/flatMap operators

A `returning` is thrown when mono.just("hello").map(s -> null);  // npe.

## Common Causes

```java
Mono.just("hello").map(s -> null);  // NPE
```

## Solutions

```java
// Fix: use Mono.empty()
Mono.just("hello").filter(s -> !s.isEmpty())
    .flatMap(s -> process(s).map(Mono::just).orElse(Mono.empty()));

// Fix: filter nulls
Flux.fromIterable(getList()).filter(Objects::nonNull)
    .filter(item -> item.getName() != null).map(Item::getName).subscribe();

// Fix: defaultIfEmpty
Mono<String> result = service.findName(id).defaultIfEmpty("Unknown");
```

## Prevention Checklist

- Never return null from reactive operators.
- Filter nulls with .filter(Objects::nonNull).
- Use defaultIfEmpty() for fallback values.

## Related Errors

[NullPointerException](nullpointerexception), [IllegalStateException](illegalstatestream-consumed)
