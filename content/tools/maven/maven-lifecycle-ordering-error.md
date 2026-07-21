---
title: "Maven Lifecycle Phase Ordering Error"
description: "Maven build fails because lifecycle phases are referenced in the wrong order or a goal is bound to an invalid phase."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Lifecycle Phase Ordering Error

Maven defines a fixed lifecycle phase ordering. An error occurs when a goal is bound to a phase that does not exist or when phases are invoked out of order.

## Common Causes

- A custom lifecycle binding references a non-existent phase
- A goal is executed directly with a phase that does not include it
- The project packaging type defines a custom lifecycle that is missing a phase
- A plugin goal is bound to the wrong phase

## How to Fix

1. Verify the lifecycle phase order for your packaging type:

```bash
mvn validate -X 2>&1 | grep "Phase"
```

2. Use the correct phase name in plugin configuration:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <executions>
    <execution>
      <phase>compile</phase>
      <goals>
        <goal>compile</goal>
      </goals>
    </execution>
  </executions>
</plugin>
```

3. Check valid phases for jar packaging:

```
validate, initialize, generate-sources, process-sources,
generate-resources, process-resources, compile, process-classes,
generate-test-sources, process-test-sources, generate-test-resources,
process-test-resources, test-compile, process-test-classes, test,
prepare-package, package, verify, install, deploy
```

4. Ensure custom lifecycle phases are defined:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-jar-plugin</artifactId>
  <executions>
    <execution>
      <phase>package</phase>
      <goals>
        <goal>jar</goal>
      </goals>
    </execution>
  </executions>
</plugin>
```

## Examples

```bash
# Error output
[ERROR] Unknown lifecycle phase "complie"
# Typo: should be "compile"
```

```xml
<!-- Correct phase binding -->
<executions>
  <execution>
    <id>generate-sources</id>
    <phase>generate-sources</phase>
    <goals>
      <goal>help</goal>
    </goals>
  </execution>
</executions>
```

## Related Errors

- [Lifecycle Phase Not Found]({{< relref "/tools/maven/maven-lifecycle-phase-not-found" >}}) -- missing lifecycle phases
- [Goal Not Found]({{< relref "/tools/maven/maven-goal-not-found-in-plugin" >}}) -- missing plugin goals
