---
title: "[Solution] IntelliJ IDEA Compilation failed"
description: "Fix IntelliJ IDEA compilation failures. Resolve build errors, missing dependencies, and compiler configuration issues."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "compilation", "build", "compiler", "javac"]
severity: "error"
---

# Compilation failed

## Error Message

```
Compilation failed
error: package org.springframework.boot does not exist
error: cannot find symbol
  symbol: variable logger
  location: class ApplicationService
Build completed with 5 errors in 2 files
Compilation failed: java compilation failed with exit code 1
```

## Common Causes

- Missing or incorrectly resolved dependencies in the project
- JDK version mismatch between project settings and system
- Source directory not marked as Source Root in the IDE
- Annotation processor not generating expected source files
- Build output directory is corrupted or has stale class files

## Solutions

### Solution 1: Rebuild Project Completely

Perform a clean build to remove stale class files and rebuild from scratch.

```
# In IDE:
Build → Rebuild Project

# Or from terminal:
mvn clean compile
# or
./gradlew clean build

# For full clean including IDE caches:
Build → Clean Project
Build → Rebuild Project
```

### Solution 2: Verify Source Root Configuration

Ensure all source directories are correctly marked in the project structure.

```
File → Project Structure → Modules
# Select your module → Sources tab
# Verify:
#   - src/main/java is marked as 'Sources' (blue)
#   - src/main/resources is marked as 'Resources' (green)
#   - src/test/java is marked as 'Test Sources' (green)
#   - build/output dirs are marked as 'Excluded' (red)

# To mark a directory:
# Right-click directory → Mark Directory as → Sources Root
```

### Solution 3: Configure Correct JDK Version

Ensure the project SDK and language level match your code requirements.

```
File → Project Structure → Project
# Project SDK: Select correct JDK version
# Project language level: Match your source code level

# For module-specific settings:
File → Project Structure → Modules → [Module] → Dependencies
# Set Module SDK to 'Project SDK' or a specific JDK

# Verify JDK installation:
# File → Project Structure → SDKs
# Ensure JDK path is valid and recognized
```

### Solution 4: Fix Missing Dependencies

Add missing library dependencies to the project configuration.

```xml
<!-- For Maven projects, verify pom.xml: -->
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
        <version>3.2.0</version>
    </dependency>
</dependencies>

<!-- After editing pom.xml: -->
# Maven Tool Window → Click 'Reload All Maven Projects'
```

## Prevention Tips

- Keep the IDE's build system in sync with the command-line build tool
- Use Build → Build History to compare successful and failed builds
- Enable 'Build project automatically' in Settings → Compiler for incremental builds
- Check 'Compile independent modules in parallel' for faster builds

## Related Errors

- [Gradle Integration Error]({{< relref "/tools/intellij/gradle-integration-error" >}})
- [Maven Integration Error]({{< relref "/tools/intellij/maven-integration-error" >}})
- [Run Configuration Error]({{< relref "/tools/intellij/run-configuration-error" >}})
