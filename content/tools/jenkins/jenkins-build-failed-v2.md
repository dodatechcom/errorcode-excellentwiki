---
title: "Jenkins Build Failed Pipeline Error"
description: "Jenkins pipeline build fails with a pipeline execution error."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jenkins", "build", "pipeline", "failure", "stage"]
weight: 5
---

# Jenkins Build Failed — Pipeline Error

This error occurs when a Jenkins pipeline build fails during execution. The pipeline stage or step encounters an error that causes the build to abort.

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

### Use Timestamps for Better Debugging

```groovy
timestamps {
    // pipeline stages
}
```

### Add Retry Logic

```groovy
stage('Build') {
    steps {
        retry(3) {
            sh 'make build'
        }
    }
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

- [Jenkins Agent Error]({{< relref "/tools/jenkins/jenkins-agent-error" >}}) — agent connection issues
- [Jenkins Pipeline Error]({{< relref "/tools/jenkins/jenkins-pipeline-error" >}}) — pipeline syntax error
- [Jenkins Permission Error]({{< relref "/tools/jenkins/jenkins-permission-error" >}}) — permission issues
