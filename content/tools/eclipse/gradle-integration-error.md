---
title: "[Solution] Eclipse Gradle integration error"
description: "Gradle integration error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "gradle", "buildship", "groovy"]
severity: "error"
---

# Gradle integration error

## Error Message

```
Could not run build script 'build.gradle': Could not determine the dependencies of task ':compileJava'. > Failed to find target with hash string 'android-33'
```

## Common Causes

- The Gradle Buildship plugin cannot locate the required Gradle distribution or Java toolchain.
- The `build.gradle` file references SDK versions or dependencies not available in the current environment.
- A Gradle daemon from a previous session is holding file locks.

## Solutions

### Solution 1: Refresh the Gradle Project

Right-click the project in **Package Explorer** and select **Gradle > Refresh Gradle Project** (or use the keyboard shortcut **Alt+F5**). This forces Buildship to re-read `build.gradle` and reconfigure the Eclipse classpath. If this fails, try deleting the `.gradle` and `bin` directories.

```java
# Kill stale Gradle daemons
gradle --stop

# Delete Buildship metadata
rm -rf <project>/.settings/org.eclipse.buildship.core.prefs
rm -rf <project>/.gradle/

# Re-import via File > Import > Gradle > Existing Gradle Project
```

### Solution 2: Configure Gradle Wrapper

Ensure the project uses the Gradle Wrapper (`gradlew`) for consistent builds. Edit `gradle/wrapper/gradle-wrapper.properties` to point to the correct distribution URL matching the project's required Gradle version.

```bash
# Run Gradle wrapper to download and cache the correct version
./gradlew wrapper --gradle-version 8.2

# Verify the wrapper properties
cat gradle/wrapper/gradle-wrapper.properties
distributionUrl=https\://services.gradle.org/distributions/gradle-8.2-bin.zip
```

## Prevention Tips

- Use the Gradle Wrapper (`gradlew`) exclusively to avoid version mismatches between team members.
- Set **Window > Preferences > Buildship > Gradle** to use the wrapper distribution by default.
- Check **Window > Show View > Error Log** for detailed Buildship error traces.

## Related Errors

- [maven-integration-error]({{< relref "/tools/eclipse/maven-integration-error" >}})
- [build-path-error]({{< relref "/tools/eclipse/build-path-error" >}})
- [compilation-error]({{< relref "/tools/eclipse/compilation-error" >}})
