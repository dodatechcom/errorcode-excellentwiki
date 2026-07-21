---
title: "[Solution] Jenkins Shared Library Load Error"
description: "Fix Jenkins shared library load errors when the pipeline cannot load classes or methods from an external shared library."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Shared Library Load Error

Shared library load errors occur when a Jenkins Pipeline cannot load classes, methods, or variables from a configured shared library due to compilation or resolution failures.

## Common Causes

- Shared library repository is not accessible
- Class file has compilation errors
- Method signature does not match the expected type
- Library version or branch does not exist
- Circular dependency between library and pipeline

## How to Fix

### Solution 1: Verify library configuration

Navigate to **Manage Jenkins > Configure System > Global Pipeline Libraries** and verify:

```groovy
@Library('my-shared-lib@main') _
import com.example.Utils
```

### Solution 2: Check library source for errors

```bash
# Test compilation of the shared library
cd shared-lib-repo
groovyc src/com/example/*.groovy
```

### Solution 3: Use correct import and method signatures

```groovy
@Library('utils@v2') _

pipeline {
    stages {
        stage('Build') {
            steps {
                script {
                    def utils = new com.example.Utils()
                    utils.deploy(environment: 'staging')
                }
            }
        }
    }
}
```

## Examples

```
ERROR: Could not resolve symbol 'Utils'
ERROR: No such method: deploy()
```

## Prevent It

- Test shared library changes in a test pipeline
- Use specific version tags for library references
- Run Groovy compilation checks before merging library changes
