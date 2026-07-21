---
title: "Gradle Local Repository Missing"
description: "Gradle cannot find a dependency in the local Maven repository or the configured local file repository path does not exist."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Local Repository Missing

Gradle resolves dependencies from remote repositories and can also use a local Maven repository or a file-based repository. This error occurs when a configured local repository path does not exist or the local Maven cache is empty.

## Common Causes

- The local repository directory path in `build.gradle` is incorrect
- The `~/.m2/repository` directory has not been populated by a Maven install
- A file-based repository points to a path that was deleted or moved
- The repository declaration uses a relative path that resolves incorrectly

## How to Fix

1. Verify the local repository path exists:

```bash
ls -la ~/.m2/repository
```

2. Check the repository configuration in `build.gradle`:

```groovy
repositories {
    mavenLocal()
    maven {
        url uri('/opt/local-repo')
    }
}
```

3. Create the directory if it does not exist:

```bash
mkdir -p /opt/local-repo
```

4. Install artifacts to the local repository manually:

```bash
mvn install:install-file \
  -Dfile=library-1.0.jar \
  -DgroupId=com.example \
  -DartifactId=library \
  -Dversion=1.0.0 \
  -Dpackaging=jar
```

## Examples

```bash
# Error output
Could not resolve all dependencies for configuration ':classpath'.
> Could not find com.example:local-lib:1.0.0.
  Searched in the following locations:
    - file:/opt/local-repo/com/example/local-lib/1.0.0/
    - Required by: project :
```

```groovy
// Correct local repository configuration
repositories {
    mavenLocal()
    maven {
        url = file("${projectDir}/local-repo")
    }
    mavenCentral()
}
```

## Related Errors

- [Repository Not Defined]({{< relref "/tools/gradle/gradle-repository-not-defined" >}}) -- missing repository declarations
- [Dependency Error]({{< relref "/tools/gradle/gradle-dependency-error" >}}) -- general dependency resolution failures
