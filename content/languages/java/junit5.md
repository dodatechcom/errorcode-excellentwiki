---
title: "[Solution] JUnit Platform Launcher Error — JUnit 5 Fix"
description: "Fix JUnit Platform launcher errors, test discovery failures, and incompatible extension issues in JUnit 5."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["junit5", "testing", "junit-platform", "launcher", "test"]
weight: 5
---

# JUnit Platform Launcher Error — JUnit 5 Fix

JUnit Platform launcher errors occur when the test runner cannot discover or execute tests. This can be caused by incompatible dependencies, missing configuration, or classpath issues.

## What This Error Means

Common messages:

- `No tests were executed`
- `TestEngine with ID 'junit-jupiter' failed to discover tests`
- `IncompatibleClassChangeError`

## Common Causes

```java
// Cause 1: Missing JUnit 5 dependency
// pom.xml doesn't include junit-jupiter

// Cause 2: JUnit 4 and JUnit 5 conflict
// Both junit:junit and junit-jupiter on classpath

// Cause 3: Wrong test method signature
public class MyTest {
    public void testSomething() { }  // Missing @Test annotation
}
```

## How to Fix

### Fix 1: Add JUnit 5 dependency

```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <scope>test</scope>
</dependency>
```

### Fix 2: Use correct test annotations

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MyTest {

    @Test
    void shouldDoSomething() {
        assertEquals(4, 2 + 2);
    }

    @Test
    void shouldHandleEdgeCase() {
        assertThrows(IllegalArgumentException.class, () -> {
            service.process(-1);
        });
    }
}
```

### Fix 3: Configure Maven Surefire plugin

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.2.5</version>
</plugin>
```

### Fix 4: Use JUnit Vintage for JUnit 4 tests

```xml
<dependency>
    <groupId>org.junit.vintage</groupId>
    <artifactId>junit-vintage-engine</artifactId>
    <scope>test</scope>
</dependency>
```

## Related Errors

- {{< relref "mockito" >}} — Mockito misuse errors
- {{< relref "assertionerror" >}} — Assertion error
- {{< relref "testcontainers" >}} — Testcontainers startup failure
