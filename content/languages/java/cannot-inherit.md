---
title: "[Solution] Java cannot inherit from final class — Fix Final Class Extension"
description: "Fix Java compiler error 'cannot inherit from final class' by using composition, removing final modifier, or using a wrapper. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 449
---

# Java Compiler Error: cannot inherit from final class

This compile-time error occurs when you try to extend (inherit from) a class declared with the `final` modifier. The `final` keyword on a class prevents subclassing — no class can extend a final class. This is by design for classes like `String`, `Integer`, and other immutable types.

## Error Message

```
error: cannot inherit from final java.lang.String
public class MyString extends String {
                           ^
```

Other variants:

```
error: cannot inherit from final com.example.ImmutableConfig
error: cannot inherit from final class java.lang.Math
```

## Common Causes

### Cause 1: Extending a JDK Final Class

```java
public class MyString extends String { // ERROR: cannot inherit from final java.lang.String
    public String toUpperCase(int limit) {
        return substring(0, Math.min(limit, length())).toUpperCase();
    }
}
```

### Cause 2: Extending a Library Final Class

```java
import com.example.library.ImmutableValue;

public class ExtendedValue extends ImmutableValue { // ERROR: cannot inherit from final class
    private int extra;

    public int getExtra() { return extra; }
}
```

### Cause 3: Extending a Class You Marked Final

```java
public final class Config {
    private String host;
    private int port;

    public String getHost() { return host; }
    public int getPort() { return port; }
}

public class ExtendedConfig extends Config { // ERROR: cannot inherit from final class
    private String apiKey;
}
```

### Cause 4: Extending Enum Types

Enums are implicitly final — you cannot extend them.

```java
enum Color { RED, GREEN, BLUE }

public class ExtendedColor extends Color { // ERROR: cannot inherit from final class
    // ...
}
```

## Solutions

### Fix 1: Use Composition Instead of Inheritance

```java
public class Config {
    private final String host;
    private final int port;

    public Config(String host, int port) {
        this.host = host;
        this.port = port;
    }

    public String getHost() { return host; }
    public int getPort() { return port; }
}

public class ExtendedConfig {
    private final Config config;
    private final String apiKey;

    public ExtendedConfig(Config config, String apiKey) {
        this.config = config;
        this.apiKey = apiKey;
    }

    public String getHost() { return config.getHost(); }
    public int getPort() { return config.getPort(); }
    public String getApiKey() { return apiKey; }
}
```

### Fix 2: Remove the final Modifier (If You Own the Class)

```java
public class Config { // removed 'final'
    private String host;
    private int port;

    public String getHost() { return host; }
    public int getPort() { return port; }
}

public class ExtendedConfig extends Config {
    private String apiKey;
    public String getApiKey() { return apiKey; }
}
```

### Fix 3: Create a Wrapper/Decorator Pattern

```java
public interface StringOperations {
    String toUpperCase(int limit);
    int countWords();
}

public class StringWrapper implements StringOperations {
    private final String value;

    public StringWrapper(String value) { this.value = value; }

    @Override
    public String toUpperCase(int limit) {
        return value.substring(0, Math.min(limit, value.length())).toUpperCase();
    }

    @Override
    public int countWords() {
        return value.trim().isEmpty() ? 0 : value.trim().split("\\s+").length;
    }

    public String getValue() { return value; }
}
```

### Fix 4: Use a Utility Class

```java
public final class StringUtils {
    private StringUtils() {} // private constructor

    public static String toUpperCase(String value, int limit) {
        return value.substring(0, Math.min(limit, value.length())).toUpperCase();
    }

    public static int countWords(String value) {
        return value.trim().isEmpty() ? 0 : value.trim().split("\\s+").length;
    }
}
```

## Prevention Checklist

- Prefer composition over inheritance for extension points
- Only mark a class `final` if you have a good reason (security, immutability guarantee)
- When designing APIs, consider whether users might need to extend your classes
- Use interfaces to define extensible contracts instead of allowing class inheritance
- Review library classes for `final` before assuming you can extend them
- Consider decorator or wrapper patterns when you need to add behavior to final classes

## Related Errors

- [anonymous class cannot extend final class (anonymous-class-cannot-extend)](/languages/java/anonymous-class-cannot-extend)
- [incompatible types (incompatible-types)](/languages/java/incompatible-types)
- [method does not override or implement a method from a supertype (override-methods)](/languages/java/override-methods)
