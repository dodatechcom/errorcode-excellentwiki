---
title: "[Solution] ExtensionConfigurationException — JUnit 5 Extension Fix"
description: "Fix ExtensionConfigurationException in JUnit 5. Resolve extension registration errors and incompatible extension issues."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ExtensionConfigurationException — JUnit 5 Extension Fix

An `ExtensionConfigurationException` is thrown when JUnit 5 cannot configure or initialize a registered extension. This happens when an extension class cannot be instantiated, has incompatible dependencies, or conflicts with another extension.

## What This Error Means

Common messages:

- `org.junit.jupiter.api.extension.ExtensionConfigurationException`
- `ExtensionConfigurationException: Failed to instantiate extension class`
- `ExtensionConfigurationException: Could not find a suitable constructor`

## Common Causes

```java
// Cause 1: Extension class has no default constructor
public class CustomExtension implements BeforeEachCallback {
    private final String config;
    public CustomExtension(String config) { // No no-arg constructor
        this.config = config;
    }
    @Override
    public void beforeEach(ExtensionContext ctx) { }
}

// Cause 2: Extension depends on bean not available
public class DatabaseExtension implements BeforeAllCallback {
    @Autowired
    private DataSource dataSource; // Not injected in test context
}

// Cause 3: Extension registration order conflict
@ExtendWith({ExtensionA.class, ExtensionB.class})
// Both extensions modify the same lifecycle hook
```

## How to Fix

### Fix 1: Ensure extension has a no-arg constructor or use @RegisterExtension

Provide a default constructor for your extension, or use @RegisterExtension with a factory method for complex initialization.

```java
public class LoggingExtension implements BeforeEachCallback {

    // No-arg constructor required for @ExtendWith
    public LoggingExtension() { }

    @Override
    public void beforeEach(ExtensionContext context) {
        String testName = context.getDisplayName();
        System.out.println("Starting test: " + testName);
    }
}

// Or use @RegisterExtension for programmatic control
class MyTest {

    @RegisterExtension
    static LoggingExtension logging = new LoggingExtension("custom-config");
}
```

### Fix 2: Use ExtensionContext.Store for sharing state between extensions

Use the ExtensionContext.Store API to share state between extension callbacks without using static fields.

```java
public class TimerExtension implements BeforeEachCallback, AfterEachCallback {

    private static final String TIMER_KEY = "testTimer";

    @Override
    public void beforeEach(ExtensionContext context) {
        context.getStore(Namespace.create(TimerExtension.class))
            .put(TIMER_KEY, System.nanoTime());
    }

    @Override
    public void afterEach(ExtensionContext context) {
        long start = context.getStore(
            Namespace.create(TimerExtension.class))
            .remove(TIMER_KEY, Long.class);
        long duration = System.nanoTime() - start;
        System.out.printf("Test %s took %d ms%n",
            context.getDisplayName(), duration / 1_000_000);
    }
}

@ExtendWith(TimerExtension.class)
class UserServiceTest {
    // ...
}
```

### Fix 3: Handle extension loading errors gracefully

Wrap extension initialization in try-catch blocks and provide meaningful error messages.

```java
public class SafeExtension implements BeforeAllCallback {

    private final Object delegate;

    public SafeExtension() {
        try {
            this.delegate = createDelegate();
        } catch (Exception e) {
            throw new ExtensionConfigurationException(
                "Failed to initialize extension: " + e.getMessage(), e);
        }
    }

    private Object createDelegate() {
        // Complex initialization that might fail
        return new Object();
    }

    @Override
    public void beforeAll(ExtensionContext context) {
        if (delegate == null) {
            throw new ExtensionNotInitializedException(
                "Extension delegate was not initialized");
        }
    }
}
```

## Related Errors

- {{< relref "junit5" >}} — JUnit Platform Launcher Error
- {{< relref "junit5-parameterized" >}} — Parameterized Test Error
