---
title: "Maven System Scope Dependency Error"
description: "Maven system scope dependencies reference local JAR files that are not portable across machines, causing build failures on different environments."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven System Scope Dependency Error

System scope dependencies point to JAR files on the local filesystem using `systemPath`. An error occurs when the referenced JAR does not exist on the build machine.

## Common Causes

- The `systemPath` uses an absolute path specific to one machine
- The JAR file was deleted or moved from the specified location
- The system scope prevents the dependency from being included in packaged artifacts
- A teammate does not have the JAR at the same filesystem path

## How to Fix

1. Install the JAR to the local repository instead:

```bash
mvn install:install-file \
  -Dfile=lib/custom.jar \
  -DgroupId=com.example \
  -DartifactId=custom-lib \
  -Dversion=1.0.0 \
  -Dpackaging=jar
```

2. Use a proper repository for internal JARs:

```xml
<repositories>
  <repository>
    <id>internal</id>
    <url>https://repo.example.com/releases</url>
  </repository>
</repositories>
```

3. If system scope is unavoidable, use `${project.basedir}`:

```xml
<dependency>
  <groupId>com.example</groupId>
  <artifactId>custom-lib</artifactId>
  <version>1.0.0</version>
  <scope>system</scope>
  <systemPath>${project.basedir}/lib/custom.jar</systemPath>
</dependency>
```

4. Add the JAR to a Git-hosted lib directory and reference relatively:

```bash
# Ensure the JAR is committed to the repository
git add lib/custom.jar
```

## Examples

```bash
# Error output
[ERROR] Could not find artifact com.example:custom-lib:jar:1.0.0 in file system
  systemPath: /Users/other-dev/lib/custom.jar (file does not exist)
```

```xml
<!-- Avoid system scope -- install to local repo instead -->
<dependency>
  <groupId>com.example</groupId>
  <artifactId>custom-lib</artifactId>
  <version>1.0.0</version>
  <!-- No scope or systemPath needed -->
</dependency>
```

## Related Errors

- [Dependency Not Found]({{< relref "/tools/maven/dependency-not-found" >}}) -- missing dependency artifacts
- [Type Not Recognized]({{< relref "/tools/maven/maven-type-not-recognized" >}}) -- unknown dependency types
