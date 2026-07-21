---
title: "Maven Named Artifacts Not Found"
description: "Maven cannot resolve named artifacts because the artifact coordinates do not match any published version in the configured repositories."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Named Artifacts Not Found

Maven resolves artifacts by groupId, artifactId, version, and packaging. A named artifacts not found error means the specific combination does not exist in any configured repository.

## Common Causes

- The artifactId or groupId contains a typo
- The artifact version does not exist on Maven Central
- The artifact uses a non-standard packaging type that is not available
- A custom repository URL is incorrect or requires different credentials

## How to Fix

1. Search Maven Central for the artifact:

```bash
curl "https://search.maven.org/solrsearch/select?q=a:my-lib&rows=5&wt=json" | python3 -m json.tool
```

2. Verify the artifact coordinates match exactly:

```xml
<dependency>
  <groupId>com.example</groupId>
  <artifactId>my-lib</artifactId>
  <version>1.0.0</version>
  <!-- groupId, artifactId, and version must match exactly -->
</dependency>
```

3. Check if the artifact is in a custom repository:

```bash
curl https://repo.example.com/releases/com/example/my-lib/1.0.0/my-lib-1.0.0.pom
```

4. Use the `dependency:get` goal to test resolution:

```bash
mvn dependency:get -Dartifact=com.example:my-lib:1.0.0:jar
```

## Examples

```bash
# Error output
[ERROR] Could not find artifact com.example:my-lib:jar:1.0.0 in central
  (https://repo.maven.apache.org/maven2)
  Did you mean: com.example:my-library:1.0.0
```

```xml
<!-- Search and verify before adding dependency -->
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-web</artifactId>
  <version>3.2.2</version>
</dependency>
```

## Related Errors

- [Artifact Not Found Repo]({{< relref "/tools/maven/maven-artifact-not-found-repo" >}}) -- repository-specific issues
- [Dependency Not Found]({{< relref "/tools/maven/dependency-not-found" >}}) -- missing dependencies
