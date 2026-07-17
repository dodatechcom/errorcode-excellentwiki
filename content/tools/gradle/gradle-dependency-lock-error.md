---
title: "Gradle Dependency Lock Resolution Error"
description: "Gradle dependency lock file prevents resolution of updated or new dependencies."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Gradle Dependency Lock Resolution Error

This error occurs when Gradle's dependency lock file conflicts with the dependencies declared in the build script. The locked versions don't match what the build requires, causing a resolution failure.

## Common Causes

- Lock file outdated after dependency version change
- New dependency added without updating locks
- Transitive dependency version changed
- Lock file was committed with wrong versions

## How to Fix

### Update Dependency Locks

```bash
./gradlew dependencies --write-locks
```

### Update a Specific Configuration Lock

```bash
./gradlew dependencies --write-locks --configuration compileClasspath
```

### Resolve and Update Locks

```bash
./gradlew resolveAndLockAll --write-locks
```

### Lock Specific Configurations

```groovy
dependencyLocking {
    lockAllConfigurations()
    // or lock specific ones
    lockMode.set(LockMode.STRICT)
}
```

### Use Lenient Locking Mode

```groovy
dependencyLocking {
    lockMode.set(LockMode.LENIENT)
}
```

### Regenerate Lock File from Scratch

```bash
rm gradle.lockfile
./gradlew dependencies --write-locks
```

### Disable Locking Temporarily

```groovy
dependencyLocking {
    lockMode.set(LockMode.NO_LOCK)
}
```

## Examples

```text
Could not determine the dependencies of task ':app:compileJava'.
> Could not resolve all dependencies for ':app:compileClasspath'.
  > Could not resolve com.google.guava:guava:31.1-jre.
    > Required by: project :app
      > Locking state mismatch: locked to 30.1-jre
```

## Related Errors

- [Gradle Dependency Error]({{< relref "/tools/gradle/gradle-dependency-error" >}}) — dependency resolution failure
- [Gradle Cache Error]({{< relref "/tools/gradle/gradle-cache-error" >}}) — corrupted cache entries
- [Gradle Build Failed]({{< relref "/tools/gradle/gradle-build-failed" >}}) — general build failure
