---
title: "Maven Missing Manifest Attribute"
description: "Maven JAR build fails or produces an unusable artifact because the MANIFEST.MF file is missing required attributes."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Missing Manifest Attribute

The MANIFEST.MF file in a JAR archive contains metadata that the JVM uses to load classes. A missing manifest attribute error occurs when the JAR is built without required manifest entries.

## Common Causes

- The maven-jar-plugin is not configured to set manifest attributes
- The `Main-Class` attribute is not specified for executable JARs
- The `Class-Path` attribute is missing for JARs with external dependencies
- The manifest generation is disabled in the plugin configuration

## How to Fix

1. Configure the maven-jar-plugin to set manifest attributes:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-jar-plugin</artifactId>
  <configuration>
    <archive>
      <manifest>
        <mainClass>com.example.Main</mainClass>
        <addClasspath>true</addClasspath>
      </manifest>
    </archive>
  </configuration>
</plugin>
```

2. Add custom manifest entries:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-jar-plugin</artifactId>
  <configuration>
    <archive>
      <manifest>
        <mainClass>com.example.Main</mainClass>
      </manifest>
      <manifestEntries>
        <Built-By>${user.name}</Built-By>
        <Build-Jdk>${java.version}</Build-Jdk>
      </manifestEntries>
    </archive>
  </configuration>
</plugin>
```

3. Verify the manifest after building:

```bash
unzip -p target/my-app.jar META-INF/MANIFEST.MF
```

4. Use the Spring Boot plugin for executable JARs:

```xml
<plugin>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-maven-plugin</artifactId>
</plugin>
```

## Examples

```bash
# Verify manifest contents
jar tf target/my-app.jar | grep MANIFEST
unzip -p target/my-app.jar META-INF/MANIFEST.MF
```

```xml
<!-- Complete manifest configuration -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-jar-plugin</artifactId>
  <version>3.3.0</version>
  <configuration>
    <archive>
      <manifest>
        <mainClass>com.example.Application</mainClass>
        <addClasspath>true</addClasspath>
        <classpathPrefix>lib/</classpathPrefix>
      </manifest>
      <manifestEntries>
        <Implementation-Title>${project.name}</Implementation-Title>
        <Implementation-Version>${project.version}</Implementation-Version>
      </manifestEntries>
    </archive>
  </configuration>
</plugin>
```

## Related Errors

- [Jar Plugin Error]({{< relref "/tools/maven/maven-jar-plugin-error" >}}) -- JAR plugin issues
- [No Main Manifest Attribute]({{< relref "/tools/maven/maven-no-main-manifest-attribute" >}}) -- missing main class
