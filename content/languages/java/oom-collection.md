---
title: "[Solution] Java OutOfMemoryError — collections growing without bound"
description: "Fix Java OutOfMemoryError when collections growing without bound with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# OutOfMemoryError — collections growing without bound

A `OutOfMemoryError` occurs when List<Event> events = new ArrayList<>();
while (processing) { events.add(readEvent()); }  // grows forever.

## Common Causes

```java
List<Event> events = new ArrayList<>();
while (processing) { events.add(readEvent()); }  // grows forever
```

## Solutions

```java
// Fix: batch processing
List<Event> batch = new ArrayList<>(BATCH_SIZE);
while (processing) {
    batch.add(readEvent());
    if (batch.size() >= BATCH_SIZE) { processBatch(batch); batch.clear(); }
}

// Fix: bounded queue
Queue<Task> queue = new ArrayBlockingQueue<>(1000);

// Fix: streaming
try (Stream<String> lines = Files.lines(path)) { lines.forEach(this::process); }
```

## Prevention Checklist

- Use bounded collections.
- Process in batches.
- Use streaming APIs.
- Monitor collection sizes.

## Related Errors

OutOfMemoryError, GC Overhead
