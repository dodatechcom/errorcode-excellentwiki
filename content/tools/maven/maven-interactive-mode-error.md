---
title: "Maven Interactive Mode Error"
description: "Maven interactive mode fails during goal execution because it cannot read user input or prompts are not supported."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Interactive Mode Error

Maven interactive mode allows prompts during build execution, such as version input for the release plugin. An error occurs when the terminal does not support interactive input or stdin is redirected.

## Common Causes

- Maven is executed in a CI pipeline where stdin is not a terminal
- The release plugin expects interactive input but is running non-interactively
- The `-B` (batch mode) flag is not used in non-interactive environments
- Terminal output is piped, disabling interactive prompts

## How to Fix

1. Use batch mode for non-interactive environments:

```bash
mvn clean install -B
```

2. Provide the required input programmatically:

```bash
mvn release:prepare -B -DdevelopmentVersion=1.1.0-SNAPSHOT -DreleaseVersion=1.0.0
```

3. Configure the release plugin to skip interactive prompts:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-release-plugin</artifactId>
  <configuration>
    <tagNameFormat>v@{project.version}</tagNameFormat>
    <autoVersionSubmodules>true</autoVersionSubmodules>
  </configuration>
</plugin>
```

4. Force non-interactive mode in scripts:

```bash
echo "" | mvn release:prepare
```

## Examples

```bash
# Error in CI pipeline
[INFO] Press Enter to accept the current value...
# Maven hangs waiting for input
# Fix: use -B flag
mvn release:prepare -B
```

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-release-plugin</artifactId>
  <configuration>
    <batchMode>true</batchMode>
  </configuration>
</plugin>
```

## Related Errors

- [Release Plugin Error]({{< relref "/tools/maven/maven-release-plugin-error" >}}) -- release plugin issues
- [Release Prepare Failed]({{< relref "/tools/maven/maven-release-prepare-failed" >}}) -- release preparation failures
