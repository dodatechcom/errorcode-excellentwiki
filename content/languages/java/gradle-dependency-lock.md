---
title: "[Solution] Could Not Resolve Dependencies — Gradle Dependency Lock Fix"
description: "Fix Gradle dependency lock errors. Resolve 'Could not resolve all dependencies' and dependency resolution failures."
languages: ["java"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Could Not Resolve Dependencies — Gradle Dependency Lock Fix

A Gradle dependency lock error occurs when Gradle cannot resolve one or more dependencies during the build. This happens when a dependency is not found in any configured repository, or when version constraints cannot be satisfied.

## What This Error Means

Common messages:

- `Could not resolve all dependencies for configuration ':app:implementation'`
- `Could not find com.example:library:3.0.0`
- `Could not resolve com.google.guava:guava:31.1-jre`

## Common Causes

```groovy
// Cause 1: Dependency not in any configured repository
dependencies {
    implementation 'com.example:internal-lib:1.0.0' // Not in Maven Central
}

// Cause 2: Version does not exist
dependencies {
    implementation 'com.google.guava:guava:99.99.99' // Invalid version
}

// Cause 3: Repository authentication failure
repositories {
    maven {
        url 'https://private.repo.com/maven'
        // Missing credentials
    }
}

// Cause 4: Network or proxy issues
```

## How to Fix

### Fix 1: Verify dependency coordinates and versions

Double-check that the group, artifact, and version exist in the configured repositories.

```java
// Check if dependency exists on Maven Central
// https://search.maven.org/artifact/com.example/library/1.0.0

// Use gradle dependencies to inspect the resolution
// ./gradlew :app:dependencies --configuration implementation

// Filter for specific dependency
./gradlew :app:dependencies --configuration implementation \
    | grep "com.example:library"

// Show all repositories being checked
./gradlew :app:dependencies --configuration implementation \
    --info
```

### Fix 2: Configure repositories and authentication

Ensure all required repositories are configured with correct URLs and credentials.

```java
// settings.gradle.kts
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        mavenCentral()
        maven {
            url = uri("https://private.repo.com/maven")
            credentials {
                username = System.getenv("MAVEN_USER") ?: ""
                password = System.getenv("MAVEN_PASSWORD") ?: ""
            }
        }
    }
}

// For offline builds
// ./gradlew build --offline
```

### Fix 3: Use dependency locking for reproducible builds

Enable Gradle dependency locking to pin exact versions and prevent resolution failures.

```java
// build.gradle.kts
dependencyLocking {
    lockAllConfigurations()
    // Or lock specific configurations
    lockMode.set(LockMode.STRICT)
}

// Generate lock file
./gradlew resolveAndLockAll --write-locks

// The gradle/dependency-locks/*.lockfile pins exact versions:
// com.google.guava:guava:31.1-jre=compile, runtime
// org.junit.jupiter:junit-jupiter:5.10.0=test
```

## Related Errors

- {{< relref "gradle-task-failed" >}} — Task Execution Failed
- {{< relref "maven-dependency-conflict" >}} — Maven Dependency Version Conflict
