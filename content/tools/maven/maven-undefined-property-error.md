---
title: "Maven Undefined Property Error"
description: "Maven build fails because a property referenced in the POM is not defined, leaving a literal ${} expression in the configuration."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Undefined Property Error

Maven uses `${property}` syntax for value substitution in POM files. An undefined property error occurs when a referenced property has no value defined anywhere in the build.

## Common Causes

- A property is referenced but never declared in the POM or profiles
- A profile that defines the property is not activated
- The property name has a typo or case mismatch
- A parent POM that defines the property is not inherited correctly

## How to Fix

1. Find the undefined property in the error message:

```bash
mvn build 2>&1 | grep "undefined property\|unresolved"
```

2. Define the property in the POM:

```xml
<properties>
  <my.app.version>1.0.0</my.app.version>
  <my.app.name>My Application</my.app.name>
</properties>
```

3. Check if the property comes from a profile:

```bash
mvn help:effective-pom -P production
```

4. Set the property via command line:

```bash
mvn clean install -Dmy.app.version=2.0.0
```

## Examples

```bash
# Error output
[ERROR] Failed to execute goal build-helper:regex-property
  Property 'app.version' is not defined
```

```xml
<!-- Define properties in the POM -->
<properties>
  <app.version>1.0.0</app.version>
  <spring.version>6.1.3</spring.version>
</properties>

<!-- Reference properties in dependencies -->
<dependency>
  <groupId>org.springframework</groupId>
  <artifactId>spring-core</artifactId>
  <version>${spring.version}</version>
</dependency>
```

## Related Errors

- [Properties Interpolation Error]({{< relref "/tools/maven/maven-properties-interpolation-error" >}}) -- property interpolation issues
- [Profile Activation Error]({{< relref "/tools/maven/maven-profile-activation-error" >}}) -- profile activation failures
