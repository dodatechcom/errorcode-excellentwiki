---
title: "Maven OSGi Manifest Error"
description: "Maven build fails to generate valid OSGi manifest headers, preventing the bundle from being loaded by an OSGi container."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven OSGi Manifest Error

OSGi bundles require specific manifest headers like `Bundle-SymbolicName`, `Export-Package`, and `Import-Package`. An error occurs when the maven-bundle-plugin cannot generate valid headers.

## Common Causes

- The maven-bundle-plugin is not configured or not included
- Package exports reference packages that do not exist
- Import-Package headers conflict with the bundle's actual dependencies
- The bundle symbolic name contains invalid characters

## How to Fix

1. Add and configure the maven-bundle-plugin:

```xml
<plugin>
  <groupId>org.apache.felix</groupId>
  <artifactId>maven-bundle-plugin</artifactId>
  <version>5.1.9</version>
  <extensions>true</extensions>
  <configuration>
    <instructions>
      <Bundle-SymbolicName>${project.groupId}.${project.artifactId}</Bundle-SymbolicName>
      <Bundle-Name>${project.name}</Bundle-Name>
      <Export-Package>com.example.api</Export-Package>
      <Import-Package>*</Import-Package>
    </instructions>
  </configuration>
</plugin>
```

2. Verify exported packages exist:

```bash
ls -la src/main/java/com/example/api/
```

3. Check the generated manifest for errors:

```bash
unzip -p target/*.jar META-INF/MANIFEST.MF
```

4. Use `maven-bundle-plugin:manifest` to test header generation:

```bash
mvn bundle:manifest
```

## Examples

```bash
# Error output
[ERROR] Failed to execute goal org.apache.felix:maven-bundle-plugin:5.1.9
  (bundle-manifest): Missing packages in Export-Package:
  com.example.api.impl (not found in project)
```

```xml
<!-- Correct OSGi bundle configuration -->
<plugin>
  <groupId>org.apache.felix</groupId>
  <artifactId>maven-bundle-plugin</artifactId>
  <version>5.1.9</version>
  <extensions>true</extensions>
  <configuration>
    <instructions>
      <_dsannotations>*</_dsannotations>
      <Bundle-SymbolicName>${project.groupId}.${project.artifactId}</Bundle-SymbolicName>
      <Export-Package>com.example.api;version="${project.version}"</Export-Package>
    </instructions>
  </configuration>
</plugin>
```

## Related Errors

- [Jar Plugin Error]({{< relref "/tools/maven/maven-jar-plugin-error" >}}) -- JAR packaging issues
- [Packaging Type Invalid]({{< relref "/tools/maven/maven-packaging-type-invalid" >}}) -- invalid packaging types
