---
title: "Could Not Find Artifact"
description: "Maven cannot find a required artifact in any configured repository, preventing the build from proceeding."
tools: ["maven"]
error-types: ["build-error"]
severities: ["error"]
tags: ["maven", "dependency", "artifact", "resolution"]
weight: 5
---

This error means Maven looked in all configured repositories (local, central, and custom) but could not find the artifact specified in your `pom.xml`.

## Common Causes

- The artifact coordinates (groupId, artifactId, version) are misspelled
- The artifact has been removed from Maven Central or never published
- A custom repository URL is incorrect or requires authentication
- The artifact only exists in a private repository not configured in the build

## How to Fix

Verify the artifact coordinates on [Maven Central](https://search.maven.org):

```bash
mvn dependency:get -Dartifact=com.example:library:1.0.0
```

Add the correct repository if the artifact is not on Central:

```xml
<repositories>
    <repository>
        <id>custom-repo</id>
        <url>https://repo.example.com/releases</url>
    </repository>
</repositories>
```

If using a private repository, configure credentials in your `settings.xml`:

```xml
<servers>
    <server>
        <id>custom-repo</id>
        <username>your-username</username>
        <password>your-password</password>
    </server>
</servers>
```

## Examples

```
[ERROR] Failed to execute goal on project my-app: Could not find artifact com.example:library:jar:1.0.0 in
        https://repo.maven.apache.org/maven2 (https://repo.maven.apache.org/maven2)
```

## Related Errors

- [Build Failed]({{< relref "/tools/maven/build-failed" >}})
