---
title: "Maven Could Not Find Artifact in Repository"
description: "Maven cannot find a required artifact in any configured repository."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Maven Could Not Find Artifact in Repository

This error occurs when Maven cannot locate a required artifact in any configured repository. The build stops because a declared dependency is unavailable at the specified coordinates.

## Common Causes

- Artifact groupId, artifactId, or version is misspelled
- Artifact does not exist in Maven Central or configured repos
- Custom repository URL is incorrect
- Repository requires authentication that is not configured
- Network issues preventing repository access

## How to Fix

### Verify Artifact Exists

```bash
mvn dependency:get -Dartifact=com.example:library:1.0.0
```

### Search Maven Central

Visit [search.maven.org](https://search.maven.org) and verify the correct coordinates.

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
        <username>deploy-user</username>
        <password>${env.REPO_PASSWORD}</password>
    </server>
</servers>
```

### Force Update Snapshots

```bash
mvn clean install -U
```

### Clear Local Repository Cache

```bash
rm -rf ~/.m2/repository/com/example/library/
mvn clean install
```

## Examples

```text
[ERROR] Failed to execute goal on project my-app:
  Could not find artifact com.example:missing-lib:jar:1.0.0
  in central (https://repo.maven.apache.org/maven2)
```

## Related Errors

- [Maven Repository Error]({{< relref "/tools/maven/maven-repository-error" >}}) — repository connection failure
- [Maven Build Error]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
- [Maven Dependency Tree Error]({{< relref "/tools/maven/maven-dependency-tree-error" >}}) — dependency conflicts
