---
title: "[Solution] Java NoClassDefFoundError — runtime library version differs from compile version"
description: "Fix Java NoClassDefFoundError when runtime library version differs from compile version with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NoClassDefFoundError — runtime library version differs from compile version

A `NoClassDefFoundError` occurs when // Compile: commons-lang3-3.12.0
// Runtime: commons-lang3-3.8.1 (no capitalize)
String r = StringUtils.capitalize(name);  // NoClassDefFoundError.

## Common Causes

```java
// Compile: commons-lang3-3.12.0
// Runtime: commons-lang3-3.8.1 (no capitalize)
String r = StringUtils.capitalize(name);  // NoClassDefFoundError
```

## Solutions

```java
// Fix: lock versions
// Maven: <dependencyManagement> with explicit versions

// Fix: verify runtime version
System.out.println(Package.getPackage("org.apache.commons.lang3").getImplementationVersion());

// Fix: maven-enforcer-plugin
// <dependencyConvergence/>
```

## Prevention Checklist

- Use BOMs for consistent versions.
- Run mvn enforcer:enforce.
- Test with exact production versions.

## Related Errors

UnsupportedClassVersionError, NoSuchMethodError
