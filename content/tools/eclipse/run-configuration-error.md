---
title: "[Solution] Eclipse Run configuration error"
description: "Run configuration error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "run-configuration", "launch", "execution"]
severity: "error"
---

# Run configuration error

## Error Message

```
Selection does not contain a main type. Select a project or class that contains a main method to launch.
```

## Common Causes

- The class does not have a valid `public static void main(String[] args)` method.
- The run configuration is pointing to the wrong class or package.
- The project has not been compiled, so Eclipse cannot locate the main class.

## Solutions

### Solution 1: Create a New Run Configuration

Go to **Run > Run Configurations**, select **Java Application**, and click **New**. Browse to select the correct project and main class. Alternatively, open the class with the `main` method and click the **Run** button (green play icon) in the toolbar.

```java
// Ensure the main method signature is correct
public class Application {
    public static void main(String[] args) {
        // Entry point for the application
        System.out.println("Application started");
    }
}
```

### Solution 2: Fix the Launch Configuration

Double-click the run configuration in **Run > Run Configurations** to open the editor. On the **Main** tab, verify the **Project** and **Main class** fields are correct. On the **Arguments** tab, ensure VM arguments and program arguments are properly formatted.

```bash
# Common VM arguments for run configurations
-Xmx512m
-Xms256m
-Dspring.profiles.active=dev
-Dapp.config.path=/path/to/config.properties
```

## Prevention Tips

- Use **Run > History** to quickly access recently used run configurations.
- Set a breakpoint at the first line of `main()` to debug launch issues.
- For Spring Boot apps, use the **Spring Boot Dashboard** view instead of manual run configurations.

## Related Errors

- [debug-error]({{< relref "/tools/eclipse/debug-error" >}})
- [console-error]({{< relref "/tools/eclipse/console-error" >}})
- [test-error]({{< relref "/tools/eclipse/test-error" >}})
