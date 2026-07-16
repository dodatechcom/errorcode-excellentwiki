---
title: "[Solution] Maven Profile Not Found"
description: "Fix Maven profile not found errors. Resolve profile activation and configuration issues."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["maven", "profile", "not-found", "activation", "pom"]
weight: 5
---

# Maven Profile Not Found

This error occurs when Maven cannot find a profile referenced via `-P` on the command line. The profile may not be defined in the POM, or the profile ID may be misspelled.

## Common Causes

- The profile ID is misspelled in the `-P` flag
- The profile is defined in a parent POM that is not being resolved
- The profile is in a profile-specific POM file not included in the build
- The profile is conditionally activated and does not match the current environment

## How to Fix

### List Available Profiles

```bash
mvn help:active-profiles
mvn help:all-profiles
```

### Verify Profile ID in pom.xml

```xml
<profiles>
    <profile>
        <id>production</id>  <!-- must match -P production -->
        <properties>
            <env>prod</env>
        </properties>
    </profile>
</profiles>
```

### Activate Profile from Command Line

```bash
mvn package -Pproduction
# No space between -P and profile ID
```

### Check Parent POM for Profiles

```bash
mvn help:effective-pom -Pproduction
```

### Define Profile in settings.xml

```xml
<!-- ~/.m2/settings.xml -->
<profiles>
    <profile>
        <id>production</id>
        <properties>
            <env>prod</env>
        </properties>
    </profile>
</profiles>
```

## Examples

```bash
# Typo in profile ID
mvn package -Pprodction
# The following profiles could not be resolved: prodction
# Fix: mvn package -Pproduction

# Profile defined only in child module
mvn package -Pintegration -pl module-a
# Fix: define the profile in the parent POM
```

## Related Errors

- [Settings Error]({{< relref "/tools/maven/settings-error" >}}) — Maven settings.xml issues
- [Plugin Error]({{< relref "/tools/maven/plugin-error2" >}}) — plugin execution failure
