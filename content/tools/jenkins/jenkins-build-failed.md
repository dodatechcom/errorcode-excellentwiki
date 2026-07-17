---
title: "Jenkins Build Failed"
description: "Jenkins build step returns a non-zero exit code or marks the build as failed."
tools: ["jenkins"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Jenkins Build Failed

A Jenkins build failure means a step in the pipeline or freestyle build returned a failure status. Jenkins marks the overall build as failed and triggers failure notifications.

## Common Causes

- Shell script exited with a non-zero code
- Test suite reported failures
- Post-build action could not complete
- Environment variables or credentials missing

## How to Fix

### Check Console Output

Go to the build page and click **Console Output** to see the failing command.

### Handle Expected Failures

```groovy
stage('Build') {
    steps {
        script {
            try {
                sh 'make build'
            } catch (Exception e) {
                currentBuild.result = 'FAILURE'
                error("Build failed: ${e.message}")
            }
        }
    }
}
```

### Ensure Correct Tool Versions

```groovy
stage('Test') {
    steps {
        sh '''
            export JAVA_HOME=/usr/lib/jvm/java-17
            mvn test
        '''
    }
}
```

### Set Build Status in Post Action

```groovy
post {
    failure {
        echo 'Build failed - check logs for details'
    }
}
```

### Use.timestamps for Better Debugging

```groovy
timestamps {
    // pipeline stages
}
```

## Examples

```text
[Pipeline] sh
+ make build
make: *** No rule to make target 'build'.  Stop.
Finished: FAILURE
```

## Related Errors

- [Agent Error]({{< relref "/tools/jenkins/agent-error" >}}) — agent connection issues
- [Pipeline Error]({{< relref "/tools/jenkins/pipeline-error" >}}) — pipeline syntax error
