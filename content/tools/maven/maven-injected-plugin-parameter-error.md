---
title: "Maven Injected Plugin Parameter Error"
description: "Maven plugin goal fails because an injected parameter is null or has an invalid value that was automatically resolved."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Injected Plugin Parameter Error

Maven automatically injects values into plugin parameters based on project context. An error occurs when the injected value is null or incompatible with the parameter type.

## Common Causes

- The `${project.build.directory}` is not available during certain phases
- A parameter annotated with `@Parameter(required=true)` receives null
- The parameter injection order conflicts with lifecycle phase availability
- System properties referenced in parameters are not set

## How to Fix

1. Check which parameters require non-null values:

```java
@Parameter(property = "myplugin.inputDir", required = true)
private File inputDirectory;
```

2. Provide the parameter via command line or POM:

```xml
<plugin>
  <groupId>com.example</groupId>
  <artifactId>my-plugin</artifactId>
  <configuration>
    <inputDirectory>${project.basedir}/src/main/input</inputDirectory>
  </configuration>
</plugin>
```

3. Use default values for optional parameters:

```java
@Parameter(property = "myplugin.outputDir", defaultValue = "${project.build.directory}/generated")
private File outputDirectory;
```

4. Set system properties for command-line parameters:

```bash
mvn my-plugin:execute -Dmyplugin.inputDir=/path/to/input
```

## Examples

```bash
# Error output
[ERROR] Parameter 'inputDirectory' is required but was not provided
  Current project: com.example:my-app:1.0-SNAPSHOT
```

```java
// Plugin with proper parameter defaults
@Mojo(name = "process", defaultPhase = Phase.GENERATE_SOURCES)
public class ProcessMojo extends AbstractMojo {
    @Parameter(property = "inputDir", required = true)
    private File inputDirectory;

    @Parameter(defaultValue = "${project.build.directory}/generated")
    private File outputDirectory;
}
```

## Related Errors

- [Plugin Parameter Error]({{< relref "/tools/maven/maven-plugin-parameter-error" >}}) -- parameter configuration issues
- [Plugin Execution Failed]({{< relref "/tools/maven/maven-plugin-execution-failed" >}}) -- plugin execution failures
