---
title: "Maven Profile Error"
description: "Maven profile configuration error prevents the build from activating or running correctly."
tools: ["maven"]
error-types: ["build-error"]
severities: ["error"]
tags: ["maven", "profile", "configuration", "activation", "properties"]
weight: 5
---

# Maven Profile Error

A Maven profile error occurs when a build profile has invalid configuration, cannot be activated, or conflicts with other profiles. Profiles customize the build for different environments.

## Common Causes

- Invalid profile activation conditions
- Profile references undefined properties
- Conflicting profiles with incompatible configurations
- Profile ID contains invalid characters

## How to Fix

### List Available Profiles

```bash
mvn help:active-profiles
```

### Check Profile Activation

```xml
<profile>
    <id>production</id>
    <activation>
        <property>
            <name>env</name>
            <value>prod</value>
        </property>
    </activation>
    <properties>
        <db.url>jdbc:mysql://prod-server/db</db.url>
    </properties>
</profile>
```

### Activate Profile Correctly

```bash
# Via property
mvn clean install -Denv=prod

# Via profile ID
mvn clean install -Pproduction
```

### Fix Undefined Properties

```xml
<profile>
    <id>dev</id>
    <properties>
        <db.url>jdbc:mysql://localhost/db</db.url>
    </properties>
</profile>
```

### Validate Profile Configuration

```bash
mvn help:effective-pom -Pdev
```

### Check for Profile Conflicts

```bash
mvn help:active-profiles -Denv=prod -Pproduction
```

## Examples

```bash
mvn clean install -Pprod
[ERROR] Failed to execute goal
[ERROR] Profile 'prod' references undefined property: db.url
```

## Related Errors

- [Build Failed]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
- [Configuration Error]({{< relref "/tools/maven/maven-profile-error" >}}) — profile configuration error
