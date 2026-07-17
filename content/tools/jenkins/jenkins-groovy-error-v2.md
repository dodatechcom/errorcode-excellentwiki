---
title: "Jenkins Groovy Script Execution Error"
description: "Jenkins Groovy script fails during execution in the pipeline or console."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Jenkins Groovy — Script Execution Error

This error occurs when a Groovy script in a Jenkins pipeline or script console fails during execution. The error may be due to syntax issues, missing classes, or security restrictions.

## Common Causes

- Groovy syntax errors
- Missing classes or imports
- Script Security sandbox restrictions
- Undefined variables or methods
- Null pointer exceptions

## How to Fix

### Check Groovy Syntax

```groovy
// Valid Groovy syntax
def result = sh(script: 'echo "Hello"', returnStdout: true).trim()
```

### Add Required Imports

```groovy
import hudson.model.*
import jenkins.model.Jenkins

def job = Jenkins.instance.getItem('my-job')
println job.name
```

### Approve Script in Script Approval

Go to **Manage Jenkins > In-process Script Approval** and approve the script.

### Fix Null References

```groovy
def job = Jenkins.instance.getItem('my-job')
if (job) {
    println job.name
} else {
    println "Job not found"
}
```

### Use Proper Error Handling

```groovy
try {
    sh 'make build'
} catch (Exception e) {
    echo "Build failed: ${e.message}"
    currentBuild.result = 'FAILURE'
}
```

### Debug with Print Statements

```groovy
println "Variable value: ${myVar}"
println "Map contents: ${myMap}"
```

## Examples

```text
org.codehaus.groovy.control.MultipleCompilationErrorsException:
  startup failed:
  Script1.groovy: 5: unexpected token: } @ line 5, column 1.
```

## Related Errors

- [Jenkins Pipeline Error]({{< relref "/tools/jenkins/jenkins-pipeline-error" >}}) — pipeline syntax error
- [Jenkins Shared Library Error]({{< relref "/tools/jenkins/jenkins-shared-library-error" >}}) — shared library load error
- [Jenkins Build Failed]({{< relref "/tools/jenkins/jenkins-build-failed" >}}) — general build failure
