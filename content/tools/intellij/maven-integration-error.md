---
title: "[Solution] IntelliJ IDEA Maven import failed"
description: "Fix IntelliJ IDEA Maven import failures. Resolve POM parsing errors, dependency resolution, and repository access issues."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "maven", "build-system", "dependency-management"]
severity: "error"
---

# Maven import failed

## Error Message

```
Maven import failed: Non-resolvable parent POM for project 'my-app':
Could not find artifact com.example:parent:pom:1.0.0
Failed to execute goal on project my-app:
Could not resolve dependencies for project
```

## Common Causes

- Maven repository is unreachable or down
- Corrupted local Maven repository (~/.m2/repository)
- Incorrect POM.xml syntax or missing dependency artifacts
- Network timeout during large dependency downloads
- JDK version mismatch with Maven compiler plugin settings

## Solutions

### Solution 1: Re-Import Maven Project

Force a complete Maven re-import to rebuild the project model. Click the **Maven reload icon** in the Maven tool window or use the menu.

```
# In IDE:
Maven Tool Window → Click 'Reload All Maven Projects' (refresh icon)

# Or from menu:
File → Invalidate Caches and Restart

# From command line:
mvn clean install -U
# -U forces snapshot updates from remote repositories
```

### Solution 2: Clear Local Maven Repository

Remove corrupted artifacts from the local Maven cache and re-download them.

```bash
# Clear entire local repository:
rm -rf ~/.m2/repository/

# Or clear specific artifact:
rm -rf ~/.m2/repository/com/example/my-artifact/

# Then re-import in IDE
# For a more surgical approach, find and delete _remote.repositories files:
find ~/.m2/repository -name '_remote.repositories' -delete
```

### Solution 3: Configure Maven in IDE Settings

Verify the Maven executable path and JDK are correctly configured in IDE settings.

```
File → Settings → Build Tools → Maven
# Verify:
#   - Maven home path: Bundled (Maven 3) or custom installation
#   - User settings file: ~/.m2/settings.xml
#   - Local repository: ~/.m2/repository
#   - JDK: Match the project SDK

# For Maven runner settings:
File → Settings → Build Tools → Maven → Runner
# Ensure JRE is set to correct JDK version
```

### Solution 4: Fix Maven Settings.xml Proxy

Configure proxy and mirror settings in Maven's settings.xml for corporate environments.

```xml
<!-- ~/.m2/settings.xml -->
<settings>
  <proxies>
    <proxy>
      <id>corporate-proxy</id>
      <active>true</active>
      <protocol>https</protocol>
      <host>proxy.company.com</host>
      <port>8080</port>
    </proxy>
  </proxies>
  <mirrors>
    <mirror>
      <id>nexus</id>
      <mirrorOf>*</mirrorOf>
      <url>https://nexus.company.com/repository/maven-public/</url>
    </mirror>
  </mirrors>
</settings>
```

## Prevention Tips

- Always use the 'Maven reimport' feature after changing pom.xml
- Keep the Maven repository clean by running 'mvn dependency:purge-local-repository' periodically
- Use 'mvn dependency:tree' to diagnose transitive dependency conflicts
- Configure Maven offline mode in IDE settings for faster builds when dependencies are cached

## Related Errors

- [Gradle Integration Error]({{< relref "/tools/intellij/gradle-integration-error" >}})
- [Compilation Failed]({{< relref "/tools/intellij/compilation-error" >}})
- [Spring Boot Error]({{< relref "/tools/intellij/spring-boot-error" >}})
