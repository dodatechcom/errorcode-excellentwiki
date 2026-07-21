---
title: "Maven Missing Plugin Artifact Error"
description: "Maven cannot find the plugin artifact in any repository, causing the build to fail before plugin execution begins."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Missing Plugin Artifact Error

Maven plugins are resolved from repositories before execution. A missing artifact error means the plugin JAR or its dependencies cannot be downloaded.

## Common Causes

- The plugin groupId, artifactId, or version is incorrect
- The plugin is only available in a repository not configured in the build
- The repository hosting the plugin is temporarily unavailable
- The plugin was removed from Maven Central

## How to Fix

1. Verify the plugin coordinates are correct:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <version>3.11.0</version>
</plugin>
```

2. Check if the plugin exists on Maven Central:

```bash
curl -I https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.11.0/maven-compiler-plugin-3.11.0.pom
```

3. Add the repository if the plugin is not on Central:

```xml
<pluginRepositories>
  <pluginRepository>
    <id>custom</id>
    <url>https://repo.example.com/releases</url>
  </pluginRepository>
</pluginRepositories>
```

4. Force update of plugin metadata:

```bash
mvn clean install -U
```

## Examples

```bash
# Error output
[ERROR] Plugin org.example:custom-plugin:1.0.0 or one of its dependencies
  could not be resolved: Cannot access central in offline mode
```

```xml
<!-- Correct plugin repository configuration -->
<pluginRepositories>
  <pluginRepository>
    <id>custom-releases</id>
    <url>https://repo.example.com/releases</url>
    <releases>
      <enabled>true</enabled>
    </releases>
  </pluginRepository>
</pluginRepositories>
```

## Related Errors

- [Plugin Error]({{< relref "/tools/maven/maven-plugin-error" >}}) -- general plugin failures
- [Plugin Not Found]({{< relref "/tools/maven/maven-plugin-not-found" >}}) -- plugin resolution failures
