---
title: "[Solution] Maven Packaging Error"
description: "Fix Maven packaging errors. Resolve JAR, WAR, and EAR packaging configuration issues."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["maven", "packaging", "jar", "war", "ear", "assembly"]
weight: 5
---

# Maven Packaging Error

A packaging error occurs when Maven cannot create the final artifact (JAR, WAR, EAR) due to configuration issues, missing dependencies, or invalid file structures.

## Common Causes

- The packaging type is not specified or is invalid
- Required files (e.g., `web.xml` for WAR) are missing
- Duplicate resources or class files cause conflicts
- The assembly descriptor is malformed

## How to Fix

### Set Packaging in pom.xml

```xml
<project>
    <packaging>jar</packaging>  <!-- or war, ear, pom -->
</project>
```

### Fix WAR Packaging

```xml
<packaging>war</packaging>

<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-war-plugin</artifactId>
            <version>3.4.0</version>
            <configuration>
                <failOnMissingWebXml>false</failOnMissingWebXml>
            </configuration>
        </plugin>
    </plugins>
</build>
```

### Fix Duplicate Resources

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-jar-plugin</artifactId>
    <configuration>
        <archive>
            <manifest>
                <mainClass>com.example.Main</mainClass>
            </manifest>
        </archive>
    </configuration>
</plugin>
```

### Use Shade Plugin for Uber JAR

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-shade-plugin</artifactId>
    <version>3.5.1</version>
    <executions>
        <execution>
            <phase>package</phase>
            <goals><goal>shade</goal></goals>
        </execution>
    </executions>
</plugin>
```

## Examples

```bash
# Missing web.xml for WAR packaging
mvn package
# [ERROR] Missing: web.xml in specified source directory
# Fix: add src/main/webapp/WEB-INF/web.xml or set failOnMissingWebXml=false

# Invalid assembly descriptor
mvn package
# [ERROR] Failed to execute goal maven-assembly-plugin
# Fix: validate the assembly descriptor XML
```

## Related Errors

- [Plugin Error]({{< relref "/tools/maven/plugin-error2" >}}) — plugin execution failure
- [Build Failed]({{< relref "/tools/maven/build-failed" >}}) — general build failure
