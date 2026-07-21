---
title: "Maven BOM Import Error"
description: "Maven BOM import fails during dependency management resolution, causing version mismatches or missing dependency versions."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven BOM Import Error

A Bill of Materials (BOM) defines dependency versions for a group of artifacts. An import error occurs when Maven cannot resolve the BOM, leading to missing version information for managed dependencies.

## Common Causes

- The BOM artifact coordinates are misspelled in the import scope
- The BOM is not available in any configured repository
- The BOM is imported inside a `<dependencies>` block instead of `<dependencyManagement>`
- The import scope is missing, causing Maven to treat it as a regular dependency

## How to Fix

1. Verify the BOM is imported with the correct scope:

```xml
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-dependencies</artifactId>
      <version>3.2.2</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

2. Ensure the BOM artifact is accessible:

```bash
mvn dependency:get -Dartifact=org.springframework.boot:spring-boot-dependencies:3.2.2:pom
```

3. Check that the BOM is not inside `<dependencies>`:

```xml
<!-- Wrong -->
<dependencies>
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-dependencies</artifactId>
    <version>3.2.2</version>
    <type>pom</type>
    <scope>import</scope>
  </dependency>
</dependencies>
```

4. Force update if the BOM is cached with errors:

```bash
mvn clean install -U
```

## Examples

```xml
<!-- Correct BOM import in dependencyManagement -->
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>io.micrometer</groupId>
      <artifactId>micrometer-bom</artifactId>
      <version>1.12.2</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

```
[ERROR] Failed to execute goal on project my-app:
  Could not find artifact org.springframework.boot:spring-boot-dependencies:3.2.2:pom
```

## Related Errors

- [Dependency Not Found]({{< relref "/tools/maven/dependency-not-found" >}}) -- missing dependency artifacts
- [Dependency Management Version]({{< relref "/tools/maven/maven-dependency-management-version" >}}) -- version management issues
