---
title: "[Solution] Java Deprecated APIs — Migration Guide & Replacements"
description: "Java deprecated API migration guides. Replace Thread.stop, Date methods, and more with modern Java equivalents. Code examples."
deprecated: ["java"]
---

The JDK uses the `@Deprecated` annotation to flag APIs that should no longer be used. Some are deprecated for removal in a future release, while others are permanently deprecated to preserve backward compatibility. Each entry below covers the most important JDK deprecations with concrete replacement code.

## Deprecated APIs

| Deprecated | Description | Replacement |
|------------|-------------|-------------|
| [Thread.stop()](/deprecated/java/thread-stop/) | Permanently deprecated — causes inconsistent object state and deadlock | Use `Thread.interrupt()` and `java.util.concurrent` coordination patterns |
| [Date.getYear() / getMonth()](/deprecated/java/date-methods/) | Deprecated since JDK 1.1 — confusing 1900-based year and 0-based month | Migrate to `java.time.LocalDate`, `LocalDateTime`, and `Instant` |

## Quick Check

```bash
# Show all deprecation warnings during compilation
javac -Xlint:deprecation -d out src/**/*.java

# Or with Maven
mvn compile -Dmaven.compiler.showDeprecation=true
```
