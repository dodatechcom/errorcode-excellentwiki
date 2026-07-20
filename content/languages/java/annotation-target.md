---
title: "[Solution] Java annotation X is not applicable to this type of declaration — Fix Annotation Target"
description: "Fix Java compiler error 'annotation X is not applicable to this type of declaration' by checking @Target meta-annotation, verifying annotation usage, and using the correct element type. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 457
---

# Java Compiler Error: annotation X is not applicable to this type of declaration

This compile-time error occurs when you use an annotation on a Java element (class, method, field, parameter, etc.) that the annotation's `@Target` meta-annotation does not allow. Each annotation declares where it can be used through its `@Target` value.

## Error Message

```
error: annotation @Override is not applicable to a field declaration
    @Override
    private String name;
    ^
```

Other variants:

```
error: annotation @Test is not applicable to a type declaration
error: annotation @FunctionalInterface is not applicable to a method
error: annotation X is not applicable to this type of declaration
```

## Common Causes

### Cause 1: Using Method Annotation on a Field

```java
public class Example {
    @Override  // ERROR: @Override is only for methods, not fields
    private String name;
}
```

### Cause 2: Using Class Annotation on a Method

```java
import java.lang.annotation.ElementType;
import java.lang.annotation.Target;

@Target(ElementType.TYPE)
public @interface MyAnnotation {}

public class Example {
    @MyAnnotation  // ERROR: @MyAnnotation targets TYPE, not METHOD
    public void doSomething() {}
}
```

### Cause 3: Using Field Annotation on a Parameter

```java
public class Example {
    public void process(@NonNull String input) { // ERROR: if @NonNull targets FIELD only
    }
}
```

### Cause 4: Using @Target(RUNTIME) Incorrectly

```java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)
public @interface RuntimeAnnotation {
    // Missing @Target — defaults to all element types
}
```

### Cause 5: Annotation Targets Only Specific Declarations

```java
import java.lang.annotation.ElementType;
import java.lang.annotation.Target;

@Target({ElementType.METHOD, ElementType.CONSTRUCTOR})
public @interface Injectable {}

public class Service {
    @Injectable  // OK — targets METHOD
    public void init() {}
}

public class Wrong {
    @Injectable  // ERROR: targets METHOD/CONSTRUCTOR, not TYPE
    public class Inner {}
}
```

## Solutions

### Fix 1: Check the Annotation's @Target and Use Correct Element

```java
import java.lang.annotation.ElementType;
import java.lang.annotation.Target;

@Target(ElementType.METHOD)
public @interface OnlyMethods {}

public class Example {
    @OnlyMethods  // OK — used on a method
    public void doWork() {}

    // @OnlyMethods
    // private String field; // ERROR — not applicable to fields
}
```

### Fix 2: Broaden the Annotation's @Target

```java
import java.lang.annotation.ElementType;
import java.lang.annotation.Target;

@Target({ElementType.TYPE, ElementType.METHOD, ElementType.FIELD})
public @interface MyAnnotation {}

public class Example {
    @MyAnnotation  // OK — now works on fields, methods, and classes
    private String name;

    @MyAnnotation
    public void doSomething() {}
}
```

### Fix 3: Use an Existing Annotation That Targets the Right Element

```java
// Instead of @NonNull on a field (if it only targets methods):
// Use @NotNull from javax.validation (which targets METHOD, FIELD, etc.)
public class Example {
    @NotNull  // javax.validation targets FIELD
    private String name;
}
```

### Fix 4: Create a Custom Annotation With Correct Targets

```java
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target({ElementType.TYPE, ElementType.METHOD, ElementType.FIELD, ElementType.PARAMETER})
@Retention(RetentionPolicy.RUNTIME)
public @interface Validated {}

public class Example {
    @Validated
    private String name;

    @Validated
    public void process(@Validated String input) {}
}
```

### Fix 5: Remove the Annotation From the Wrong Element

```java
public class Example {
    // Removed @Override from field — it only applies to methods
    private String name;

    @Override  // Correct usage — on a method overriding a superclass method
    public String toString() {
        return "Example{" + name + "}";
    }
}
```

## Prevention Checklist

- Check the `@Target` meta-annotation before using any annotation
- Understand Java annotation target types: TYPE, METHOD, FIELD, CONSTRUCTOR, PARAMETER, etc.
- Use IDE documentation to see where an annotation can be applied
- When creating custom annotations, always specify `@Target` explicitly
- Use broad `@Target` values ({ElementType.TYPE, ElementType.METHOD, ElementType.FIELD}) for general-purpose annotations
- Review `@Retention` as well — RUNTIME annotations are available via reflection

## Related Errors

- [annotation format error (annotationformaterror)](/languages/java/annotationformaterror)
- [annotation type mismatch (annotationtypemismatchexception)](/languages/java/annotationtypemismatchexception)
- [cannot find symbol (cannot-find-symbol)](/languages/java/cannot-find-symbol)
