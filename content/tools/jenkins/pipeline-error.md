---
title: "[Solution] Jenkins Pipeline Syntax Error"
description: "Fix Jenkins pipeline syntax errors. Resolve Groovy DSL and Jenkinsfile parsing issues."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jenkins", "pipeline", "syntax", "groovy", "jenkinsfile"]
weight: 5
---

# Jenkins Pipeline Syntax Error

A pipeline syntax error means the Jenkinsfile contains invalid Groovy syntax or uses incorrect Jenkins pipeline DSL. Jenkins cannot parse the pipeline definition and fails before execution.

## Common Causes

- Missing or mismatched braces, brackets, or quotes in the Jenkinsfile
- Using declarative syntax inside scripted pipeline blocks (or vice versa)
- Referencing an undefined variable or function
- Incorrect use of pipeline steps (e.g., `sh` with wrong argument type)

## How to Fix

### Validate Jenkinsfile Syntax

```bash
# Use the Jenkins Pipeline Linter
java -jar jenkins-cli.jar declarative-linter < Jenkinsfile
```

### Check Common Declarative Pipeline Structure

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'make build'
            }
        }
    }
}
```

### Fix Quoting Issues

```groovy
// WRONG: mixed quotes
sh echo "Building version $VERSION"

// CORRECT
sh "echo Building version ${env.VERSION}"
```

### Fix Block Nesting

```groovy
// WRONG: missing closing braces
pipeline {
    stages {
        stage('Build') {
            steps {
                sh 'make'
            // missing }
        }
    }
}
```

### Use Pipeline Syntax Generator

```
Jenkins > Pipeline Syntax (under Tools section)
```

## Examples

```groovy
// Undefined variable
echo ${UNDEFINED_VAR}
// ERROR: No such property: UNDEFINED_VAR
// Fix: define the variable or use env.UNDEFINED_VAR

// Wrong step argument type
sh(['cmd1', 'cmd2'])
// ERROR: expects String, got List
// Fix: sh command: 'cmd1 && cmd2'
```

## Related Errors

- [Build Failed]({{< relref "/tools/jenkins/build-failed" >}}) — build step returned error
- [SCM Error]({{< relref "/tools/jenkins/scm-error" >}}) — source checkout failure
