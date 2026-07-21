---
title: "Maven Snapshot Version Error"
description: "Maven snapshot dependency resolution fails because snapshot versions are not properly configured or the repository does not host snapshots."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Snapshot Version Error

Maven snapshots are versions with a `-SNAPSHOT` suffix that resolve to the latest build. A snapshot version error occurs when the repository does not support snapshots or the version format is incorrect.

## Common Causes

- The snapshot dependency uses a non-standard version format
- The repository does not allow snapshot downloads
- The `updatePolicy` in settings.xml forces stale snapshot resolution
- The snapshot artifact was deleted from the remote repository

## How to Fix

1. Verify the snapshot version format:

```xml
<dependency>
  <groupId>com.example</groupId>
  <artifactId>my-lib</artifactId>
  <version>1.0.0-SNAPSHOT</version>
</dependency>
```

2. Configure a repository that hosts snapshots:

```xml
<repositories>
  <repository>
    <id>snapshots</id>
    <url>https://repo.example.com/snapshots</url>
    <snapshots>
      <enabled>true</enabled>
    </snapshots>
    <releases>
      <enabled>false</enabled>
    </releases>
  </repository>
</repositories>
```

3. Force update of snapshots:

```bash
mvn clean install -U
```

4. Check the snapshot repository for available versions:

```bash
curl https://repo.example.com/snapshots/com/example/my-lib/maven-metadata.xml
```

## Examples

```bash
# Error output
[ERROR] Could not find artifact com.example:my-lib:1.0.0-SNAPSHOT
```

```xml
<!-- Snapshot repository configuration -->
<repositories>
  <repository>
    <id>snapshots</id>
    <url>https://repo.example.com/snapshots</url>
    <snapshots>
      <enabled>true</enabled>
      <updatePolicy>daily</updatePolicy>
    </snapshots>
  </repository>
</repositories>
```

## Related Errors

- [Dependency Not Found]({{< relref "/tools/maven/dependency-not-found" >}}) -- missing dependency artifacts
- [Version Error]({{< relref "/tools/maven/maven-version-error" >}}) -- version resolution issues
