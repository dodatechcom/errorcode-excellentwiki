---
title: "[Solution] IntelliJ IDEA Test runner error"
description: "Fix IntelliJ IDEA test runner failures. Resolve JUnit, TestNG, and other test framework execution errors."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "testing", "junit", "testng", "test-runner"]
severity: "error"
---

# Test runner error

## Error Message

```
Test runner error
No tests found in class 'MyTestClass'
java.lang.Exception: No tests in package 'com.example.tests'
Process finished with exit code -1
Test framework not configured. Please configure a test framework.
```

## Common Causes

- Test class does not follow naming conventions (e.g., *Test.java)
- Test framework dependency is missing from the project
- JUnit/TestNG plugin is not installed or enabled in IDE
- Test source root is not correctly configured
- Test class has compilation errors preventing execution

## Solutions

### Solution 1: Configure Test Framework Dependencies

Add the correct test framework dependency to your build configuration.

```xml
<!-- Maven pom.xml: -->
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.10.1</version>
    <scope>test</scope>
</dependency>

<!-- For TestNG: -->
<dependency>
    <groupId>org.testng</groupId>
    <artifactId>testng</artifactId>
    <version>7.9.0</version>
    <scope>test</scope>
</dependency>

<!-- Then reload Maven project in IDE -->
```

### Solution 2: Verify Test Source Root

Ensure test files are in directories marked as Test Sources.

```
File → Project Structure → Modules
# Select your module → Sources tab
# Verify:
#   src/test/java → Marked as 'Test Sources' (green folder)
#   src/test/resources → Marked as 'Test Resources'

# If not marked:
#   Right-click on 'src/test/java' directory
#   → Mark Directory as → Test Sources Root

# Move test files to the correct directory if needed
```

### Solution 3: Run Tests from IDE Toolbar

Use the IDE's built-in test runner instead of external tools to ensure proper configuration.

```
# Run a single test class:
# Right-click on test class → Run 'TestClassName'

# Run a single test method:
# Right-click on test method → Run 'testMethodName'

# Run all tests in package:
# Right-click on package → Run 'Tests in <package>'

# Run with coverage:
# Right-click → Run 'TestClassName' with Coverage

# Debug a test:
# Right-click → Debug 'TestClassName'
```

### Solution 4: Enable JUnit Plugin

Ensure the JUnit or TestNG plugin is installed and enabled in the IDE.

```
File → Settings → Plugins → Installed
# Search for 'JUnit'
# Ensure 'JUnit' plugin is enabled
# For TestNG, search for 'TestNG' and enable it

# If not installed:
# Plugins → Marketplace → Search 'JUnit' → Install
# Restart IDE after installation

# Verify plugin is working:
# Create a test class → should show green 'run' arrows
```

## Prevention Tips

- Name test classes with 'Test' suffix (e.g., UserServiceTest) for auto-detection
- Use @Test annotation from the correct package (org.junit.jupiter.api for JUnit 5)
- Run tests with coverage to identify untested code paths
- Configure test configuration templates in Run → Edit Configurations → Defaults

## Related Errors

- [Compilation Failed]({{< relref "/tools/intellij/compilation-error" >}})
- [Run Configuration Error]({{< relref "/tools/intellij/run-configuration-error" >}})
- [Debug Error]({{< relref "/tools/intellij/debug-error" >}})
