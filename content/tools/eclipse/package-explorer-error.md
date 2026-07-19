---
title: "[Solution] Eclipse Package explorer error"
description: "Package explorer error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "package-explorer", "project-explorer", "navigation"]
severity: "error"
---

# Package explorer error

## Error Message

```
Package Explorer does not display project contents. Right-click the project and select Refresh, or try Window > Reset Perspective to restore the view.
```

## Common Causes

- The Package Explorer's internal model cache is stale or corrupted.
- The project was modified outside of Eclipse (e.g., by git or another IDE) without refreshing.
- A resource change event was not delivered to the view due to a plugin error.

## Solutions

### Solution 1: Refresh the Project

Select the project in the Package Explorer and press **F5** to refresh, or right-click the project and select **Refresh**. For a full workspace refresh, select all projects (**Ctrl+A**) and press **F5**. You can also enable **Window > Preferences > General > Workspace > Refresh automatically**.

```java
# Eclipse keyboard shortcuts for navigation
# F5          - Refresh selected resource
# F11         - Debug last launched
# Ctrl+F5     - Refresh workspace
# Ctrl+Shift+F - Format code
```

### Solution 2: Rebuild the Project Tree

If the Package Explorer shows empty or broken project entries, close the project (**right-click > Close Project**), then reopen it (**right-click > Open Project**). This forces Eclipse to re-read the project metadata from disk and rebuild the explorer tree.

```bash
# Verify project metadata files exist
ls -la <project>/.project
ls -la <project>/.classpath
ls -la <project>/.settings/

# If .project is missing, recreate it
# File > Import > General > Existing Projects into Workspace
```

## Prevention Tips

- Use **Package Explorer > View Menu > Filters** to customize which files are displayed.
- Switch to **Project Explorer** view for a different project tree perspective.
- Use **Package Explorer > Collapse All** (Ctrl+Shift+F11) to quickly collapse expanded trees.

## Related Errors

- [outline-error]({{< relref "/tools/eclipse/outline-error" >}})
- [problems-view-error]({{< relref "/tools/eclipse/problems-view-error" >}})
- [workspace-corruption]({{< relref "/tools/eclipse/workspace-corruption" >}})
