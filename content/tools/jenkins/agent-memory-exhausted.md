---
title: "[Solution] Jenkins Agent Memory Exhausted"
description: "Fix Jenkins agent memory exhaustion errors. Resolve OutOfMemoryError and agent JVM crashes."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Agent Memory Exhausted

Agent memory exhaustion occurs when the agent JVM runs out of memory.

## How to Fix

```bash
export JAVA_OPTS="-Xmx4g -XX:MaxMetaspaceSize=512m"
java $JAVA_OPTS -jar agent.jar -url http://jenkins:8080 -secret @secret
```

```groovy
properties([disableConcurrentBuilds()])
environment { MAVEN_OPTS = '-Xmx2g'; GRADLE_OPTS = '-Xmx2g' }
```
