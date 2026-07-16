---
title: "[Solution] Java OutOfMemoryError — Heap Space Fix"
description: "Fix Java OutOfMemoryError: Java heap space by increasing JVM memory with -Xmx, fixing memory leaks, and optimizing application memory usage."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
tags: ["outofmemoryerror", "heap", "memory", "jvm"]
weight: 30
---

# OutOfMemoryError — Heap Space Fix

An `OutOfMemoryError` (OOME) is thrown when the JVM cannot allocate enough memory to satisfy an object creation request. Unlike most exceptions, this is an `Error` (not an `Exception`), meaning the JVM considers the situation unrecoverable. The most common variant is `Java heap space`, but others include `Metaspace` and `GC overhead limit exceeded`.

## Description

The JVM divides memory into several regions — heap, metaspace, native memory, and stack. When the heap fills up and garbage collection cannot free enough space, the OOME fires. Common variants:

- `java.lang.OutOfMemoryError: Java heap space` — the heap is full.
- `java.lang.OutOfMemoryError: Metaspace` — class metadata storage exhausted (Java 8+).
- `java.lang.OutOfMemoryError: GC overhead limit exceeded` — GC spent >98% time reclaiming <2% memory.
- `java.lang.OutOfMemoryError: Direct buffer memory` — native (off-heap) memory exhausted.
- `java.lang.OutOfMemoryError: unable to create new native thread` — OS thread limit reached.

## Common Causes

```java
// Cause 1: Unbounded collection growth
List<byte[]> data = new ArrayList<>();
while (true) {
    data.add(new byte[1024 * 1024]);  // adds 1 MB each iteration until OOM
}

// Cause 2: Cache without eviction policy
Map<String, Object> cache = new HashMap<>();
while (scanner.hasNext()) {
    cache.put(scanner.next(), loadObject(scanner.next()));  // never evicts
}

// Cause 3: Large array allocation
byte[] hugeArray = new byte[Integer.MAX_VALUE];  // ~2 GB allocation

// Cause 4: Memory leak via static reference
static List<Object> leak = new ArrayList<>();
public void addItem(Object o) {
    leak.add(o);  // objects never GC'd because static ref is permanent
}

// Cause 5: Unclosed resources (streams, connections)
FileInputStream fis = new FileInputStream("huge.log");
// fis is never closed — native memory and file descriptors leak
```

## Solutions

### Fix 1: Increase JVM heap size

```bash
# Default heap is often 256 MB or 1 GB — increase it
java -Xms512m -Xmx4g -jar myapp.jar

# For large data processing
java -Xms2g -Xmx8g -jar myapp.jar

# For Docker containers, set both min and max
java -Xms2g -Xmx4g -jar myapp.jar
```

### Fix 2: Fix memory leaks with profiling

```bash
# Enable heap dumps on OOM
java -XX:+HeapDumpOnOutOfMemoryError \
     -XX:HeapDumpPath=/tmp/heapdump.hprof \
     -jar myapp.jar

# Analyze with Eclipse MAT or VisualVM
# Look for "Leak Suspects" report to find objects consuming the most memory
```

```java
// Add a pre-OOM dump trigger for debugging
ManagementFactory.getMemoryMXBean().setObjectName(
    new ObjectName("java.lang:type=Memory"));
```

### Fix 3: Use bounded caches with eviction

```java
// Wrong — unbounded cache grows forever
Map<String, byte[]> cache = new HashMap<>();

// Correct — use a size-bounded cache
Map<String, byte[]> cache = new LinkedHashMap<>(1000, 0.75f, true) {
    @Override
    protected boolean removeEldestEntry(Map.Entry<String, byte[]> eldest) {
        return size() > 1000;  // evict oldest entry when over 1000
    }
};
```

### Fix 4: Close resources properly with try-with-resources

```java
// Wrong — resource leak if exception occurs
FileInputStream fis = new FileInputStream("data.bin");
byte[] buffer = fis.readAllBytes();
fis.close();  // never reached if readAllBytes throws

// Correct — try-with-resources guarantees cleanup
try (FileInputStream fis = new FileInputStream("data.bin")) {
    byte[] buffer = fis.readAllBytes();
}  // fis.close() is called automatically, even on exception
```

### Fix 5: Process data in streaming fashion instead of loading all at once

```java
// Wrong — loads entire file into memory
List<String> lines = Files.readAllLines(Path.of("huge.csv"));
for (String line : lines) {
    process(line);
}

// Correct — stream lines one at a time
try (Stream<String> lines = Files.lines(Path.of("huge.csv"))) {
    lines.forEach(this::process);
}
```

### Fix 6: Use WeakReference and SoftReference for caches

```java
// SoftReference — GC will reclaim only when memory is low
Map<String, SoftReference<byte[]>> cache = new HashMap<>();

// WeakReference — GC will reclaim as soon as no strong references remain
Map<String, WeakReference<Object>> weakCache = new HashMap<>();

// Usage
byte[] data = new byte[1024];
cache.put("key", new SoftReference<>(data));

SoftReference<byte[]> ref = cache.get("key");
byte[] retrieved = ref != null ? ref.get() : null;  // may be null if GC'd
```

## Monitoring and Diagnosis

```bash
# Check current heap usage at runtime
jcmd <PID> GC.heap_info

# Watch heap usage over time
jstat -gcutil <PID> 1000

# Print GC activity to console
java -verbose:gc -XX:+PrintGCDetails -jar myapp.jar

# Use JFR (Java Flight Recorder) for comprehensive profiling
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar myapp.jar
```

## Related Errors

- [StackOverflowError](stackoverflowerror) — stack memory exhausted from deep recursion.
- [GC Overhead Limit Exceeded](#) — JVM spends too much time in garbage collection.
- [Direct Buffer Memory](#) — off-heap native memory exhausted.
