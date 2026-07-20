---
title: "[Solution] Jenkins Downstream Job Failed"
description: "Fix Jenkins downstream job failure errors. Resolve build dependency and trigger chain issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Downstream Job Failed

Downstream jobs are triggered by upstream jobs. When downstream fails, upstream may also be affected.

## How to Fix

```groovy
stage('Trigger Downstream') {
    steps {
        build job: 'my-downstream-job', parameters: [string(name: 'VERSION', value: env.BUILD_VERSION)]
    }
}
```

```groovy
stage('Trigger Downstream') {
    steps {
        script {
            try { build job: 'my-downstream-job' }
            catch (err) {
                echo "Downstream job failed: ${err.message}"
                currentBuild.result = 'UNSTABLE'
            }
        }
    }
}
```
