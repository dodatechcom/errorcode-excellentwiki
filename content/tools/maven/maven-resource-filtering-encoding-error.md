---
title: "Maven Resource Filtering Encoding Error"
description: "Maven resource filtering produces corrupted files because the encoding does not match the file content, causing character replacement failures."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Resource Filtering Encoding Error

Maven resource filtering replaces `${property}` placeholders in resource files. An encoding error occurs when the filtering process corrupts non-ASCII characters due to encoding mismatches.

## Common Causes

- Resource files use UTF-8 but filtering assumes platform encoding
- The `maven-resources-plugin` encoding is not configured
- Property values contain special characters that are not encoded
- Binary files are accidentally included in resource filtering

## How to Fix

1. Configure resource filtering encoding:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-resources-plugin</artifactId>
  <version>3.3.1</version>
  <configuration>
    <encoding>UTF-8</encoding>
    <propertiesEncoding>UTF-8</propertiesEncoding>
  </configuration>
</plugin>
```

2. Exclude binary files from filtering:

```xml
<resources>
  <resource>
    <directory>src/main/resources</directory>
    <filtering>true</filtering>
    <excludes>
      <exclude>**/*.png</exclude>
      <exclude>**/*.jar</exclude>
    </excludes>
  </resource>
</resources>
```

3. Set the global encoding property:

```xml
<properties>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>
```

4. Verify the filtered output:

```bash
mvn resources:resources
cat target/classes/config.properties
```

## Examples

```bash
# Before filtering (config.properties)
app.name=MyApp
app.description=Caf\u00e9 application

# After filtering with wrong encoding
app.description= CafÃ© application  # corrupted
```

```xml
<!-- Correct resource filtering configuration -->
<build>
  <resources>
    <resource>
      <directory>src/main/resources</directory>
      <filtering>true</filtering>
      <includes>
        <include>**/*.properties</include>
        <include>**/*.xml</include>
      </includes>
      <excludes>
        <exclude>**/*.png</exclude>
      </excludes>
    </resource>
  </resources>
</build>
```

## Related Errors

- [Resource Encoding Error]({{< relref "/tools/maven/maven-resource-encoding-error" >}}) -- resource file encoding
- [Filtering Resource Error]({{< relref "/tools/maven/maven-filtering-resource-error" >}}) -- filtering configuration
