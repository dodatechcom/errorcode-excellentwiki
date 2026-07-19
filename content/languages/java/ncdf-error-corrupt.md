---
title: "[Solution] Java NoClassDefFoundError — JAR file is corrupt, truncated, or incomplete on classpath"
description: "Fix Java NoClassDefFoundError when jar file is corrupt, truncated, or incomplete on classpath with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NoClassDefFoundError — JAR file is corrupt, truncated, or incomplete on classpath

A `NoClassDefFoundError` occurs when // jar verify library.jar
// java.lang.NoClassDefFoundError: org/apache/commons/lang3/StringUtils.

## Common Causes

```java
// jar verify library.jar
// java.lang.NoClassDefFoundError: org/apache/commons/lang3/StringUtils
```

## Solutions

```java
// Fix: verify JAR integrity
// jar tf library.jar | head -20
// jar verify library.jar

// Fix: clean and re-download
// rm -rf ~/.m2/repository/groupId/artifactId && mvn clean install
```

## Prevention Checklist

- Configure Maven to verify checksums.
- Clean local repo on class loading failures.
- Verify JAR integrity after deployment.

## Related Errors

ClassNotFoundException, ZipException
