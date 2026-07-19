---
title: "[Solution] Java ClassNotFoundException — webapp ClassLoader in Tomcat/Jetty cannot find classes due to delegation"
description: "Fix Java ClassNotFoundException when webapp classloader in tomcat/jetty cannot find classes due to delegation with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassNotFoundException — webapp ClassLoader in Tomcat/Jetty cannot find classes due to delegation

A `ClassNotFoundException` occurs when Class.forName("com.mysql.cj.jdbc.Driver");  // not in WEB-INF/lib.

## Common Causes

```java
Class.forName("com.mysql.cj.jdbc.Driver");  // not in WEB-INF/lib
```

## Solutions

```java
// Fix: ensure JARs in WEB-INF/lib/
// Maven: <scope>runtime</scope>

// Fix: parent-last config
// <Context><Loader delegate="false"/></Context>

// Fix: Thread context ClassLoader
ClassLoader loader = Thread.currentThread().getContextClassLoader();
loader.loadClass("com.mysql.cj.jdbc.Driver");
```

## Prevention Checklist

- Include all runtime deps in WEB-INF/lib/.
- Use maven-shade-plugin for fat JARs.
- Test in target container.

## Related Errors

ClassNotFoundException, NoClassDefFoundError
