---
title: "[Solution] Java NoClassDefFoundError — classloader hierarchy in WAR/EAR cannot find library classes"
description: "Fix Java NoClassDefFoundError when classloader hierarchy in war/ear cannot find library classes with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NoClassDefFoundError — classloader hierarchy in WAR/EAR cannot find library classes

A `NoClassDefFoundError` occurs when // myapp.ear/
//   myapp.war/WEB-INF/lib/lib1.jar
//   lib/lib2.jar  — not visible to WAR classloader.

## Common Causes

```java
// myapp.ear/
//   myapp.war/WEB-INF/lib/lib1.jar
//   lib/lib2.jar  — not visible to WAR classloader
```

## Solutions

```java
// Fix: correct JAR placement
// WAR: WEB-INF/lib/
// EAR: root lib/ or WAR's WEB-INF/lib/

// Fix: jboss-deployment-structure.xml
// <dependencies><module name="org.hibernate"/></dependencies>

// Fix: MANIFEST.MF Class-Path
// Class-Path: lib/lib1.jar lib/lib2.jar
```

## Prevention Checklist

- Verify EAR/WAR structure.
- Use Class-Path in MANIFEST.MF.
- Test in target application server.

## Related Errors

ClassNotFoundException, LinkageError
