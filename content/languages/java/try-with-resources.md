---
title: "[Solution] Java try-with-resources is not applicable to variable type — Fix AutoCloseable"
description: "Fix Java compiler error 'try-with-resources is not applicable to variable type' by implementing AutoCloseable, using finally block, or wrapping the resource. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 415
---

# Java Compiler Error: try-with-resources is not applicable to variable type

This compile-time error occurs when you try to use a variable in a try-with-resources statement, but its type doesn't implement `AutoCloseable` (or `Closeable`). The try-with-resources feature (Java 7+) requires resources to be `AutoCloseable` so they can be automatically closed after use.

## Error Message

```
error: try-with-resources is not applicable to variable type MyResource
        try (MyResource r = new MyResource()) {
                  ^
    (resource type must implement java.lang.AutoCloseable)
```

Other variants:

```
error: in a try-with-resources statement, resource type must implement AutoCloseable
error: try-with-resources is not applicable to variable type
```

## Common Causes

### Cause 1: Class Doesn't Implement AutoCloseable

```java
class MyResource {
    void use() { System.out.println("Using resource"); }
}

public void process() {
    try (MyResource r = new MyResource()) { // ERROR: not AutoCloseable
        r.use();
    }
}
```

### Cause 2: Using Non-Closeable Objects

```java
public void process() {
    try (StringBuilder sb = new StringBuilder()) { // ERROR: StringBuilder is not AutoCloseable
        sb.append("hello");
    }
}
```

### Cause 3: Collection or Stream Used as Resource

```java
public void process() {
    try (List<String> list = List.of("a", "b")) { // ERROR: List is not AutoCloseable
        System.out.println(list);
    }
}
```

### Cause 4: Third-Party Library Class

```java
public void process() {
    try (ThirdPartyService svc = serviceFactory.create()) { // ERROR if not AutoCloseable
        svc.doWork();
    }
}
```

### Cause 5: Wrong Import or Type

```java
// Using java.io.InputStream (AutoCloseable) correctly
// vs using a custom InputStream-like class that isn't AutoCloseable
public void process() {
    try (CustomStream cs = getStream()) { // ERROR if CustomStream doesn't implement AutoCloseable
        cs.read();
    }
}
```

## Solutions

### Fix 1: Implement AutoCloseable on Your Class

```java
class MyResource implements AutoCloseable {
    void use() { System.out.println("Using resource"); }

    @Override
    public void close() {
        System.out.println("Resource closed");
    }
}

public void process() {
    try (MyResource r = new MyResource()) { // OK
        r.use();
    }
}
```

### Fix 2: Use a Finally Block

For classes that can't implement `AutoCloseable`, use try-finally.

```java
MyResource r = null;
try {
    r = new MyResource();
    r.use();
} finally {
    if (r != null) {
        r.cleanup(); // manual cleanup
    }
}
```

### Fix 3: Wrap in an AutoCloseable Wrapper

```java
class CloseableAdapter implements AutoCloseable {
    private final Object resource;
    private final Runnable cleanup;

    CloseableAdapter(Object resource, Runnable cleanup) {
        this.resource = resource;
        this.cleanup = cleanup;
    }

    @Override
    public void close() {
        cleanup.run();
    }

    Object get() { return resource; }
}

public void process() {
    MyResource raw = new MyResource();
    try (CloseableAdapter wrapped = new CloseableAdapter(raw, raw::cleanup)) {
        ((MyResource) wrapped.get()).use();
    }
}
```

### Fix 4: Use Standard Closeable Types

Prefer standard library types that already implement `AutoCloseable`.

```java
// Good — standard AutoCloseable types
try (InputStream is = new FileInputStream("file.txt");
     BufferedReader br = new BufferedReader(new InputStreamReader(is))) {
    String line = br.readLine();
} catch (IOException e) {
    e.printStackTrace();
}
```

### Fix 5: Implement Closeable Interface

`Closeable` extends `AutoCloseable` with a more specific `close()` contract.

```java
class MyResource implements Closeable {
    void use() { System.out.println("Using resource"); }

    @Override
    public void close() throws IOException {
        System.out.println("Resource closed");
    }
}
```

## Prevention Checklist

- Always implement `AutoCloseable` on classes that manage resources
- Provide a meaningful `close()` method that releases all held resources
- Implement `Closeable` (extends `AutoCloseable`) for IO-related resources
- Use try-with-resources for all `AutoCloseable` resources — it's safer than try-finally
- When wrapping third-party classes, create an `AutoCloseable` adapter
- Check the class hierarchy if a type seems like it should be closeable but isn't

## Related Errors

- [NullPointerException in try-with-resources (npe-try-resources)](/languages/java/npe-try-resources)
- [non-static method cannot be referenced from a static context (non-static-method)](/languages/java/non-static-method)
- [X is abstract; cannot be instantiated (abstract-method)](/languages/java/abstract-method)
