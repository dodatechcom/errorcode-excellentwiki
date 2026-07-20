---
title: "[Solution] Java ServiceConfigurationError — ServiceLoader Provider Failure"
description: "Fix Java ServiceConfigurationError by correcting META-INF/services files, verifying provider classes, and resolving classpath issues."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 42
---

# ServiceConfigurationError — ServiceLoader Provider Failure

A `ServiceConfigurationError` is thrown when the Java ServiceLoader mechanism fails to locate, load, or instantiate a service provider. This error commonly occurs during application startup or when using the SPI (Service Provider Interface) pattern. It signals a configuration or deployment problem rather than a runtime bug — the provider class referenced in the configuration cannot be used as intended.

## Description

Java's `ServiceLoader` (introduced in Java 6) locates implementations of a service by reading `META-INF/services/<interface-name>` files. When something goes wrong in this process — a missing file, a class that cannot be found, a constructor that throws an exception — `ServiceConfigurationError` is thrown. It extends `Error`, not `Exception`, because a broken service configuration is considered unrecoverable.

Common message variants:

- `ServiceConfigurationError: <provider> Provider <class> not found` — classpath issue.
- `ServiceConfigurationError: <provider> <class>: java.lang.InstantiationException` — no-arg constructor missing or throws.
- `ServiceConfigurationError: <provider> <class>: java.lang.ClassNotFoundException` — class not on classpath.
- `ServiceConfigurationError: <provider> <class>: java.lang.IllegalAccessException` — class is not public.

## Common Causes

```java
// Cause 1: META-INF/services file references a non-existent class
// File: META-INF/services/com.example.LoggerFactory
// Contains: com.example.Log4jLogger  (class doesn't exist on classpath)
ServiceLoader<LoggerFactory> loader = ServiceLoader.load(LoggerFactory.class);
for (LoggerFactory factory : loader) {  // ServiceConfigurationError
    // never reached
}

// Cause 2: Provider class is not public
// com.example.MyLogger is package-private
public class MyLogger implements LoggerFactory { }  // WRONG: missing 'public'
// Should be:
public class MyLogger implements LoggerFactory { }  // CORRECT

// Cause 3: Provider has no no-arg constructor
public class ConfiguredLogger implements LoggerFactory {
    public ConfiguredLogger(String name) { }  // no no-arg constructor!
}
ServiceLoader.load(LoggerFactory.class);  // ServiceConfigurationError

// Cause 4: Provider constructor throws an exception
public class BrokenLogger implements LoggerFactory {
    public BrokenLogger() {
        throw new RuntimeException("Init failed");  // propagates as ServiceConfigurationError
    }
}

// Cause 5: Duplicate entries in META-INF/services file
// File: META-INF/services/com.example.LoggerFactory
// Contains:
// com.example.LoggerA
// com.example.LoggerA  (duplicate — causes confusion or error)
```

## Solutions

### Fix 1: Verify META-INF/services file structure

```
# Correct file path and format:
src/main/resources/META-INF/services/com.example.LoggerFactory

# File contents — one fully qualified class name per line:
com.example.Log4jLogger
com.example.Slf4jLogger
```

```bash
# Validate the file exists and is in the right location
find . -name "com.example.LoggerFactory" -path "*/META-INF/services/*"

# Check for trailing whitespace or BOM characters
xxd META-INF/services/com.example.LoggerFactory | head -5
```

### Fix 2: Ensure provider classes are public with no-arg constructors

```java
// BEFORE (broken): class is package-private, no no-arg constructor
class MyProvider implements MyService {
    MyProvider(String config) { }  // private constructor
}

// AFTER (correct): public class with public no-arg constructor
public class MyProvider implements MyService {
    public MyProvider() { }

    @Override
    public void execute() {
        // implementation
    }
}
```

### Fix 3: Check classpath for provider classes at startup

```java
public class ServiceValidator {
    public static void validateServiceProviders(Class<?> serviceInterface) {
        try {
            ServiceLoader<?> loader = ServiceLoader.load(serviceInterface);
            loader.forEach(provider -> {
                System.out.println("Loaded provider: "
                    + provider.getClass().getName());
            });
        } catch (ServiceConfigurationError e) {
            System.err.println("Service configuration error for "
                + serviceInterface.getName() + ": " + e.getMessage());
            // Log the full cause chain
            e.printStackTrace();
            throw e;  // fail fast on startup
        }
    }
}

// Use at application bootstrap
ServiceValidator.validateServiceProviders(MyService.class);
```

### Fix 4: Handle duplicate providers in META-INF/services

```java
// ServiceLoader loads ALL listed providers, including duplicates
// Deduplicate manually if needed
ServiceLoader<MyService> loader = ServiceLoader.load(MyService.class);
Set<String> seen = new HashSet<>();
for (MyService provider : loader) {
    String name = provider.getClass().getName();
    if (!seen.add(name)) {
        System.out.println("Skipping duplicate provider: " + name);
        continue;
    }
    // use provider
}
```

### Fix 5: Debug service loading with system property

```bash
# Enable ServiceLoader debug output
java -Djava.util.ServiceLoader=debug -jar myapp.jar

# This prints which files are read and which classes are loaded
# Useful for diagnosing classpath and configuration issues
```

```java
// Or use the module system (Java 9+) for explicit exports
// In module-info.java:
// module myapp {
//     uses com.example.MyService;
//     provides com.example.MyService with com.example.MyProvider;
// }
```

## Prevention Checklist

- Always place `META-INF/services/<interface-name>` files in `src/main/resources/`.
- Ensure every provider class is `public` with a `public` no-arg constructor.
- Validate service configurations during build or at application startup.
- Use `module-info.java` (Java 9+) for explicit service declarations instead of META-INF/services.
- Write integration tests that actually load and instantiate providers via ServiceLoader.

## Related Errors

- [ClassNotFoundException](../classnotfoundexception) — class not found on classpath (related but distinct).
- [NoClassDefFoundError](../noclassdeffounderror) — JVM cannot find a class that was available at compile time.
- [InstantiationException](../instantiationexception) — reflection cannot instantiate a class (no no-arg constructor).
- [IllegalAccessException](../illegalaccessexception) — cannot access a class or constructor due to visibility rules.
