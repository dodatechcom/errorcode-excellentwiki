---
title: "Maven Plugin Compatibility Error"
description: "Maven plugin is incompatible with the current Maven or Java version, causing the plugin to fail during goal execution."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Plugin Compatibility Error

Maven plugins may require specific Maven or Java versions. A compatibility error occurs when the installed Maven version does not meet the plugin's minimum requirements.

## Common Causes

- The plugin was built for a newer Maven API not present in the installed version
- The plugin requires Java features not available in the current JDK
- A plugin update introduced breaking API changes
- Multiple plugins with conflicting Maven version requirements are used

## How to Fix

1. Check the installed Maven version:

```bash
mvn --version
```

2. Review the plugin's requirements:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <version>3.11.0</version> <!-- check release notes for compatibility -->
</plugin>
```

3. Update Maven to the latest version:

```bash
# Using the wrapper
./mvnw wrapper:wrapper -Dmaven=3.9.6
./mvnw clean install
```

4. Downgrade the plugin to a compatible version:

```xml
<!-- Use an older version if needed -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <version>3.10.1</version>
</plugin>
```

## Examples

```bash
# Error output
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:4.0.0
  Plugin requires Maven 3.9.0 or later. Current version: 3.8.8
```

```xml
<!-- Maven version check in plugin -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <version>3.11.0</version>
  <prerequisites>
    <maven>3.6.0</maven>
  </prerequisites>
</plugin>
```

## Related Errors

- [Plugin Error]({{< relref "/tools/maven/maven-plugin-error" >}}) -- general plugin failures
- [Plugin Version Not Specified]({{< relref "/tools/maven/maven-plugin-version-not-specified" >}}) -- missing version declarations
