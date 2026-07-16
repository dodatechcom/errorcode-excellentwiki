---
title: "[Solution] Java finalize() Deprecated — Use try-with-resources / Cleaner"
description: "Replace deprecated Object.finalize() with try-with-resources, AutoCloseable, and java.lang.ref.Cleaner in Java. Deterministic cleanup patterns."
deprecated_function: "Object.finalize"
replacement_function: "try-with-resources / Cleaner"
languages: ["java"]
deprecated_since: "JDK 9"
error_message: "Finalizers are deprecated"
tags: ["finalize", "cleaner", "try-with-resources", "autocloseable", "memory"]
weight: 130
---

# [Solution] Java finalize() Deprecated — Use try-with-resources / Cleaner

The `Object.finalize()` method was deprecated in JDK 9 because it is unreliable, slow, and can lead to resource leaks, resurrection of objects, and performance degradation. The Java documentation strongly recommends using `try-with-resources` with `AutoCloseable` for deterministic cleanup, or `java.lang.ref.Cleaner` (introduced in JDK 9) for non-deterministic cleanup when you cannot use try-with-resources. Finalizers are not guaranteed to run promptly — or at all — before the JVM exits.

## What You'll See

Using `finalize()` triggers a deprecation warning:

```
Warning: The method Object.finalize() is deprecated
```

In newer JDK versions, the message is:

```
Note: /path/to/MyClass.java uses or overrides a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
```

## Why Deprecated

`finalize()` was deprecated because:

- **Non-deterministic**: The garbage collector decides when (or whether) to call `finalize()`. You cannot predict when cleanup will happen.
- **Performance**: Objects with finalizers are placed in a finalization queue, which adds overhead to every garbage collection cycle.
- **Resurrection**: Calling `this` inside `finalize()` can resurrect the object, causing it to escape garbage collection.
- **Security risk**: Finalizers can be overridden by subclasses, creating unpredictable behavior in security-sensitive contexts.
- **No ordering guarantee**: Multiple finalizers may run in any order, making resource dependencies dangerous.

## Old Code (Deprecated)

```java
public class DatabaseConnection implements AutoCloseable {
    private Connection conn;

    public DatabaseConnection(String url) throws SQLException {
        this.conn = DriverManager.getConnection(url);
    }

    // DEPRECATED — unreliable cleanup
    @Override
    protected void finalize() throws Throwable {
        try {
            if (conn != null && !conn.isClosed()) {
                conn.close();
            }
        } finally {
            super.finalize();
        }
    }

    @Override
    public void close() throws SQLException {
        if (conn != null && !conn.isClosed()) {
            conn.close();
        }
    }
}
```

## New Code — try-with-resources (Recommended)

```java
public class DatabaseConnection implements AutoCloseable {
    private Connection conn;
    private boolean closed = false;

    public DatabaseConnection(String url) throws SQLException {
        this.conn = DriverManager.getConnection(url);
    }

    public Connection getConnection() {
        if (closed) {
            throw new IllegalStateException("Connection is closed");
        }
        return conn;
    }

    @Override
    public void close() throws SQLException {
        if (!closed) {
            closed = true;
            if (conn != null) {
                conn.close();
                System.out.println("Database connection closed");
            }
        }
    }
}

// Usage — guaranteed cleanup even if an exception occurs
try (DatabaseConnection db = new DatabaseConnection("jdbc:mysql://localhost/mydb")) {
    Connection conn = db.getConnection();
    PreparedStatement stmt = conn.prepareStatement("SELECT * FROM users");
    ResultSet rs = stmt.executeQuery();
    // Process results...
}  // close() is automatically called here, even on exception
```

## New Code — java.lang.ref.Cleaner (JDK 9+)

```java
import java.lang.ref.Cleaner;

public class NativeResource implements AutoCloseable {
    private static final Cleaner cleaner = Cleaner.create();
    private final Cleaner.Cleanable cleanable;

    // Cleaning action — must NOT reference the enclosing object
    private static class CleaningAction implements Runnable {
        private final long nativePointer;

        CleaningAction(long nativePointer) {
            this.nativePointer = nativePointer;
        }

        @Override
        public void run() {
            // Release native resources outside the object
            System.out.println("Cleaning native resource: " + nativePointer);
            freeNative(nativePointer);  // call JNI cleanup
        }
    }

    private long nativePointer;

    public NativeResource() {
        this.nativePointer = allocateNative();
        this.cleanable = cleaner.register(this, new CleaningAction(nativePointer));
    }

    public void use() {
        if (nativePointer == 0) {
            throw new IllegalStateException("Resource is closed");
        }
        System.out.println("Using native resource: " + nativePointer);
    }

    @Override
    public void close() {
        cleanable.clean();  // explicit cleanup
    }

    // Native methods (stubs)
    private static long allocateNative() { return 12345L; }
    private static void freeNative(long ptr) { /* JNI call */ }
}
```

## New Code — try-with-resources with Multiple Resources

```java
public class FileProcessor implements AutoCloseable {
    private final BufferedReader reader;
    private final BufferedWriter writer;
    private int linesProcessed = 0;

    public FileProcessor(String inputPath, String outputPath) throws IOException {
        this.reader = new BufferedReader(new FileReader(inputPath));
        this.writer = new BufferedWriter(new FileWriter(outputPath));
    }

    public void processAll() throws IOException {
        String line;
        while ((line = reader.readLine()) != null) {
            writer.write(line.toUpperCase());
            writer.newLine();
            linesProcessed++;
        }
    }

    @Override
    public void close() throws IOException {
        System.out.println("Processed " + linesProcessed + " lines");
        // Close in reverse order of opening
        try {
            writer.close();
        } finally {
            reader.close();
        }
    }

    // Usage — both resources are closed automatically
    public static void convertFile(String input, String output) throws IOException {
        try (FileProcessor processor = new FileProcessor(input, output)) {
            processor.processAll();
        }
    }
}
```

## Migration Steps

1. **Find all finalize overrides**:

```bash
grep -rn "finalize\s*(" --include="*.java" /path/to/project/
```

2. **Implement `AutoCloseable`** on any class that overrides `finalize()`.

3. **Move cleanup logic from `finalize()` to `close()`**.

4. **Replace `new Resource()` patterns with try-with-resources**:

```java
// Before
Resource res = new Resource();
try {
    res.doWork();
} finally {
    res.close();
}

// After
try (Resource res = new Resource()) {
    res.doWork();
}
```

5. **For native resources that cannot use try-with-resources**, use `java.lang.ref.Cleaner` as a safety net.

6. **Remove the `finalize()` override** after migration is complete.

7. **Compile with `-Xlint:deprecation`** to find remaining issues:

```bash
javac -Xlint:deprecation src/**/*.java
```

## When to Use Each Approach

| Approach | When to Use |
|---|---|
| `try-with-resources` | Any `AutoCloseable` resource — the preferred approach |
| `Cleaner` | Safety net for non-deterministic cleanup (native memory, file handles) |
| `PhantomReference` | Custom cleanup queues with fine-grained control |
| Never use `finalize()` | It is deprecated and unreliable in all cases |

## Related Errors

- [Thread.stop() deprecated](thread-stop) — another deprecated Java API.
- [date() deprecated](date-methods) — deprecated Date methods.
