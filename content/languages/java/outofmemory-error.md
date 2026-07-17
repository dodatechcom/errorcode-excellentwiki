---
title: "[Solution] Java OutOfMemoryError: Java Heap Space Fix"
description: "Fix Java OutOfMemoryError: Java heap space. Increase JVM memory with -Xmx, fix memory leaks, use bounded caches, and process data in streaming fashion."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# OutOfMemoryError: Java Heap Space

An `OutOfMemoryError: Java heap space` is thrown when the JVM cannot allocate enough memory for a new object because the heap is full and garbage collection cannot free sufficient space. This is an `Error` (not an `Exception`), meaning the JVM considers it unrecoverable.

## Description

The JVM heap stores all object instances. When the heap fills up and GC can't reclaim enough space, the OOME fires. The default heap size varies by JVM but is typically 256MB-1GB.

Common variants:

- `OutOfMemoryError: Java heap space` — heap is full
- `OutOfMemoryError: Metaspace` — class metadata exhausted (Java 8+)
- `OutOfMemoryError: GC overhead limit exceeded` — GC spent >98% time reclaiming <2% memory
- `OutOfMemoryError: Direct buffer memory` — native off-heap memory exhausted

## Common Causes

```java
// Cause 1: Unbounded collection growth
List<byte[]> data = new ArrayList<>();
while (true) {
    data.add(new byte[1024 * 1024]);  // adds 1MB each iteration
}

// Cause 2: Cache without eviction
Map<String, Object> cache = new HashMap<>();
while (scanner.hasNext()) {
    cache.put(scanner.next(), loadObject(scanner.next()));  // never evicts
}

// Cause 3: Large array allocation
byte[] hugeArray = new byte[Integer.MAX_VALUE];  // ~2GB

// Cause 4: Memory leak via static reference
static List<Object> leak = new ArrayList<>();
public void addItem(Object o) {
    leak.add(o);  // objects never GC'd
}

// Cause 5: Unclosed resources
FileInputStream fis = new FileInputStream("huge.log");
// fis is never closed — memory and file descriptors leak
```

## How to Fix

### Fix 1: Increase JVM heap size

```bash
# Default is often 256MB — increase it
java -Xms512m -Xmx4g -jar myapp.jar

# For large data processing
java -Xms2g -Xmx8g -jar myapp.jar

# For Docker containers
java -Xms2g -Xmx4g -jar myapp.jar
```

### Fix 2: Enable heap dump on OOM for diagnosis

```bash
java -XX:+HeapDumpOnOutOfMemoryError \
     -XX:HeapDumpPath=/tmp/heapdump.hprof \
     -jar myapp.jar

# Analyze with Eclipse MAT or VisualVM
# Look for "Leak Suspects" report
```

### Fix 3: Use bounded caches with eviction

```java
// Wrong — unbounded cache
Map<String, byte[]> cache = new HashMap<>();

// Correct — LRU cache with max size
Map<String, byte[]> cache = new LinkedHashMap<>(1000, 0.75f, true) {
    @Override
    protected boolean removeEldestEntry(Map.Entry<String, byte[]> eldest) {
        return size() > 1000;
    }
};
```

### Fix 4: Close resources properly with try-with-resources

```java
// Wrong — resource leak
FileInputStream fis = new FileInputStream("data.bin");
byte[] buffer = fis.readAllBytes();
fis.close();  // never reached if readAllBytes throws

// Correct — auto-closed
try (FileInputStream fis = new FileInputStream("data.bin")) {
    byte[] buffer = fis.readAllBytes();
}
```

### Fix 5: Process data in streaming fashion

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
// SoftReference — GC reclaims only when memory is low
Map<String, SoftReference<byte[]>> cache = new HashMap<>();

// WeakReference — GC reclaims as soon as no strong references remain
Map<String, WeakReference<Object>> weakCache = new HashMap<>();
```

## Monitoring and Diagnosis

```bash
# Check current heap usage
jcmd <PID> GC.heap_info

# Watch heap over time
jstat -gcutil <PID> 1000

# Use JFR for comprehensive profiling
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar myapp.jar
```

## Related Errors

- [StackOverflowError](stackoverflow-error) — stack memory exhausted from deep recursion
- [GC Overhead Limit Exceeded](#) — JVM spends too much time in garbage collection
- [Direct Buffer Memory](#) — off-heap native memory exhausted
