---
title: "[Solution] Java NoClassDefFoundError — class available at compile time missing from classpath at runtime"
description: "Fix Java NoClassDefFoundError when class available at compile time missing from classpath at runtime with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NoClassDefFoundError — class available at compile time missing from classpath at runtime

A `NoClassDefFoundError` occurs when ThirdPartyLib.doWork();  // works in IDE, fails at runtime.

## Common Causes

```java
ThirdPartyLib.doWork();  // works in IDE, fails at runtime
```

## Solutions

```java
// Fix: ensure compile scope
// <dependency>... <scope>compile</scope> (default) </dependency>

// Fix: verify classpath
System.out.println("Classpath: "+System.getProperty("java.class.path"));

// Fix: analyze dependencies
// mvn dependency:analyze
```

## Prevention Checklist

- Run mvn dependency:tree.
- Use mvn dependency:analyze.
- Test in actual deployment environment.

## Related Errors

ClassNotFoundException, LinkageError
