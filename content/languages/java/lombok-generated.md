---
title: "[Solution] Java Lombok generated method conflicts — Fix Lombok Method Already Defined"
description: "Fix Java compiler error 'method X is already defined' from Lombok-generated methods by checking annotations, renaming conflicting methods, or excluding from Lombok processing. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 461
---

# Java Compiler Error: Lombok generated method conflicts

This compile-time error occurs when Lombok generates a method that conflicts with an existing method in your class. Lombok annotations like `@Data`, `@Getter`, `@Setter`, `@Builder`, and `@AllArgsConstructor` automatically generate methods — if you've already defined a method with the same name and signature, the compiler reports a duplicate.

## Error Message

```
error: method getName() is already defined in class User
```

Other variants:

```
error: method setName(String) is already defined in class User
error: name clash: getName() and getName() have the same erasure
error: Lombok annotation processor generated method that conflicts with existing method
```

## Common Causes

### Cause 1: Manual Getter/Setter With @Getter/@Setter

```java
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class User {
    private String name;

    public String getName() { // ERROR: Lombok already generates getName()
        return name.toUpperCase();
    }
}
```

### Cause 2: @Data Conflicts With Manual toString()

```java
import lombok.Data;

@Data
public class User {
    private String name;

    @Override
    public String toString() { // ERROR: @Data generates toString()
        return "User: " + name;
    }
}
```

### Cause 3: @AllArgsConstructor Conflicts With Existing Constructor

```java
import lombok.AllArgsConstructor;

@AllArgsConstructor
public class User {
    private String name;
    private int age;

    public User(String name, int age) { // ERROR: @AllArgsConstructor generates this
        this.name = name;
        this.age = age;
        validate();
    }
}
```

### Cause 4: @Builder Generates Conflicting Methods

```java
import lombok.Builder;

@Builder
public class User {
    private String name;

    public static UserBuilder builder() { // ERROR: @Builder generates builder()
        return new UserBuilder();
    }
}
```

### Cause 5: Multiple Lombok Annotations Generate Conflicting Methods

```java
import lombok.Data;
import lombok.experimental.Accessors;

@Data
@Accessors(fluent = true)
public class User {
    private String name;
    // @Accessors(fluent = true) generates name() — conflicts if you define name()
}
```

## Solutions

### Fix 1: Remove the Duplicate Manual Method

```java
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class User {
    private String name;

    // Remove the manual getName() — let Lombok generate it
    // Or use a different method name:
    public String getNameUpper() {
        return name.toUpperCase();
    }
}
```

### Fix 2: Disable Lombok Generation for That Element

```java
import lombok.AccessLevel;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class User {
    @Getter(AccessLevel.NONE) // disable getter generation for this field
    private String name;

    public String getName() { // now you can define your own
        return name.toUpperCase();
    }
}
```

### Fix 3: Rename the Manual Method

```java
import lombok.Data;

@Data
public class User {
    private String name;

    public String getDisplayName() { // different name — no conflict
        return "User: " + name;
    }
}
```

### Fix 4: Exclude Lombok Processing for the Class

```java
import lombok.experimental.Tolerate;

public class User {
    private String name;

    @Tolerate // tells Lombok to tolerate the existing method
    public String getName() {
        return name.toUpperCase();
    }
}
```

### Fix 5: Use @SuperBuilder for Complex Hierarchies

```java
import lombok.Builder;
import lombok.SuperBuilder;

@SuperBuilder
public class User {
    private String name;
    private int age;

    // Remove manual builder() — let @SuperBuilder handle it
}
```

## Prevention Checklist

- Check which methods Lombok generates before defining manual versions
- Use `@Getter(AccessLevel.NONE)` and `@Setter(AccessLevel.NONE)` to disable generation for specific fields
- Use `@Tolerate` when you need both Lombok-generated and manual methods
- Review Lombok documentation for each annotation's generated methods
- Use IDE Lombok plugin to see generated methods in the class view
- Avoid mixing `@Data` with manual `toString()`, `equals()`, or `hashCode()`

## Related Errors

- [method is already defined in class (method-overload)](/languages/java/method-overload)
- [Lombok annotation processing error (lombok)](/languages/java/lombok)
- [name clash — erasure causes duplicate JVM signatures (name-clash)](/languages/java/name-clash)
