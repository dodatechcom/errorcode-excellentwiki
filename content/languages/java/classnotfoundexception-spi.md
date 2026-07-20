---
title: "[Solution] Java ServiceConfigurationError — SPI Provider Not Found Fix"
description: "Fix Java ServiceConfigurationError when SPI provider not found by checking META-INF/services, verifying provider class, and ensuring proper classpath."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# ServiceConfigurationError — SPI Provider Not Found Fix

A `ServiceConfigurationError` is thrown by `ServiceLoader` when the Java SPI (Service Provider Interface) mechanism cannot find, load, or instantiate a provider class listed in `META-INF/services/`. This wraps or precedes `ClassNotFoundException` when the provider class is missing from the classpath.

## Description

The SPI mechanism reads `META-INF/services/<interface-name>` files to discover implementations. Each line in the file is a fully qualified class name of a provider. If the listed class does not exist on the classpath, is not a valid implementation, or its constructor throws, `ServiceConfigurationError` is raised.

Message variants:

- `java.util.ServiceConfigurationError: com.example.spi.PluginProvider: Provider com.example.impl.DefaultProvider not found`
- `java.util.ServiceConfigurationError: com.example.spi.Formatter: Error locating provider`
- `java.util.ServiceConfigurationError: com.example.spi.Plugin: No service found`

## Common Causes

```java
// Cause 1: Provider class not on classpath
// META-INF/services/com.example.spi.PluginProvider contains:
// com.example.impl.DefaultProvider
// But the JAR with DefaultProvider is missing from classpath

// Cause 2: Typo in fully qualified class name in services file
// META-INF/services/com.example.spi.Formatter contains:
// com.example.impl.TxtFormatter  // should be TextFormatter

// Cause 3: Provider class exists but does not implement the service interface
// META-INF/services/com.example.spi.Plugin contains:
// com.example.impl.NotAPlugin  // doesn't implement Plugin interface

// Cause 4: Provider constructor throws an exception
public class MyProvider implements Plugin {
    public MyProvider() {
        throw new RuntimeException("Init failed");  // ServiceConfigurationError
    }
}

// Cause 5: Services file in wrong location or wrong name
// File at META-INF/service/ (missing 's') or wrong path
```

## Solutions

### Fix 1: Verify META-INF/services file structure

```java
// The services file MUST be:
// 1. Named exactly: META-INF/services/<fully.qualified.interface.Name>
// 2. In the root of the JAR (not in a subdirectory)
// 3. Contain one fully qualified class name per line
// 4. UTF-8 encoded (no BOM)

// Check file exists in JAR
try (JarFile jar = new JarFile("mylib.jar")) {
    JarEntry entry = jar.getJarEntry("META-INF/services/com.example.spi.Plugin");
    if (entry == null) {
        System.err.println("Missing services file");
    } else {
        try (InputStream is = jar.getInputStream(entry)) {
            String content = new String(is.readAllBytes(), StandardCharsets.UTF_8);
            System.out.println("Providers: " + content);
        }
    }
}
```

### Fix 2: List and verify provider classes

```java
import java.util.ServiceLoader;
import java.util.ServiceConfigurationError;

public class SpiDiagnostics {
    public static <T> void diagnose(Class<T> serviceInterface) {
        System.out.println("Looking for providers of: " + serviceInterface.getName());

        try {
            ServiceLoader<T> loader = ServiceLoader.load(serviceInterface);
            for (T provider : loader) {
                System.out.println("  Found: " + provider.getClass().getName());
            }
        } catch (ServiceConfigurationError e) {
            System.err.println("SPI Error: " + e.getMessage());
            Throwable cause = e.getCause();
            if (cause instanceof ClassNotFoundException) {
                System.err.println("  Missing class: " + cause.getMessage());
                System.err.println("  Classpath: "
                    + System.getProperty("java.class.path"));
            }
        }
    }
}

// Usage
SpiDiagnostics.diagnose(Plugin.class);
```

### Fix 3: Ensure provider class is on classpath

```bash
# Check that the provider JAR is in the classpath
# Maven — ensure dependency is compile scope
# pom.xml
<dependency>
    <groupId>com.example</groupId>
    <artifactId>my-impl</artifactId>
    <version>1.0</version>
    <scope>compile</scope>  <!-- NOT test or provided -->
</dependency>

# Verify JAR contents
jar tf my-impl-1.0.jar | grep "META-INF/services"
jar tf my-impl-1.0.jar | grep "DefaultProvider"

# List all providers for a service interface
find . -path "*/META-INF/services/com.example.spi.Plugin" -exec cat {} \;
```

### Fix 4: Implement provider with safe constructor

```java
// Right — provider with safe constructor
public class MyProvider implements Plugin {
    public MyProvider() {
        // No exceptions in constructor
        // Defer initialization to a separate init() method if needed
    }

    @Override
    public void execute() {
        // Lazy initialization here
    }
}

// Right — use ServiceLoader with fallback
public static Plugin loadPlugin() {
    ServiceLoader<Plugin> loader = ServiceLoader.load(Plugin.class);
    Iterator<Plugin> iterator = loader.iterator();

    if (iterator.hasNext()) {
        try {
            return iterator.next();
        } catch (ServiceConfigurationError e) {
            System.err.println("Provider failed: " + e.getMessage());
        }
    }

    return new DefaultPlugin();  // fallback
}
```

## Prevention Checklist

- Verify `META-INF/services/` file name matches the interface's fully qualified name.
- Ensure all listed provider classes are on the runtime classpath.
- Provider constructors should not throw exceptions.
- Test `ServiceLoader.load()` during integration tests.
- Use `jar tf` to verify services file exists in built JARs.
- Document SPI requirements in module documentation.

## Related Errors

- [ClassNotFoundException](../classnotfoundexception) — provider class not found
- [NoClassDefFoundError](../noclassdeffounderror) — class missing at runtime
- [ServiceConfigurationError](../serviceconfigurationerror) — general SPI loading error
