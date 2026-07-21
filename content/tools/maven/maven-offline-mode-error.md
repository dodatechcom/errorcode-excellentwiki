---
title: "Maven Offline Mode Error"
description: "Maven offline mode fails because required dependencies or plugins are not available in the local repository cache."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Offline Mode Error

Maven offline mode (`-o`) prevents network access during builds. An error occurs when a dependency or plugin is not in the local repository and cannot be downloaded.

## Common Causes

- The dependency was never downloaded to the local repository
- The local repository was cleaned before the offline build
- A snapshot dependency was removed and the offline cache is stale
- The plugin was not installed before going offline

## How to Fix

1. Download all dependencies before going offline:

```bash
mvn dependency:go-offline
```

2. Install all plugins needed for the build:

```bash
mvn dependency:resolve-plugins
```

3. Check what is available in the local repository:

```bash
ls ~/.m2/repository/com/example/library/
```

4. Pre-build to populate the cache:

```bash
mvn clean install
mvn clean install -o  # now offline build works
```

## Examples

```bash
# Offline build error
mvn clean install -o
[ERROR] Could not resolve dependencies for project my-app
  Artifact com.example:library:jar:1.0.0 not found in local repository
  (-o option specified, cannot access remote repositories)
```

```bash
# Fix -- populate cache first
mvn dependency:go-offline
mvn clean install -o
```

## Related Errors

- [Offline Mode Error]({{< relref "/tools/maven/maven-repository-error" >}}) -- repository access issues
- [Repository Not Accessible]({{< relref "/tools/maven/maven-repository-not-accessible" >}}) -- unreachable repositories
