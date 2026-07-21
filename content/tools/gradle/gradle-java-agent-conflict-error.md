---
title: "Gradle Java Agent Conflict Error"
description: "Gradle build fails because a Java agent attached to the JVM conflicts with build tasks or agent arguments are misconfigured."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Java Agent Conflict Error

Java agents instrument the JVM at startup for profiling, coverage, or logging. A conflict error occurs when the agent interferes with Gradle's own JVM operations.

## Common Causes

- The `-javaagent` flag in `GRADLE_OPTS` conflicts with task JVM arguments
- A JaCoCo or coverage agent is attached to both the daemon and test JVM
- The agent JAR path is incorrect or the file does not exist
- Multiple agents are loaded and cause bytecode instrumentation conflicts

## How to Fix

1. Check for Java agent flags in the environment:

```bash
echo $GRADLE_OPTS
echo $JAVA_TOOL_OPTIONS
```

2. Remove conflicting agent flags for Gradle daemon startup:

```bash
unset GRADLE_OPTS
unset JAVA_TOOL_OPTIONS
./gradlew build
```

3. Configure the agent only for test tasks:

```groovy
tasks.withType(Test) {
    jvmArgs = ['-javaagent:' + file('lib/jacocoagent.jar').absolutePath]
}
```

4. Verify the agent JAR exists:

```bash
ls -la lib/jacocoagent.jar
```

## Examples

```bash
# Error output
Error occurred during initialization of VM
  agent library jacocoagent failed to initialize: java.lang.instrument.IllegalStateException
```

```groovy
// Correct agent configuration for tests only
tasks.withType(Test) {
    jvmArgs "-javaagent:${classpath.find('org.jacoco:org.jacoco.agent:0.8.11:runtime.jar')}"
}
```

## Related Errors

- [JaCoCo Plugin Error]({{< relref "/tools/gradle/gradle-jacoco-plugin-error" >}}) -- JaCoCo configuration issues
- [Process Forking Error]({{< relref "/tools/gradle/gradle-process-forking-error" >}}) -- JVM process failures
