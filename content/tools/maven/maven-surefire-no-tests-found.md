---
title: "Maven Surefire No Tests Found"
description: "Maven surefire plugin reports no tests were found even though test classes exist, typically due to naming convention mismatches."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Surefire No Tests Found

The Maven surefire plugin runs unit tests. A no-tests-found error means the plugin cannot find test classes matching its naming patterns, even though test files exist in the project.

## Common Causes

- Test class names do not match the default pattern (`**/Test*.java`, `**/*Test.java`)
- Test source directory is not configured correctly
- The surefire plugin version is incompatible with the test framework
- Test classes have compilation errors preventing them from being discovered

## How to Fix

1. Check surefire naming conventions:

```bash
# Default patterns:
# **/Test*.java
# **/*Test.java
# **/*Tests.java
# **/*TestCase.java
```

2. Configure custom file name patterns:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-surefire-plugin</artifactId>
  <version>3.2.5</version>
  <configuration>
    <includes>
      <include>**/Test*.java</include>
      <include>**/*Test.java</include>
      <include>**/*Tests.java</include>
      <include>**/*IT.java</include>
    </includes>
  </configuration>
</plugin>
```

3. Verify test source directories:

```bash
mvn help:effective-pom | grep -A3 "testSourceDirectory"
```

4. Run with verbose output to see what is scanned:

```bash
mvn test -X 2>&1 | grep -i "test.*class\|scanning\|include"
```

## Examples

```bash
# Error output
[INFO] No tests were executed!
# Test files exist but naming does not match
```

```xml
<!-- Custom surefire configuration for non-standard names -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-surefire-plugin</artifactId>
  <version>3.2.5</version>
  <configuration>
    <includes>
      <include>**/*Spec.java</include>
      <include>**/*IT.java</include>
    </includes>
    <excludes>
      <exclude>**/*DisabledTest.java</exclude>
    </excludes>
  </configuration>
</plugin>
```

## Related Errors

- [Surefire Test Failure]({{< relref "/tools/maven/maven-surefire-test-failure" >}}) -- test execution failures
- [Test Error]({{< relref "/tools/maven/maven-test-error" >}}) -- general test failures
