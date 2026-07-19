---
title: "[Solution] Eclipse Code formatter error"
description: "Code formatter error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "formatter", "code-style", "formatting"]
severity: "error"
---

# Code formatter error

## Error Message

```
Formatter error: Unable to format code. The formatter settings reference a profile that does not exist. Check Window > Preferences > Java > Code Style > Formatter.
```

## Common Causes

- The project-specific formatter profile references a formatter configuration file that has been deleted or moved.
- The Eclipse formatter profile XML file is corrupted or contains invalid XML.
- The formatter profile was exported from a different Eclipse version with incompatible settings.

## Solutions

### Solution 1: Restore Default Formatter Profile

Go to **Window > Preferences > Java > Code Style > Formatter** and click **Edit**. If the current profile is corrupted, click **Import** and select a formatter profile XML file, or click **Restore Defaults** to use Eclipse's built-in Java conventions profile. For projects, import the team formatter profile from the project repository.

```java
<!-- eclipse-formatter.xml - Custom formatter profile example -->
<profiles version="21">
    <profile kind="CodeFormatterProfile"
             name="TeamStandard"
             version="21">
        <setting id="org.eclipse.jdt.core.formatter.tabulation.char"
                 value="tab"/>
        <setting id="org.eclipse.jdt.core.formatter.tabulation.size"
                 value="4"/>
        <setting id="org.eclipse.jdt.core.formatter.lineSplit"
                 value="120"/>
        <setting id="org.eclipse.jdt.core.formatter.insertNewLineBeforeElseInIfStatement"
                 value="do not insert"/>
    </profile>
</profiles>
```

### Solution 2: Share Formatter Profile via Maven Plugin

Use the **Eclipse Code Formatter** Maven/Gradle plugin to share a team formatter profile across all developers. This ensures consistent formatting regardless of individual Eclipse settings and prevents formatter errors caused by missing profiles.

```bash
<!-- pom.xml - Eclipse Code Formatter plugin -->
<plugin>
    <groupId>net.revelc.code.formatter</groupId>
    <artifactId>formatter-maven-plugin</artifactId>
    <version>2.23.0</version>
    <configuration>
        <configFile>eclipse-formatter.xml</configFile>
    </configuration>
</plugin>
```

## Prevention Tips

- Always commit the formatter profile XML to version control so all team members use the same settings.
- Use **Ctrl+Shift+F** to format code, and **Ctrl+Shift+O** to organize imports before formatting.
- Export your formatter profile via **Formatter > Export** to share with team members.

## Related Errors

- [checkstyle-error]({{< relref "/tools/eclipse/checkstyle-error" >}})
- [pmd-error]({{< relref "/tools/eclipse/pmd-error" >}})
- [compilation-error]({{< relref "/tools/eclipse/compilation-error" >}})
