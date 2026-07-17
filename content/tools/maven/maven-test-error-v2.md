---
title: "Maven Tests in Error Surefire Failure"
description: "Maven surefire plugin reports test failures or errors during build."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Maven Tests in Error — Surefire Failure

This error occurs when the Maven surefire plugin reports test failures or errors. Tests either fail assertions or throw unexpected exceptions during execution.

## Common Causes

- Test assertions failing due to code changes
- Test environment not configured correctly
- Tests depend on external services that are unavailable
- Test isolation issues (shared state between tests)
- Memory issues in test JVM

## How to Fix

### Run Tests with Detailed Output

```bash
mvn test -Dtest=MyTestClass -Dsurefire.useFile=false
```

### Show Test Output in Console

```bash
mvn test -Dsurefire.useFile=false
```

### Run Specific Failing Test

```bash
mvn test -Dtest=MyTestClass#testMethod
```

### Configure Surefire Plugin

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.2.2</version>
    <configuration>
        <includes>
            <include>**/*Test.java</include>
        </includes>
        <argLine>-Xmx2g</argLine>
    </configuration>
</plugin>
```

### Skip Failing Tests Temporarily

```bash
mvn package -DskipTests
```

### Fix Test Environment

```java
@Before
public void setup() {
    System.setProperty("test.db.url", "jdbc:h2:mem:testdb");
}
```

### Generate Test Report

```bash
mvn surefire-report:report
```

## Examples

```text
[ERROR] Tests run: 15, Failures: 2, Errors: 1, Skipped: 0

[ERROR] com.example.UserServiceTest.testCreateUser  Time elapsed: 0.342 s
  <<< FAILURE!
  java.lang.AssertionError: expected:<200> but was:<400>
```

## Related Errors

- [Maven Build Error]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
- [Maven Out of Memory]({{< relref "/tools/maven/maven-out-of-memory" >}}) — test JVM heap space
- [Maven Enforcer Error]({{< relref "/tools/maven/maven-enforcer-error" >}}) — build policy violations
