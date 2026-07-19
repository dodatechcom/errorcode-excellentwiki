---
title: "[Solution] Surefire Test Failures — Maven Test Execution Fix"
description: "Fix Maven Surefire test failures. Resolve test execution errors, forked process crashes, and report generation issues."
languages: ["java"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Surefire Test Failures — Maven Test Execution Fix

A Surefire test failure message means one or more tests failed during Maven build execution. The "Please refer to surefire-reports" message indicates that detailed failure information is available in the generated report files.

## What This Error Means

Common messages:

- `There are test failures. Please refer to surefire-reports`
- `Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin`
- `Tests run: 10, Failures: 2, Errors: 1, Skipped: 0`

## Common Causes

```java
// Cause 1: Test assertions failing
@Test
void shouldCalculateTotal() {
    assertEquals(100, order.calculateTotal()); // Actual: 95
}

// Cause 2: Forked JVM crashed (OutOfMemoryError)
// Test uses too much memory in forked process

// Cause 3: Test depends on external resource
@Test
void shouldCallExternalApi() {
    // External API is down — test fails
}

// Cause 4: Test order dependency
@Test
void testA() { /* modifies shared state */ }
@Test
void testB() { /* depends on clean state */ }
```

## How to Fix

### Fix 1: View Surefire report files for details

Read the XML and text reports in target/surefire-reports to identify which specific tests failed and why.

```java
# View the summary text report
cat target/surefire-reports/*.txt

# View XML report for specific failing test
cat target/surefire-reports/TEST-com.example UserServiceTest.xml

# List all failed tests
grep -l 'failure\|error' target/surefire-reports/TEST-*.xml

# Run only failing tests for quick iteration
mvn test -Dtest=UserServiceTest#shouldCalculateTotal
```

### Fix 2: Configure Surefire for better diagnostics

Update the Surefire plugin configuration to increase fork memory and enable better reporting.

```java
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.2.5</version>
    <configuration>
        <argLine>-Xmx1024m -XX:MaxMetaspaceSize=256m</argLine>
        <includes>
            <include>**/*Test.java</include>
            <include>**/*Tests.java</include>
            <include>**/*Spec.java</include>
        </includes>
        <reportFormat>plain</reportFormat>
        <trimStackTrace>false</trimStackTrace>
    </configuration>
</plugin>
```

### Fix 3: Run failing tests in isolation

Use -Dtest to run specific test classes or methods to isolate and debug failures quickly.

```java
# Run a specific test class
mvn test -Dtest=UserServiceTest

# Run a specific test method
mvn test -Dtest=UserServiceTest#shouldCalculateTotal

# Run multiple specific tests
mvn test -Dtest="UserServiceTest,OrderServiceTest"

# Run tests matching a pattern
mvn test -Dtest="*ServiceTest"

# Skip tests temporarily for debugging build
mvn install -DskipTests
```

## Related Errors

- {{< relref "maven-plugin-error" >}} — Plugin Execution Error
- {{< relref "junit5" >}} — JUnit Platform Launcher Error
