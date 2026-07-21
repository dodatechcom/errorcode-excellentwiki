---
title: "Maven Module Path Error"
description: "Maven module path resolution fails because the module directory does not exist or the path in the parent POM is incorrect."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Module Path Error

Maven multi-module projects define submodules in the parent POM. A module path error occurs when Maven cannot find the directory specified in a `<module>` element.

## Common Causes

- The `<module>` path does not match the actual directory name
- The module directory was deleted or renamed after being added to the parent
- The path uses incorrect casing on case-sensitive filesystems
- A nested module path uses an incorrect relative reference

## How to Fix

1. Verify the module directories exist:

```bash
ls -la app/ core/ lib/
```

2. Check the parent POM module declarations:

```xml
<modules>
  <module>app</module>
  <module>core</module>
  <module>lib</module>
</modules>
```

3. List the project structure:

```bash
mvn validate --recursive
```

4. Fix incorrect paths:

```xml
<!-- Wrong -- directory is "my-app" not "app" -->
<module>app</module>

<!-- Correct -->
<module>my-app</module>
```

## Examples

```bash
# Error output
Could not find module 'app' in project 'my-project'
  Expected directory: /path/to/project/app/
  Module declared in parent POM: <module>app</module>
```

```xml
<!-- Correct multi-module parent POM -->
<project>
  <groupId>com.example</groupId>
  <artifactId>my-project</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>pom</packaging>

  <modules>
    <module>app</module>
    <module>core</module>
    <module>shared-lib</module>
  </modules>
</project>
```

## Related Errors

- [Module Not Found]({{< relref "/tools/maven/maven-module-not-found" >}}) -- missing modules
- [Multi Module Error]({{< relref "/tools/maven/maven-multi-module-error" >}}) -- multi-module configuration
