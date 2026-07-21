---
title: "Maven Unresolved Relative Path Error"
description: "Maven parent POM resolution fails because the relativePath element points to a non-existent POM file location."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Unresolved Relative Path Error

The `<relativePath>` element in a child POM tells Maven where to find the parent POM. An error occurs when the path does not point to a valid POM file.

## Common Causes

- The `relativePath` points to a directory that does not exist
- The parent POM file was moved or renamed
- The default `../pom.xml` does not match the actual parent location
- The path uses forward slashes on a Windows system or vice versa

## How to Fix

1. Set `relativePath` to empty if the parent is only in a repository:

```xml
<parent>
  <groupId>com.example</groupId>
  <artifactId>my-parent</artifactId>
  <version>1.0.0</version>
  <relativePath/>
</parent>
```

2. Verify the relative path resolves correctly:

```bash
# From the child directory
ls -la ../pom.xml
# or
ls -la ../../parent/pom.xml
```

3. Install the parent POM locally first:

```bash
mvn install -N -f parent/pom.xml
```

4. Use the correct path:

```xml
<parent>
  <groupId>com.example</groupId>
  <artifactId>my-parent</artifactId>
  <version>1.0.0</version>
  <relativePath>../my-parent/pom.xml</relativePath>
</parent>
```

## Examples

```bash
# Error output
[ERROR] The parent POM at ../parent/pom.xml could not be resolved
```

```xml
<!-- Empty relativePath -- look in repository only -->
<parent>
  <groupId>com.example</groupId>
  <artifactId>spring-boot-starter-parent</artifactId>
  <version>3.2.2</version>
  <relativePath/>
</parent>
```

## Related Errors

- [Parent POM Not Found]({{< relref "/tools/maven/maven-parent-pom-not-found" >}}) -- parent resolution failures
- [Relative Path Not Resolved]({{< relref "/tools/maven/maven-relativepath-not-resolved" >}}) -- path resolution issues
