---
title: "Maven Plugin Execution Goal Not Found"
description: "Maven plugin goal cannot be found or does not exist in the plugin."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["maven", "plugin", "goal", "execution", "not-found"]
weight: 5
---

# Maven Plugin Execution Goal Not Found

This error occurs when Maven cannot find a plugin goal specified in the build. The plugin may not contain the requested goal, or the plugin itself is not available.

## Common Causes

- Plugin goal name is misspelled
- Plugin version does not include the specified goal
- Plugin not configured in the POM
- Goal requires a specific packaging type
- Plugin is not in the configured repositories

## How to Fix

### List Available Plugin Goals

```bash
mvn <plugin:help>
mvn help:describe -Dplugin=compiler
```

### Verify Plugin Goal Name

```bash
mvn <plugin:describe -Dplugin=exec -Ddetail>
```

### Configure Plugin Correctly

```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>exec-maven-plugin</artifactId>
    <version>3.1.0</version>
    <executions>
        <execution>
            <goals>
                <goal>java</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

### Check Plugin Version Compatibility

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.2.2</version>
</plugin>
```

### Use the Correct Plugin Coordinate

```xml
<!-- Wrong: goal name -->
<goal>test-compile</goal>

<!-- Right: check actual goal name -->
<goal>compile</goal>
```

## Examples

```text
[ERROR] Unknown goal 'complie'. You must specify a valid lifecycle phase
  or a goal in the format <plugin-prefix>:<goal> or
  <plugin-group-id>:<plugin-artifact-id>[:<plugin-version>]:<goal>
```

## Related Errors

- [Maven Plugin Error]({{< relref "/tools/maven/maven-plugin-error" >}}) — plugin execution failure
- [Maven Build Error]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
- [Maven Profile Error]({{< relref "/tools/maven/maven-profile-error" >}}) — profile activation issues
