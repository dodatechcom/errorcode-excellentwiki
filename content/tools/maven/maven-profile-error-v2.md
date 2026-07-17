---
title: "Maven Profile Activation Error"
description: "Maven profile is not active or fails to activate during build."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Maven Profile Not Active — Activation Error

This error occurs when a Maven profile fails to activate or is not active when expected. Dependencies or configurations provided by the profile are missing, causing the build to fail.

## Common Causes

- Profile activation conditions not met
- Missing properties required for profile activation
- Incorrect profile ID in command line
- Profile is defined in a parent POM but not inherited
- File-based activation path does not exist

## How to Fix

### List Active Profiles

```bash
mvn help:active-profiles
```

### Activate Profile by ID

```bash
mvn clean install -P production
```

### Define Profile with Correct Activation

```xml
<profiles>
    <profile>
        <id>production</id>
        <activation>
            <property>
                <name>env</name>
                <value>prod</value>
            </property>
        </activation>
        <dependencies>
            <!-- production-only dependencies -->
        </dependencies>
    </profile>
</profiles>
```

### Set Required Properties

```bash
mvn clean install -Denv=prod
```

### Activate Multiple Profiles

```bash
mvn clean install -P production,docker
```

### Use File-Based Activation

```xml
<profile>
    <id>local-dev</id>
    <activation>
        <file>
            <exists>local.properties</exists>
        </file>
    </activation>
</profile>
```

## Examples

```text
[WARNING] The following profiles could not be activated:
  - production (activation: property 'env' must equal 'prod')
```

## Related Errors

- [Maven Build Error]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
- [Maven Dependency Error]({{< relref "/tools/maven/maven-dependency-error" >}}) — missing dependencies
- [Maven Multi Module Error]({{< relref "/tools/maven/maven-multi-module-error" >}}) — reactor build issues
