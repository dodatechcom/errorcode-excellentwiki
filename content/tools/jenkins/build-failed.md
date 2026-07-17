---
title: "Build Step Marked Build as Failure"
description: "A Jenkins build step returned a non-zero exit code or explicitly marked the build as failed."
tools: ["jenkins"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

This error means a step in the Jenkins pipeline or freestyle build returned a failure status. Jenkins marks the overall build as failed and may trigger failure notifications.

## Common Causes

- A shell script or command in the build step exited with a non-zero code
- A test suite reported failures and the step is configured to fail on test failure
- A post-build action (like artifact archiving) could not complete
- Environment variables or credentials are missing

## How To Fix

Check the console output for the specific step and failing command. Use `try/catch` in scripted pipelines to handle expected failures:

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

Ensure the correct tool versions and paths are available in the build environment:

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

Set the build status explicitly in a post action:

```groovy
post {
    failure {
        echo 'Build failed - check logs for details'
    }
}
```

## Examples

```
[Pipeline] sh
+ make build
make: *** No rule to make target 'build'.  Stop.
Finished: FAILURE
```

## Related Errors

- [Agent Error]({{< relref "/tools/jenkins/agent-error" >}})
