---
title: "[Solution] Jenkins Load Step Error in Pipeline"
description: "Fix Jenkins load step errors when loading Groovy scripts dynamically in pipeline."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Load Step Error in Pipeline

The `load` step reads and evaluates a Groovy script file from the workspace. Errors occur when the file path is wrong or the script has compilation errors.

## Common Causes

- File does not exist at the specified path
- Groovy script has syntax or compilation errors
- Script references variables not available in the pipeline context

## How to Fix

```groovy
stage('Load Config') {
    steps {
        script {
            if (fileExists('scripts/config.groovy')) {
                def config = load('scripts/config.groovy')
                config.run()
            } else {
                error 'config.groovy not found'
            }
        }
    }
}
```

### Return a Callable Object

```groovy
// scripts/build.groovy
def call(version) {
    echo "Building version ${version}"
    sh "make VERSION=${version}"
}
return this
```
