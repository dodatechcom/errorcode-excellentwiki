---
title: "Maven Repository Layout Error"
description: "Maven repository URL or layout configuration is incorrect, preventing artifact resolution from custom or corporate repositories."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Repository Layout Error

Maven repositories use a specific directory layout based on groupId, artifactId, and version. A layout error occurs when the repository URL or layout type does not match the actual structure.

## Common Causes

- The repository URL is missing a trailing slash or contains extra path segments
- A legacy layout repository is configured without `<layout>legacy</layout>`
- The repository uses a flat layout that Maven does not recognize
- The repository ID in settings.xml does not match the POM declaration

## How to Fix

1. Verify the repository URL follows Maven convention:

```xml
<repository>
  <id>my-repo</id>
  <url>https://repo.example.com/maven2</url>
</repository>
```

2. Use legacy layout for older repositories:

```xml
<repository>
  <id>legacy-repo</id>
  <url>https://repo.example.com/maven</url>
  <layout>legacy</layout>
</repository>
```

3. Check the repository structure:

```bash
# Expected layout: groupId/artifactId/version/artifact-version.jar
curl https://repo.example.com/maven2/com/example/lib/1.0.0/lib-1.0.0.pom
```

4. Match the repository ID between POM and settings.xml:

```xml
<!-- settings.xml must use the same ID -->
<servers>
  <server>
    <id>my-repo</id> <!-- matches POM repository id -->
    <username>user</username>
    <password>pass</password>
  </server>
</servers>
```

## Examples

```bash
# Error output
[ERROR] Could not find artifact com.example:lib:1.0.0 in repo (https://repo.example.com/maven2/)
```

```xml
<!-- Correct repository configuration -->
<repository>
  <id>company-repo</id>
  <name>Company Repository</name>
  <url>https://repo.company.com/maven/releases</url>
  <layout>default</layout>
</repository>
```

## Related Errors

- [Repository Error]({{< relref "/tools/maven/maven-repository-error" >}}) -- repository access issues
- [Repository Not Accessible]({{< relref "/tools/maven/maven-repository-not-accessible" >}}) -- unreachable repositories
