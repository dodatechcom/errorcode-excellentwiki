---
title: "[Solution] Jenkins Build Discarder Error"
description: "Fix Jenkins build discarder configuration errors. Resolve build log rotation and retention issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Build Discarder Error

Build discarder settings control how many builds are retained.

## How to Fix

```groovy
options {
    buildDiscarder(logRotator(daysToKeepStr: '30', numToKeepStr: '100', artifactDaysToKeepStr: '7', artifactNumToKeepStr: '10'))
}
```

```groovy
import jenkins.model.Jenkins
Jenkins.instance.getAllItems(Job.class).each { job ->
    job.builds.findAll { it.number < job.lastBuild.number - 100 }.each { it.delete() }
}
```
