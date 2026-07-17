---
title: "Maven Dependency Resolution Error"
description: "Maven cannot resolve a required dependency from any configured repository."
tools: ["maven"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Maven Dependency Resolution Error

Maven dependency resolution error means Maven searched all configured repositories but could not find the artifact specified in the `pom.xml`. The build cannot proceed without the required dependency.

## Common Causes

- The artifact coordinates (groupId, artifactId, version) are misspelled
- The artifact does not exist in Maven Central or custom repositories
- A custom repository URL is incorrect or requires authentication
- Network issues prevent repository access
- Local repository cache is corrupted

## How to Fix

### Verify Artifact Coordinates

```bash
mvn dependency:get -Dartifact=com.example:library:1.0.0
```

### Check Maven Central

Search [Maven Central](https://search.maven.org) for the correct artifact coordinates.

### Add Missing Repository

```xml
<repositories>
    <repository>
        <id>custom-repo</id>
        <url>https://repo.example.com/releases</url>
    </repository>
</repositories>
```

### Configure Repository Authentication

```xml
<!-- ~/.m2/settings.xml -->
<servers>
    <server>
        <id>custom-repo</id>
        <username>your-username</username>
        <password>your-password</password>
    </server>
</servers>
```

### Force Update Snapshots

```bash
mvn clean install -U
```

### Check Network Connectivity

```bash
curl -I https://repo.maven.apache.org/maven2/
```

### Clear Local Repository

```bash
rm -rf ~/.m2/repository/com/example/library/
mvn clean install
```

## Examples

```bash
mvn clean install
[ERROR] Failed to execute goal on project my-app:
Could not find artifact com.example:library:jar:1.0.0 in
central (https://repo.maven.apache.org/maven2)
```

## Related Errors

- [Build Failed]({{< relref "/tools/maven/build-failed" >}}) — general build failure
- [Repository Error]({{< relref "/tools/maven/repository-error" >}}) — repository connection failure
