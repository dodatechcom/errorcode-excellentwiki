---
title: "Maven Parent Version Mismatch"
description: "Maven child module references a parent POM version that does not exist, causing build resolution to fail."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Parent Version Mismatch

Child modules reference parent POMs by version. A mismatch error occurs when the child specifies a parent version that does not exist in the repository or local cache.

## Common Causes

- The parent POM was released with a different version than what the child declares
- A parent version was updated in the parent POM but not in child modules
- The parent POM has not been installed to the local repository
- The parent version uses `${revision}` but the property is not defined

## How to Fix

1. Verify the parent version exists:

```bash
mvn help:effective-pom -N | grep "<version>"
```

2. Update the parent version in the child POM:

```xml
<parent>
  <groupId>com.example</groupId>
  <artifactId>my-parent</artifactId>
  <version>1.0.0</version> <!-- must match released version -->
  <relativePath>../pom.xml</relativePath>
</parent>
```

3. Install the parent POM locally first:

```bash
mvn install -N -f parent/pom.xml
```

4. Use the versions plugin to update parent versions:

```bash
mvn versions:update-parent -DparentVersion=1.0.0
```

## Examples

```bash
# Error output
Could not find artifact com.example:my-parent:pom:1.0.1 in central
  Parent POM version 1.0.1 does not match available version 1.0.0
```

```xml
<!-- Correct parent reference -->
<parent>
  <groupId>com.example</groupId>
  <artifactId>my-parent</artifactId>
  <version>1.0.0</version>
  <relativePath>../pom.xml</relativePath>
</parent>
```

## Related Errors

- [Parent POM Not Found]({{< relref "/tools/maven/maven-parent-pom-not-found" >}}) -- parent POM missing
- [Version Error]({{< relref "/tools/maven/maven-version-error" >}}) -- version resolution issues
