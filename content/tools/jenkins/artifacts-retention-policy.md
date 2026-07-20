---
title: "[Solution] Jenkins Artifacts Retention Policy Error"
description: "Fix Jenkins artifacts retention policy errors. Resolve artifact storage and cleanup issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Artifacts Retention Policy Error

Artifacts retention policy controls how long build artifacts are kept.

## How to Fix

```groovy
options {
    buildDiscarder(logRotator(numToKeepStr: '50', artifactDaysToKeepStr: '30', artifactNumToKeepStr: '10'))
}
```

```groovy
import jenkins.model.Jenkins
Jenkins.instance.getAllItems(Job.class).each { job ->
    def keep = 10
    def builds = job.builds.toList()
    if (builds.size() > keep) builds.drop(keep).each { it.delete() }
}
```
