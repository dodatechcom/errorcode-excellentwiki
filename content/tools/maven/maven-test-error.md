---
title: "Maven Test Failure"
description: "Maven test phase fails with test errors or assertion failures."
tools: ["maven"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Maven Test Failure

A Maven test failure occurs when the `maven-surefire-plugin` detects test failures or errors during the test phase. The build reports which tests failed and why.

## Common Causes

- Test assertions failed (expected vs. actual values)
- Test environment not properly configured
- Test database or service unavailable
- Flaky tests that pass intermittently
- Missing test dependencies

## How to Fix

### Run Tests with Detailed Output

```bash
mvn test -Dsurefire.useFile=false
```

### Run Specific Test Class

```bash
mvn test -Dtest=MyTestClass
```

### Run Specific Test Method

```bash
mvn test -Dtest=MyTestClass#testMethod
```

### Skip Tests Temporarily

```bash
mvn clean install -DskipTests
```

### Check Test Reports

```bash
# View test reports
cat target/surefire-reports/*.txt
```

### Fix Flaky Tests

```java
@Test
@Timeout(value = 30, unit = TimeUnit.SECONDS)
public void testWithTimeout() {
    // test code
}
```

### Configure Surefire Plugin

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <includes>
            <include>**/*Test.java</include>
        </includes>
        <rerunFailingTestsCount>2</rerunFailingTestsCount>
    </configuration>
</plugin>
```

## Examples

```bash
mvn test
[ERROR] Tests run: 10, Failures: 2, Errors: 1, Skipped: 0, Time elapsed: 15.3s
[ERROR] Failed tests:
[ERROR]   UserServiceTest.testLogin:45 expected:<200> but was:<401>
[ERROR]   OrderServiceTest.testCreate:67 NullPointerException
```

## Related Errors

- [Build Failed]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
- [Compiler Error]({{< relref "/tools/maven/maven-compiler-error" >}}) — compilation failure
- [Out of Memory]({{< relref "/tools/maven/maven-out-of-memory" >}}) — test OOM
