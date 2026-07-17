---
title: "Jenkins Groovy Script Error"
description: "Jenkins pipeline Groovy script fails with syntax or runtime errors."
tools: ["jenkins"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Jenkins Groovy Script Error

A Jenkins Groovy script error occurs when the pipeline's Groovy code has syntax errors, type mismatches, or runtime exceptions. Jenkins pipelines use Groovy as their scripting language.

## Common Causes

- Groovy syntax errors in pipeline script
- Incorrect use of Jenkins pipeline steps
- Missing imports for custom classes
- Type mismatch errors in Groovy code

## How to Fix

### Check Groovy Syntax

```groovy
// Groovy requires proper syntax
def result = sh(script: 'echo hello', returnStdout: true)
echo result.trim()
```

### Fix Common Groovy Errors

```groovy
// String interpolation
def name = "world"
echo "Hello ${name}"  // Correct
// echo "Hello $name"  // Works but less clear

// Null safety
def value = someMap?.key ?: 'default'
```

### Use @NonCPS for Non-Step Methods

```groovy
@NonCPS
def listToString(List<String> list) {
    return list.join(', ')
}
```

### Check Pipeline Step Usage

```groovy
// Correct step usage
sh 'echo hello'
sh(script: 'echo hello', returnStdout: true)

// Wrong
sh(echo: 'hello')  // Invalid
```

### Add Error Handling

```groovy
try {
    sh 'make build'
} catch (Exception e) {
    echo "Error: ${e.message}"
    throw e
}
```

### Debug Groovy Code

```groovy
stage('Debug') {
    steps {
        script {
            echo "Variable: ${myVar}"
            echo "Map: ${myMap}"
        }
    }
}
```

## Examples

```text
org.codehaus.groovy.control.MultipleCompilationErrorsException:
startup failed:
WorkflowScript: 10: unexpected token: def @ line 10, column 13
```

## Related Errors

- [Pipeline Error]({{< relref "/tools/jenkins/pipeline-error" >}}) — pipeline syntax error
- [Build Failed]({{< relref "/tools/jenkins/jenkins-build-failed" >}}) — build failure
- [Shared Library Error]({{< relref "/tools/jenkins/jenkins-shared-library-error" >}}) — shared library issue
