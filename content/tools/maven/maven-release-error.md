---
title: "Maven Release SNAPSHOT Version Error"
description: "Maven release plugin fails with SNAPSHOT version error."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["maven", "release", "snapshot", "version", "deploy"]
weight: 5
---

# Maven Release — SNAPSHOT Version Error

This error occurs when the Maven release plugin encounters issues with SNAPSHOT versions. The release process fails because of SNAPSHOT dependencies, uncommitted changes, or incorrect version configuration.

## Common Causes

- Project contains SNAPSHOT dependencies
- Working directory has uncommitted changes
- Release version already exists in repository
- SCM connection not configured
- Version number format is invalid

## How to Fix

### Prepare the Release

```bash
mvn release:prepare -DdevelopmentVersion=1.1-SNAPSHOT -DreleaseVersion=1.0
```

### Check for SNAPSHOT Dependencies

```bash
mvn dependency:tree | grep SNAPSHOT
```

### Remove SNAPSHOT Versions

```xml
<dependency>
    <groupId>com.example</groupId>
    <artifactId>library</artifactId>
    <version>1.0.0</version>  <!-- use release version -->
</dependency>
```

### Clean Up Failed Release

```bash
mvn release:clean
```

### Configure Release Plugin

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-release-plugin</artifactId>
    <version>3.0.1</version>
    <configuration>
        <tagNameFormat>v@{project.version}</tagNameFormat>
        <autoVersionSubmodules>true</autoVersionSubmodules>
    </configuration>
</plugin>
```

### Commit Changes Before Release

```bash
git status
git add -A
git commit -m "Prepare for release"
mvn release:prepare release:perform
```

## Examples

```text
[ERROR] The repository contains uncommitted changes.
[ERROR] Cannot prepare a release version when the POM contains SNAPSHOT dependencies.
[ERROR] Could not find the SCM URL in the POM.
```

## Related Errors

- [Maven Dependency Error]({{< relref "/tools/maven/maven-dependency-error" >}}) — dependency resolution failure
- [Maven Multi Module Error]({{< relref "/tools/maven/maven-multi-module-error" >}}) — reactor build issues
- [Maven Build Error]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
