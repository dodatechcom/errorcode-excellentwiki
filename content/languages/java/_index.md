---
title: "[Solution] Java Exceptions & Errors — Complete Reference"
description: "Find solutions for Java exceptions including NullPointerException, ClassNotFoundException, and OutOfMemoryError. Copy-paste fixes."
languages: ["java"]
---

Java exceptions are split into checked exceptions (which you must handle) and unchecked `RuntimeException`s (which are programming bugs). On top of that, the JVM itself can throw `Error` subtypes like `OutOfMemoryError` that signal unrecoverable problems. Each entry below covers the most common Java exceptions with fixes you can apply immediately.

## Error Codes

| Error | Description | Fix |
|-------|-------------|-----|
| [NullPointerException](/languages/java/nullpointerexception/) | Dereferencing `null` before calling a method or accessing a field | Add null checks, use `Optional`, and apply `Objects.requireNonNull()` for validation |
| [ClassNotFoundException](/languages/java/classnotfoundexception/) | Class cannot be found at runtime — missing from classpath or build output | Verify classpath, check JAR files, confirm Maven/Gradle dependencies, and inspect classloaders |
| [ClassCastException](/languages/java/classcastexception/) | Object cannot be cast to the specified type — invalid type conversion | Use `instanceof` before casting, apply generics, and use safe casting patterns |
| [OutOfMemoryError](/languages/java/outofmemoryerror/) | JVM heap space exhausted — application cannot allocate more memory | Increase heap with `-Xmx`, fix memory leaks, and profile with VisualVM or MAT |
| [StackOverflowError](/languages/java/stackoverflowerror/) | Infinite recursion or excessively deep call stack | Add a base case to recursive methods, convert to iteration, or increase `-Xss` stack size |

## Quick Debug

```bash
# Enable verbose class loading
java -verbose:class -jar myapp.jar

# Get a thread dump on a running JVM
jstack <PID>
```
