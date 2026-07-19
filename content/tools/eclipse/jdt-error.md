---
title: "[Solution] Eclipse JDT error"
description: "JDT errors"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "jdt", "java-development-tools", "compiler"]
severity: "error"
---

# JDT error

## Error Message

```
Internal error: java.lang.AssertionError at org.eclipse.jdt.internal.core.JavaProject.computeSourceSegments(JavaProject.java:3421)
```

## Common Causes

- A bug in the JDT plugin caused by corrupted project metadata or an internal state inconsistency.
- The Java project has circular dependencies or malformed `.classpath` entries.
- A JDT cache file has become corrupted after a failed workspace build.

## Solutions

### Solution 1: Rebuild All Java Projects

Select **Project > Clean** from the menu bar, choose **Clean all projects**, and click **OK**. This forces JDT to recompile all source files and regenerate its internal symbol tables. If the error persists, try deleting the `bin` directory of the affected project manually.

```java
# Remove compiled output and JDT cache
rm -rf <project>/bin
rm -rf <project>/.settings/org.eclipse.jdt.core.prefs
# Restart Eclipse and let JDT rebuild the project
```

### Solution 2: Reset JDT Compiler Settings

Navigate to **Window > Preferences > Java > Compiler** and ensure the compiler level is set correctly. Then go to **Project > Properties > Java Compiler** and verify the project-specific settings override is consistent with the workspace defaults.

```bash
# eclipse.ini - increase JVM heap for JDT compilation
-Xmx2g
-Xms512m
-XX:MaxMetaspaceSize=512m
```

## Prevention Tips

- Keep your Eclipse installation updated to the latest service release for JDT bug fixes.
- Avoid changing Java compiler settings mid-project; set them at project creation time.
- If JDT errors appear randomly, check for disk space issues or filesystem corruption.

## Related Errors

- [compilation-error]({{< relref "/tools/eclipse/compilation-error" >}})
- [build-path-error]({{< relref "/tools/eclipse/build-path-error" >}})
- [code-completion-error]({{< relref "/tools/eclipse/code-completion-error" >}})
