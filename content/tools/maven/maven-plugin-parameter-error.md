---
title: "Maven Plugin Parameter Error"
description: "Maven plugin goal fails because a required parameter is missing, has an invalid value, or is not properly configured in the POM."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Plugin Parameter Error

Maven plugin goals accept parameters through POM configuration or command-line arguments. A parameter error occurs when a required parameter is missing or the value is not valid.

## Common Causes

- A required plugin parameter is not specified in the POM or command line
- The parameter value type does not match the expected type
- The plugin version does not support the configured parameter
- Default parameter values are overridden with invalid values

## How to Fix

1. Check the plugin's parameter documentation:

```bash
mvn help:describe -Dplugin=compiler -Dgoal=compile -Ddetail
```

2. Add the missing parameter to the plugin configuration:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <configuration>
    <source>11</source>
    <target>11</target>
    <encoding>UTF-8</encoding>
  </configuration>
</plugin>
```

3. Pass parameters from the command line:

```bash
mvn compile -Dmaven.compiler.source=11 -Dmaven.compiler.target=11
```

4. Verify parameter values match the expected type:

```xml
<!-- Wrong -- string instead of boolean -->
<configuration>
  <verbose>true</verbose> <!-- should be a property reference -->
</configuration>

<!-- Correct -->
<configuration>
  <verbose>${maven.compiler.verbose}</verbose>
</configuration>
```

## Examples

```bash
# Error output
[ERROR] Failed to execute goal compiler:compile:
  The parameter 'source' is required
```

```xml
<!-- Complete compiler plugin with all parameters -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <version>3.11.0</version>
  <configuration>
    <source>17</source>
    <target>17</target>
    <encoding>UTF-8</encoding>
    <showDeprecation>true</showDeprecation>
    <showWarnings>true</showWarnings>
  </configuration>
</plugin>
```

## Related Errors

- [Plugin Execution Failed]({{< relref "/tools/maven/maven-plugin-execution-failed" >}}) -- plugin execution failures
- [Goal Not Found]({{< relref "/tools/maven/maven-goal-not-found-in-plugin" >}}) -- missing plugin goals
