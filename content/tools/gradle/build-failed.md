---
title: "Build Failed: Could Not Resolve Dependencies"
description: "Gradle build failed because it could not resolve one or more dependencies from the configured repositories."
tools: ["gradle"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

This error occurs when Gradle cannot download or resolve a dependency declared in your build configuration. The build stops and reports a failure related to dependency resolution.

## Common Causes

- The dependency artifact or version does not exist in any configured repository
- Repository URLs are incorrect or unreachable
- Authentication credentials are missing or expired for a private repository
- Network connectivity issues prevent downloading artifacts

## How to Fix

Check that the dependency coordinates are correct in your `build.gradle`:

```groovy
dependencies {
    implementation 'com.example:library:1.0.0' // verify group, artifact, and version
}
```

Verify your repository configuration:

```groovy
repositories {
    mavenCentral()
    maven {
        url 'https://repo.example.com/maven'
        credentials {
            username = findProperty('repoUser') ?: ''
            password = findProperty('repoPass') ?: ''
        }
    }
}
```

Run with debug output to see which repositories were checked:

```bash
./gradlew build --info
```

## Examples

```
FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileJava'.
> Could not resolve all files for configuration ':classpath'.
   > Could not find com.example:library:1.0.0.
     Searched in the following locations:
       - https://repo.maven.apache.org/maven2/com/example/library/1.0.0/
```

## Related Errors

- [Out of Memory]({{< relref "/tools/gradle/out-of-memory" >}})
