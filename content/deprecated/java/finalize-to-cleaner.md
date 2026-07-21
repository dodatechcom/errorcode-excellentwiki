---
title: "[Solution] Deprecated Function Migration: finalize() to try-with-resources"
description: "Migrate from deprecated Object.finalize() to try-with-resources or java.lang.ref.Cleaner."
deprecated_function: "finalize()"
replacement_function: "try-with-resources / Cleaner"
languages: ["java"]
deprecated_since: "Java 9+"
---

# [Solution] Deprecated Function Migration: finalize() to try-with-resources

The `finalize()` has been deprecated in favor of `try-with-resources / Cleaner`.

## Migration Guide

finalize() is unpredictable and has performance issues. Use try-with-resources for AutoCloseable objects.

## Before (Deprecated)

```java
public class Resource {
    private long handle;

    public Resource() {
        handle = allocateResource();
    }

    @Override
    protected void finalize() throws Throwable {
        try {
            releaseResource(handle);
        } finally {
            super.finalize();
        }
    }
}
```

## After (Modern)

```java
public class Resource implements AutoCloseable {
    private long handle;

    public Resource() {
        handle = allocateResource();
    }

    @Override
    public void close() {
        releaseResource(handle);
    }
}

// Usage
try (Resource r = new Resource()) {
    r.use();
}
```

## Key Differences

- finalize() deprecated since Java 9
- try-with-resources is preferred
- Cleaner for non-closeable resources
- finalize causes extra GC cycles
