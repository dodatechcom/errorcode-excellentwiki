---
title: "Gradle Test Report XML Error"
description: "Gradle test report generation fails because test result XML files are missing, malformed, or contain invalid data."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Test Report XML Error

Gradle generates HTML and XML test reports from JUnit or TestNG result XML files. A report generation error occurs when the XML files are missing, corrupt, or contain unexpected content.

## Common Causes

- Test execution crashed before producing result XML files
- The XML output directory is not configured correctly
- A test framework writes XML in a non-standard format
- Disk space ran out during test execution, truncating XML files

## How to Fix

1. Verify that test result XML files exist:

```bash
ls -la build/test-results/test/
```

2. Configure the XML output directory explicitly:

```groovy
tasks.withType(Test) {
    reports {
        junitXml.required = true
        html.required = true
        junitXml.outputLocation = layout.buildDirectory.dir("test-results/test")
    }
}
```

3. Run tests to generate XML output and check for errors:

```bash
./gradlew test --info 2>&1 | grep -i "test result\|xml\|report"
```

4. Clean and re-run tests to regenerate XML files:

```bash
./gradlew clean test
```

## Examples

```bash
# Error output
> Report generation failed
  No test result XML files found in build/test-results/test/
  Check that tests ran successfully before generating reports
```

```groovy
// Test task with report configuration
tasks.withType(Test) {
    useJUnitPlatform()
    reports {
        junitXml.required = true
        html.required = true
        junitXml.outputLocation = layout.buildDirectory.dir("test-results")
    }
    afterSuite { suite, result ->
        println "Test results: ${result.testCount} tests, ${result.successfulTestCount} passed"
    }
}
```

## Related Errors

- [Test Execution Failed]({{< relref "/tools/gradle/gradle-test-execution-failed" >}}) -- test runtime failures
- [Test Report Generation]({{< relref "/tools/gradle/gradle-test-report-generation" >}}) -- report generation issues
