---
title: "Maven Encoding Configuration Error"
description: "Maven build fails because source or resource encoding is not configured, causing platform-dependent character corruption."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Encoding Configuration Error

Maven requires explicit encoding configuration to ensure consistent builds across platforms. An encoding error occurs when source files contain characters that do not match the platform default encoding.

## Common Causes

- The `project.build.sourceEncoding` property is not set
- Source files use UTF-8 but the platform default is a different encoding
- The `maven.compiler.sourceEncoding` property is missing
- Resource filtering corrupts non-ASCII characters

## How to Fix

1. Set the source encoding in your `pom.xml`:

```xml
<properties>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
</properties>
```

2. Configure the compiler encoding explicitly:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <configuration>
    <encoding>UTF-8</encoding>
  </configuration>
</plugin>
```

3. Set the resource filtering encoding:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-resources-plugin</artifactId>
  <configuration>
    <encoding>UTF-8</encoding>
  </configuration>
</plugin>
```

4. Verify file encoding before build:

```bash
file -i src/main/java/com/example/*.java
```

## Examples

```xml
<!-- Complete encoding configuration -->
<properties>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
  <maven.compiler.encoding>UTF-8</maven.compiler.encoding>
</properties>
```

```
[WARNING] Using platform encoding (UTF-8 actually) to copy filtered resources,
  i.e. build is platform dependent!
```

## Related Errors

- [Resource Encoding Error]({{< relref "/tools/maven/maven-resource-encoding-error" >}}) -- resource file encoding
- [Filtering Resource Error]({{< relref "/tools/maven/maven-filtering-resource-error" >}}) -- resource filtering issues
