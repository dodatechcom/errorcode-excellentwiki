---
title: "Maven WAR Overlapped Resources Error"
description: "Maven WAR plugin fails because multiple resource directories produce overlapping files in the WEB-INF directory."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven WAR Overlapped Resources Error

The Maven WAR plugin assembles web application resources. An overlapped resources error occurs when multiple `<resource>` directories contain files with the same relative path.

## Common Causes

- Multiple `<resource>` blocks point to directories with overlapping content
- Filtered and non-filtered versions of the same file exist
- A dependency JAR contains the same files as the web resources directory
- The `failOnMissingWebXml` setting conflicts with resource overlap

## How to Fix

1. Identify overlapping resources:

```bash
mvn war:war -X 2>&1 | grep -i "overlap\|duplicate"
```

2. Merge resource directories to avoid overlap:

```xml
<build>
  <resources>
    <resource>
      <directory>src/main/resources</directory>
      <filtering>true</filtering>
    </resource>
  </resources>
</build>
```

3. Use the `excludes` element to prevent overlap:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-war-plugin</artifactId>
  <version>3.4.0</version>
  <configuration>
    <overlays>
      <overlay>
        <groupId>com.example</groupId>
        <artifactId>shared-web</artifactId>
        <excludes>
          <exclude>WEB-INF/web.xml</exclude>
        </excludes>
      </overlay>
    </overlays>
  </configuration>
</plugin>
```

4. Check the WAR contents after building:

```bash
jar tf target/my-app.war | sort | uniq -d
```

## Examples

```bash
# Error output
[WARNING] Overlapping resources detected:
  src/main/webapp/WEB-INF/web.xml
  src/main/webapp/WEB-INF/views/web.xml
```

```xml
<!-- WAR plugin with overlay configuration -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-war-plugin</artifactId>
  <configuration>
    <failOnMissingWebXml>false</failOnMissingWebXml>
    <overlays>
      <overlay>
        <excludes>
          <exclude>META-INF/**</exclude>
        </excludes>
      </overlay>
    </overlays>
  </configuration>
</plugin>
```

## Related Errors

- [WAR Plugin Error]({{< relref "/tools/maven/maven-war-plugin-error" >}}) -- WAR plugin issues
- [Web XML Missing]({{< relref "/tools/maven/maven-web-xml-missing" >}}) -- missing web.xml
