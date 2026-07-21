---
title: "Maven Nested Module Error"
description: "Maven build fails when processing nested modules because submodules reference parents or dependencies that cannot be resolved in the reactor."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Nested Module Error

Maven supports nested multi-module projects where submodules contain their own submodules. A nested module error occurs when the module hierarchy references cannot be resolved by the reactor.

## Common Causes

- A nested module references a parent POM that does not exist at the expected path
- The `<relativePath>` element points to the wrong location
- A deeply nested module is not included in its immediate parent's `<modules>` list
- The reactor cannot find a module because it is not in the build path

## How to Fix

1. Verify the relative path to the parent POM:

```xml
<parent>
  <groupId>com.example</groupId>
  <artifactId>my-project</artifactId>
  <version>1.0-SNAPSHOT</version>
  <relativePath>../../pom.xml</relativePath>
</parent>
```

2. List all modules recursively:

```bash
mvn validate --also-make
```

3. Ensure nested modules declare their parent correctly:

```xml
<!-- In nested-module/pom.xml -->
<parent>
  <groupId>com.example</groupId>
  <artifactId>my-project-core</artifactId>
  <version>1.0-SNAPSHOT</version>
  <relativePath>../pom.xml</relativePath>
</parent>
```

4. Build from the root to include all modules:

```bash
mvn clean install -f root/pom.xml
```

## Examples

```bash
# Error output
The project com.example:nested-module:1.0-SNAPSHOT
  has been referenced as a module of 'my-project' but does not exist
```

```xml
<!-- Correct nested module structure -->
<!-- root/pom.xml -->
<modules>
  <module>core</module>
</modules>

<!-- root/core/pom.xml -->
<modules>
  <module>plugin-a</module>
  <module>plugin-b</module>
</modules>
```

## Related Errors

- [Module Not Found]({{< relref "/tools/maven/maven-module-not-found" >}}) -- missing modules
- [Parent POM Not Found]({{< relref "/tools/maven/maven-parent-pom-not-found" >}}) -- parent resolution failures
