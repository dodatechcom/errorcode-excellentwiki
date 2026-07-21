---
title: "Test Filtering Configuration Error"
description: "Gradle test filtering is misconfigured causing tests to be skipped or the wrong test methods to be executed during the test task."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Test Filtering Configuration Error

Gradle test filtering allows you to run specific test classes or methods using the `--tests` flag. A configuration error causes tests to be skipped entirely or the filter to match unintended tests.

## Common Causes

- The test filter pattern does not match any test class or method names
- Wildcard patterns use incorrect syntax for the test framework
- Test class names do not follow the expected naming convention
- The filter references a test in a subproject that is not included

## How to Fix

1. Use the correct filter syntax for your test framework:

```bash
# Run a specific test class
./gradlew test --tests "com.example.MyTestClass"

# Run a specific test method
./gradlew test --tests "com.example.MyTestClass.testMethod"

# Run all tests in a package
./gradlew test --tests "com.example.unit.*"
```

2. List available tests to verify the filter pattern:

```bash
./gradlew test --tests "*" --info | grep "Test result"
```

3. Configure test filtering in `build.gradle` for recurring patterns:

```groovy
tasks.withType(Test) {
    useJUnitPlatform()
    filter {
        includeTestsMatching "com.example.unit.*"
        includeTestsMatching "*IntegrationTest"
    }
}
```

4. Run with debug output to see which tests match:

```bash
./gradlew test --tests "com.example.*" --debug | grep "Matching test"
```

## Examples

```bash
# Error -- no tests matched
./gradlew test --tests "com.example.NonExistentTest"
# No tests were found for the filter: com.example.NonExistentTest

# Correct pattern
./gradlew test --tests "com.example.UserServiceTest"
```

```groovy
// build.gradle test filtering
test {
    useJUnitPlatform()
    filter {
        includeTestsMatching "*.SlowTest"
        includeTestsMatching "*.FastTest"
        excludeTestsMatching "*.DisabledTest"
    }
}
```

## Related Errors

- [Test Execution Failed]({{< relref "/tools/gradle/gradle-test-execution-failed" >}}) -- test runtime failures
- [Test Task Not Found]({{< relref "/tools/gradle/gradle-test-task-not-found" >}}) -- missing test task
